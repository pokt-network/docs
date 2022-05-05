---
description: Pocket nodes require a DNS name.
---

# 1-2: Configure DNS

Pocket nodes require a DNS name. DNS ([Domain Name Service](https://www.cloudflare.com/learning/dns/what-is-dns/)) names are used to map an IP address to more human-friendly names. So rather than referencing a server with an address like `134.23.153.21` we can use a name like `pokt001.pokt.run`.

{% hint style="info" %}
 Most domain registrars allow you to add DNS records. The steps are similar but refer to the DNS setup documentation for your provider.
{% endhint %}

Specifically, you'll need to add an `A` record for the domain name. For the exact steps, consult the DNS documentation for your provider. Then create a record with the following information:

- **Name**: `pokt001`
- **Type**: `A`
- **Value**: `{Linode_IP_Address}`
- **TTL**: `300`

After setting up your DNS record, wait a few minutes for the DNS to propagate. Then use the following command to check that the DNS record is working:

> NOTE: Replace the hostname in the following command with the hostname of your DNS record. Also, it can sometimes take longer than a minute for the DNS to propagate. So, be patient if things don't seem to work right away.

```bash
ping -c 3 pokt001.pokt.run
```
You should see a response that looks something like this:

```
64 bytes from 134.23.153.21: icmp_seq=0 ttl=47 time=92.403 ms
64 bytes from 134.23.153.21: icmp_seq=1 ttl=47 time=142.828 ms
64 bytes from 134.23.153.21: icmp_seq=2 ttl=47 time=182.456 ms
```

If the IP address matches the IP address of your Linode, you're all set!

Now that we have a DNS record setup, we will look at using SSH to login and continue the setup process.