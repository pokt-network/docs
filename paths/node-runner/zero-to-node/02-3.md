# 2-3: Install Pocket

Now we're ready to install the Pocket software. We'll be downloading [Pocket Core](https://docs.pokt.network/core/) from GitHub and then compiling it with Go to get it fully installed.

To download and install Pocket Core, do the following:

1. Create a project directory
    ```bash
    sudo mkdir -p $GOPATH/src/github.com/pokt-network
    ```
2. CD to the project directory
    ```bash
    cd $GOPATH/src/github.com/pokt-network
    ```
3. Get the Pocket Core code
    ```bash
    sudo git clone https://github.com/pokt-network/pocket-core.git
    ```
4. CD to the code directory
    ```bash
    cd pocket-core
    ```
5. Checkout the latest version
    ```bash
    sudo git checkout tags/RC-0.7.1
    ```
6. Build project code
    ```bash
    go build -o $GOPATH/bin/pocket $GOPATH/src/github.com/pokt-network/pocket-core/app/cmd/pocket_core/main.go
    ```
7. Test the installation
    ```bash
    pocket version
    ```

At this point we have all the software we need to run our Pocket node. But we'll need to configure it first. We'll start that next.