# 4-1: Download Snapshot

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
3. Go to the [Pocket Snapshots Repository](https://github.com/pokt-network/pocket-snapshots) and copy the command that begins with `wget -qO- ` and run it while in the `data` directory.

> NOTE: This process can take a few hours depending on your internet connection.

After the snapshot is downloaded, se permissions on the `data` directory to allow the `pocket` user to read and write to the directory.

```bash
sudo chown -R pocket ~/.pocket/data
```

Next, we'll configure the Pocket service using systemd.
