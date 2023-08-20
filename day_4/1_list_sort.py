# sort()
# sort method can take two parameters: akey and a reverse
# reverse takes boolean type and key takes a function

data = [10, 23, 1, 2, 4, 12, 40, 5]
result = data.sort()
print(result) # none
print(result) # [1, 2, 4, 5, 10, 12, 23, 40]

data.sort(reverse=true)
print(data) # [40, 23, 12, 10, 5, 4, 2, 1]

data = ["mango", "banana", "apple", "pineapple"]
data.sort
print(data) # [ "apple", "banana", "mango", " pineapple"]

data.sort (reverse=true)
data ["pinapple", "mango", "banana", "apple"]



data = [(10,12), (3,5), (2,1), (40,10), (3,8)]
#result [(2,1), (3,5), (3,8), ), (40,10), (10,12)]


def get_secod_element (data):
    pass

data.sort(key=get_second_element)
print(data)

