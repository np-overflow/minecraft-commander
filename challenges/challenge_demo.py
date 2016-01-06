#Generates a 3 x 3 flat stone block for demo 

from ..mcpy_simplified import minecraft, location

def main() :
	block_list = ["BEDROCK", "COBBLESTONE", "GLASS", "BRICK", "ICE"]

	#Change to username
	mc = minecraft.create_connection("rias", "http://cfcmc.duncanleo.me:8080")
	world = minecraft.getWorld(0)

	player = minecraft.getPlayer()
	location = player.getLocation()

	x = location.x
	y = location.y 
	z = location.z

	world.setTime("day")
	
	"""
	START EDITING HERE
	"""

	#create 3 x 3 stone block_list
	for j in range(3) : 
		for k in range(3) :
			block = world.getBlock(x + k, y, z + j)
			block.setType("STONE")

	""""
	END OF EDITING
	"""

if __name__ == "__main__" :
	main()