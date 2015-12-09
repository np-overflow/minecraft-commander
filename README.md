# minecraft-commander

This python library allows the usage of python scripts to communicate directly with a Minecraft server. This is useful if you would like to use scripts to easily build structures in Minecraft. [mineslave](#) plugin will need to be installed on the server for the library to work.

## Usage
Import library
```python
from mcpy_simplified.mcpy_simplified import minecraft, location
```

Create connection to Minecraft Server
```python
minecraft.create_connection(user, server_url)
```


### World
```python
#get world object
world = minecraft.getWorld(world_index)

#set time to day
world.setTime("day")

#set time to night
world.setTime("night")

#get block object
block = world.getBlock(x, y, z)

#set block type
block.setType(typ)

#spawn and get entity
entity = world.spawnEntity(entity_type, x, y, z)
```


### Player
```python
#get player object
player = minecraft.getPlayer()

#get player location
playerLoca = player.getLocation()

#set player location (teleport)
player.setLocation(x, y, z)

#chat
player.chat("Hello World")
```


### Entity
```python
#set name
entity.setName("cow1")

#burn
entity.burn()

#shoot up
entity.shootUp()

#hurt
entity.hurt()

#kill
entity.kill()
```


*Location object contains position x, y and z as its attributes.*


Have fun and enjoy using the library!
