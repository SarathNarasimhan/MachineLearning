from functools import reduce

nums = [2,4,8,7,3,6,9]

evens = list (filter(lambda n : n%2==0, nums))

doubles = list (map(lambda n : n*2, nums))

sum = reduce(lambda a,b : a+b, evens)


print(sum)
print (evens)
print(doubles)