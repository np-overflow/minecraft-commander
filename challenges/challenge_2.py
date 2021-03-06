#Generates a 5 x 5 cube with alternating blocks

from ..mcpy_simplified import minecraft, location

def main() :
	block_list = ["WOOD", "STONE"]

	#Change to username
	mc = minecraft.create_connection("rias", "http://cfcmc.duncanleo.me:8080")
	world = minecraft.getWorld(0)

	player = minecraft.getPlayer()
	location = player.getLocation()

	x = location.x
	y = location.y
	z = location.z

	world.setTime("day")

	checker = 0
	blockType1 = block_list[0]
	blockType2 = block_list[1]

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