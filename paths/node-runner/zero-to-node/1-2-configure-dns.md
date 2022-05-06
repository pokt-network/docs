# 1-2: Configure DNS

Now that the Linode instance is created and running, you'll need to set up a DNS record that points to the IP address of the Linode instance.

Pocket nodes require a DNS name. DNS ([Domain Name Service](https://www.cloudflare.com/learning/dns/what-is-dns/)) names are used to map an IP address to more human-friendly names. So rather than referencing a server with an address like `134.23.153.21` we can use a name like `pokt001.pokt.run`.

{% hint style="info" %}
Most domain registrars allow you to add DNS records. Please refer to the DNS setup documentation for your provider.
{% endhint %}

Specifically, you'll need to add an `A` record for the domain name. For the exact steps, consult the DNS documentation for your provider. Then create a record with the following information:

- **Name**: `pokt001`
- **Type**: `A`
- **Value**: `{Linode_IP_Address}`
- **TTL**: `300`

After setting up your DNS record, wait a few minutes for the DNS to propagate. Then use the following command to check that the DNS record is working:

{% hint style="info" %}
The examples in this tutorial will use `pokt001` as the server on the `pokt.run` domain, so `pokt001.pokt.run` will be used as the DNS name. **Please replace this throughout with your own server and domain name.**
{% endhint %}

```bash
ping -c 3 pokt001.pokt.run
```

You should see a response that looks something like this:

```
64 bytes from 134.23.153.21: icmp_seq=0 ttl=47 time=92.403 ms
64 bytes from 134.23.153.21: icmp_seq=1 ttl=47 time=142.828 ms
64 bytes from 134.23.153.21: icmp_seq=2 ttl=47 time=182.456 ms
```

If the IP address matches the IP address of your Linode instance, you're all set!

{% hint style="info" %}
It can sometimes take longer than a minute for the DNS to propagate. So, be patient if things don't seem to work right away.
{% endhint %}
