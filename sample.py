from mcpy_simplified import minecraft, location

mc = minecraft.create_connection("dave", "http://localhost:8080")
world = minecraft.getWorld(0)

player = minecraft.getPlayer()
location = player.getLocation()

for x in range(100):
	block = world.getBlock(location.x + x, location.y, location.z)
	block.setType("STONE")