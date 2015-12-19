#Generates a 5 x 5 cube 
#using two different types of blocks interlacing each other

from ..mcpy_simplified import minecraft, location
import time, json, random

def loadData():
	global block_list

	with open("mcpy_simplified/data/minecraft_data.json", "r") as f:
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

	world.setTime("day")
	time.sleep(2)

	checker = 0
	blockType1 = random.choice(block_list)
	blockType2 = random.choice(block_list)
	while (blockType1 == blockType2) :
		blockType1 = random.choice(block_list)
		blockType2 = random.choice(block_list)

	for k in range(5) :
		for i in range(5) :
			for j in range(5) :
				block = world.getBlock(x + j, y + k, z + i)
				if (checker % 2) == 0 : 
					block.setType(blockType1)
				else : 
					block.setType(blockType2)
				checker += 1
				
if __name__ == "__main__" :
	main()