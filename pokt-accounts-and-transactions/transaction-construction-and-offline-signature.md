# Transaction Construction

### Sending a Transaction

To send a transaction on the POKT blockchain:

```javascript
import { Pocket } from '@pokt-network/pocket-js'

const RECEIVER_ADDRESS = '...'
const SENDER_ADDRESS = '...'
const SENDER_PRIVATE_KEY = '...'

  // The passphrase used to encrypt the private key while in memory:
const PASSPHRASE = 'foobar'

// PocketJS must always be initialized with at least one dispatcher.
const POCKET_DISPATCHER = 'https://dispatch-1.nodes.pokt.network:4201'

// To send a transaction, you can use one of the public RPCs or
// your own Pocket node.
const POCKET_RPC = 'https://mainnet-1.nodes.pokt.network:4201'

const pocket = new Pocket(POCKET_DISPATCHER, POCKET_RPC)

// Create a transaction signer using the `withPrivateKey` method:
const txSigner = pocket.withPrivateKey(
  SENDER_PRIVATE_KEY
)

const transactionResponse = await txSigner.send(
  // Origin address for the send
  SENDER_ADDRESS, 
  // Receiver address
  RECEIVER_ADDRESS,
  // 10 POKT
  "10000000"
  ).submit(
    "mainnet",
    // The transaction fee is always 10,000 uPOKT
    "10000"
  )

// Check if the transaction returned an error:
if (typeGuard(transactionResponse, RpcError)) {
  throw new Error(transactionResponse.message)
}

// You will be able to look up this transaction through this hash after the 
// next block clears.
const { hash } = transactionResponse

console.log(hash)
```

### Creating a Signed SEND Transaction Offline

To create a signed transaction that can be sent immediately or stored:

```javascript
import { Pocket } from '@pokt-network/pocket-js'

const RECEIVER_ADDRESS = '...'
const SENDER_ADDRESS = '...'
const SENDER_PRIVATE_KEY = '...'

// The passphrase used to encrypt the private key while in memory:
const PASSPHRASE = 'foobar'

// PocketJS must always be initialized with at least one dispatcher.
const POCKET_DISPATCHER = 'https://dispatch-1.nodes.pokt.network:4201'
const pocket = new Pocket(POCKET_DISPATCHER)

// Create a transaction signer using the `withPrivateKey` method:
const txSigner = pocket.withPrivateKey(
  SENDER_PRIVATE_KEY
)

// Now use the tranasaction signer to create a signed SEND transaction
const txSignerWithSendTransaction = txSigner.send(
  // Origin address for the send
  SENDER_ADDRESS, 
  // Receiver address
  RECEIVER_ADDRESS,
  // 10 POKT
  "10000000"
)

// Send the transaction on POKT mainnet:
const sendTx = await txSignerWithSendTransaction.submit(
  "mainnet",
  // The transaction fee is always 10,000 uPOKT
  "10000"
)
```
