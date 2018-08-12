def iteration(counter):
    return((4 * counter**2) / (4 * counter**2 - 1))

sum = 1
for i in range (1, 10000):
    sum = sum * iteration(i)
sum = sum * 2
print(sum)