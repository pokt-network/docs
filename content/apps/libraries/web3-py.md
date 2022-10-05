---
title: Python – Web3.py
menuTitle: Python – Web3.py
description: Web3.py is a Python library for interacting with Ethereum nodes; it originally began as a port of web3.js, but has evolved to better serve the needs of Python developers.
---

## Overview

{{< description >}}

## Resources

- [Documentation](https://web3py.readthedocs.io/en/stable/)
- [Installation Guide](https://web3py.readthedocs.io/en/stable/quickstart.html)

## Basic Usage

{{< expand title="Supported Chains" >}}
{{< supported-chains "evm" >}}
{{</ expand >}}

```python
from web3 import Web3

POCKET_URL = "https://<PREFIX>.gateway.pokt.network/v1/lb/<PORTAL-ID>"

provider = Web3(Web3.HTTPProvider(POCKET_URL))

print(provider.blockNumber)
```
