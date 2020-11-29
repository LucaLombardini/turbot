FILE ORGANIZATION:
	bot.py:	the bot script
	myutil.py: 	module which contains the dictionary of all commands, organized as command names used as the keyword to access their respective dictionary, containing a briefly command synopsis
			and documentation, the regex used to check the argumets syntax and the eventual command string to be executed by the bot. It also contains useful functions used by the bot.
	bot.token:	Contains the bot token used to interface the API to the actual user-bot.
	text.channel:	Contains the ids of the various channels, which belongs to a guild where the bot is part of. Those channels are the ones where the bot reads and responds.
			As a human-help to recognize the channel, the discord guild name is written after the "#" symbol. The bot ignores this part!
