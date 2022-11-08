---
title: Java – Web3j
menuTitle: Java – Web3j
description: Web3j is a Java and Android library for interacting with ethereum nodes.
---

## Overview

{{< description >}}

## Resources

- [Documentation](https://docs.web3j.io/4.8.7/)
- [Installation Guide](https://docs.web3j.io/4.8.7/quickstart/)

## Basic Usage

{{< expand title="Supported Chains" >}}
{{< supported-chains "evm" >}}
{{</ expand >}}

```java
import org.web3j.protocol.Web3j;
import org.web3j.utils.Convert;
import org.web3j.protocol.http.HttpService;
import org.web3j.protocol.core.DefaultBlockParameterName;
import org.web3j.protocol.core.methods.response.EthGetBalance;
import java.math.BigInteger;
import java.math.BigDecimal;
import java.io.IOException;

class Main
{
    public Main(){}

    public void GetAccountBalance()
    {
        String URL = "https://<PREFIX>.gateway.pokt.network/v1/lb/<PORTAL-ID>";
        String ACCOUNT = "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae";
       Web3j web3j = Web3j.build(new HttpService(URL));

       try {
          EthGetBalance ethGetBalance = web3j.ethGetBalance(ACCOUNT,               DefaultBlockParameterName.LATEST).send();

          BigInteger balance = ethGetBalance.getBalance();

          System.out.println("Balance in Wei: " + balance);

          BigDecimal etherAmount = Convert.fromWei(balance.toString(),             Convert.Unit.ETHER);
          System.out.println("Balance in Ether :" + etherAmount);
       }
       catch(IOException e) {
          // Code to handle an IOException here
           return;
         }


    }

    public static void main(String[] args)
    {
        //GetAccountBalance();
    }
}
```
