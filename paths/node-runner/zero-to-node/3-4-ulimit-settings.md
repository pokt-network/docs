# 3-4: Set open file limits

Ubuntu and other UNIX-like systems have a `ulimit` shell command that's used to set resource limits for users. One of the limits that can be set is the number of open files a user is allowed to have. Pocket nodes will have a lot of files open at times, so we'll want to increase the default ulimit for the `pocket` user account.

## Increasing the ulimit

1. Before increasing the ulimit, you can check the current ulimit with the following command:
    ```bash
    ulimit -n
    ```
2. Increase the ulimit to 16384:
    ```bash
    ulimit -Sn 16384
    ```
    {% hint style="info" %}
    The `-Sn` option is for setting the soft limit on the number of open files.
    {% endhint %}
3. Check the new ulimit to confirm that it was set correctly:
    ```bash
    ulimit -n
    ```
    {% hint style="info" %}
    The `-n` option is for getting the limit for just the number of open files.
    {% endhint %}

## Permanent settings

Using the above method for setting the `ulimit` only keeps the change in effect for the current session. To permanently set the ulimit, you can do the following:

1. Open the `/etc/security/limits.conf` file.
    ```bash
    sudo nano /etc/security/limits.conf
    ```
2. Add the following line to the bottom of the file:
    ```bash
    pocket           soft    nofile          16384
    ```
3. Save the file with `Ctrl+O` and then `Enter`.
4. Exit nano with `Ctrl+X`.

After permanently setting the ulimit, the next thing we'll do is download a snapshot of the Pocket blockchain.
