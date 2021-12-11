# Tutorial 6

## Exercise 1 - Code Review

With your tutor you will review someone's code from the week 5 lab. Try to identify:
* Places where the code style could be improved
* Whether the code could be made more pythonic

## Exercise 2 - Frontend discussion

Break up into your project groups. Within your group, take a look at the (slackr app)[http://www.slackr.com.au] and discuss areas of improvement in terms of the UI/UX. Discuss:
* What can be improved
* Why particular things should be improved

## Exercise 3 - HTTP Testing

Look at the `key.py` server from week 5. Write a series of HTTP level system tests `key_test.py` to ensure it's behaving as expected.

## Exercise 4 - Design Smells

A simple piece of code `box.py` that generates an ASCII box has been provided. What are possible code smells with this code? How would you refactor it to be more consistent with basic software engineering design principles?

## Exercise 5 - Design Smells

A simple piece of code `bubble.py` that uses bubble sort to sort numbers passed in via argv has been provided. What are possible code smells with this code? How would you refactor it to be more consistent with basic software engineering design principles?

## Exercise 6 - Top Down Design

Use top-down thinking to implement a registration function in `register.py` for an social network where a new user enters a username, password, and the repeat password. To successfully register users must:
 * Enter a username that is not already taken
 * Enter a password of minimum 10 characters
 * Both password and repeat password match