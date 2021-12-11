# Tutorial 4


## A. Activity

1. Take a look at [this webpage](https://www.youtube.com/watch?v=GfL5zOhpB14). What routes do you think are necessary to allow this webpage to function? For each route:
 * Discuss the data it might take in
 * Discuss the data it might return

2. Are there any considerations that need to be made when choosing how to breakup routes?

## B. Network questions

1. What is the difference between the internet and the world wide web? What network protocols are used in each?

2. Breakdon the key components of an HTTP URL, such as http://unsw.com/calendar/view?term=t3&week=5#top

## C. Writing a route

1. Write a simple flask surver `names.py` that does the following:
 * Has a route that can take a name and a date of birth (as a (unix timestamp)[https://www.epochconverter.com/])
 * Has a route that will produce all names/ages of people who've been entered previously

2. (Optional) Instead of storing the state locally, store the state in a file

*Ensure pylint is run on your code.*

## D. Verification & Validation

Given the Zune bug example from the lecture (in `day_to_year.py`) and a test that **doesn't** find the bug (in `day_to_year_test.py`), fix the implementation of `day_to_year()` such that it no longer has the bug.

To check whether you have in fact removed the bug and that your tests are adequate, use Coverage.Py to measure and inspect your code coverage. You may need to add more to the test to have satisfactory coverage. Make sure you're doing **branch** coverage checking!

Run your `day_to_year.py` through pylint. Consider what issues it highlights and discuss, as a class, the alternatives for resolving them.

* Fixing the code so the issue no longer exists.
* Adding a pragma to the line the issue occurs, so pylint stops reporting it.
* Suppressing all instances of such errors via a config file.

You may wish to consult the [Google python style guide](https://google.github.io/styleguide/pyguide.html)

*Ensure pylint is run on your code.*

## E. More Python Practice

Write a program `prettydate.py` that converts 24 hour time into 12 hour time.You may assume that all inputs will be a valid 24 hour time.You program should read each line of input from standard input until EOF and output the result to standard output.

Sample input:
```python
1234
0525
0000
0001
1904
```

Sample output:
```python
12:34 PM
05:25 AM
00:00 AM
00:01 AM
07:04 PM
```

*Ensure pylint is run on your code.*