# DerLevBot
This is my little "Python-Discord-Bot" Project

## Dependencies
- [Python](https://www.python.org/downloads/)
- [Discord.py](https://pypi.org/project/discord.py/) (`pip install discord.py`)
- [discord-py-slash-command](https://pypi.org/project/discord-py-slash-command/) (`pip install discord-py-slash-command`)

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

1. Put in your Client ID `https://discord.com/api/oauth2/authorize?client_id=<CLIENT-ID>&permissions=519240&scope=bot%20applications.commands`
2. Open the link in your Browser

### Advanced Customization

- Go into `config.json`
  - edit the OwnerID
  - edit the Twitch-Page

## To-Dos

- [x] Slash Commands
- [ ] More Features...

## Links

**DerLev:**

[GitHub](https://derlev.github.io/) - [Twitter](https://twitter.com/_derlev_) - [Website](https://mc-mineserver.de/)
