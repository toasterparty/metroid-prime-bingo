### Quick Links
- [Welcome](index.md)
- [Bingosync](https://www.bingosync.com/)
- [Presets](presets/presets.md)
- [Rules](rules.md)

# Rules

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

In the event of an unexpected death, softlock or crash, the affected player may have progress towards certain tiles reverted. In the event of a reset:
- **Item-Related Goals** - Reverts to match the new player inventory state. For example, if a player dies after completing the `40 Missiles`, `Get Plasma Processing Item` and `Ice Beam` tiles, but their last save was before all 3 of those events, then they must unmark those boxes on bingosync and recollect those items before remarking them.
- **Action Goals** - Completion persists through the reset. For example, `Use 2 Map Stations`, `Activate the Observatory` and `2 Mini-Bosses` all remain completed after a reset.

Abusing this rule to deathwarp to save stations after completing Action Goals is frowned upon.

# Goals
*A neat list of all the goals and their descriptions will go here.*
