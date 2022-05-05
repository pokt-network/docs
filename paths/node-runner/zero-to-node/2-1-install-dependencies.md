# 2-1: Install dependencies

At this point you should be logged in via SSH as the `pocket` user that we set up in the previous step.

Before we install the Pocket software, there are a few dependencies we'll need to add. But before we install anything, we'll update the existing system packages first.

## Updating system packages

1. Update the repository index with the following command:
    ```bash
    sudo apt update
    ```
2. Update the distribution with the following command:
    ```bash
    sudo apt dist-upgrade -y
    ```

After the update completes, we're ready to install the dependencies.

## Installing dependencies

There are a handful of dependencies but installing them won't take long. Also, some might already be installed. So if one of the dependencies exists, you can just move on to the next one.

### git

```bash
sudo apt-get install git -y
```
### build tools
```bash
sudo apt-get install build-essential -y
```

### curl
```bash
sudo apt-get install curl -y
```
### file
```bash
sudo apt-get install file -y
```
### nginx
```bash
sudo apt install nginx -y
```
### certbot
```bash
sudo apt install certbot -y
```
### python3-certbot-nginx
```bash
sudo apt-get install python3-certbot-nginx -y
```

After installing the previous dependencies, there is one more dependency we'll need to add - that's Go, we'll do that next.