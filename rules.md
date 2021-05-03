# Rules

### Quick Links
- [Welcome](index.md)
- [Bingosync](https://www.bingosync.com/)
- [Presets](presets/presets.md)
- [Rules](rules.md)

In addition to standard Metroid Prime Randomizer racing rules, the following rules apply:

# Modes

There are various Bingo objectives which you can use as the goal. While you are welcome to use any objectives you would like, Prime Bingo has been balanced with the following modes in mind:

### Triple Bingo (1+ players)

The board is revealed when time starts. The game is over when a player completes 3 horizontal, vertical or diagonal lines on the board.

### Lockout (2 Players)

When creating the Bingosync room, choose "Lockout" as the Mode.

The board is revealed when time starts. The first player to complete any 13 tiles wins. Each tile can only be completed by 1 player. Clicking on the corresponding square on Bingosync "locks" the other player from being able to complete that tile. If one player completes an objective, but forgets to click a tile before the other player completes that same objective, the tile goes to the first player to actually click the tile on Bingosync. If a player loses items due to a death or softlock, the corresponding item-related goals become available to be "stolen" by their opponent until

### Double Anti-Bingo (DAB) (2+ Players)

"Double" means that 2 lines are needed to win. "Anti-Bingo" means that each player will be forced to complete 1 line of an opponent's choosing. 

The board is revealed to all players prior to the start of the race. After all the participants have been determined, a circular order of assignment is created randomly. For example:
```
Player 1 -> Player 2 -> Player 3 -> Player 1
```

Following this assignment order, players discretely decide a row, column or diagonal which their assignee must complete during the game. Once all players are ready, each player announces the line which they have chosen for their assignee. As soon as the last player has been informed of their forced line, time begins and gameplay starts. Optionally, you may choose to implement a rule here where each line can only have at most 1 player assigned to it (less fair; more interesting).

The winner is the first player to complete all bingo tiles in the forced line in addition to all tiles in any other 2nd line. Forced lines cannot be changed after being revealed at the start of the game. The self-determined 2nd line does not have to be revealed publicly and can be changed freely. The order of line completion does not matter.

# Reset

In the event of an unexpected death, softlock or crash, the affected player may have progress towards certain tiles reverted. In the event of a reset, apply the following:
- **Item Goals** - Completion reverts to match the new player inventory state. For example, if a player dies after completing the `40 Missiles`, `Get Plasma Processing Item` and `Ice Beam` tiles, but their last save was before all 3 of those events, then they must unmark those boxes on bingosync and recollect those items before remarking them.
- **Action Goals** - Completion persists through the reset. For example, `Use 2 Map Stations`, `Activate the Observatory` and `2 Mini-Bosses` all remain completed after a reset.

Abusing this rule to deathwarp to save stations after completing Action Goals is frowned upon.

# Goals

### Minor/Major Boss (By Name)

Simply defeat the named boss enemy.

Both Phazon Elite and Omega Pirate count as an Elite Pirate.

### X Minor Bosses

Defeat the specified number of Minor Bosses. Minor Bosses include:
- Hive Mecha
- Plated Beetle
- Incinerator Drone
- Chozo Ghosts
- Adult Sheegoth
- Elite Pirate
- Cloaked Drone
- Phazon Elite

Only the first of each mini-boss type (e.g. Elite Pirate) counts towards the goal.

### X Major Bosses

Defeat the specified number of Major Bosses. Major Bosses include:
- Flaahgra
- Thardus
- Omega Pirate
- Meta Ridley
- Metroid Prime (Exo and Essence as one)

### Defeat X Colored Pirates using Y

Defeat the specified number of Colored Pirates (X) using beam combo (Y). Only the killing blow needs to be the beam combo for it to count. Pirates cannot be repeated.

### Clear X in Y Rooms

Find (Y) rooms with the specified enemy type (X), and defeat all of that enemy in that room. Rooms cannot be repeated.

### Boost in X Spinners

Use the specified number of spinners with boost ball. Spinners cannot be repeated.

### Break X [Bendenzium|Cordite] Objects

Find and break the specified number of destructible objects which require either Power Bombs or Super Missiles to destory. Re-destroyed objects do not count. For bendenzium, walls which do not have scan points but require Power Bombs (e.g. Plasma Processing Center) count towards the total.

### All Hall of the Elders Bomb Slots

Activate all 4 bomb slots in HoTE. HoTE and Elder Chamber items are optional.

### Activate the Observatory

Use the scan panel, 2 bomb slots and 4 spinners to activate the Observatory in Phendrana Drifts.

### X Item

Collect the item in the specified location.

### All 3 Vanilla Beam Location Items

Collect the items in Antechamber, Chapel of the Elders and Plasma Processing.

### <Item Name>

Find and collect the specified item.

### Have X Y

Find and collect the specified item (Y) until you have met the count (X). For example, "Have 3 Suits" means that you need to have Varia, Gravity and Phazon. Picking up Varia, Gravity and a duplicate Varia would NOT count.

### Use a Save Station in X Regions

Use at least 1 save station in X regions. This can include Impact Crater, but it will never be required.

### Use X Y Save/Map/Missile Stations

Use the specified number of Save, Map or Missile Stations (X) in the specified Region (Y).

# Locations

### Plated Beetle
- **Ruined Shrine** - Before picking up item or After defeating Flaahgra
- **Main Plaza** - After defeating Flaahgra

### Sheegoth
- **Chapel of the Elders**
- **Quarantine Cave** - After defeating Thardus
- **Ice Ruins East** - After obtaining “Research Core” Item
- **Ice Ruins West** - After obtaining “Research Core” Item

### Elite Pirates
- **Elite Control**
- **Omega Research** - After Defeating Cloaked Drone
- **Dynamo Access** - Have Plasma Beam

### Chozo Ghosts
- **Hall of the Elders** - First visit
- **Furnace** - After using the Wave Bomb Slot in “Hall of the Elders”
- **Ruined Shrine** - After using the Wave Bomb Slot in “Hall of the Elders”
- **Arboretum** - After using the Wave Bomb Slot in “Hall of the Elders”
- **Training Chamber** - First visit
- **Sunchamber** - After defeating Flaaghra and going partially down “Sun Tower”
- **Life Grove** - First visit

### Flying Pirates
- **Frigate Crash Site**
- **Magmoor Workstation**
- **Monitor Station**
- **Triclops Pit**
- **Ruined Courtyard**
- **Control Tower**
- **Research Core**
- **Frozen Pike**
- **Frost Cave**
- **Hunter Cave**
- **Phendrana’s Edge**

### Shadow Pirate
- **Specimen Storage** (yes that's a Shadow Pirate, it just isn’t invisible)
- **Research Entrance** - After obtaining “Research Core” item
- **Research Lab Hydra** - After obtaining “Research Core” item
- **Research Lab Aether** - After obtaining “Research Core” item
- **Research Core** - After obtaining “Research Core” item
- **Mine Security Station** - First visit
- **Elite Control** - After defeating the Elite Pirate here
- **Security Access A**
- **Security Access B**

### Power Pirates
- **Elite Research** - First visit
- **Ore Processing** - Before releasing the Metroids in “Metroid Quarantine A”.
- **Omega Research**
- **Phazon Processing Center** - After obtaining “Plasma Processing” item.
- **Elite Quarters** - During Omega Pirate fight only

### Wave Pirates
- **Elite Research** - First visit
- **Ore Processing** - Before releasing the Metroids in “Metroid Quarantine A”.
- **Omega Research**
- **Mine Security Station**
- **Metroid Quarantine B**
- **Phazon Processing Center** - After obtaining “Plasma Processing” item.
- **Elite Quarters** - During Omega Pirate fight only

### Ice Pirates
- **Elite Control** - Only spawns before Elite Pirate here is defeated.
- **Central Dynamo** - On return after defeating Cloaked Drone.
- **Mine Security Station** - Return after first visit.
- **Elite Quarters** - During Omega Pirate fight only

### Plasma Pirates
- **Metroid Quarantine B**
- **Phazon Processing Center** - After obtaining “Plasma Processing” item.
- **Elite Quarters Access** - First visit
- **Elite Quarters** - During Omega Pirate fight only

### Metroids
- **Research Lab Hydra** - After obtaining “Research Core” item
- **Research Lab Aether**
- **Research Core** - After obtaining “Research Core” item
- **Ore Processing** - After releasing the Metroids in “Metroid Quarantine A”
- **Metroid Quarantine A**
- **Fungal Hall B**

### Super Missile Objects
- **Biohazard Containment**
- **Main Plaza**
- **Sun Tower x2**
- **Crossway**
- **Phendrana Shorelines**
- **Ruined Courtyard**
- **Research Lab Hydra**
- **Metroid Quarantine B**

### Bendenzium Objects
- **Life Grove Tunnel**
- **Life Grove**
- **Furnace**
- **Magmoor Caverns**
- **Warrior Shrine**
- **Geothermal Core**
- **Shore Tunnel**
- **Workstation Tunnel**
- **Phendrana's Edge**
- **Security Access A**
- **Mine Security Station**
- **Elite Research**
- **Ore Processing**
- **Maintenance Tunnel**
- **Phazon Processing Center**
- **Omega Research**
- **Ventilation Shaft**
- **Omega Research**
- **Central Dynamo**
- **Metroid Quarantine A**
- **Phazon Mining Tunnel**
