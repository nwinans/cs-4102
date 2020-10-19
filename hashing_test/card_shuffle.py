import random

def hash_location(l):
    ret = ""
    for i in l:
        ret += str(i)
    return ret

cards = [1,2,3]
results = {}
for _ in range(10000):
    iteration = cards
    for i in range(len(cards)):
        j = random.randint(0, len(cards) - 1)

        temp = cards[j]
        cards[j] = cards[i]
        cards[i] = temp
    
    location = hash_location(iteration)

    if location not in results:
        results[location] = 1
    else:
        results[location] += 1

print(results)