from connection import Connection
from location import Location
from processReturnMsg import processReturnMsg
import json
import requests

def create_connection(name, url):
	global conn, playerName, serverUrl
	serverUrl = url + "/" + name
	playerName = name
	# conn = Connection(name, url)
	print "Connection with " + url + " established"

def getWorld(index):		#done
	#return worldObj
	global conn, serverUrl
	json_string = [
		{
			"className": "wrapper.ServerWrapper",
			"methodName": "getWorld",
			"methodParams": [
				index
			]
		}
	]
	returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
	print returned_json
	processReturnMsg(returned_json, "getWorld")

	returned_dict = json.loads(returned_json)
	return World(returned_dict["index"])

	#Process returnMsg
	#processReturnMsg(self.conn.recv(), "getWorld")

	#return world

def getPlayer():		#done
	#return Player
	global conn, playerName
	json_string = [
		{
			"className": "wrapper.ServerWrapper",
			"methodName": "getPlayer",
			"static": True,
			"methodParams": [
				playerName
			]
		}
	]

	returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text

	processReturnMsg(returned_json, "getPlayer")

	returned_dict = json.loads(returned_json)
	return Player(returned_dict["playerName"])

		
class Block:
	def __init__(self, worldIndex, ty, location):
		self.worldIndex = worldIndex
		self.type = ty
		self.location = location

	def setType(self, ty):		#done
		global conn
		json_string = [
			{
				"className": "wrapper.ServerWrapper",
				"methodName": "getWorld",
				"static": True,
				"methodParams": [
					self.worldIndex
				]
			},
			{
				"methodName": "getBlock",
				"static": False,
				"methodParams": [
					self.location.x, 
					self.location.y,
					self.location.z
				]
			},
			{
				"methodName": "setType",
				"static": False,
				"methodParams": [
					ty
				]
			}
		]

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "setBlockType")

class Player:
	def __init__(self, name):
		self.name = name

	def getLocation(self): 		#done
		#return Location 
		json_string = [
			{
				"className": "wrapper.ServerWrapper",
				"methodName": "getPlayer",
				"methodParams": [
					self.name
				]
			},
			{
				"methodName": "getLocation",
				"methodParams": []
			}
		]

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text

		processReturnMsg(returned_json, "getLocation")

		returned_dict = json.loads(returned_json)
		return Location(returned_dict["x"], returned_dict["y"], returned_dict["z"])	

	def setLocation(self, x, y, z):		#done
		#send location
		json_string = [
			{
				"className": "wrapper.ServerWrapper",
				"methodName": "getPlayer",
				"methodParams": [
					self.name
				]
			},
			{
				"methodName": "setLocation",
				"methodParams": [
					x,
					y,
					z
				]
			}
		]

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "setLocation")		

	def chat(self, msg):		#done
		global conn
		json_string = [
			{
				"className": "wrapper.ServerWrapper",
				"methodName": "getPlayer",
				"methodParams": [
					self.name
				]
			},
			{
				"methodName": "chat",
				"methodParams": [
					msg
				]
			}
		]

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "chat")

class Entity:
	def __init__(self, uniqueId, location):
		self.uniqueId = uniqueId
		self.initLoca = location

	def burn(self):
		self.sendCommand("burn", [])

	def shootUp(self):
		self.sendCommand("shootUp", [])

	def hurt(self):
		self.sendCommand("hurt", [])	

	def kill(self):
	 	self.sendCommand("kill", [])

	def setName (self, name):
		self.sendCommand("setName", [name])

	def sendCommand(self, cmd, params):
		json_string = [
			{
				"className": "wrapper.ServerWrapper",
				"methodName": "getEntity",
				"methodParams": [
					self.uniqueId
				]
			},
			{
				"methodName": cmd,
				"methodParams": params
			}
		]

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		#server returns invoke
		processReturnMsg(returned_json, cmd + "Entity")


class World:
	def __init__(self, index):
		self.index = index 

	def getBlock(self, x, y, z):		#done
		#return Block
		global conn
		json_string = [
			{
				"className": "wrapper.ServerWrapper",
				"methodName": "getWorld",
				"static": True,
				"methodParams": [
					self.index
				]
			},
			{
				"className": "wrapper.WorldWrapper",
				"methodName": "getBlock",
				"methodParams": [
					x,
					y,
					z
				]
			}
		]

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "getBlock")		

		returned_dict = json.loads(returned_json)
		return Block(self.index, returned_dict["type"], Location(x, y, z))

	def spawnEntity(self, ty, x, y, z):		#done
		#return entity
		json_string = [
			{
				"className": "wrapper.ServerWrapper",
				"methodName": "getWorld",
				"static": True,
				"methodParams": [
					self.index
				]
			},
			{
				"className": "wrapper.WorldWrapper",
				"methodName": "spawnEntity",
				"methodParams": [
					ty,
					x,
					y,
					z
				]
			}
		]

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "spawnEntity")
		
		returned_dict = json.loads(returned_json)
		return Entity(returned_dict["uniqueId"], Location(x, y, z))

		
	def setTime(self, time):	#done
		time = time.lower()

		if time == "day" :
			timeIndex = 0
		elif time == "night" :
			timeIndex = 15000

		json_string = [
			{
				"className": "wrapper.ServerWrapper",
				"methodName": "getWorld",
				"static": True,
				"methodParams": [
					self.index
				]
			},	
			{
				"className": "wrapper.WorldWrapper",
				"methodName": "setTime",
				"methodParams": [
					timeIndex
				]
			}
		]

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "setTime")
