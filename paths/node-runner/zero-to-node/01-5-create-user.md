# 1-5: Create a user

For security reasons it's best not to use the root user. Instead, it's better to create a new user and add the user to the sudo group.

Also, by default, the Pocket CLI will place the data directory for the node in the user's home directory. So, when you create a new user, you'll want to make sure the home directory is on a volume that has plenty of room for the data directory.

{% hint style="warning" %}
At the time of writing, Pocket requires ~200GB. The following user setup process assumes that the location of your user's home directory is on a volume with enough room for the pocket data with room to grow.
{% endhint %}

## Creating a new user

To create a new user, and home directory, do the following:

1. Create a new user with the following command:
    ```bash
    useradd -m -g sudo -s /bin/bash pocket && passwd pocket
    ```
    > Note: The user `pocket` will be created, added to the `sudo` group, and the default shell will be `bin/bash`. A home directory will also be created. If you want to specify the location of the home directory, you can use the `-d` option followed by the path to the home directory.

2. For the rest of this guide, we'll be using the `pocket` user. So now that the `pocket` user is created, you can switch from using `root` to the `pocket` user with the following command:

    ```bash
    su - pocket
    ```

Alright, that's it for the server setup. Now let's move on to the Pocket CLI installation.