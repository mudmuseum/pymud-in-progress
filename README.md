# PyMud

A very simple start to a single player Python based MUD.

## Features

1. Login
2. Saving
3. Prompt
4. Commands list
5. Quitting
6. World loading via JSON
7. Player loading / saving via JSON

## Intended outcome

### Object / Class Structure

* World object  - represents a world, has list of zones, world.zone[0].rooms[0][0] == room
* Zone objet    - represents an area on the world, has climate, language, ...
* Room object   - a location on a map, has short/long descriptions
* Item object   - something to be equipped, picked up, dropped, held
* Player object - the titular character of the story
* Mob object    - the challenges in the world
* Event object  - things that happen in the world

### Directory Structure
```bash
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
```
