from collections import defaultdict
from dataclasses import dataclass
import re
import os


@dataclass
class ContentPage:
    title: str
    path: str
    menuTitle: str
    weight: int

    def frontmatter_lines(self, enclose=False):
        lines = ["title: {}\n".format(self.title)]
        lines.append("menuTitle: {}\n".format(self.menuTitle))
        lines.append("weight: {}\n".format(self.weight))
        fname = os.path.basename(self.path)
        if fname == "README.md":
            dn = os.path.dirname(self.path)
            if dn:
                lines.insert(0, "archetype: chapter\n")
            else:
                lines.insert(0, "archetype: home\n")
        if enclose:
            lines.insert(0, "---\n")
            lines.append("---\n\n")
        return lines

    @property
    def frontmatter(self):
        return "".join(self.frontmatter_lines())


@dataclass
class LinkEntry:
    menuTitle: str
    weight: int
    url: str

    def config_lines(self):
        lines = ["[[menu.shortcuts]]\n"]
        lines.append('name = "{}"\n'.format(self.menuTitle))
        lines.append('url = "{}"\n'.format(self.url))
        lines.append("weight = {}\n".format(self.weight))
        lines.append("\n")
        return lines

    @property
    def config_entry(self):
        return "".join(self.config_lines())


GITBOOK_DIR = os.path.dirname(os.path.abspath(__file__))
_parent = os.path.dirname(GITBOOK_DIR)
HUGO_DIR = GITBOOK_DIR

levels = defaultdict(int)


def get_level(line):
    return int(line.find("*") / 2 + 1)


def get_menu_title(line):
    reg_match = re.match(r".*[[](.*)[]].*", line)
    if reg_match:
        return reg_match.group(1)
    return ""


def get_path(line):
    reg_match = re.match(r".*[(](.*)[)].*", line)
    if reg_match:
        return reg_match.group(1)
    return ""


def get_page_title(path):
    with open(path, "r", encoding="utf-8") as p:
        line = p.readline()
        while "#" not in line:
            line = p.readline()
    return line.replace("#", "").replace(":", " – ").strip()


def get_content():
    summary_file = os.path.join(GITBOOK_DIR, "SUMMARY.md")

    with open(summary_file, "r", encoding="utf-8") as sf:
        lines = sf.readlines()

    lines = [line for line in lines if "*" in line]

    pages = []
    links = []
    for line in lines:
        level = get_level(line)
        levels[level] += 1
        weight = levels[level]
        path = get_path(line)
        menu_title = get_menu_title(line)
        if path.startswith("https"):
            links.append(LinkEntry(menuTitle=menu_title, weight=weight, url=path))
        else:
            page_title = get_page_title(path)
            pages.append(
                ContentPage(
                    title=page_title, path=path, menuTitle=menu_title, weight=weight
                )
            )
    return pages, links


def wrap_latex(page_lines):
    idx = 0
    to_change = []
    for i, line in enumerate(page_lines):
        if "$$" in line:
            if idx % 2 == 0:
                new = "```math\n$$\n"
            else:
                new = "$$\n```\n"
            to_change.append((i, new))
            idx += 1
    for idx, new in to_change:
        page_lines[idx] = new
    return page_lines


def strip_h1(page_lines):
    return [line for line in page_lines if not line.startswith("# ")]


def fix_image_links(page_lines):
    to_change = []
    for i, line in enumerate(page_lines):
        if "assets/" in line:
            assets_path = re.match(r".*[(](.*)[)].*", line).group(1)
            asset_bn = os.path.basename(assets_path)
            end = line.find("]")
            new = line[: end + 1] + "(/images/{})".format(asset_bn)
            to_change.append((i, new))
    for idx, new in to_change:
        page_lines[idx] = new
    return page_lines


def fix_content_links(page_lines):
    to_change = []
    for i, line in enumerate(page_lines):
        url_path = re.match(r".*[(](.*)[)].*", line)
        if url_path:
            url = url_path.group(1)
            if ".md" in url and "http" not in url:
                if "../../protocol-parameters" in url:
                    new_url = '{{< ref "/learn/protocol-parameters" >}}'
                elif "../../../v0/glossary" in url:
                    new_url = '{{< ref "/learn/glossary" >}}'
                elif "../node/trophies/app-developers" in url:
                    url = url.replace("node", "community")
                else:
                    new_url = url.replace(".md", "").replace("README", "")
                    new_url = '{{< relref "%s" >}}' % new_url
                new = line.replace(url, new_url)
                to_change.append((i, new))
    for idx, new in to_change:
        page_lines[idx] = new
    return page_lines


def remap_hint(page_lines):
    to_change = []
    for i, line in enumerate(page_lines):
        if "{% hint" in line:
            new = line.replace("{% hint", "{{% notice")
            new = new.replace("%}", "%}}")
            to_change.append((i, new))
        elif "{% endhint %}" in line:
            to_change.append((i, "{{% /notice %}}\n"))
    for idx, new in to_change:
        page_lines[idx] = new
    return page_lines


def remap_tabs(page_lines):
    to_change = []
    for i, line in enumerate(page_lines):
        if "{% tab title=" in line:
            new = line.replace("{% tab title=", "{{% tab name=")
            new = new.replace("%}", "%}}")
            to_change.append((i, new))
        elif "{% endtab %}" in line:
            to_change.append((i, "{{% /tab %}}\n"))
        elif "{% tabs %}" in line:
            to_change.append((i, "{{< tabs >}}\n"))
        elif "{% endtabs %}" in line:
            to_change.append((i, "{{< /tabs >}}\n"))
    for idx, new in to_change:
        page_lines[idx] = new
    return page_lines


def remap_content_ref(page_lines):
    to_change = []
    for i, line in enumerate(page_lines):
        if "{% content-ref" in line:
            url_start = line.find('"')
            url_end = line.find('"', url_start)
            url = line[url_start:url_end]
            new = "**[Buy Store and Stake]({})**".format(url)
            to_change.append((i, new))
        elif "{% endcontent-ref" in line:
            new = ""
            to_change.append((i, new))
    for idx, new in to_change:
        page_lines[idx] = new
    return page_lines
    pass


def remap_youtube(page_lines):
    to_change = []
    for i, line in enumerate(page_lines):
        if "{% embed" in line and "yout" in line:
            if "youtube" in line:
                youtube_val_start = line.find("?")
                youtube_val_end = line.find('"', youtube_val_start)
                youtube_val = line[youtube_val_start + 2 : youtube_val_end]
            else:
                youtube_url_start = line.find('"')
                youtube_url_end = line.find('"', youtube_url_start)
                youtube_url = line[youtube_url_start:youtube_url_end]
                youtube_val = youtube_url.split("/")[-1]
            new = "{{< youtube %s >}}" % youtube_val
            to_change.append((i, new))
    for idx, new in to_change:
        page_lines[idx] = new
    return page_lines


def migrate_pages(pages):
    content_dir = os.path.join(HUGO_DIR, "content")
    if not os.path.exists(content_dir):
        os.mkdir(content_dir)
    for page in pages:
        _dir = os.path.dirname(page.path)
        out_dir = os.path.join(content_dir, _dir)
        if _dir:
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)
        bn = os.path.basename(page.path)
        local_parent = os.path.dirname(os.path.relpath(page.path, GITBOOK_DIR))
        if bn == "README.md":
            bn = "_index.md"
        elif len(local_parent) < 1:
            new_dir, _ = os.path.splitext(os.path.relpath(page.path, GITBOOK_DIR))
            out_dir = os.path.join(content_dir, new_dir)
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)
            bn = "_index.md"
        out_file = os.path.join(out_dir, bn)
        with open(page.path, "r", encoding="utf-8") as p:
            page_lines = p.readlines()
        page_lines = strip_h1(page_lines)
        page_lines = wrap_latex(page_lines)
        page_lines = remap_hint(page_lines)
        page_lines = remap_tabs(page_lines)
        page_lines = remap_youtube(page_lines)
        page_lines = remap_content_ref(page_lines)
        page_lines = fix_content_links(page_lines)
        page_lines = fix_image_links(page_lines)
        if not page_lines:
            page_lines = ["\n"]
        if page_lines[0].startswith("---"):
            page_lines = [page_lines[0]] + page.frontmatter_lines() + page_lines[1:]
        else:
            page_lines = page.frontmatter_lines(enclose=True) + page_lines[:]
        with open(out_file, "w", encoding="utf-8") as of:
            of.writelines(page_lines)


def migrate_links(links):
    out_file = os.path.join(HUGO_DIR, "config.toml.menulinks")
    out_lines = "\n".join([link.config_entry for link in links])
    with open(out_file, "w", encoding="utf-8") as of:
        of.writelines(out_lines)


def todo():
    """
    - Root pages get directories and _index.md files. Done.
    - URLs become properly reffed. Done?
    - Page for redirects
    """
    pass


def main():
    pages, links = get_content()
    migrate_pages(pages)
    migrate_links(links)


if __name__ == "__main__":
    main()
