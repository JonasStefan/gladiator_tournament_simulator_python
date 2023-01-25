import random
import time

nameList = ["Rüdiger", "Franz Dietrich", "Helmut", "Herbert", "Leopoldine", "Wilhelmine", "Gisela", "Olga", "Ludmilla", "Rudolfine", "Victor", "Adalbert", "Albrecht", "Willibald", "Raimund", "Arnold", "Reinhold", "Rolf", "Leonhard", "Dionysius", "Crescentia", "Agatha", "Apollonia"] # actual popular names between the year 1700 and 1900

class Player:
    def __init__(self):
        self.name = nameList[random.randrange(0, len(nameList))]
        self.dead = False
        self.health = random.randint(50, 100)
        self.damage = random.randint(2, 10)
        self.regen = random.randint(1, 5)
        self.dodgeProbability = random.randint(0, 25)
    
    def take_damage(self, dmg):
        if random.randint(0, 100) > self.dodgeProbability:
            self.health -= dmg
            if self.health <= 0:
                self.dead = True

    def attack(self, opponent):
        opponent.take_damage(self.damage)
    
    def regenerate(self):
        self.health += self.regen

while True:
    deadPlayers = []
    playerList = []

    while True:
        playerAmount = int(input("how many players should participate(power of 2): "))

        if (playerAmount != 0) and (playerAmount & (playerAmount-1) == 0) and (playerAmount != 1):
            break
        print(f"{playerAmount} is not a power of 2!\n")


    for i in range(playerAmount):
        playerList.append(Player())

    print("players participating:")
    for player in playerList:
        print(player.name)

    bet = input("which player do you think will win the game?\nWrite 'no bet' if you don't want to bet: ")

    while True:
        i = 0
        while i < len(playerList):
            player1 = playerList[i]
            player2 = playerList[i + 1]
            print(f"new round!\n{player1.name} vs {player2.name}:")
            i += 2
            
            while True:
                action = random.randint(0, 4)
                if action <= 3:
                    player1.attack(player2)
                else:
                    player1.regenerate()
                time.sleep(0.02) # reroll the RNG
                action = random.randint(0, 4)
                if action <= 3:
                    player2.attack(player1)
                else:
                    player2.regenerate()
                
                if player1.dead:
                    if not player2.dead:
                        print(f"{player1.name} died\n{player2.name} has survived the round with {player2.health} health left!\n")
                        deadPlayers.append(player1)
                        break
                    else:
                        print(f"game was a draw!\n{player1.name} and {player2.name} revived with 10 health left!")
                        player1.health, player1.dead = 10, False
                        player2.health, player2.dead = 10, False
                elif player2.dead:
                    print(f"{player2.name} died\n{player1.name} has survived the round with {player1.health} health left!\n")
                    deadPlayers.append(player2)
                    break
        for i in deadPlayers:
            playerList.remove(i)
        deadPlayers.clear()
        if len(playerList) == 1:
            print(f"{playerList[0].name} is the winner!\nstats:\nhealth left: {playerList[0].health}/100\ndamage per attack: {playerList[0].damage}/10\nhealth regenerated per regeneration: {playerList[0].regen}/5\nprobability to dodge incoming attack: {playerList[0].dodgeProbability}/25\n")
            if bet == "no bet":
                pass
            elif bet == playerList[0].name:
                print("you bet on the right player!")
            else:
                print("you bet on the wrong player. Better luck next time!")
            break
    playAgain = input("Play again(y/n)?: ")
    if playAgain == "n":
        break
    elif playAgain != "y":
        break