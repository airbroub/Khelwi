import random

# Créer une liste de 1 à 13, chaque nombre apparaissant 4 fois
init_list = [i for i in range(1, 14) for _ in range(4)]

# Mélanger cette liste de manière aléatoire
random.shuffle(init_list)

print(len(init_list))

# Initialiser les joueurs
number_of_players = 2  # Changez ce nombre pour le nombre de joueurs souhaité
players = {f'player_{i+1}': [] for i in range(number_of_players)}

# Attribuer 4 nombres aléatoires à chaque joueur
for player in players:
    players[player] = [init_list.pop() for _ in range(4)]

# Afficher les résultats
print("Liste initiale après distribution :")
print(init_list)
print("\nNombres attribués à chaque joueur :")
for player, numbers in players.items():
    print(f"{player}: {numbers}")

trash_list = []

def toTrash(t):
    trash_list.append(t) #ajout a la poubelle

def piocher(P):
    if P==1:
        return init_list.pop(0)
    return init_list.pop(1)
#print('voici ta pioche : ',piocher(1))

def choix():
    print('1- Echanger') 
    print('2- Eliminer') 
    print('3- Special card')
    print('4- Jeter')
    x = input('je choisi : ')
    return x

def echanger(player, P):
    r = int(input('quelle carte remplacer ? : '))
    
    toTrash(players[player][r]) #ajout a la poubelle
    players[player][r] = P #remplacer la carte numero r avec celle Pioché


def eliminer(player, P):
    e = int(input('Quelle carte veux tu éliminer ? : '))
    
    if players[player][e] == P:
        toTrash(players[player][e])
        toTrash(P) 
        players[player][e] = None
    else:
        players[player].append(P)

def jeter(P):
    toTrash(P)

def spCard(player,P):
    if P==7 or P==8:
        c = int(input('Quelle carte de ton deck veux tu check ? : '))
        print(players[player][c])

spCard('player_1',7)