---
description: Install all the necessary software for your node. Part 2 of 5 in the Zero to Node tutorial.
---

# Part 2: Software installation

This section will help you install all the necessary software for your node.


## Install dependencies

Now let's move on to the Pocket CLI installation.

At this point you should be logged in via SSH as the `pocket` user that we set up in a previous step. Before we install the Pocket software, we need to update the existing system packages and add a few dependencies.

### Updating system packages

1. Update the repository index with the following command:
    ```bash
    sudo apt update
    ```
2. Update the distribution with the following command:
    ```bash
    sudo apt dist-upgrade -y
    ```

After the update completes, we're ready to install the dependencies.

### Installing dependencies

There are a handful of dependencies but installing them won't take long. Also, some might already be installed. So if one of the dependencies exists, you can just move on to the next one.

#### git

```bash
sudo apt-get install git -y
```

#### build tools
```bash
sudo apt-get install build-essential -y
```

#### curl
```bash
sudo apt-get install curl -y
```

#### file
```bash
sudo apt-get install file -y
```

#### nginx
```bash
sudo apt install nginx -y
```

#### certbot
```bash
sudo apt install certbot -y
```

#### python3-certbot-nginx
```bash
sudo apt-get install python3-certbot-nginx -y
```

#### jq
```bash
sudo apt install jq -y
```


## Install Go

After installing the dependencies, there is one more dependency we'll need to add, and that's Go. Go (sometimes known as "Golang") is the programming language that the Pocket software was written in.

We could install Go using `apt`, but we want to get the latest stable version which probably isn't available by default in the `apt` repository. So, we'll use the steps below to install Go.

1. Make sure you're in the pocket home directory.
    ```bash
    cd ~
    ```
2. Find the latest version of Go from https://golang.org/dl/ then download it with the following command. (Make sure to change the link below to point to the correct version of Go.)
    ```bash
    wget https://dl.google.com/go/go1.17.7.linux-amd64.tar.gz
    ```
3. Extract the archive:
    ```bash
    sudo tar -xvf go1.17.7.linux-amd64.tar.gz
    ```
4. Set permissions on the extracted files:
    ```bash
    sudo chown -R pocket ./go
    ```
5. Add Go to the `PATH`:
    ```bash
    echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.profile
    ```
6. Set the `GOPATH` and `GOBIN` environment variables:
    ```bash
    echo 'export GOPATH=$HOME/go' >> ~/.profile
    ```
    ```bash
    echo 'export GOBIN=$HOME/go/bin' >> ~/.profile
    ```
7. Reload your `.profile`:
    ```bash
    source ~/.profile
    ```
8. Verify the installation:
    ```bash
    go version
    ```
    You should see something like this:
    ```bash
    go version go1.17.7 linux/amd64
    ```
    Make sure the version number matches the version you downloaded. If the `go version` command doesn't work, try logging out and logging back in.
9. Verify the `GOPATH` and `GOBIN` variables are set correctly:
    ```bash
    go env
    ```
    You should see the `GOPATH` and `GOBIN` variables set correctly.


## Install Pocket

After you can verify that you have the latest stable version of Go, we're ready to install the Pocket software.

We'll be downloading [Pocket Core](https://docs.pokt.network/core/) from GitHub and then compiling it with Go to get it fully installed.

To download and install Pocket Core, do the following:

1. Create a project directory:
    ```bash
    sudo mkdir -p $GOPATH/src/github.com/pokt-network
    ```
2. Change to the project directory:
    ```bash
    cd $GOPATH/src/github.com/pokt-network
    ```
3. Clone the Pocket Core repository:
    ```bash
    sudo git clone https://github.com/pokt-network/pocket-core.git
    ```
4. Change to the code directory:
    ```bash
    cd pocket-core
    ```
5. Checkout the latest version. You can find the latest tag by going to https://github.com/pokt-network/pocket-core/tags.
    ```bash
    sudo git checkout tags/RC-0.8.2
    ```
6. Build project code:
    ```bash
    go build -o $GOPATH/bin/pocket $GOPATH/src/github.com/pokt-network/pocket-core/app/cmd/pocket_core/main.go
    ```
7. Test that the build succeeded:
    ```bash
    pocket version
    ```

That's it for the software installation. Now let's move on to the Pocket core configuration.
