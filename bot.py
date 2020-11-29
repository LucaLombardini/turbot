#! /env/python

# import os
import sys
import discord
import json
import datetime
import re
import myutil

class clientBot(discord.Client):
	async def on_ready(self):					# async event: when logged in do stuff
		print("Logged in successfully as", self.user)
		self.target_channels = [self.get_channel(int(line.split("#")[0])) for line in open("text.channel",'r').readlines()] # list of listening channels, obtained from their id stored in a file
		for guild in self.guilds:
			for channel in guild.channels:
				if channel in self.target_channels:
					await channel.send('turBot service is now online')

	async def on_message(self, message):
		if message.channel in self.target_channels and message.author != self.user:	# check if the message comes from the channel where the bot has to read the chat
			parsedMessage = message.content.split()
			commandName = parsedMessage[0].lower()				# get command
			if myutil.isCommand(commandName):					# in a command message, the first string is the command name.
				regex = myutil.getSyntax(commandName)				# get the regex used to check if command arguments are correct
				args = ' '.join(parsedMessage[1:])				# re-assemble the message arguments
				if re.match(regex, args) is not None:
					if myutil.message(commandName):			# send the command related text message to the channel
						await message.channel.send(myutil.message(commandName))
					myutil.localActions(commandName)			# execute the command the BOT has to do if any
					
					#try:
						#await message.channel.send('contacting turboServer...')
						# send message to minecraft@turboServer
					#except asyncio.TimeoutError:
						# wait for the server response: if not received in a time window, tell that the server doesn't respond back...
				else:
					message.channel.send("Invalid syntax!\n" + myutil.getInfo(commandName))
		else:
			return

# load token, message channel name used by the bot
TOKEN_FILE = "bot.token"
CHANNEL_FILE = "text.channel"
TOKEN = myutil.loadFromFile(TOKEN_FILE)

turBot = clientBot()
turBot.run(TOKEN)
