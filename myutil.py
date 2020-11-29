## command utilities
import os

commandList={}

def start():
	return

def stop():
	return

def help():
	outstring="INTERNAL REFERENCE MANUAL:\n"
	for command in commandList:
		outstring = outstring + command + ": " + commandList[command]["info"] + "\n\n\n"
	return outstring

def isCommand(commandName):
	return commandName in commandList

def getSyntax(commandName):
	return commandList[commandName]["syn"]

def message(commandName):
	return commandList[commandName]["send"] if type(commandList[commandName]["send"]) is str else commandList[commandName]["send"]()

def localActions(commandName):
	return None

def getInfo(commandName):
	return commandList[commandName]["info"]

commandList={
	"start":{	"info":"Start a specific Minecraft world.\n\tSyntax: start <world_name/enumeration>",
			"syn":"([0-9]|[a-zA-Z])+",
			"send":"dummy",
			"exec_self":start},
	"stop":{	"info":"Stop a specific Minecraft world.\n\tSyntax: stop <world_name/enumeration>",
			"syn":"([0-9]|[a-zA-Z])+",
			"send":"",
			"exec_self":stop},
	"numworld":{	"info":"List the world names available for this Discord guild",
			"syn":"",
			"send":"",
			"exec_self":""},
	"regrade":{	"info":"Make the specified world point to a different server version instance\nWARNING: be carefull when regrade to a lower version!!! This operation could break your world!!!",
			"syn":"<world_name> <server_version>",
			"send":"",
			"exec_self":""},
	"new":{	"info":"Create a new Minecraft world with the specified name and version. This will also associate a identifier number to it.\n\tSyntax: new <server_version> <world_name>",
			"syn":"",
			"send":"",
			"exec_self":""},
	"help":{	"info":"Get the information about what this BOT can do",
			"syn":"",
			"send":help,
			"exec_self":""}
}

## general bot utilities
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
		
