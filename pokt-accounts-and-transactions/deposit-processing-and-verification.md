# Transaction Verification

### Confirming that Funds have been Received

```javascript
// The 64-character transaction hash is necessary to retrieve the transaction:
const tx = await pocket.query.getTX(hash)

if (typeGuard(tx, RpcError)) {
    throw new Error(tx.message)
  }

// The retrieved transaction object:
console.log(tx)
```

The return code of the transaction must be `0` — indicating success:

```
"tx_result": {
  "code": 0,
  "codespace": "",
  "data": null,
  "events": null,
  "info": "",
  "log": "",
  "message_type": "send",
  "recipient": "...",
  "signer": "..."
}
```

Consult the [error types in Pocket Core](https://github.com/pokt-network/pocket-core/blob/staging/x/auth/types/error.go) for information on failed transactions.
