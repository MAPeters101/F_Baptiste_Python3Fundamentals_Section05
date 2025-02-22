"""
Exercise 1
Given a variable a (containing any value), re-assign the value "N/A" if a is None, and leave a unchanged otherwise. Use an if...else... statement.

We need to create a variable a assign it some value, and then test the value of a to see if we need to change it to 'N/A':

a = 100

if a is None:
    a = 'N/A'

print(a)
Now let's try our code with a few more possible values for a:

a = 'Python'

if a is None:
    a = 'N/A'

print(a)
a = None

if a is None:
    a = 'N/A'

print(a)
Exercise 2
Do the same thing as Question 1, but this time use a ternary operator.

A ternary operator always calculates a value, but we don't want to modify a if it is not None.

To do this we'll simply have the ternary operator evaluate to a if a is not None and to N/A otherwise:

a = 100
a = 'N/A' if a is None else a
print(a)
And again we should test this with a few values:

a = 'Python'
a = 'N/A' if a is None else a
print(a)
Python
a = None
a = 'N/A' if a is None else a
print(a)
N/A
Exercise 3
Given an credit score score, assign a string value to another variable rating based on the following scale:

[0, 580) --> Poor
[580, 670) --> Fair
[670, 740) --> Good
[740, 800) --> Very Good
[800, 850] --> Excellent
We can do this using a series of if...elif...else statements:

score = 720

if score < 580:
    rating = 'Poor'
elif score < 670:
    rating = 'Fair'
elif score < 740:
    rating = 'Good'
elif score < 800:
    rating = 'Very Good'
else:
    rating = 'Excellent'

print(rating)
Good
Let's test this with a few values:

score = 100
if score < 580:
    rating = 'Poor'
elif score < 670:
    rating = 'Fair'
elif score < 740:
    rating = 'Good'
elif score < 800:
    rating = 'Very Good'
else:
    rating = 'Excellent'

print(rating)
Poor
score = 740
if score < 580:
    rating = 'Poor'
elif score < 670:
    rating = 'Fair'
elif score < 740:
    rating = 'Good'
elif score < 800:
    rating = 'Very Good'
else:
    rating = 'Excellent'

print(rating)
Very Good
score = 810
if score < 580:
    rating = 'Poor'
elif score < 670:
    rating = 'Fair'
elif score < 740:
    rating = 'Good'
elif score < 800:
    rating = 'Very Good'
else:
    rating = 'Excellent'

print(rating)
Excellent
Exercise 4
Given an elapsed time (in seconds), write code to set a variable magnitude based on the following conditions:

if elapsed time is less than 1 minute, magnitude --> 'seconds'
if elapsed time is more than 1 minute, but less than 1 hour, magnitude --> 'minutes'
if elapsed time is more than 1 hour, but less than 1 day, magnitude --> 'hours'
if elapsed time is more than 1 day, but less than 1 week: magnitude --> 'days'
if elapsed time is more than 1 week, magnitude --> 'weeks'
Our conditional expression might look something like this (pseudo code = not real code):

if elapsed < 1 minute:
    magnitude = 'seconds'
elif elapsed < 1 hour:
    magnitude = 'minutes'
 elif elapsed < 1 day:
     magnitude = 'hours'
 elif elapsed < 1 week:
     magnitude = 'days'
 else:
     magnitude = 'weeks'
What now remains to be calculated is what 1 minute, 1 hour, 1 day, and 1 week are in terms of seconds (which is the units used for elapsed).

We'll calculate those values and store them in variables - this not only "decomposes" the problem (break into smaller more managable parts), but will also help clarify the conditional statement so that it will look very much like the pseudo-code above.

seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour
seconds_in_week = 7 * seconds_in_day
We can now write our code this way:

elapsed = 23  # secs

if elapsed < seconds_in_minute:
    magnitude = 'seconds'
elif elapsed < seconds_in_hour:
    magnitude = 'minutes'
elif elapsed < seconds_in_day:
    magnitude = 'hours'
elif elapsed < seconds_in_week:
    magnitude = 'days'
else:
    magnitude = 'weeks'

print(magnitude)

seconds
Let's try this with a few more values:

elapsed = 30 * 60  # 30 minutes in seconds

if elapsed < seconds_in_minute:
    magnitude = 'seconds'
elif elapsed < seconds_in_hour:
    magnitude = 'minutes'
elif elapsed < seconds_in_day:
    magnitude = 'hours'
elif elapsed < seconds_in_week:
    magnitude = 'days'
else:
    magnitude = 'weeks'

print(magnitude)
minutes
elapsed = 12 * 60 * 60  # 12 hours in seconds

if elapsed < seconds_in_minute:
    magnitude = 'seconds'
elif elapsed < seconds_in_hour:
    magnitude = 'minutes'
elif elapsed < seconds_in_day:
    magnitude = 'hours'
elif elapsed < seconds_in_week:
    magnitude = 'days'
else:
    magnitude = 'weeks'

print(magnitude)
hours
elapsed = 48 * 60 * 60  # 48 hours in seconds

if elapsed < seconds_in_minute:
    magnitude = 'seconds'
elif elapsed < seconds_in_hour:
    magnitude = 'minutes'
elif elapsed < seconds_in_day:
    magnitude = 'hours'
elif elapsed < seconds_in_week:
    magnitude = 'days'
else:
    magnitude = 'weeks'

print(magnitude)
days
elapsed = 3 * 7 * 24 * 60 * 60  # 3 weeks in seconds

if elapsed < seconds_in_minute:
    magnitude = 'seconds'
elif elapsed < seconds_in_hour:
    magnitude = 'minutes'
elif elapsed < seconds_in_day:
    magnitude = 'hours'
elif elapsed < seconds_in_week:
    magnitude = 'days'
else:
    magnitude = 'weeks'

print(magnitude)
weeks
Click to add a cell.

Simple
0
2
Python 3 (ipykernel) | Idle
1
02+-+Solutions.ipynb
Ln 1, Co
"""