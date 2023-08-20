# Methods are also functions but methods are the functions onside the class
# Methods must be called class object


def addition(a,b):
    return a+b

 # heren addition is just a function but not a method
 result = addition(2,3) # function call
 print(result) # 5


class student:
    def get_age_after_10(self,current_age):
        return current_age + 10


student student()
result = student.get_age_age_after_10_years(21.)
print(result) #31
# here get_age_after_10_years ()is a method



#### list methods####
# 1. append()
vowels = ["a","e","i","o"]
vouwels.append("u")
print (vowels) # ["a","e","i","o","u"]


# 2. extend()
data = [1,2,3]
data.extend( [4,5,6])
print(data) #[1,2,3,4,5,6]


# 3. insert()
vowels =['a','e','o','u']
vowels.imsert (2,'i')
print(vowels) # ["a","e",'"i","o","u"]


# 4. remove()
vowels ["a","e",'"i","o","u"]
vowels.remove("o")
print (vowels) # ["a","e",'"i","u"]

# vowels.remove ("2") # this raises error: value error

#5. pop()
vowels =['a','e','o','u']
result = vowels.pop()
print(result) #u
print(vowels) # ["a","e",'"i","o"]

result =vowels.pop(1)
print(result)#e
print(vowels) = ["a","i","o"]


#6. clear()
vowels.clear()
print(vowels) #[]


#7. index()
vowels = ["a","e",'"i","o","u"]
result = vowels.index ("e")
print(vowels) # ["a","e",'"i","o","u"]
print(resul) #1

# 8. count()
data [1,2,1,2,2,5,4,4,5]
result = data.count(2)
result = data.count(2)
print (result) #3
