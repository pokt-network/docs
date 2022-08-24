---
title: Initial Setup
menuTitle: Initial Setup
weight: 10
description: All of the tools needed to get started.
---

## Required Installations

There are only 2 tools needed to get started contributing to the documentation:

1. hugo version 0.93 or newer.
2. git

### Installing Hugo

For this guide, we're going to cover the easiest way to install hugo, which is
downloading an already built executable. If you would prefer to install from a
package manager like `brew`, `chocolately`, or `apt`, then you should follow
along with the corresponding [installation guide from hugo's
documentation](https://gohugo.io/getting-started/installing/).


First you'll want to navigate to the [releases page for hugo](https://github.com/gohugoio/hugo/releases). You'll be greeted with a bunch of text describing the latest release.

{{< figure src="/images/hugo-releases-1.png" alt="Releases Page" caption="**Note:** the version number might not match." >}}

From there you'll want to scroll down until you see a heading called **Assets**.

![Assets for download](/images/hugo-releases-2.png)

From here, you'll want to click on build for your system to download it.

{{< tabs >}}
{{% tab name="Windows" %}}

### Installing the Executable

If you're on a **Windows computer**, you need to know how many bits the
operating system is, and what kind of processor you're running.

If you're unsure of these things, you can find them by:

1. Opening the Settings App.
2. Navigate to *System*, then *About*
3. The details are available under the *System type* value.

Using those details you should install your corresponding version.

- 64-bit - x64: `hugo_<ver>_Windows-64bit.zip`
- 64-bit - ARM: `hugo_<ver>_Windows-ARM64.zip`
- 32-bit - x86: `hugo_<ver>_Windows-32bit.zip`
- 32-bit - ARM: `hugo_<ver>_Windows-ARM.zip`

Then make a new folder called `C:\Hugo\bin`.

Move the downloaded `.zip` file into the newly created `C:\Hugo\bin` folder.
Then double click on the `.zip` file and extract its contents. The folder should
now contain the following 3 new files:

- `hugo.exe`
- `LICENSE`
- `README.md`

From here, we're going to need to add hugo to your Windows PATH settings to know
that `hugo` means to run the `hugo.exe` program in this folder. To do this in
Windows 10, you'll need to go through the following steps:

1. Right click on the *Start* button.
2. Click on *System*.
3. Click on *Advanced System Settings*
4. Click on the button that says *Environment Variables...* on the bottom
5. Click on the button that says *Browse...*, and select the `C:\Hugo\bin` **folder**.
6. Click *OK* on all following windows.

### Using Package Managers

Alternatively, you can use the following if you have
[Chocolately](https://chocolatey.org/) installed.

```sh
choco install hugo -confirm
```

Or the following if you have [Scoop](https://scoop.sh/) installed.

```sh
scoop install hugo
```

{{% /tab %}}
{{% tab name="Mac" %}}

### Installing the Executable

If you're on a Mac with an **Intel Processor**, you should use `hugo_<ver>_macOS-64bit.tar.gz`.

If you're on a Mac with an **M1/M2 Processor**, you should use `hugo_<ver>_macOS-ARM64.tar.gz`.

Once you've downloaded the corresponding release, we'll need to open up a Terminal, and
start by making a folder for the hugo program.

```sh
mkdir -p ~/bin
```

Then we're going to navigate into it.

```sh
cd ~/bin
```

From here, we're going to extract the downloaded release into this folder.

```sh
tar -xvzf ~/Downloads/hugo_<ver>_macOS-<ARCH>.tar.gz
```

Where `<ver>` is going to match the version you downloaded, and `<ARCH>` will
match given then processor in your Mac.

After this, we're going to check if `hugo` is in your path by running:

```sh
which hugo
```

If there's no answer, that means we have to add it to your path.

First we'll need to see which shell you're working with by running:

```sh
echo $SHELL
```

If the answer is `zsh`, you'll want to run:

```sh
echo "export PATH=$PATH:$HOME/bin" >> ~/.zprofile
```

and if the answer is `bash` you'll want to run:

```sh
echo "export PATH=$PATH:$HOME/bin" >> ~/.bash_profile
```

Finally close your terminal. When opening a new terminal, hugo will be ready to
use.

### Using Package Managers

Alternatively, you can also run the following if you have
[Homebrew](https://brew.sh/) installed.

```sh
brew install hugo
```

Or the following if you have [MacPorts](https://www.macports.org/) installed.

```sh
port install hugo
```

{{% /tab %}}
{{% tab name="Linux/OpenBSD" %}}
If you're on Linux/OpenBSD, it's highly recommended you use a package manager install
hugo since it does not require a new install like in Windows and Mac.

### Debian, Ubuntu

```sh
snap install hugo
```

### Arch

```sh
sudo pacman -Syu hugo
```

### Fedora, Red Hat, CentOS

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

You'll want to download and install the corresponding [Git for Windows
Setup](https://git-scm.com/download/win), depending on if your system
is 32 or 64 bit. Instructions for how to do so can be found in the section
above for installing hugo.

{{% /tab %}}
{{% tab name="Mac" %}}

From a terminal run

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

## Recommended Installations

While this is everything you need to get up and editing the documentation site,
if you're used to working in something like Google Docs or Microsoft Word, I'd
recommend getting setup with an environment that will take care of content
editing, managing git changes, and running the hugo commands all in one place.
If you'd prefer to use your own tools, know that you'll be expected to do the
following:

- Start and stop the hugo live server from the command line.
- Manage git changes and commits from the command line.
- Edit Markdown files directly from a text editor, not a document editor like Word or Docs.

If you already have a text editor of choice, vim, emacs, sublime etc, I
recommend checking out the [following page for
plugins](https://gohugo.io/tools/editors/) that will help with working with
hugo.

If you don't have a text editor of choice, I'd recommend installing [Visual
Studio Code](https://code.visualstudio.com/). It comes built with the tools
we need to work with hugo and git without having to resort to a command line.

Once you have Visual Studio Code installed, you'll want to launch it and install
the following plugins:

- [Hugo Language and Syntax Support](https://marketplace.visualstudio.com/items?itemName=budparr.language-hugo-vscode)
- [Hugo Helper](https://marketplace.visualstudio.com/items?itemName=rusnasonov.vscode-hugo)

