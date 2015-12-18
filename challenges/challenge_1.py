#Generates a 5 x 5 cube with randomized type for each row

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

	usedBlockTypes = []
	player = minecraft.getPlayer()
	location = player.getLocation()

	x = location.x
	y = location.y
	z = location.z

	world.setTime("day")
	time.sleep(2)

	for i in range(5) :
		#when i changes, randomizes x
		randBlockType = random.choice(block_list)
		while (randBlockType in usedBlockTypes) :
			randBlockType = random.choice(block_list)
			
		for j in range(5) : 
			for k in range(5) :
				block = world.getBlock(x + j, y + i, z + k)
				block.setType(randBlockType)

		usedBlockTypes.append(randBlockType)

				
if __name__ == "__main__" :
	main()