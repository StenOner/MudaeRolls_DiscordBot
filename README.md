# MudaeRolls DiscordBot
I made this bot to trigger some extra rolls for the popular mudae bot. This requires the **bearer token** of a dummy user in order to trigger the rolls.

## Configuration
Before running the bot you must run this commands to install some dependencies:
```
pip install discord
pip install python-dotenv
```

You must also add the *.env* file with this keys:
```
BOT_TOKEN=<YOUR BOT'S TOKEN>
USER_TOKEN=<USER'S TOKEN>
```

## Running the bot
Now you can run the bot by executing the ***main.py*** file.
```
python main.py
```

## Commands
The bot can respond to the prefix **?** which can be changed in the *bot.py* file and some ***/*** commands.

### Examples
```
# Can trigger a roll type (wa | ha | ma) by the amount given (min 1, max 10) any other value will by parsed, amount being optional
?<command> <amount>
?wa 10
?ha 5
?ma 300
```

```
# Can trigger a roll type (wa | ha | ma) by the amount given (min 1, max 10) any other value will by parsed, arguments are mandatory
/roll <type> <amount>
/roll wa 10
/roll ha 5
/roll ma -110
```