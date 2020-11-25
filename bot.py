#! /env/python

# import os
import sys
import discord
import json
import datetime
import re
import myutil

class clientBot(discord.Client):
	target_channels = []		#### THI LIST IS NOT SEEN IN THE FUNCTIONS BELOW !!!!
	dummy="a"
	async def on_ready(self):					# async event: when logged in do stuff
		print("Logged in successfully as", self.user)
		target_channels = [self.get_channel(int(line.split("#")[0])) for line in open("text.channel",'r').readlines()] # list of channels of interest, obtained from their id stored in a file
		for guild in self.guilds:
			for channel in guild.channels:
				if channel in target_channels:
					await channel.send('turBot service is now online')

	async def on_message(self, message):
		if message.channel in target_channels and message.author != self.user:	# check if the message comes from the channel where the bot has to read the chat
			parsedMessage = message.content.split()
			commandName = parsedMessage[0].lower()			# get command
			if commandName in myutil.commandList:			# in a command message, the first string is the command name.
				regex = myutil.commandList[commandName]["syn"]	# get the regex used to check if command arguments are correct
				args = ' '.join(parsedMessage[1:])			# re-assemble the message arguments
				if re.match(regex, args) is not None:
					if myutil.commandList[commandName]["exec_self"]: # execute the command the BOT has to do if any
						exec(myutil.commandList[commandName]["exec_self"]) 
					#try:
						message.channel.send('contacting turboServer...')
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
