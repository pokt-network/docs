# 1-5: Create a user

For security reasons it's best not to use the `root` user. Instead, it's better to create a new user and add the user to the `sudo` group.

Also, by default, the Pocket CLI will place the data directory for the node in the user's home directory. So, when you create a new user, you'll want to make sure the home directory is on a volume that has plenty of room for the data directory.

{% hint style="warning" %}
At the time of writing, Pocket requires ~200GB for its blockchain data. The following user setup steps assumes that the location of your user's home directory is on a volume with enough room for the pocket data.
{% endhint %}

## Creating a new user

To create a new user and home directory, enter the following commands:

1. Create a new user named `pocket`, add it to the `sudo` group, and set the default shell to `bash`:
    ```bash
    useradd -m -g sudo -s /bin/bash pocket && passwd pocket
    ```
    {% hint style="warning" %}
    If you want to specify the location of the home directory, you can use the `-d` option followed by the path to the home directory.
    {% endhint %}

2. For the rest of this guide, we'll be using the `pocket` user. So now that the `pocket` user is created, you can switch from using `root` to the `pocket` user with the following command:

    ```bash
    su - pocket
    ```

That's it for the server setup!