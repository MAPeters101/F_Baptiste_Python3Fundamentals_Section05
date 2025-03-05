'''
Exercise 1
Given the following string:

s = 'FfEeDdCcBbAa'
Create two new variables that contain just the lower and upper case letters
of s respectively, in the correct alphabetical order, i.e:

'ABCDEF'
'abcdef'
Solution
The string s is in reverse order, so at some point we'll need to reverse the
string. We could either do it before we extract the upper and lower case
characters, or we could do it after. Let's do both ways.

We'll start by reversing the order first:

reversed_s = s[::-1]
reversed_s
'aAbBcCdDeEfF'
Now we can use extended slicing starting at 0 to pick out every second
character:

reversed_s[::2]
'abcdef'
And starting at 1 to pick out the upper case characters:

reversed_s[1::2]
'ABCDEF'
Alternatively, we could pick the upper/lower case characters first, and then
reverse each result:

s[::2][::-1]
'ABCDEF'
s[1::2][::-1]
'abcdef'


Exercise 2
Concatenate the following tuples into a single one, but replacing the odd
values with zeros (0).

t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17
You can assume that every tuple is a sequence of consecutive integers
starting with an odd integer.

Try to write your code to be as generic as possible.

Solution
We cannot mutate tuples, so we'll need to convert our tuples to lists first:

l1 = list(t1)
l2 = list(t2)
l3 = list(t3)
Now that we have mutable sequences, we can use extended slicing to replace
the odd integers with 0 in each list:

l1[::2] = [0, 0, 0]
l2[::2] = [0, 0]
l3[::2] = [0, 0, 0, 0]
l1
[0, 2, 0, 4, 0, 6]
l2
[0, 8, 0, 10]
l3
[0, 12, 0, 14, 0, 16, 0]
So this works, but you'll notice that we had to calculate (in our heads) how
many zeros to replace the extended slice with (since with extended slicing the
number of elements on both sides of the assignment must match).

This is not very generic code - instead we can determine how many elements are
in each extended slice by using the len function:

len(l1[::2]), len(l2[::2]), len(l3[::2])
(3, 2, 4)
We also know that we can create a list of n repeated elements simply by
multiplying a list by an integer:

[0] * 5
[0, 0, 0, 0, 0]
So, we could replace each extended slice by a list [0] multiplied by the
length of the extended slice:

l1 = list(t1)
l2 = list(t2)
l3 = list(t3)

l1[::2] = [0] * len(l1[::2])
l2[::2] = [0] * len(l2[::2])
l3[::2] = [0] * len(l3[::2])

l1, l2, l3
([0, 2, 0, 4, 0, 6], [0, 8, 0, 10], [0, 12, 0, 14, 0, 16, 0])
Now we can concatenate those lists:

result = l1 + l2 + l3
result
[0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16, 0]
But we actually want a tuple for our result:

result = tuple(l1 + l2 + l3)
result
(0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16, 0)
Putting everything together:

l1 = list(t1)
l2 = list(t2)
l3 = list(t3)

l1[::2] = [0] * len(l1[::2])
l2[::2] = [0] * len(l2[::2])
l3[::2] = [0] * len(l3[::2])

result = tuple(l1 + l2 + l3)
result
(0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16, 0)

Exercise 3
Given the following matrix:

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
Make this matrix into an identity matrix (setting the diagonal elements to 1).

Your code should mutate m.

Solution
Since we need to mutate m, we can simply assign the values directly into m:

m[0][0] = 1
m[1][1] = 1
m[2][2] = 1
m
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]

Exercise 4
Do the same problem as Exercise 3, but do not mutate m.

Solution
We can not perform the operations from above directly on m.

The simplest is to make a copy of m - but a shallow copy would not be
enough - let's see that first:

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
result = m.copy()
result
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
result[0][0] = 1
result[1][1] = 1
result[2][2] = 1

result
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
So result looks good, but what about m?

m
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
That was mutated too, since the shallow copy still had references to the
sub-lists in m.

To get around this, we have to do a *deep copy.

from copy import deepcopy
Let's get m back to its original state:

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
And let's make the deep copy:

result = deepcopy(m)

result[0][0] = 1
result[1][1] = 1
result[2][2] = 1

result
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
And m now remains completely untouched:

m
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]


Exercise 5
You are given a list of tuples that each contain 4 values:

(amount, currency, target_currency, exchange_rate)
data = [
    (100, 'USD', 'EUR', 0.83),
    (100, 'USD', 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]
Write code that converts the amount from its currency to its target_currency
using the exchange_rate (which is the exchange rate for 1 currency in
target_currency).

Try to make your code as generic as possible (we'll see later how to use loops
so we don't have to write three separate statements).

In other words, you'll need three blocks of code here that are essentially
almost identical.

Use unpacking to assign the values in each tuple to variables.

Your result for each row should print something like this out:

100 USD = 83 EUR
Solution
We'll deal with row 0 first, and the repeat our code for the other two rows.

row = 0

amount, currency, target_currency, exchange_rate = data[row]
converted = amount * exchange_rate
print(amount, currency, '=', converted, target_currency, sep=' ')
100 USD = 83.0 EUR
Now we can use this same code, just changing the value of row to get the rest
of our results:

row = 1

amount, currency, target_currency, exchange_rate = data[row]
converted = amount * exchange_rate
print(amount, currency, '=', converted, target_currency, sep=' ')
100 USD = 127.0 CAD
row = 2

amount, currency, target_currency, exchange_rate = data[row]
converted = amount * exchange_rate
print(amount, currency, '=', converted, target_currency, sep=' ')
100 CAD = 65.0 EUR
'''