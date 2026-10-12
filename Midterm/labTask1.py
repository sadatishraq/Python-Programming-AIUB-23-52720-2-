players = []
runs = []

n = int(input("Enter the number of players: "))
for i in range(n):
    name = input(f"Enter the name of the player {i+1} :")
    run = int(input(f"Enter the runs scored by {name}: "))

    players.append(name)
    runs.append(run)
    
print("Player Performance: \n")

for i in range(n):
    print(players[i],"scored:", runs[i], "runs")

total = 0
for i in range(n):
    total = total + runs[i]

print("Total score by all the player: ", total)

print()

avg = total / n
print("Average Score:", avg)

highest = 0
for i in range(n):
    if(runs[i]>highest):
        highest = runs[i]

print("Highest Score:", highest)