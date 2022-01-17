"""
Condition

We can have conditions in python  to set a block of code if something is met or not met
"""

a = 20
b = 10

if a > b:
    print("a")
else: 
    print("b")

"""
Condiions will receive a boolean value.
"""

res = True #The boolean value can be taken from a variable
res = a > b #Or from an operand

if res:
    print("a")

"""
We can also perform arithmetic calculations inside the conditions
"""

if a + b > 20:
    print("bigger")

"""
The elif keyword is pythons way of saying "if the previous conditions were not true, 
then try this condition".
"""

if a > b:
    print("a")
elif b > a:
    print("b")
else:
    print("a and b are equal")

"""
The available operands are:
> bigger then
< less then
>= bigger or equals to
<= less then or equals to
== equals
!= not equals
"""

"""
we can also have multiple conditions on one if block using:
and - if the two conditions are met
or - if one condition is met
"""

if (a > b and a > 0 and b > 0) or a > 20:
    print("Either a is bigger than b, a is bigger than 0 and b is bigger than 0 or a is bigger than 20")