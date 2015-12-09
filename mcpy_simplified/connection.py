from websocket import create_connection
from processReturnMsg import processReturnMsg
import json

class Connection:
	def __init__(self, name, url):
		self.ws = create_connection(url)
		json_string = {
			"name": name
		}

		self.ws.send(json.dumps(json_string))
		#Receive initial server greetings
		processReturnMsg(self.ws.recv(), "initConn")

	def send(self, message):
		self.ws.send(message)

	def close(self):
		self.ws.close()

	def recv(self):
		return self.ws.recv()
