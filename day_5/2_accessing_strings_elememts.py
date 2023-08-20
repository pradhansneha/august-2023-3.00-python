# we can access strings elemnts using indexing and slicing which is similar
# to the list
# Forward indexing starts from ) and reverse indexing from -1

message = "hello world"
print(message[0])# h
print(message[5]) # <space>
print(message[-1]) # d
print(message[-8]) # l
print(message[20]) # error
print(message[-20]) # error



# Slicing
message = "I am learning Python"
print(message[:6]) # 'I am l'
print(message[0:5]) # 'I am  '
print(message[3: 8]) #'m lea'
print(message[4:]) 'learning python'
print(message[7: 2]) # ' '
print(message[-8:-2]) # 'g pyth'
print(message[-6: -8]) # ' '
print(message[3:-3]) # 'mlearning pyt'
print(message[9:-11]) # ' '
print(message[3:8: 2 ]) # 'mla'

# Creating the object(empty and non empty)
#accessing the elements (indexing/slicing/accessing element using key)
# Operations
# methods
# built-in function



# message = "hello
# message[2]" = "L"
# print(message) # It is not possible because string is immutable
# print(message)

# message = "Hello"
# message[2] = "L"   # It is not possible because string is immutable
# print(message)

del message  # del is a keyword that deletes the object
