# 2-3: Install Pocket

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
