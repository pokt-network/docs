---
title: Contributors Guide
menuTitle: Contributors Guide
weight: 10
description: How to contribute to the Pocket Network documentation.
---

This page will go into detail on how to contribute to the Pocket Network documentation site at <https://docs.pokt.network>. If you are familiar with Markdown and contributing to an open-source repo on GitHub, the [Quick setup](/contributing/#quick-setup) section may be all you need.

## Required installations

There are only 2 tools needed to get started contributing to the documentation:

1. [Hugo](https://gohugo.io/) version 0.93 or newer
2. [Git](https://git-scm.com/)

### Installing Hugo

For this guide, we'll cover the easiest way to install Hugo, which is
downloading an already built executable. If you would prefer to install from a
package manager like `brew`, `chocolately`, or `apt`, then you should follow
along with the corresponding Hugo [installation guide](https://gohugo.io/getting-started/installing/).

1. Navigate to the [Hugo releases page on GitHub](https://github.com/gohugoio/hugo/releases). Find the latest release.

2. Scroll down until you see a heading called **Assets**.

![Assets for download](/images/hugo-releases.png)

3. Click the appropriate build for your system to download it.

{{< tabs >}}
{{% tab name="Windows" %}}

### Installing the Executable

If you're running **Windows**, you need to know how many bits the operating system is and what kind of processor you're running.

If you're unsure of these things, open the Start Menu and type **About your PC** and press Enter. The details will be available under the **System type** value.

Using those details you should download your corresponding version.

- 64-bit x64: `hugo_<ver>_Windows-64bit.zip`
- 64-bit ARM: `hugo_<ver>_Windows-ARM64.zip`
- 32-bit x86: `hugo_<ver>_Windows-32bit.zip`
- 32-bit ARM: `hugo_<ver>_Windows-ARM.zip`

For most people, the 64-bit x64 version will be appropriate.

Make a new folder called `C:\Hugo\bin`.

Move the downloaded `.zip` file into the newly created `C:\Hugo\bin` folder.
Then double click on the `.zip` file and extract its contents. The folder should
now contain the following 3 new files:

```
hugo.exe
LICENSE
README.md
```

From here, we'll need to add Hugo to your Windows PATH settings. To do this:

1. Open the Start Menu and type "Environment variables".
2. Select **Edit the System environment variables**.
3. Click the button that says **Environment Variables...**.
4. Click to select the **Path** row under **User variables**.
5. Click **Edit...** under **User variables**.
6. Click **Browse...**, and select the `C:\Hugo\bin` folder.
7. Click **OK** on all following windows.

### Using Package Managers

Alternatively, if you have [Chocolately](https://chocolatey.org/) installed, you can run this command:

```sh
choco install hugo -confirm
```

Or, if you have [Scoop](https://scoop.sh/) installed:

```sh
scoop install hugo
```

{{% /tab %}}
{{% tab name="Mac" %}}

### Installing the Executable

* If you're on a Mac with an **Intel Processor**, use: `hugo_<ver>_macOS-64bit.tar.gz`.
* If you're on a Mac with an **M1/M2 Processor**, use: `hugo_<ver>_macOS-ARM64.tar.gz`.

1. Once you've downloaded the corresponding release, open a Terminal, and make a folder for the hugo executable.

  ```sh
  mkdir -p ~/bin
  ```

2. Navigate into that directory.

  ```sh
  cd ~/bin
  ```

3. Extract the downloaded release into this folder.

  ```sh
  tar -xvzf ~/Downloads/hugo_<ver>_macOS-<ARCH>.tar.gz
  ```

  Where `<ver>` is going to match the version you downloaded, and `<ARCH>` will match the processor in your Mac.

4. Check if `hugo` is in your path by running:

  ```sh
  which hugo
  ```

  If there's no answer, that means we have to add it to your path (steps 5-8).

5. We'll need to see which shell you're working with by running:

  ```sh
  echo $SHELL
  ```

6. If the answer is `zsh`, you'll want to run:

  ```sh
  echo "export PATH=$PATH:$HOME/bin" >> ~/.zprofile
  ```

  and if the answer is `bash` you'll want to run:

  ```sh
  echo "export PATH=$PATH:$HOME/bin" >> ~/.bash_profile
  ```

7. Close your Terminal. When you reopen your Terminal, Hugo will be ready to
use.

### Using Package Managers

Alternatively, if you have [Homebrew](https://brew.sh/) installed, you can also run the following: 

```sh
brew install hugo
```

Or if you have have [MacPorts](https://www.macports.org/) installed, you can run the following:

```sh
port install hugo
```

{{% /tab %}}
{{% tab name="Linux/OpenBSD" %}}
If you're on Linux/OpenBSD, it's highly recommended you use a package manager install since Hugo does not require a new installation like in Windows and Mac.

### Debian/Ubuntu

```sh
snap install hugo
```

### Arch

```sh
sudo pacman -Syu hugo
```

### Fedora/Red Hat/CentOS

```sh
sudo dnf install hugo
```

### openSUSE Tumbleweed

```sh
sudo zypper install hugo
```

### OpenBSD

```sh
doas pkg_add hugo
```

{{% /tab %}}
{{< /tabs >}}

### Install git

{{< tabs >}}
{{% tab name="Windows" %}}

Download and install the corresponding [Git for Windows](https://git-scm.com/download/win) setup for your system, either 32- or 64-bit.

{{% /tab %}}
{{% tab name="Mac" %}}

From a terminal, run:

```sh
git --version
```

If it's not installed, you'll be prompted with an installer.

{{% /tab %}}
{{% tab name="Linux/OpenBSD" %}}

### Debian, Ubuntu

```sh
sudo apt install git
```

### Arch

```sh
sudo pacman -Syu git
```

### Fedora, Red Hat, CentOS

```sh
sudo dnf install git
```

### openSUSE Tumbleweed

```sh
sudo zypper install git
```

### OpenBSD

```sh
doas pkg_add git
```

{{% /tab %}}
{{< /tabs >}}

## Recommended installations

While Hugo and Git are everything you need to get up and running, we recommend setting up an environment that will take care of content editing, managing Git changes, and running the Hugo commands all in one place.

If you already have a text editor of choice such as vim, emacs, or SublimeText, check out the [Editor plugins for Hugo](https://gohugo.io/tools/editors/) page. This will show how to integrate Hugo with your familiar environment.

If you don't have a text editor of choice, we recommend installing [Visual Studio Code](https://code.visualstudio.com/). It comes built with the tools we need to work with Hugo and Git without having to resort to a command line.

Once you have Visual Studio Code installed, launch it and install the following plugins:

- [Hugo Language and Syntax Support](https://marketplace.visualstudio.com/items?itemName=budparr.language-hugo-vscode)
- [Hugo Helper](https://marketplace.visualstudio.com/items?itemName=rusnasonov.vscode-hugo)

If you'd prefer to use your own tools, know that you'll be expected to do the following:

- Start and stop the Hugo live server from the command line.
- Manage Git changes and commits from the command line.
- Edit Markdown files directly from a text editor like Notepad or nano, not a document editor like Microsoft Word or Google Docs.


## Running a local server

You can see local changes made before committing to the repo.

To start a local Hugo server:

1. Open a terminal and change into the directory where you checked out the repo.

2. Run `hugo serve`.

3. Open <http://localhost:1313> in a browser.

Saving any file will cause the page to be automatically updated in the browser.


## Making changes

### Editing existing pages

To edit an existing page, you can open a Markdown file in a text editor, make any textual changes you'd like, and save the file. If you are running a local server, you will be able to immediately see the changes as they will appear.

### Adding pages to existing sections

If you want to add content, simply create a new markdown file in the `content` directory in the directory you want the content to live in.

Once created, each file needs a front matter (header), which can be either `yaml`, `toml`, or `json` specifying the following 3 things: `title`, `menuTitle`, `weight`.

The following shows an example of the front matter for a Glossary page:

```yaml
---
title: Glossary
menuTitle: Glossary
weight: 10
---
```

* The `title` represents what the page will be referred to as in the browser tab, as well as in link tooltips, and possibly in external cards that are displayed in tweets and in message previews.
* The `menuTitle` represents what the page will be called in the navigation sidebar.
* The `weight` determines the order in which pages in that same section level will be ordered. If we wanted a page to come before this in the tree, we would need to give it a weight smaller than 10, and if we wanted a page to come after this in the tree, we would need to give it a weight larger than 10.

After the front matter, the rest of the content in the page can be created in [Markdown](https://www.markdownguide.org/), as well as a handful of "shortcodes" that can be used to embed slightly more sophisticated elements easily.

Let's look at the "Own POKT" section (found at <https://docs.pokt.network>). This is how the directory looks:

```sh
├── | pokt
│   ├── _index.md   ["Own POKT"]
│   ├── buy.md      ["Buy POKT"]
│   ├── stake.md    ["Stake POKT"]
│   └── wallets.md  ["POKT Wallets"]
```

While the navigation displays the following:

![Navbar preview](/images/sidebar.png)

This should make sense, as the weights to `buy.md`, `stake.md` and `wallets.md` are 20, 30, and 10, respectively.

### Adding new sections

Sections are defined by directories with an `_index.md` file in them. The site also has an `_index.md` file that serves as the home page in the root of `content/`. As mentioned above, sections are ordered by their weights relative to other pages in their section. Sections are ordered against each other by the weight listed in the corresponding `_index.md`.

To add a new section, create a new directory under `content/` and add an `_index.md` file. You can also add any additional markdown files in that directory, as described above.


<!-- TBD: Git section on cloning, committing, and making PRs -->