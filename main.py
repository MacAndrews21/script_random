import random
''' x = random.randint(start,end) ==> start <= x <= end '''
winner = []
start= 0 
participants = 30
winners = 5
while True:
    randomVariable = random.randint(start, participants)
    if randomVariable not in winner:
        winner.append(randomVariable)
    if len(winner) == winners:
        break

print len(winner), winner        