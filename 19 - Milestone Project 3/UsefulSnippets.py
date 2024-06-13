array = [0,1,2,3,4,5]
print(array[3:])
print(array[:3])
print(array[3::-1])
print(array[:3:-1])
print(array[::3])
print(array[::-2])

print(5%8)
print(13%8)
print(-3%8)

print(5//8)
print(13//8)
print(-3//8)

print(list(map(lambda n: n%3, array)))

set1 = (1, 2, 3)
print(set1)
print(1 in set1)