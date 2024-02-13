#1. Write a program that uses a single print command with a number of arguments to print to the screen the
#strings “Hello,” and “world.” The output should include a space between the comma and the word “world”.

greeting = "Hello" + ", " + "world" + "."
print(greeting)

#2. Write a program that uses a single print command with a single argument to print to the screen the concate-
#nation of the strings “Hello,” and “world.” Again, the output should include a space between the comma and
#the word “world”.

greeting = "Hello"
name = "world"
sentence = greeting + ', ' + name + "."
print(sentence)

#3. Write a program that assigns to a variable the concatenation of the strings “Hello,” and “world.” and includes
#a space between the comma and the word “world”. The program should then print out the value of this
#variable.

name = "world"
sentence = f"Hello, {name}."
print(sentence)

#3.5. An additional way to write strings which may be encountered similar to f-strings 
# is using the following format where the variable is left

name = "world"
sentence = "Hello, {}."
print(sentence.format(name))

#4.A string in Python is a sequence of characters. You can access the characters one at a time using the index,
#an expression in square brackets. The index indicates which letter is required from the string. For example,
#consider the following code segment:

my_string = "Hello, world"
b = my_string[0:]
print(b)

#5. In Python, a segment (substring) of a string is called a slice. Selecting a slice is done in a similar way to
#selecting a character, for example:

#animals = 'herd of elephants'
#seg = animals [x:y]
#print ('Segment is:', seg)

#where x and y are replaced by integers (indexes).
#Experiment with different values of x and y. For example:
#(a) What happens when x and y are the same?
#(b) What happens when x is greater than y?
#(c) What happens when x is omitted?
#(d) What happens when y is omitted?
#(e) What happens when both x and y are omitted?

animals = 'herd of elephants'
seg = animals[0:8]
a = animals[1:1]
b = animals[5:2]
c = animals[:5]
d = animals[6:]
e = animals[:]

print("Segment is:", seg)
print("Segment is:", a)
print("Segment is:", b)
print("Segment is:", c)
print("Segment is:", d)
print("Segment is:", e)
