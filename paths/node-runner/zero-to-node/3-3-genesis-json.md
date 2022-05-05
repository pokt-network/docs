# 3-3: Create genesis.json

When you start a pocket node for the first time it will need to find other nodes (aka: peers) to connect with. To do that we use a file named genesis.json with details about peers the node should connect to get on the network.

To create a json file with the genesis information, do the following:

1. Change to the `.pocket/config` directory:
    ```bash
    cd ~/.pocket/config
    ```
2. Use the following command to get the genesis.json file from GitHub:
    ```bash
    wget https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/mainnet/genesis.json genesis.json
    ```