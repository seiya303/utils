from itertools import permutations

# a = [1, 2, 3, 4]
permute = permutations(range(1,10), 6)

res = list(permute)
print(len(res))