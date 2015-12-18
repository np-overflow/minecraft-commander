from connection import Connection
from location import Location
from processReturnMsg import processReturnMsg
import json
import requests
import sys

def create_connection(name, url):	
	global conn, playerName, serverUrl
	serverUrl = url + "/" + name
	playerName = name
	# conn = Connection(name, url)
	print "Connection with " + url + " established"

def getWorld(index):		
	#return worldObj
	try :
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
		feedback = "got world {worldIndex}".format(worldIndex = index)

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "getWorld", [feedback])

		returned_dict = json.loads(returned_json)
		return World(returned_dict["index"])
	except :
		print "[ERROR] Unable to get world " + str(index) 
		sys.exit("Script will exit...")

def getPlayer():		
	#return Player
	try :
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

		feedback = "got {player}".format(player = playerName.upper())

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "getPlayer", [feedback])

		returned_dict = json.loads(returned_json)
		return Player(returned_dict["playerName"])
	except :
		print "[ERROR] Unable to get player " + playerName
		sys.exit("Script will exit...")
		
class Block:
	def __init__(self, worldIndex, ty, location):
		self.worldIndex = worldIndex
		self.type = ty
		self.location = location

	def setType(self, ty):		
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

		feedback = "set {type} at {x:.2f}, {y:.2f}, {z:.2f}".format(type = ty.upper(), x = self.location.x, 
			y = self.location.y, z = self.location.z)

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "setBlockType", [feedback])


class Player:
	def __init__(self, name):
		self.name = name

	def getLocation(self): 
		try : 		
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
			returned_dict = json.loads(returned_json)
			feedback = "returned {x:.2f}, {y:.2f}, {z:.2f}".format(x = returned_dict["x"], y = returned_dict["y"], z = returned_dict["z"])

			processReturnMsg(returned_json, "getLocation", [feedback])
			return Location(returned_dict["x"], returned_dict["y"], returned_dict["z"])	
		except : 
			print "[ERROR] Unable to get location of " + playerName
			sys.exit("Script will exit...")\
			

	def setLocation(self, x, y, z):		
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

		feedback = "set {player} at {x:.2f}, {y:.2f}, {z:.2f}".format(player = self.name.upper(), x = x, y = y, z = z)

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "setLocation", [feedback])		

	def chat(self, msg):		
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
		processReturnMsg(returned_json, "chat", [])

class Entity:
	def __init__(self, uniqueId, ty, location):
		self.uniqueId = uniqueId
		self.type = ty
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
		feedback = "{cmd} {entity} at init location {x:.2f}, {y:.2f}, {z:.2f}".format(cmd = cmd, entity = self.type, 
				x = self.initLoca.x, y = self.initLoca.y, z = self.initLoca.z)

		#server returns invoked
		processReturnMsg(returned_json, cmd + "Entity", [feedback])


class World:
	def __init__(self, index):
		self.index = index 

	def getBlock(self, x, y, z):		
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
		processReturnMsg(returned_json, "getBlock", [])		

		returned_dict = json.loads(returned_json)
		return Block(self.index, returned_dict["type"], Location(x, y, z))

	def spawnEntity(self, ty, x, y, z):		
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

		feedback = "spawn {type} at {x:.2f}, {y:.2f}, {z:.2f}".format(type = ty.upper(), x = x, y = y, z = z)

		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "spawnEntity", [feedback])
		
		returned_dict = json.loads(returned_json)
		return Entity(returned_dict["uniqueId"], ty, Location(x, y, z))

		
	def setTime(self, time):	
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

		feedback = "set time to {time}".format(time = time.upper())
		returned_json = requests.post(serverUrl, data=json.dumps(json_string)).text
		processReturnMsg(returned_json, "setTime", [feedback])
