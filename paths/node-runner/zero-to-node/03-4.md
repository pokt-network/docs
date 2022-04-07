# 3-4: Set open file limits

Ubuntu and other UNIX-like systems have a `ulimit` shell command that's used to set resource limits for users. One of the limits that can be set is the number of open files a user is allowed to have. Pocket nodes will have a lot of files open at times. So we'll need to increase the default ulimit for the user account pocket runs under.

## Increasing the ulimit

Before increasing the ulimit, you can check the current ulimit with the following command:
```bash
ulimit -n
```

You'll want to increase the ulimit to 16384. You can do that with the following command:
```bash
ulimit -Sn 16384
```
> Note: The `-Sn` option is for setting the soft limit on the number of open files.

Finally, check the new ulimit to confirm that it was set correctly:
```bash
ulimit -n
```
> Note: The `-n` option is for getting the limit for just the number of open files.

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
3. Save the file with <kbd>Ctrl+O</kbd> and then <kbd>return</kbd>.
4. Exit nano with <kbd>Ctrl+X</kbd>.

After permanently setting the ulimit, the next thing we'll do is download a snapshot of the Pocket blockchain.