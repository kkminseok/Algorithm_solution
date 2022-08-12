from itertools import permutations

n = int(input())
li = [x for x in range(1,n+1)]

result = list(permutations(li))

for i in range(len(result)):
    print(' '.join(map(str,result[i])))
