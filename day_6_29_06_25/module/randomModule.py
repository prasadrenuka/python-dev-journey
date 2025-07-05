import random
# total functions ?
## 69
print(len(dir(random)))
print(dir(random))
# print(random.)
print(random.randint(1,100))
print(random.random())
print(random.uniform(1,10))
print(random.choice(['java', 'python', 'javascript', 'c++', 'c']))
languages = ['java', 'python', 'javascript', 'c++', 'c']
random.shuffle(languages)
print(languages)
print(random.sample(range(1,10),3))

# 📝 Problem Statement:
# Create a "Lucky Draw" game that:
#
# Takes a list of player names
#
# Randomly picks one winner
#
# Shuffles the original list and displays it
print('Enter players')
players =input