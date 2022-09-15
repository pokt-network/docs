---
title: Get An Endpoint
menuTitle: Get An Endpoint
weight: 10
aliases:
  - /resources/faq/app-integration
  - /home/resources/faq/app-integration
  - /paths/app-developer/use-ethersjs
  - /home/paths/app-developer/use-ethersjs
  - /paths/app-developer
  - /home/paths/app-developer
  - /home/use/get-endpoint
description: Use the Pocket Portal to "mint" endpoints you can use in your decentralized applications to connect to the blockchain of your choice.
---

In order to take advantage of Pocket's network of thousands of decentralized nodes, you need to get an endpoint that you can use in your application.

You can create your own using the **Pocket Portal**.

The [Pocket Portal](https://www.portal.pokt.network) is a gateway to a decentralized RPC network, where developers can create ("mint") blockchain network endpoints for use in their applications. Portal users can also monitor network performance and configure custom security features around their endpoint.

In this way, the Pocket Portal provides similar functionality to more centralized API services, all while retaining the decentralization that Pocket Network is built on.

The Portal has two usage tiers, an Always Free tier that allows for up to 250,000 relays per day, and a Pay As You Go tier that also offers relays beyond that with a nominal fee. 

![](/images/portal.png)

**Jump to:**

* [**Create an account**](#create-an-account)
* [**Explore the Portal**](#explore-the-portal)
* [**Test Your Endpoint**](#test-your-endpoint)

## Create an account

To use the Pocket Portal, you must first create an account.

The Portal accepts two different methods of account creation and authentication:

* Using your email address
* Using your [GitHub](https://github.com) account

{{% notice style="warning" %}}
Once you create an account with one login method, you can't switch to another method with that account, so make sure you choose the method that works best for you.
{{% /notice %}}

### Sign up with email

From the main [Pocket Portal](https://www.portal.pokt.network) page:

1. Click **Get Started** at the bottom of the page. Alternatively, you can click **Sign Up** at the top right.

2. On the sign up page, enter your email address and a password. When done, click **Continue**.

   ![](/images/portal-signup.png)

   {{% notice style="info" %}}
   Your password must contain at least 8 characters, and at least 3 of the following character types: lower case letters, upper case letters, numbers, and special characters. If your password does not meet these requirements, the failing criteria will be displayed on the screen.
   {{% /notice %}}

3. On the next screen, click **Accept** to authorize the app to allow access to your newly-created account.

   ![](/images/portal-authorize.png)

4. You will then be sent a verification email to the address you entered above. Open this email, and click **Confirm Email Address**.

   ![](/images/portal-emailconfirmation.png)

   {{% notice style="info" %}}
   When you click this link, you will be taken to the main Portal homepage. You will know that verification succeeded because you will receive a subsequent email confirming your registration.
   {{% /notice %}}

5. You can now log in. Click the **Log In** button and you will be taken to the Login page. Enter your credentials as previously given and click **Continue**.

Continue below at [Explore the Portal](#explore-the-portal).

### Sign up with GitHub

You can also log in the Portal using your existing GitHub account.

1. Click **Get Started** at the bottom of the page. Alternatively, you can click **Sign Up** at the top right.

2. Click **Continue with GitHub**.

   ![](/images/portal-signup-github.png)

3. On the next screen, click **Accept** to authorize the app to allow access to your GitHub account.

   ![](/images/portal-authorize.png)

4. You will then be logged in and taken to the Network Overview page. You will also receive an email confirming your registration.

Continue below at [Explore the Portal](#explore-the-portal).


## Explore the Portal

Once you've logged in, you'll be taken to the **Network** page (also known as the **Dashboard**).

### Network Summary

![](/images/portal-networksummary.png)

In this section, you'll see all the important parts of the Pocket network: how many nodes are staked on the network, blockchains supported, number of relays served over time, latest block details, and much more.

To search for a specific chain and its details, the **Available Networks** section has a search box where you can type in the name of a chain you would like to see.

![](/images/portal-availablenetworks.png)

### Apps and Endpoints

Your Portal account is organized into Applications (Apps), which are subdivided into Endpoints.

* An **App** is a project or container that allows you to view network throughput and relays across multiple blockchains.
* An **Endpoint** is the RPC URL that connects to a specific blockchain via Pocket's network of decentralized nodes.

**Your account can contain a maximum of two Apps, and each App can contain any number of Endpoints for any number of chains.**

### Usage Tiers

**Pocket Portal allows you to have 250,000 blockchain relays per App daily, absolutely free.**

For many users, this is probably all you need. For others, especially with production-ready apps, you may wish to have more usage on-demand.

With both of these cases in mind, Pocket Portal offers two tiers: **Always Free** and **Pay As You Go**.

* **Always Free**: Provides 250,000 relays per App per day, through any combination of Endpoints.
* **Pay As You Go**: Also provides the same 250,000 relays per App per day, through any combination of Endpoints. However, should your App request more than this in a day, you will be charged a per-relay usage fee.

You can always switch between tiers. If you are hitting your limits in the Always Free tier, you can Upgrade to the Pay As You Go tier. And if you don't need or want the extra daily relays, you can downgrade to the Always Free tier.

{{% notice style="info" %}}
The Portal has overflow protection in case an App in the Always Free plan accidentally goes over 250,000 relays in a day. All surplus relays are served by our backup infrastructure, ensuring no service interruptions. This is only a temporary measure, so the app owner should upgrade the plan to Pay As You Go or contact sales for an enterprise plan.
{{% /notice %}}

If your App doesn't hit the 250,000 relay cap, the tiers are identical; the only difference is that you will be asked to enter your payment information during the creation of the App (or during the Upgrade process).

### Calculate usage

On the page where you create your app, there is a pricing calculator that allows you to estimate what the costs could be, given a certain number of relays per day.

For example, 500,000 daily relays at a price per relay of $0.000007456 would cost approximately $56.68 per month.

![](/images/portal-calculatepricing.png)

{{% notice style="info" %}}
This is necessarily an estimate, as the way the relays vary over a period of time will affect the total cost. To take a simple example, if 1,000,000 relays were to happen in a single day, there would be a charge for 750,000 relays, but if those 1,000,000 relays were spread out equally over four days, there wouldn't be a charge, due to the 250,000 free relays per day.
{{% /notice %}}

If your App uses less than 250,000 relays per day, across all of your Endpoints, you will not be charged.


### Create an App

When you first create an account on the Pocket Portal, you will have no Apps, so the first thing to do is to create one.

Click the **Apps** link on the top bar to go to its section. This is where you manage your Apps.

To create a new App:

1. Click **Create New Application**.

2. Enter a name for your App (which can be anything, as it's just a container).

3. Choose your tier: **Pay As You Go** or **Always Free**.

   {{% notice style="info" %}}
   See the section on [Usage Tiers](#usage-tiers) for the differences between the two tiers.
   {{% /notice %}}

   ![](/images/portal-tiers.png)

4. When finished, click **Create App**.

5. If you chose the Always Free tier, you will be taken to the [App overview](#app-overview) section.

6. If you chose the Pay As You Go tier, you will be redirected to a checkout page. Enter your payment information and click **Subscribe**. You will then be taken to the App overview section.

   ![](/images/portal-checkout.png)

Congratulations! You have created an App and are ready to start connecting to Pocket's network of decentralized infrastructure. You can find a list of your Apps by clicking the **Apps** link on the top bar.

![](/images/portal-apps.png)


### App Overview

Clicking one of your Apps in the list takes you to the App Overview page.

The App Overview displays all the metrics associated with your App. The charts will start being populated as soon as you start submitting requests through an Endpoint associated with your App.

![](/images/portal-appoverview.png)

You'll see key details:

* **Endpoints**: List of Endpoints associated with the App, from the list of [supported blockchains](/supported-blockchains). Any number of Endpoints can be created for a given App. 
* **Portal ID**: Unique identifier for the App. This string is included as part of the URL for each Endpoint.
* **Secret Key**: Security feature for Apps. If "Private Secret Key Required" is selected in the [Security](#security) section, the Secret Key will need to be sent along with the request using HTTP Basic Authentication.
* **Public Key**: Unique identifier for a given App that will allow you to inspect the App on-chain.

### Manage Endpoints

Every App gets created with Ethereum Mainnet as its single Endpoint.

To add a new Endpoint to your App:

1. Click **Add New** in the Endpoint section.

2. In the box that appears, click the name of the chain you wish to connect to. You may also use the search box to narrow down the choices.

   ![](/images/portal-addchain.png)

The new Endpoint will then appear in the list.

![](/images/portal-newchainsadded.png)

To delete an Endpoint, click the trash can icon next to the Endpoint.

All Endpoints have a similar URL structure:

```
https://<NETWORK>.gateway.pokt.network/v1/lb/<YOUR-PORTAL-ID>
```

* The network prefix. You can find them on the list of [supported blockchains](/supported-blockchains) in the column **Portal API Prefix**. For example, Ethereum Mainnet is `eth-mainnet`.
* The main URL (`gateway.pokt.network/v1/`)
* If it's a load-balanced endpoint (and most of them are), it will also have the `/lb/` prefix.
* The Portal ID, which is unique to your App.


### Requests

The **Requests** page for a given App shows the success and error rates for your App across all of your Endpoints. It will also log the errors found as part of the requests made.

![](/images/portal-requests.png)

### Security

The **Security** page for a given App allows you to better secure your Endpoints and your associated dApps. We recommend setting some or all of these for your specific App to reduce the risk of undesired activity.

![](/images/portal-security.png)

* **Private Secret Key Required**: When this is enabled every request sent to an Endpoint has to be sent using [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) with your Secret Key to be accepted. (When using `curl`, you would add `--user :YOUR-SECRET-KEY`.)
* **Approved Chains**: Limits the Endpoints to be used only with specific chains. This list need not be exactly the same as the list of Endpoints on the App Overview page.
* **Whitelist User-Agents**: Limits requests to only the [HTTP User-Agents](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) specified. If a User-Agent not on the list attempts to connect to the Endpoint, the request will be blocked. If nothing is specified, all User-Agents will be accepted.
* **Whitelist Origins**: Limits requests to only the [HTTP Origins](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin) specified. If an Origin not on the list is used in a request to the Endpoint, the request will be blocked. If nothing is specified, all Origins will be accepted. Wildcards are supported.
* **Whitelist Contracts**: Limits requests to the smart contract addresses specified. If the Endpoint is used in a contract address not specified in the list, the request will be denied. Each contract address listed is chain-specific. If nothing is specified, all contract addresses on all chains will be valid.
* **Whitelist Methods**: Limits requests to use specific RPC methods. If a request uses a method not on this list, the request will be denied. Each method listed is chain-specific. If nothing is specified, all methods on all chains will be valid.

When making changes, be sure to click **Save** at the bottom of the page.

### Notifications

{{% notice style="info" %}}
This section is only visible for Apps on the Always Free tier. If your App is on the Pay As You Go tier, you will see the [Plan Details](#plan-details) page instead.
{{% /notice %}}

On this page, you can set up email alerts to be warned when you are approaching your relay limits.

There are four thresholds available for alerts. Each can be individually toggled:

* 25% of 250,000 relays per day
* 50% of 250,000 relays per day
* 75% of 250,000 relays per day
* 100% of 250,000 relays per day

You can also see your weekly bandwidth usage on this page, including average, maximum, and minimum values. 

When making any changes, be sure to click **Save Changes**.

![](/images/portal-notifications.png)

### Plan Details

{{% notice style="info" %}}
This section is only visible for Apps on the Pay As You Go tier. If your App is on the Always Free tier, you will see the [Notifications](#notifications) page instead.
{{% /notice %}}

This page shows you details about your subscription, including your total relays on the billing period, and your latest invoice. You can view and download your latest invoice, as well as manage your plan.

![](/images/portal-plandetails.png)

## Test your Endpoint

Once you've set up your Apps and Endpoints to your liking, you can send requests to them to test that your settings are correct.

For EVM-based chains such as Ethereum, you can refer to the official [JSON-RPC](https://ethereum.org/en/developers/docs/apis/json-rpc/#json-rpc-methods) specification. Below is an example of such a request using cURL.

{{< tabs >}}
{{% tab name="macOS/Linux" %}}
```
curl -X POST \\
-H "Content-Type: application/json" \\
--data '{"jsonrpc": "2.0", "id": 1, "method": "eth_blockNumber", "params": []}' \\
"https://<NETWORK>.gateway.pokt.network/v1/lb/<YOUR-PORTAL-ID>"
```
{{% /tab %}}
{{% tab name="Windows" %}}
```
curl -X POST ^
-H "Content-Type: application/json" ^
--data "{\"jsonrpc\": \"2.0\", \"id\": 1, \"method\": \"eth_blockNumber\", \"params\": []}" ^
"https://<NETWORK>.gateway.pokt.network/v1/lb/<YOUR-PORTAL-ID>"
```
{{% /tab %}}
{{< /tabs >}}


Pocket also maintains API docs that include various methods to test out your specific Endpoint, by generating and sending requests to that Endpoint.

To test out your Endpoint, navigate to the [API Docs](/api-docs/pokt/#/api-docs/pokt/) page for the Pocket blockchain, and click any of the queries on the left sidebar. For example, a simple request is to check the [block height](/api-docs/pokt/#/api-docs/pokt/operations/height_v1_query_height_post).

![](/images/portal-apidocsheight.png)

Once on the page, enter your Portal ID in the box on the right and then click **Send API Request**. The response will be shown below.

There are also code samples for various platforms available in the **Request Sample** box. You can copy these code samples and use them in your own test applications. 

![](/images/portal-apidocsheightresponse.png)


### More questions?

If you have more questions about the Portal, please see the [Portal FAQ](https://www.portal.pokt.network/faq). And you can always reach out to the team on [Discord](https://discord.gg/pokt).
