# True and false are the boolean types in python
# True and False are also the key words in python

# Operations rgat give boolean type

a = 5
b = 10
 c = 15

 # relations Operations
 print(b > a) # true
 print (b != a) # true
 print(b < a) # false
 print(a = c) # false


 # Logical Operations
 print(b > a and a == c) # False
 print(b > a or  a == c) # true
 print (not true ) # False
 print(not false) # true 
 print (not a) # false 


 # Identity Operations
 a = 1
 b = 1
 print(a=b) # true
 print(a is b) # true


 a = 1234475732567 # it is creates in one mermory location
 b = 1234475732567 # It is creates in another memory location
print(a = b)  #true
print(a is b) # false



# Concept of Truthy and Falsy
# Truthy
# All non-empty datatypes and non-zero are truthy values
a = 12
b = 5,7
c = [1,2]
d = [4,5]
e = {1,2}
f = {name;"John"}
g = true
 # all these datatypes are truthy datatypes
# we can also check truthiness of the data dunction using bool function


# Falsy
# All empty datatypes and zero are falsy values
a = 0
b = 0.0
c = []
d = ()
e = {}
f = set()
g = False
h = None
print(bool(g))  # false



  # Membership Operations\
  print(2 in[1, 2, 3]) #True
  print(3 not in [1,2,3])  # False

  # Python Booleans are the subclass of the integer class. That means True is 1 and False is 0
  a = 5
  b = 3
  print(a+b) #4 
  print(70 * false) # 0
  print(true + true) # 2
