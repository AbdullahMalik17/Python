import copy 
# Swallow Copy of list 
a = [1, 2, 3, 4, 5]
b = a 
b.append(6)
print("Original:",a)
print("Swallow Copy:",b)

# Deep Copy of List
list1 = [1, 2, 3, 4, 5]
list2 = copy.copy(list1)  
list2.append(6)
print("Original:", list1)
print("Swallow Copy:", list2)
 # Swallow Copy of Immutable Type
num = 4
num1 = num
num1 = 5
print("Original:", num)
print("Swallow Copy:", num1)