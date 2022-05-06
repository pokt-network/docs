# 2-2: Install Go

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
    Make sure to change the link to point to the latest version of Go you find at the above URL.
3. Extract the archive:
    ```bash
    sudo tar -xvf go1.17.7.linux-amd64.tar.gz
    ```
    Make sure to change the command to point to the version of Go you downloaded in the previous step.
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
