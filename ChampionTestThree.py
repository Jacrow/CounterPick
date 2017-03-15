champions = []
with open('CleanChampionStats.txt') as inputfile:
    for line in inputfile:
        champions.append(line.strip().split(','))
        
numberOfChampions = len(champions)
for x  in champions:
    champion_x=[champions[1]]
    print (champion_x)


