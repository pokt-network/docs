---
description: Install all the necessary software for your node. Part 2 of 5 in the Zero to Node tutorial.
---

# Software installation

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
2. Find the latest version of Go from https://golang.org/dl/ then download it with the following command:
    ```bash
    wget https://dl.google.com/go/go1.17.7.linux-amd64.tar.gz
    ```
    {% hint style="info" %}
    Make sure to change the link to point to the latest version of Go you find at the above URL.
    {% endhint %}

3. Extract the archive:
    ```bash
    sudo tar -xvf go1.17.7.linux-amd64.tar.gz
    ```
    {% hint style="info" %}
    Make sure to change the command to point to the version of Go you downloaded in the previous step.
    {% endhint %}

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
    {% hint style="info" %}
    Make sure the version number matches the version you downloaded.
    {% endhint %}
    {% hint style="info" %}
    If the `go version` command doesn't work, try logging out and logging back in.
    {% endhint %}
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
5. Checkout the latest version:
    ```bash
    sudo git checkout tags/RC-0.8.2
    ```
    {% hint style="info" %}
    You can find the latest tag by going here: https://github.com/pokt-network/pocket-core/tags
    {% endhint %}
6. Build project code:
    ```bash
    go build -o $GOPATH/bin/pocket $GOPATH/src/github.com/pokt-network/pocket-core/app/cmd/pocket_core/main.go
    ```
7. Test that the build succeeded:
    ```bash
    pocket version
    ```


## Create a Pocket wallet account

At this point we have all the software we need to run our Pocket node, but we'll need to configure it first.

Pocket nodes are associated with a Pocket wallet account. This is the account that will be used to send and receive transactions. You can either create a new account using the Pocket CLI we just installed, or you can use an existing account. For this guide, we'll be creating a new account.

### Creating an account

To create an account, run the following command:

```bash
pocket accounts create
```

You'll be prompted to set a passphrase for the account. You can use any passphrase you like but for security reasons, it's best to use a passphrase that is at least 12 characters long, preferably longer.

### Listing accounts

After you've created the account you can use the `pocket accounts list` command to confirm that the account was added successfully.

```bash
pocket accounts list
```

### Setting the validator address

Next, to set the account as the one the node will use, run the following command:

```bash
pocket accounts set-validator {YourAccountAddress}
```

### Confirm the validator address

Finally, you can confirm that the validator address was set correctly by running the following command:

```bash
 pocket accounts get-validator
```

That's it for the account setup. Now let's move on to the Pocket core configuration.
