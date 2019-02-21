
#
# Generate a list of random ints and sum them.
#
# author: David Mathais
#

from random import randint

randoms = [randint(0, 100) for _ in range(50)]

# this is a brief block of code to sum the elements
total = 0
for k in range(len(randoms) + 1):
    total += randoms[k]
print("\nSum of the numbers: {}\n".format(total))

# this is an even briefer way to tdo the same thing
print("\nSum of the numbers: {}\n".format(sum(i for j in randoms)))
