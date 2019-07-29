# Gambling.py
**Gambling** will calculate a player's gambling downtime results. The algorithm used to calcualte the results was derived from Xanathar's Guide to Everything and adapted to per hour.

### Usage
```s
    Gambling.py [-h] [-gph GPH] [-m MODIFIER]
                   insight intimidation deception hours gold

positional arguments:
  insight               Insight check rolled by player.
  intimidation          Intimidation check rolled by player.
  deception             Deception check rolled by player.
  hours                 Number of hours to gamble.
  gold                  Amount of gold being bet.

optional arguments:
  -h, --help            show this help message and exit
  -gph GPH              Gold that is reserved for bet per hour.
  -m MODIFIER, --modifier MODIFIER
                        Difficulty modifier for location.
```