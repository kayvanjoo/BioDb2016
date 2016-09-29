from sys import argv

def rabbits(n, k):
    fib_seq = []

    for i in range(n):
        if i < 2:
            fib_seq.append(1)
        else:
            adults = fib_seq[-1]     # Previous month's rabbits are all adults
            babies = fib_seq[-2] * k  # All rabbits from 2 months ago have babies
            fib_seq.append(adults + babies)

    return fib_seq[-1]


def main():
    with open(argv[1], 'r') as inf:
        data = inf.read()

    n = int(data.split()[0])  # Months
    k = int(data.split()[1])  # Rabbit pairs produced per pair

print (rabbits(32, 3))