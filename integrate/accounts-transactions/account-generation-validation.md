---
description: Generate and validate accounts on the native POKT blockchain.
---

# Account Generation and Validation

The simplest way to generate new accounts, or addresses, on the POKT blockchain is to use the official Pocket client, [PocketJS](https://github.com/pokt-network/pocket-js).

## Creating a New Account

To create a new account on the POKT blockchain and export it:

```typescript
import { Pocket } from '@pokt-network/pocket-js'

// PocketJS must always be initialized with at least one dispatcher.
const POCKET_DISPATCHER = 'https://dispatch-1.nodes.pokt.network:4201'
const pocket = new Pocket(POCKET_DISPATCHER)

// The passphrase used to encrypt the private key while in memory:
const PASSPHRASE = 'foobar'
const account = await pocket.keybase.createAccount(PASSPHRASE)

// The result of successful account creation:
console.log(account)

// Using the exportAccount function, you can obtain a plaintext private key.
const exportedAccountPrivateKey = await pocket.keybase.exportAccount(
  account.address.toString('hex'),
  PASSPHRASE
)

// This plaintext private key should be encrypted before storage.
console.log(exportedAccountPrivateKey.toString('hex'))

// You can also export an encrypted JSON version of the same private key.
// The passphrase used to encrypt this JSON file is separate from the 
// previous PASSPHRASE.
const exportedPPK = await pocket.keybase.exportPPK(
  exportedAccountPrivateKey,
  // The PPK passphrase used to encrypt the JSON file
  'foo',
  // A hint for the PPK passphrase
  'what comes before bar'
)

console.log(exportedPPK)
```

## Importing an Existing Account

To import an existing account using either the raw private key or the encrypted JSON PPK:

```javascript
import { Pocket } from '@pokt-network/pocket-js'

// PocketJS must always be initialized with at least one dispatcher.
const POCKET_DISPATCHER = 'https://dispatch-1.nodes.pokt.network:4201'
const pocket = new Pocket(POCKET_DISPATCHER)

// The passphrase used to encrypt the private key while in memory:
const PASSPHRASE = 'foobar'
const PRIVATE_KEY = '...'

// Import an existing account using the raw private key:
const importedAccount = await pocket.keybase.importAccount(
  PRIVATEKEY,
  // The passphrase to encrypt the private key while in memory
  PASSPHRASE
)

// Import an account using the encrypted JSON PPK:
const importedPPKAccount = await pocket.keybase.importPPK(
  // The PPK passphrase used when the key was exported
  'foo',
  exportedPPK.salt,
  exportedPPK.secParam,
  exportedPPK.hint,
  exportedPPK.cypherText,
  // The passphrase to encrypt the private key while in memory
  PASSPHRASE,
)
```

## Verifying an Address

To verify a POKT blockchain address, public key, or raw private key:

```javascript
import { 
  validateAddressHex, 
  validatePrivateKey, 
  validatePublicKey 
} from '@pokt-network/pocket-js'

// Validate a POKT blockchain address: returns undefined if valid.
// This should be wrapped in a try / catch block as it will throw the 
// appropriate error if the address is not valid.
try {
  const isValidAddress = !(
    validateAddressHex(account.addressHex) instanceof Error
  )
} catch (e) {
  // Handle the error
}

// Validate a public key: returns true or false.
const isValidPublicKey = validatePublicKey(account.publicKey.toString('hex'))

// Validate a private key: returns true or false.
const isValidPrivateKey = validatePrivateKey(privateKey)
```
