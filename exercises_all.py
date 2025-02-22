"""
Exercise 1
Given the following string:

s = 'FfEeDdCcBbAa'
Create two new variables that contain just the lower and upper case letters of
s respectively, in the correct alphabetical order, i.e:

'ABCDEF'
'abcdef'
Exercise 2
Concatenate the following tuples into a single one, but replacing the odd value
s with zeros (0).

t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17
You can assume that every tuple is a sequence of consecutive integers starting
with an odd integer.

Try to write your code to be as generic as possible.

Exercise 3
Given the following matrix:

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
Make this matrix into an identity matrix (setting the diagonal elements to 1).

Your code should mutate m.

Exercise 4
Do the same problem as Exercise 3, but do not mutate m.

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
"""