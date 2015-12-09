import json

onlyStatusCodeCommands = ["setBlock", "spawnEntity", "chat", "teleport", 
							"initConn", "setBlockType", "chat", "setTime",
							"burnEntity", "shootUpEntity", "hurtEntity", "killEntity", "setName"]
locationBasedCommands = ["getBlock", "getLocation"]

class processReturnMsg:
	#Process returned json from server
	#3 diff types of return msg
	def __init__(self, recvMsg, comm):
		self.recvMsg = recvMsg
		self.comm = comm
		self.processMsg()

	def processMsg(self):
		returned_dict = json.loads(self.recvMsg)
		if self.comm == "initConn" :
			#Handle return for initReturnMsg
			print "[SUCCESS] " + returned_dict["status"]

		elif self.comm == "getPlayer" :
			if "playerName" in returned_dict :
				self.checkStatus("ok")
			else :
				self.checkStatus("failed")

		elif self.comm == "getWorld" :
			if "index" in returned_dict :
				self.checkStatus("ok")
			else : 
				self.checkStatus("failed")

		elif self.comm == "spawnEntity" :
			if "uniqueId" in returned_dict :
				self.checkStatus("ok")
			else :
				self.checkStatus("failed")

		elif self.comm in onlyStatusCodeCommands :
			#Handle return for onlyStatusCodeCommands
			code = returned_dict["status"]
			self.checkStatus(code)

		elif self.comm in locationBasedCommands :
			#Handle return for otherCommands
			#returned_dict must contain a Location dict
			if "x" in returned_dict : 
				self.checkStatus("ok")
			else : 
				self.checkStatus("failed")

		else :		#commands that are not in onlyStatusCodeCmds and locationBasedCmds
			self.checkStatus("invoked")

	def checkStatus(self, code):
		if code == "ok" or code == "success" :
			print "[SUCCESS] " + self.comm
		elif code == "invoked" :
			print "[EXECUTED] " + self.comm
		else : 
			print "[FAILURE] " + self.comm
