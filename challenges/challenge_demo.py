#Generates a 3 x 3 flat stone block for demo 

from ..mcpy_simplified import minecraft, location
import time, json, random

def loadData():
	global block_list

	with open("mcpy_simplified/minecraft_data.json", "r") as f:
		data = json.loads(f.read())

	block_list = data['blockTypes']

def main() :
	global block_list
	loadData()

	#Change to username
	mc = minecraft.create_connection("rias", "http://cfcmc.duncanleo.me:8080")
	world = minecraft.getWorld(0)

	player = minecraft.getPlayer()
	location = player.getLocation()

	x = location.x
	y = location.y 
	z = location.z

	#world.setTime("day")
	#time.sleep(2)
	
	#create 3 x 3 stone block
	for j in range(3) : 
		for k in range(3) :
			block = world.getBlock(x + k, y, z + j)
			block.setType("STONE")

if __name__ == "__main__" :
	main()