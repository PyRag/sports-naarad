# PyRag Sports API
A collection of command line tool and web API
## Installing Command line tool for pyrag
You must have python3 installed on your local system.
Download the [zip](https://github.com/npcoder2k14/HackInTheNorth-PYRAG/archive/dev.zip) file or clone the repository dev's branch
```bash
$ git clone https://github.com/npcoder2k14/HackInTheNorth-PYRAG/
```
Install the requirements
```bash
$ pip3 install -r requirements.txt
```
Run setup.py
```bash
$ python3 setup.py install
```
# Usage
```bash
$ pyrag -h
Usage: pyrag [-h] [-F] [-C] live_score|news|[player_stats name] [-my_fav_team]

Get latest updates for football and cricket

Options:

-h, --help                shows help(this) message

-F, --football [uefa,
barclay, fifa]            Get football updates. The tournament for which you
                          want to get updates. One of the argumets from uefa,
                          barclay and fifa is compulsory.

-C, --cricket             Get cricket updates for international matches.

[live-score, news,
,fixtures
player-stats[name]]       Fields to get. `live-scores` to get live socre of
                          on-going matches, `news` to get latest news headlines,
                          `player-stats` to get statistics of player specified.
                          `fixtures` to get updates on upcoming matches.
                          Compulsory single argument. For football option you
                          can give additional options topscorer.
                          Use `-` instead of space in names.

-proxy                    To specify proxy. Defaults to system proxy. Take name of
                          a file. Sample -proxy http://username:password@host:port/

$ pyrag -F barclay topscorer
╒══════════════════╤═══════════════╕
│ Player Name      │   Goal Scored │
╞══════════════════╪═══════════════╡
│ Harry Kane       │            22 │
├──────────────────┼───────────────┤
│ Jamie Vardy      │            19 │
├──────────────────┼───────────────┤
│ Romelu Lukaku    │            18 │
├──────────────────┼───────────────┤
│ Sergio Agüero    │            17 │
├──────────────────┼───────────────┤
│ Riyad Mahrez     │            16 │
├──────────────────┼───────────────┤
│ Odion Ighalo     │            14 │
├──────────────────┼───────────────┤
│ Olivier Giroud   │            12 │
├──────────────────┼───────────────┤
│ Jermain Defoe    │            12 │
├──────────────────┼───────────────┤
│ Diego Costa      │            11 │
├──────────────────┼───────────────┤
│ Gylfi Sigurdsson │            10 │
╘══════════════════╧═══════════════╛

```
## WEB API USAGE

The sportsAPI is hosted at http://cherry-shortcake-81993.herokuapp.com

The API at present contains data for Football and Cricket.

More Sports will be added later so stay tuned :)

To access Cricket data :-

for cricket live scores : go to /cric/live/

for cricket news : go to /cric/news/

for cricket upcoming match list : go to /cric/matches/

for cricket player stats : go to /cric/player_stats/?player-name="PLAYER_NAME"  # In the double quotes player name will be provided


To access Football data :-

for football live scores : go to /foot/live/

for football latest match results : go to /foot/results/

for football news : go to /foot/news/

for football pointstable : go to /foot/pointstable/

for football player stats : go to /foot/stats/?player-name=PLAYER_NAME          # There will be no double quotes

