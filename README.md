<h1 align="center" style="position: relative;">
	<a href="#visit"><img src="./docs/images/icon.png" width="200" height="200"></a><br>
    <strong>RoboBilly</strong>
</h1>

<p align="center">
    "Don't bully me pls"
</p>

<br/>

<p align="center">
    <img alt="Discord" src="https://img.shields.io/discord/750945243305869343?label=Basement&style=flat-square">
    <!-- <img alt="Travis (.com)" src="https://travis-ci.org/github/billydevyt/RoboBilly"> -->
    <!-- <img alt="Python" src=https://img.shields.io/github/pipenv/locked/python-version/billydevyt/RoboBilly> -->
    <img alt="Release" src=https://img.shields.io/github/v/release/billydevyt/RoboBilly?style=flat-square>
    <img alt="Heroku" src="https://img.shields.io/badge/heroku-passing-green?style=flat-square">
    <img alt="License" src="https://img.shields.io/github/license/billydevyt/RoboBilly?style=flat-square">
</p>

<p align="center">
    <a href="#building--running">Building & running</a> •
    <a href="#features">Features</a> •
    <a href="https://github.com/billydevyt/RoboBilly/blob/main/LICENSE">License</a> •
    <a href="https://github.com/billydevyt/RoboBilly/blob/main/.github/CODE_OF_CONDUCT.md">Code of Conduct</a> •
    <a href="#contributing">Contributing</a>
</p>

## Building & running

The bot is written in **Python 3.8**, you can run it via `python bot.py` from command line or just use the `run.bat` file to run it. If you are missing packages make sure to run install mentioned ones in `requirements.txt` prior to building. Also all the files required to Launch to **Heroku** is included.

## Configuration

1. `config.json` is where all of the bot configuration will be placed. The only fields that are essential for running the bot are `Token` and `Prefix`.

```json
{
    "Token": "get it from discord developer portal",
    "Prefix": "[]",
    "mails_channel": "mails",
    "server_name": "server's name here"
}
```

2. give the bot `Administrator` permissions.

3. Run `setup` command in the discord server.(for running this command, the user will need administrator permissions)

## What is new?
<p>
<img alt="Release" src=https://img.shields.io/github/v/release/billydevyt/RoboBilly?style=flat-square>
</p>

- counting (need a channel called 'counting')
- Emojify text

## Features

|Feature|Description|
|--:|:--|
|ModMail system|Makes it easier for users to contact moderators and admins for help.|
|Rich Interpreters|Run commands from discord channels! `BrainFuck`, `JB` languages are currently supported.|
|Moderation Module|All Moderation tools needed to keep the server safe and peaceful.|
|User Module|A lot of Fun & useful commands.|
|custom commands|custom command module, add custom commands|
|Error Handling|error handling module|

## Contributing

contributions are accepted. Check out the [Contributing](./.github/CONTRIBUTING.md) for more info.
RoboBilly is [MIT-licensed](./LICENSE.md).

## Visit

Visit us here: https://billy-s-basement.github.io
