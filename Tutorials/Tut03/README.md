# Tutorial 3

## A. Code Review

Your tutor will select one of your classmate's code from lab02 to present and discuss as a class.

Is the code:
* Compliant with the COMP1531/Google style guide?
* Pythonic in nature?

## B. Requirements

Your tutor may break you up into groups to complete this activity.

* Q. What are attributes of good requirements?
* Q. How could we clean this up into well described requirements? "I want a burger with lots of pickles and mayo but I need to make sure that the mayo doesn't make the burger bun really wet. Oh, and it needs t obe warm, like, made less than 5 minutes ago warm but not so hot that I burn myself. I'm also not a big fan of plastic containers so if it could be in a paper bag that would be good. Actually, make that a brown paper bag, I like the colour of that"

## C. Agile

Each group should share their current plans/methods in terms of:
 * When (or if) they are running standups and whether they are synchronous or asynchronous
 * How often they meet, how they meet, and what the goals/outcomes of any meetings so far have been
 * Have they or will they try pair programming
 * Any challenges they've faced already after being in a group for a week

## D. Dictionaries

Write a python program `vowel.py` that takes in a series of words on a single line in from STDIN and outputs the frequency of how often each vowel appears. Assume all words passed in are lowercase.

## E. Importing

Here is a file *foo.py*
```python
def bar(txt):
    return txt

name = 'Ralph'
def editName(string):
    name = string
def getName():
    return name
```

In the same directory we have a file *imp.py*. There are multiple ways we can import and use a function in another file. Discuss each.
```python
import foo
print(foo.bar('hi')) # 1

import foo as fooFile
print(fooFile.bar('hi')) # 2

from foo import bar
print(bar('hi')) # 3

from foo import *
print(bar('hi')) # 4
```

Why does the following function not behave as intended?
```python
import foo

print(foo.getName())
foo.editName('Hayden')
print(foo.getName())
```

## F. Functional and Non-functional

* What is the difference between functional and non functional requirements?
* Are the following requirements functional or non functional?
  * Every unsuccessful attempt by a user to access an item of data shall be recorded on an audit trail. 
  * Privacy of information, the export of restricted technologies, intellectual property rights, etc. should be audited. 
  * The software system should be integrated with banking API
