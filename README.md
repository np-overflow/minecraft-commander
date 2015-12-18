# minecraft-commander

This python library allows the usage of python scripts to communicate directly with a Minecraft server. This is useful if you will like to use scripts to easily build structures in Minecraft. [Mineslave](https://github.com/np-overflow/mineslave) plugin will need to be installed on the server for the library to work.

## Challenge
A demo and 2 challenge scripts with different difficulties are provided in the repository. The demo script can be run in the terminal using
```
python -m mcpy_simplified.challenges.challenge_demo
```

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
entity.setName("cow")

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

## Libraries
This project depends on the following libraries:
- [Requests](https://pypi.python.org/pypi/requests/#downloads)

Have fun and enjoy using the library!
