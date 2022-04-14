# 4-3: Setup SSL

Pocket requires that nodes have an SSL certificate for secure communications. SSL or [Secure Sockets Layer](https://www.cloudflare.com/learning/ssl/what-is-ssl/) is a layer of security that sits on top of TCP/IP. It's used to encrypt the data sent between a client and a server. To use SSL, you need to have a certificate and a key. Thankfully, getting an SSL certificate is easy, and it's free.

To get a certificate, we'll be using [Let's Encrypt](https://letsencrypt.org/) which is a service that issues SSL certificates for free. We'll also be using software called [certbot](https://certbot.eff.org/) to register, install, and renew the certificate.

## Registering an SSL certificate

We installed certbot in a previous step so we just need to use it to request a certificate.

### Make certbot request

To get a certificate, we'll need to use the `certbot` command with the following options:

- `--register-unsafely-without-email`: This option is required to get a certificate without an email address.
- `--agree-tos`: This option is required to agree to the Let's Encrypt Terms of Service.
- `--nginx`: This option is required to use the nginx plugin.
- `--no-redirect`: This option is required to disable the redirect to the Let's Encrypt website.
- `--domain`: This option is required to specify the domain name.

Here's an example of how to request a certificate, just replace `$HOSTNAME` with the DNS name of your node:

```bash
sudo certbot --nginx --domain $HOSTNAME --register-unsafely-without-email --no-redirect --agree-tos
```
The output from this command should confirm that the certificate was successfully registered. But to be sure you'll also want to test that the certificate is working.

## Testing your certificate

There is a command that certbot provides to test your certificate. It's used for testing the auto-renwal of the certificate but it also confirms that the certificate is working. You can run it using the following command:
```bash
sudo certbot renew --dry-run
```
The resulting output should confirm that the certificate is working. If so, we can continue on to the next step.