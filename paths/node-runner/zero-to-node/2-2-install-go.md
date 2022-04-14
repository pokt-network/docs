# 2-2: Install Go

Go is the programming language that the Pocket software was written in. So, you'll need to install Go. We could install it using `apt` but we want to get the latest stable version which probably isn't available by default in the `apt` repository. So, we'll use the steps below to install Go.

1. Make sure you're in the pocket home directory.
    ```bash
    cd ~
    ```

2. Find the latest version of Go from https://golang.org/dl/ then download it with the following command:
    ```bash
    wget https://dl.google.com/go/go1.17.7.linux-amd64.tar.gz
    ```

    > Note: Change `go1.17.7.linux-amd64.tar.gz` to the most recent version of Go.

3. Extract the archive
    ```bash
    sudo tar -xvf go1.17.7.linux-amd64.tar.gz
    ```

4. Set permissions on the extracted files
    ```bash
    sudo chown -R pocket ./go
    ```

5. Set the `PATH` variable
    ```bash
    echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.profile
    ```

6. Set the `GOPATH` and `GOBIN` variables
    ```bash
    echo 'export GOPATH=$HOME/go' >> ~/.profile
    ```

    ```bash
    echo 'export GOBIN=$HOME/go/bin' >> ~/.profile
    ```

7. Source the `.profile`
    ```bash
    source ~/.profile
    ```

8. Verify the installation
    ```bash
    go version
    ```

    You should see something like:

    ```bash
    go version go1.17.7 linux/amd64
    ```

    > Note: Make sure the version matches the version you downloaded.

    {% hint style="info" %}
    If `go version` doesn't work try logging out and logging back in. Then test the `go version` command again.
    {% endhint %}

9. Verify the `GOPATH` and `GOBIN` variables are set correctly
    ```bash
    go env
    ```

    You should see the `GOPATH` and `GOBIN` variables set correctly.

After you can verify that you have the latest stable version of Go, you're ready to continue.