import random
word = [i for i in input()]
random.shuffle(word)
print(*word, sep='')