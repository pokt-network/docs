---
description: Configure the proxy for your node. Part 4 of 5 in the Zero to Node tutorial.
---

# Part 4: Proxy configuration

This section will help you set up the proxy setting on your node.


## Download snapshot

Rather than synchronizing your Pocket node from block zero (which could take weeks), you can use a snapshot. A snapshot of the Pocket blockchain is taken every 12 hours and can be downloaded using the instructions on the [Pocket Snapshots Repository](https://github.com/pokt-network/pocket-snapshots) README page. 

{% hint style="info" %}
As of this writing, the snapshots are refreshed every 12 hours. In the GitHub repo you can look at when the `README.md` file was last updated to determine when the last snapshot was taken. It's best to download the snapshot that is less than a few hours old.
{% endhint %}

Here are the steps for download the snapshot using the `wget` command:

1. Change into the `.pocket` directory.
    ```bash
    cd ~/.pocket
    ```
2. Make a directory named `data` and change into it.
    ```bash
    mkdir data && cd data
    ```
3. Download the latest snapshot using the following command:
    ```bash
    wget -qO- https://snapshot.nodes.pokt.network/latest.tar.gz | tar xvfz -
    ```
4. Make the `pocket` user the owner of the `data` directory.
    ```bash
    sudo chown -R pocket ~/.pocket/data
    ```

{% hint style="warning" %}
This process can take a few hours depending on your internet connection.
{% endhint %}


## Configure systemd

Next, we'll configure the Pocket service using [systemd](https://en.wikipedia.org/wiki/Systemd), a Linux service manager. This will enable the Pocket node to run and restart even when we're not logged in.

### Creating a systemd service in Linux

To setup a systemd service for Pocket, do the following:

1. Open nano and create a new file called `pocket.service`:
    ```bash
    sudo nano /etc/systemd/system/pocket.service
    ```
2. Add the following lines to the file:

    ```ini
    [Unit]
    Description=Pocket service
    After=network.target
    Wants=network-online.target systemd-networkd-wait-online.service

    [Service]
    User=pocket
    Group=sudo
    ExecStart=/home/pocket/go/bin/pocket start
    ExecStop=/home/pocket/go/bin/pocket stop

    [Install]
    WantedBy=default.target
    ```
3. Make sure the `User` is set to the user that will run the Pocket service.
4. Make sure the `ExecStart` and `ExecStop` paths are set to the path for the Pocket binary.
5. Save the file with `Ctrl+O` and then `return`.
6. Exit nano with `Ctrl+X`.
7. Reload the service files to include the pocket service:
    ```bash
    sudo systemctl daemon-reload
    ```
8. Start the pocket service:
    ```bash
    sudo systemctl start pocket.service
    ```
9. Verify the service is running:
    ```bash
    sudo systemctl status pocket.service
    ```
10. Stop the pocket service:
    ```bash
    sudo systemctl stop pocket.service
    ```
11. Verify the service is stopped:
    ```bash
    sudo systemctl status pocket.service
    ```
12. Set the service to start on boot:
    ```bash
    sudo systemctl enable pocket.service
    ```
13. Verify the service is set to start on boot:
    ```bash
    sudo systemctl list-unit-files --type=service
    ```
14. Start the pocket service:
    ```bash
    sudo systemctl start pocket.service
    ```

### Other systemctl commands

- To restart the service:
    ```bash
    sudo systemctl restart pocket.service
    ```
- To prevent the service from starting on boot:
    ```bash
    sudo systemctl disable pocket.service
    ```
- To see mounted volumes:
    ```bash
    sudo systemctl list-units --type=mount
    ```
    {% hint style="info" %}
    If your pocket data is on a separate partition, you can use the following command in the `pocket.service` file to mount it before the pocket service starts.
        ```
        After=network.target mnt-data.mount
        ```
    {% endhint %}

    This ensures that the network is up and the volume is mounted before the pocket service starts.


### Viewing the logs

To view the logs for the pocket service:

```bash
sudo journalctl -u pocket.service
```

To view just the last 100 lines of the logs (equivalent to the `tail -f` command):

```bash
sudo journalctl -u pocket.service -n 100 --no-pager
```

### Finding Errors

You can use `grep` to find errors in the logs.

```bash
sudo journalctl -u pocket.service | grep -i error
```


## Setup SSL

Pocket requires that nodes have an SSL certificate for secure communications. SSL ([Secure Sockets Layer](https://www.cloudflare.com/learning/ssl/what-is-ssl/)) is a layer of security that sits on top of TCP/IP. It's used to encrypt the data sent between a client and a server. To use SSL, you need to have a certificate and a key. Thankfully, getting an SSL certificate is straightforward and free.

To get a certificate, we'll be using [Let's Encrypt](https://letsencrypt.org/) which is a service that issues SSL certificates for free. We'll also be using software called [certbot](https://certbot.eff.org/) to register, install, and renew the certificate.

### Registering an SSL certificate

We installed certbot in a previous step so we just need to use it to request a certificate.

To get a certificate, we'll need to use the `certbot` command with the following options:

- `--register-unsafely-without-email`: This option is required to get a certificate without an email address.
- `--agree-tos`: This option is required to agree to the Let's Encrypt Terms of Service.
- `--nginx`: This option is required to use the nginx plugin.
- `--no-redirect`: This option is required to disable the redirect to the Let's Encrypt website.
- `--domain`: This option is required to specify the domain name.

Here's an example of how to request a certificate. Just replace `$HOSTNAME` with the DNS name of your node:

```bash
sudo certbot --nginx --domain $HOSTNAME --register-unsafely-without-email --no-redirect --agree-tos
```

The output from this command should confirm that the certificate was successfully registered.

### Testing your certificate

To be sure, you'll also want to test that the certificate is working.

There is a command that certbot provides to test your certificate. It's used for testing the auto-renewal of the certificate but it also confirms that the certificate is working. You can run it using the following command:
```bash
sudo certbot renew --dry-run
```
The resulting output should confirm that the certificate is working.


## Configure Nginx

Nginx is a web server. We installed it in aprevious step but we need to do some additional configuration. 

Nginx uses config files to define servers and routes for incoming requests. For Pocket nodes, nginx needs to relay public requests to a local HTTP server that pocket core is running. This is referred to as the proxy. We'll also need to proxy requests made by the Pocket CLI. For example, when we run the command `pocket query height`, the CLI makes an http request to the node's local HTTP server.

### Config files

The nginx configuration files we're interested in are located in the `/etc/nginx/sites-available/` directory. In that directory there is a default configuration file named `default`. This is the configuration that is created when you install nginx, but we'll be creating our own for our node.

To configure nginx:

1. Confirm the name of your SSL certificate:
    ```bash
    sudo ls /etc/letsencrypt/live/
    ```
2. Create a new config file with nano:
    ```bash
    sudo nano /etc/nginx/sites-available/pocket
    ```
3. Add the following code but change the hostname values (`pokt001.pokt.run`) to your node's DNS hostname:
    ```
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
            try_files $uri $uri/ =404;
        }
    }

    server {
        add_header Access-Control-Allow-Origin "*";
        listen 80 ;
        listen [::]:80 ;
        listen 8081 ssl;
        listen [::]:8081 ssl;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name pokt001.pokt.run;

        location / {
            try_files $uri $uri/ =404;
        }

        listen [::]:443 ssl ipv6only=on;
        listen 443 ssl;

        ssl_certificate /etc/letsencrypt/live/pokt001.pokt.run/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/pokt001.pokt.run/privkey.pem;

        include /etc/letsencrypt/options-ssl-nginx.conf;
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

        access_log /var/log/nginx/reverse-access.log;
        error_log /var/log/nginx/reverse-error.log;

        location ~* ^/v1/client/(dispatch|relay|challenge|sim) {
            proxy_pass http://127.0.0.1:8082;
            add_header Access-Control-Allow-Methods "POST, OPTIONS";
            allow all;
        }

        location = /v1 {
            add_header Access-Control-Allow-Methods "GET";
            proxy_pass http://127.0.0.1:8082;
            allow all;
        }
    }
    ```
4. Save the change with `Ctrl+O`.
5. Exit nano with `Ctrl+X`.
6. Stop nginx with:
    ```bash
    sudo systemctl stop nginx
    ```
7. Disable the default configuration:
    ```bash
    sudo rm /etc/nginx/sites-enabled/default
    ```
8. Enable our new configuration:
    ```bash
    sudo ln -s /etc/nginx/sites-available/pocket /etc/nginx/sites-enabled/pocket
    ```
9. Start nginx:
    ```bash
    sudo systemctl start nginx
    ```


## Enable UFW

We're almost done, but before we finish we'll make our server more secure by setting firewall rules to limit network exposure. The [Uncomplicated Firewall](https://wiki.ubuntu.com/UncomplicatedFirewall) (UFW) is a security tool that makes configuring the firewall reasonably simple. We'll use it to disable unnecessary ports.

### Ports you need to open

For running a Pocket node, you'll need to open the following ports:

- `22`: SSH
- `80`: HTTP
- `443`: HTTPS
- `8081`: For the Pocket HTTP API
- `26656`: For the Pocket RPC API

### Use UFW to disable unnecessary ports

To use UFW to configure the firewall:

1. Enable UFW. When prompted, press `y` to confirm:
    ```bash
    sudo ufw enable
    ```
2. Set the default to deny all incoming connections:
    ```bash
    sudo ufw default deny
    ```

3. Allow the SSH port:
    ```bash
    sudo ufw allow ssh
    ```

4. Allow port 80:
    ```bash
    sudo ufw allow 80
    ```

5. Allow port 443:
    ```bash
    sudo ufw allow 443
    ```

6. Allow port 8081:
    ```bash
    sudo ufw allow 8081
    ```

7. Allow port 26656:
    ```bash
    sudo ufw allow 26656
    ```

That's it for the UFW setup. Let's just check the status to confirm the ports are open. To do that, run the following command:

```bash
sudo ufw status
```

After confirming only the necessary ports are open, you can move on to the next step.
