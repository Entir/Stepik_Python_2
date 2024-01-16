cost = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
total = 0
word = input()
for i in word:
    for c in cost:
        if i in cost[c]:
            total += c

print(total)
