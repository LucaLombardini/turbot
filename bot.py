#! /env/python

import os
import sys
import discord
import json
import datetime
import re

def logger(string):
	logFile = "bot.log"
	with open(logFile,'a') as fileout:
		fileout.write(string)
	if os.path.exists(logFile):
		return
	else:
		print("[",print("[",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"]"),"] [ ERROR ] : unable to append data to",logFile)
		sys.exit(-1)

def loadFromFile(filename):
	if os.path.exists(filename):
		with open(filename,'r') as filein:
			tmp = filein.read()
		if tmp:
			return tmp
		else:
			logger("[ " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ] [ ERROR ] : " + filename + " is empty or unreadable or formatted wrongly")
			sys.exit(-2)
	else:
		logger("[ " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ] [ ERROR ] : " + filename + " cannot be opened")
		sys.exit(-3)


class clientBot(discord.Client):
	textChannel = ""
	commandList = {}
	async def on_ready(self):					# async event: when logged in do stuff
		print("Logged in successfully as", self.user)
		message.channel.send('turBot service is now online')	# send to chat the bot is now available
		commandList = json.loads(loadFromFile(COMMANDS_FILE))
		textChannel = loadFromFile(CHANNEL_FILE)

	async def on_message(self,message):
		if message.channel == textChannel and message.author != self.user:	# check if the message comes from the channel where the bot has to read the chat
			parsedMessage = message.content.split()
			commandName = parsedMessage[0].lower()
			if commandName in commandList:					# in a command message, the first string is the command name.
				if re.search(commandList[commandName]["syntax"], ' '.join(parsedMessage[1:]):	# check syntax
					# send message to minecraft@turboServer
				else:
					message.channel.send("Invalid syntax!\n" + commandList[commandName]["info"])
				# wait for server response: if not received in a time window, tell error (unreachable server + info on the error)
		else:
			return

# load token, message channel name and command dictionary used by the bot
TOKEN_FILE = "bot.token"
CHANNEL_FILE = "text.channel"
COMMANDS_FILE = "command.list"
TOKEN = loadFromFile(TOKEN_FILE)

turBot = clientBot()
turBot.run(TOKEN)
