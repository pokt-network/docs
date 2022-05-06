# 4-4: Configure Nginx

Nginx is a web server. We installed it in aprevious step but we need to do some additional configuration. 

Nginx uses config files to define servers and routes for incoming requests. For Pocket nodes, nginx needs to relay public requests to a local HTTP server that pocket core is running. This is referred to as the proxy. We'll also need to proxy requests made by the Pocket CLI. For example, when we run the command `pocket query height`, the CLI makes an http request to the node's local HTTP server.

## Config Files

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
