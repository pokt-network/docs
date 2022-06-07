# Transaction Construction

## Sending a Transaction

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

// If you are using Pocket Mainnet, make sure to disable legacyCodec
pocket.configuration.useLegacyTxCodec = false;

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
  '10000000'
  ).submit(
    'mainnet',
    // The transaction fee is always 10,000 uPOKT
    '10000'
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

## Creating a Signed SEND Transaction Offline

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

// If you are using Pocket Mainnet, make sure to disable legacyCodec
pocket.configuration.useLegacyTxCodec = false;

// Create a transaction signer using the `withPrivateKey` method:
const txSigner = pocket.withPrivateKey(
  SENDER_PRIVATE_KEY
)

// Now use the transaction signer to create a signed SEND transaction
const txSignerWithSendTransaction = txSigner.send(
  // Origin address for the send
  SENDER_ADDRESS, 
  // Receiver address
  RECEIVER_ADDRESS,
  // 10 POKT
  '10000000'
)

// Generate offline signed send transaction
const sendTx = await txSignerWithSendTransaction.createTransaction(
  'mainnet',
  // The transaction fee is always 10,000 uPOKT
  '10000'
)

console.log('Offline signed send transaction:', sendTx)
```

After calling `.sendTransaction()`, you will get back a response with this format:

```json
RawTxRequest {
  address: "1e829f34ce5533c913638310408632242f6fbd43",
  txHex: "d1010a4....bf8970d"
}
```

## Calculate transaction hash from raw transaction bytes

```javascript
const crypto = require('crypto');

// This is the raw transaction bytes obtained from offline signed transaction
const txHex = 'd1010a4....bf8970d'

const txHash = crypto.createHash('sha256').update(Buffer.from(txHex, 'hex')).digest('hex');

console.log(txHash)
```

## Deserialize offline signed SEND transaction

You can also decode the raw transaction bytes generated offline (only works for SEND transactions):

```javascript

// Only supported for versions >= 0.7.1
const { ProtoTxDecoder } = require('@pokt-network/pocket-js')

const ENCODED_TX_BYTES = Buffer.from('d1010a4....bf8970d', 'hex')

const protoTxDecoder = await pocket.withProtoTxDecoder()

const protoStdTx = await protoTxDecoder.unmarshalStdTx(ENCODED_TX_BYTES)
  
const data = await protoTxDecoder.decodeStdTxData(protoStdTx)

console.log('Deserialized transaction:', data)
```
