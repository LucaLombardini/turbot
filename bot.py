#! /env/python

# import os
import sys
import discord
import json
import datetime
import re
import myutil

class clientBot(discord.Client):
	textChannel = ""
	async def on_ready(self):					# async event: when logged in do stuff
		print("Logged in successfully as", self.user)
		await Message.channel.send('turBot service is now online')
		# message.channel.send('turBot service is now online')	# send to chat the bot is now available
		textChannel = loadFromFile(CHANNEL_FILE)

	async def on_message(Message):
		if Message.channel == textChannel and Message.author != self.user:	# check if the message comes from the channel where the bot has to read the chat
			parsedMessage = Message.content.split()
			commandName = parsedMessage[0].lower()			# get command
			if commandName in myutil.commandList:			# in a command message, the first string is the command name.
				regex = myutil.commandList[commandName]["syn"]	# get the regex used to check if command arguments are correct
				args = ' '.join(parsedMessage[1:])			# re-assemble the message arguments
				if re.match(regex, args) is not None:
					if myutil.commandList[commandName]["exec_self"]: # execute the command the BOT has to do if any
						exec(myutil.commandList[commandName]["exec_self"]) 
					#try:
						Message.channel.send('contacting turboServer...')
						# send message to minecraft@turboServer
					#except asyncio.TimeoutError:
						# tell that the server doesn't respond back...
				else:
					Message.channel.send("Invalid syntax!\n" + commandList[commandName]["info"])
				# wait for server response: if not received in a time window, tell error (unreachable server + info on the error)
		else:
			return

# load token, message channel name used by the bot
TOKEN_FILE = "bot.token"
CHANNEL_FILE = "text.channel"
TOKEN = myutil.loadFromFile(TOKEN_FILE)

turBot = clientBot()
turBot.run(TOKEN)
