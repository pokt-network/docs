# 4-2: Configure systemd

To enable the pocket to run and restart even when we're not logged in, we'll be using [systemd](https://en.wikipedia.org/wiki/Systemd) which is a Linux service manager.

## Creating a systemd service in Linux

To setup a systemd service for Pocket, do the following:

1. Open nano and create a new file called `pocket.service`
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
5. Save the file with <kbd>Ctrl+O</kbd> and then <kbd>return</kbd>.
6. Exit nano with <kbd>Ctrl+X</kbd>.
7. Reload the service files to include the pocket service.
    ```bash
    sudo systemctl daemon-reload
    ```
8. Start the pocket service.
    ```bash
    sudo systemctl start pocket.service
    ```
9. Verify the service is running.
    ```bash
    sudo systemctl status pocket.service
    ```
10. Stop the pocket service.
    ```bash
    sudo systemctl stop pocket.service
    ```
11. Verify the service is stopped.
    ```bash
    sudo systemctl status pocket.service
    ```
12. Set the service to start on boot.
    ```bash
    sudo systemctl enable pocket.service
    ```
13. Verify the service is set to start on boot.
    ```bash
    sudo systemctl list-unit-files --type=service
    ```
14. Start the pocket service.
    ```bash
    sudo systemctl start pocket.service
    ```
## Other systemctl commands

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
    Note: If your pocket data is on a separate partition, you can use the following command in the `pocket.service` file to mount it before the pocket service starts.

    ```
    After=network.target mnt-data.mount
    ```
    This ensures that the network is up and the volume is mounted before the pocket service starts.

## Viewing the logs

To view the logs for the pocket service, do the following:

```bash
sudo journalctl -u pocket.service
```

To view just the last 100 lines of the logs (equiv. tail -f), do the following:

```bash
sudo journalctl -u pocket.service -n 100 --no-pager
```

## Finding Errors

There are a few ways to find errors in the logs.

```bash
sudo journalctl -u pocket.service | grep -i error
```