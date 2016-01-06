from mcpy_simplified import minecraft, location
import json, time

def loadData():
	global block_list

	with open("data/minecraft_data.json", "r") as f:
		data = json.loads(f.read())

	block_list = data['blockTypes']

def main():
	global block_list
	loadData()

	mc = minecraft.create_connection("rias", "http://cfcmc.duncanleo.me:8080")
	world = minecraft.getWorld(0)

	#set world to day
	world.setTime("day")

	player = minecraft.getPlayer()
	location = player.getLocation()

	x = location.x
	y = location.y
	z = location.z

	#create 3 stone blocks at current location
	for i in xrange (3) : 
		block = world.getBlock(x + i, y, z)
		block.setType("STONE")

	#Spawn 3 cows at current location
	cow1 = world.spawnEntity("COW", x, y, z)
	cow2 = world.spawnEntity("COW", x, y, z)
	cow3 = world.spawnEntity("COW", x, y, z)

	#burn one cow after 2 seconds
	time.sleep(2)
	cow1.burn()

	"""
	#Spawn all blocks that can be used in script
	count = x
	countFromZero = 0

	for item in block_list : 
		block = world.getBlock(count, y, z)
		block.setType(block_list[countFromZero])
		count += 1
		countFromZero += 1
	"""

if __name__ == "__main__" :
	main()