import random
count = 0
while count < 100:
    bill = []

    while len(bill) < 7:
        bill.append(random.randrange(1, 10))

    print(*bill, sep='')
    count += 1

