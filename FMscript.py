import urllib.request
from player import Player
 

#carico le previsioni
playersFile = urllib.request.urlopen("https://raw.github.com/legard9/FantaMasterchef2018-2019/master/players.txt")

players = []; playerName = None; bet = []; exits = []

for line in playersFile:
    line = line.decode('utf-8')
    if '-' in line:
        playerName = line[1:].rstrip()

    elif line == '\n':    
        players.append(Player(playerName,bet))
        bet = []
        playerName = None

    else:
        bet.append(line.rstrip().lower())

#carico gli usciti
usciteFile = urllib.request.urlopen("https://raw.github.com/legard9/FantaMasterchef2018-2019/master/uscite.txt")
for uscito in usciteFile:
    uscito = uscito.decode('utf-8').rstrip()
    if uscito != '':
        exits.append(uscito.rstrip().lower())
    else:
        exits.append('none')

#invoco il calcolo punti 
for player in players:
    player.calc_points(exits)

#ordino la lista giocatori per punti 
players = sorted(players, key=lambda x: x.points, reverse = True)

#stampo il menù opzioni
while True:
    selection=input("Selezionare una opzione: \n1)Classifica \n2)Uscite \n3)Partecipanti\n")
    if selection == '1':
        print("\nClassifica: \n")
        for player in players:
            print(player.name, " -> ", player.points)
    elif selection == '2':
        print("\nUscite: \n")
        i = 1
        for uscito in exits:
            print(i, ")", uscito)
            i += 1
    elif selection == '3':
        print("\nPartecipanti: \n")
        for player in players:
            player.status()
    else:
        print("\ncomando non valido! \n")    
  