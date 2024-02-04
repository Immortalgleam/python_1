# 1. Index of the Maximum Element:
# Create a list of numbers and find the index of the maximum element in the list.
new_list = [1, 2, 30, 40, 50, 100]
max_index = new_list.index(max(new_list)) # max index
print(max_index)

# 2. String Concatenation:
# Ask the user for their first name and last name, then concatenate them into a single string.
first_name = 'John'
last_name = 'Dou'
print(first_name, last_name)
full_name = f"{first_name} {last_name}"  # f-string
print(full_name)

# 3. String Reversal:
# Input a string from the user and print it in reverse order.
print(full_name[::-1])

# 4. Checking Element Presence:
# Create a list and ask the user to input a number, then check if this number is present in the list.
list_numbers = [1, 2, 3]
user_number = int(input("Please enter the number: ")) # input() function
if user_number in list_numbers:
    print(True)
else:
    print(False)

# 5. String Comparison:
# Input two strings from the user and check if they are equal.
print(first_name == last_name) # equality of 2 objects

# 6. Sum of Tuple Elements:
# Create a tuple of numbers and print their sum.
new_tuple = (1, 3, 4, 5)
print(new_tuple)
print(sum(new_tuple))

# 7. Splitting a String into Words:
# Input a sentence from the user and split it into words, then print each word on a new line.
sentence = 'Python is cool!'
words = sentence.split()
for word in words:
    print(word)

# 8. Every Second Element:
# Create a list of 10 elements (of any type) and print every second element on the screen.
list_1 = [1, 2, 3, 4, 5, 6]
print(list_1[::2])

# 9. List Operations:
# Perform basic operations on a list, such as appending an element, removing an element, and finding the length.
# create empty list
empty_list = []
# add first element
empty_list.append(0)
print(empty_list)
# add second  element
empty_list.append(1)
print(empty_list)
# add third element
empty_list.append(2)
print(empty_list)
# remove second element from a list
empty_list.remove(1) # method for this operation
# create a variable which will store first element from a list and remove it from  alist at the same time(one operation)
my_list = [1, 2, 3, 4, 5]
first_element = my_list.pop(0)
print('First_element:', first_element)
print('List after element was removed:', my_list)
# clear list
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)

# 10. Create a string of length 10 with empty spaces in it. change empty spaces with '+' sign
str_new = ' ' * 10
str_new = str_new.replace(' ', '+') # fixed
print(str_new)

# 11. Simple Arithmetic Operations:
# Input two numbers from the user and perform simple arithmetic operations (addition, subtraction, multiplication, division).
a = 14
b = 2
print(a + b)
print(a / b)
print(a - b)
print(a * b)