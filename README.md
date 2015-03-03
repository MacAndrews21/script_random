# script_random
Little script to get X winners out of N participants.

Just type in the little scipt below in your python console, or rather start `main.py` in your python console. (At this time you get 5 winners in 30 participants) 
```
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
```

