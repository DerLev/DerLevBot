# DerLevBot
This is my little "Python-Discord-Bot" Project

*Please don't tell me the code is bad. I know it !!!*

### Help-Response from the Bot

<img src="https://mc-mineserver.de/images/dlb-help-2020-08-25.png" width="50%" />

## Dependencies
- [Python](https://www.python.org/downloads/)
- [Discord.py](https://pypi.org/project/discord.py/) (`pip install discord.py`)

## Quick Start
- Clone Repo (`git clone https://github.com/DerLev/DerLevBot.git`)
- Go into the Directory (`cd ~/DerLevBot/`)
- Create Bot-App https://discordapp.com/developers/applications
- Create a JSON-File named `config.json` and put in your Token under `token`
```json
{
  "token": "",
  "owner_id": 377103974081495042,
  "prefix": "dlb!",
  "twitch": "https://twitch.tv/derlev"
}
```
- Start the bot with `python3 derlevbot.py`

### Invite

1. Put in your Client ID `https://discord.com/api/oauth2/authorize?client_id=<CLIENT-ID>&permissions=519240&scope=bot`
2. Open the link in your Browser

### Advanced Customization

- Go into `config.json`
  - edit the OwnerID
  - edit the Prefix
  - edit the Twitch-Page

## To-Dos

- [x] Post Code on GitHub
- [x] Create README.md
- [x] Make JSON file for handling TOKEN, OwnerID, Prefix and Twitch-Page

## Links

**DerLev:**

[GitHub](https://derlev.github.io/) - [YouTube](https://www.youtube.com/channel/UCpEdoioUxagDLt56nT1WWaw) - [Twitter](https://twitter.com/_derlev_) - [Website](https://mc-mineserver.de/)

**Bot:**

[**Ready to Invite**](https://mc-mineserver.de/#discordbot)
