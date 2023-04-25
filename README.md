# About

Just a bot made in Python using [discord.py](https://discordpy.readthedocs.io/en/stable/) API. Currently it sends a message when logged and can perform few operations like sort, string manipulation and can reply or send an embedded message.

# Get started

A. Before coding
1. Go to [Discord Developper Portal](https://discord.com/developers/applications).
2. Create a new application, give a name to your bot and accept General Terms of Using.
3. On side bar click on 'Bot' and copy token (make sure to not share with anyone), if not click on reset button to get a new token.
4. Enable public bot in order to invite it to your servers.
5. On side bar go to OAuth2 -> URL Generator and click on `bot` option : it will display you all permissions you can give to your bot.
6. It will generate an URL : copy and paste it in URL search.
7. Choose a server to invite your bot.
8. And then it's good now you can code!

B. Setup
1. Set an `virtual environment` in the directory that will contain bot code :

    **Warning**: This is for Windows user
    ```bash
    # create virtual environment but does not activate it
    # add venv folder to current directory
    python -m venv venv

    # activate it and see (venv) pop aside command prompt current path
    venv/Scripts/Activate
    ```

2. Install discord.py :

    ```bash
    pip install discord.py
    ```

3. You can now start coding!