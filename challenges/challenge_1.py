#Generates a 5 x 5 cube with different rows

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

	for i in range(5) :
		for j in range(5) :
			for k in range(5) :
				block = world.getBlock(x + j, y + i, z + k)
				block.setType(block_list[i])
				
if __name__ == "__main__" :
	main()