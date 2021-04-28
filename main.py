import json

from sys import exit
from pathlib import Path

from world import World
from command import Command

class Main:

  """
Object / Class Structure
  World object  - represents a world, has list of zones, world.zone[0].rooms[0][0] == room
  Zone objet    - represents an area on the world, has climate, language, ...
  Room object   - a location on a map, has short/long descriptions
  Item object   - something to be equipped, picked up, dropped, held
  Player object - the titular character of the story
  Mob object    - the challenges in the world
  Event object  - things that happen in the world
Directory Structure
  /world
    /zone-name
      /zone-name.information
      /items/
      /mobs/
      /resets/
      /rooms/
      /events/
  /players
    /player-name
      /items/
      /player-name.information
      /player-name.explored
  """

  text = ''
  plist = []

  def __init__(self):
    pass

  def load_world(self):
    ftest = Path('world/admin/admin.information')
    if (ftest.is_file()):
      with open('world/admin/admin.information') as json_file:
        data = json.load(json_file)
        self.world = World(data)
      return True
    else:
      return False

  def load_player(self, player_name):
    ftest = Path('players/' + player_name + '.json')
    if (ftest.is_file()):
      with open('players/' + player_name + '.json') as json_file:
        self.plist.append(json.load(json_file))
      return True
    else:
      return False

  def save_player(self):
    if (self.plist):
      with open('players/' + self.plist[0]['info']['name'] + '.json', 'w') as json_file:
        json.dump(self.plist[0], json_file)
      return True
    else:
      return False

  def quit(self):
    self.save_player()
    exit(0)

  def loop(self):
    while(1):
      if (self.plist):
        self.text = input(self.plist[0]['info']['prompt'])
      else:
        self.text = input('Prompt > ')
      if (self.text in Command.command_list):
        getattr(Command, self.text)(self, self.plist)


if (__name__ == "__main__"):
  main = Main()
  main.load_world()
  main.loop()
