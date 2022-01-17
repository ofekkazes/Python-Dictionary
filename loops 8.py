"""
A for loop is used for iterating over a sequence (that is either a list, a dictionary, or a string).
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

"""
We can break a loop using the break keyword
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

"""
If we want to simply iterate x number of times we can use the range function
"""

for x in range(6):
  print(x) # prints 0 1 2 3 4 5

"""
Inner Loops

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop"
"""

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)