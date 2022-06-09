# Get An Endpoint

## Pocket Portal

The [Pocket Portal](https://www.portal.pokt.network) lets you create an endpoint for the chain you want in just a few clicks and provides you with the features you've come to expect in centralized API services, such as usage/uptime metrics and notifications/alerts.

### Setup Guide

Go to the [Pocket Portal](https://www.portal.pokt.network), sign up and verify your email.

![](../assets/portal-login.png)

Once you've done so, log in and you'll be greeted by the Network Overview section.

![](../assets/portal-network.png)

{% hint style="info" %}
In this section, you'll see all the important parts of the network: how many relays are being served daily, the overall success rate of the network, and the number of apps, nodes, and POKT staked. A summary of chains being served by the network is also available.
{% endhint %}

Head over to the "My Apps" section and create your app.

![](../assets/portal-app-setup.png)

{% hint style="info" %}
In this section, you'll be able to select one of the available chains that are currently available. More will be made available depending on demand.
{% endhint %}

Once you've hit "Launch Application", all is done and you can start using your endpoint! You should be greeted by the main application screen, which will show all the metrics, which as soon as you start submitting requests, should start appearing.

![](../assets/portal-app.png)

The view you see is the main view for your application. Here, you'll see key details:

* On the top left, you'll see and will be able to copy your endpoint URL.
* On the right, first you'll see key information about your Pocket application:
  * The **app status**, which indicates if the app is currently staked or unstaked. The app must be staked in order to be eligible for service.
  * The **amount of POKT** staked, which will be enough to add up to the free tier.
  * The **max amount of relays you can send per day,** which currently is 1M as per the free tier.
* On the bottom right, you'll see important identifying information:
  * The **Gateway ID,** used by the Dashboard to fetch your app's information. It's part of your endpoint URL as well.
  * The **App's public key**, which will let you inspect your application on-chain.
  * The **Secret Key**, which is a security feature you can use to make your Pocket Dashboard endpoint more secure.
* On the left side, you'll see all the metrics available for your app.

### Setting Up Notifications

Turning on notifications is a great way to stay up to date with your app. We respect our users' privacy, and therefore we only send important emails, such as usage notifications. To activate them:

* Click on the "Notifications" button on your app's dashboard, and you'll see the notifications screen.
* Turn on any notifications you're interested in receiving, and then click "Save changes" when you're done.

![](../assets/portal-notifications.png)

### Securing your Application

For securing your endpoint, you can go to the "App Security" section of the Portal. This section of the app contains all the security settings you'll have at your disposal for security. We provide whitelisting for both origins and user agents and also let you enable and disable secret key usage.

#### Whitelisting User Agents

Mainly useful for mobile apps, whitelisting user agents lets you limit requests to only the ones you've put in the whitelist. An example user agent would be `com.example.bobapp`. This would let Bob's mobile app use the endpoint as his user agent would be whitelisted. If Alice, with user agent `com.example.aliceapp` tried to use the endpoint, she wouldn't be able to, as her requests would be blocked before they're sent to the network.

#### Whitelisting Origins

To whitelist origins, just write the URL of the domain you want to allow. All requests from other domains will be blocked. This is a very effective way to only use your app in production, staging, or test environments and to stop malicious users from stealing your endpoint and using it in their project.

For origins, we support wildcard domains as well as normal domains. An example URL would be `https://portal.pokt.network`.

#### Using your Secret Key

Every application has a secret key associated with it, which can be enabled so that every request has to send it using [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) to be accepted. An example cURL request with the secret key enabled would be:

{% tabs %}
{% tab title="macOS/Linux" %}
```
curl --user :YOUR-SECRET-KEY \\
...
https://<NETWORK>.gateway.pokt.network/v1/YOUR-GATEWAY-ID
```
{% endtab %}

{% tab title="Windows" %}
```
curl --user :YOUR-SECRET-KEY ^
...
https://<NETWORK>.gateway.pokt.network/v1/YOUR-GATEWAY-ID
```
{% endtab %}
{% endtabs %}

This is a truncated example of a call that does not actually send a request. See below for a more detailed example.

### Testing your Endpoint

Once you've set up your endpoint as per your liking, you can test it however you'd like. In the main application view of the dashboard, you'll be able to see and copy your endpoint to the clipboard. The way endpoints are used in terms of content sent in the body will depend on the chain.

For EVM-based chains (Ethereum, BSC, and others), which see the majority of traffic in Pocket Network, you can refer to the official [JSON-RPC](https://ethereum.org/en/developers/docs/apis/json-rpc/#json-rpc-methods) specification. Below we have a few examples of requests for Pocket compatible chains.

#### Ethereum, BSC and EVM-based chains

{% tabs %}
{% tab title="macOS/Linux" %}
```
curl -X POST \\
-H "Content-Type: application/json" \\
--data '{"jsonrpc": "2.0", "id": 1, "method": "eth_blockNumber", "params": []}' \\
"https://<NETWORK>.gateway.pokt.network/v1/<YOUR-GATEWAY-ID>"
```
{% endtab %}

{% tab title="Windows" %}
```
curl -X POST ^
-H "Content-Type: application/json" ^
--data "{\"jsonrpc\": \"2.0\", \"id\": 1, \"method\": \"eth_blockNumber\", \"params\": []}" ^
"https://<NETWORK>.gateway.pokt.network/v1/<YOUR-GATEWAY-ID>"
```
{% endtab %}
{% endtabs %}

#### How Endpoints are Constructed

All endpoints have a similar structure, as they all have:

* The network prefix; see the RelayChainIDs [here](../supported-blockchains.md)
* The main URL (`gateway.pokt.network/v1/`)
* If it's a load-balanced endpoint, it will also have the LB prefix (`/lb/`)
* The Gateway ID.

### Switching Chains

If you ever need to switch chains for your endpoint, you have the ability to do so once a week. Click on the "Switch chains" button to do so.

### Earn Trophies, Join the DAO

You can earn a [vote in the DAO](../community/governance/README.md) and help shape the future of Pocket Network, including deciding which ecosystem tooling our treasury supports and how we configure important on-chain parameters such as the cost of a relay.

Once you've sent 1k relays through the Portal, join our [Discord](https://discord.gg/uCZZkHTQjV) and report this in the [🏆trophies](https://discord.com/channels/553741558869131266/763504639299289138) channel.

This is your first trophy on the path to earning a vote in the DAO on the [App Developer path](../node/trophies/app-developers.md):


## ♦ Use EthersJS

You can use Pocket as your node provider with this complete and compact Ethereum library

First, you need to get an endpoint from the [Pocket Portal](https://www.portal.pokt.network).

Then you need to get the Gateway ID

![](../assets/portal-app.png)

and insert it like so

```
ethers.providers.PocketProvider('homestead', process.env.GatewayID)
```


## 📲 Endpoint FAQ

### I just want an endpoint, where can I get one?

The [Pocket Portal](https://www.portal.pokt.network/) stakes on your behalf and generates the endpoint you need.

### How does the Pocket Portal work?

The Pocket Portal is tasked with connecting to the Pocket Network through PocketJS on your behalf—essentially doing the integration work for you. The only thing that changes here is the layer of abstraction between you, the developer, and the nodes. You are still ultimately being served by a decentralized network of thousands of nodes.

### Is there a more "decentralized" solution?

Yes! You can integrate with [PocketJS](https://docs.pokt.network/js/) directly, which would be the most censorship-resistant way to connect to our network of full nodes. All of the functionality we built into the Pocket Portal, including "load-balanced" endpoints, are 100% reproducible using only PocketJS. In fact, we anticipate competing dashboards to emerge. Get started with PocketJS at the link below:

### What does it mean for an endpoint to be "load-balanced"?

This means that there's more than one Application behind your endpoint, where an Application is defined as the account staking into the network for the purpose of submitting relay requests. For each request you need to submit, one of these app stakes gets chosen pseudorandomly and is used to make the request to the network. We have several algorithms in place to cherry-pick the best-performing app stakes for each session, based on the nodes they've been matched with, and ensure the best QoS.

### What can I do if I exceed my allotted requests?

If you ever exceed the amount of daily \(or per-session\) amount of requests, contact the sales team or jump into our Discord to let us know; we'll work something out!

