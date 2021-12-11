# Tutorial 5

## Activities

## Exercise 1 - Code Review

With your tutor you will review someone's code from the week 3 lab. Try to identify:
* Places where the code style could be improved
* Whether the code could be made more pythonic

## Exercise 2

Break into groups of 3. The only rule is that no one in the group of 3 can be in your project team. In your team, you will be given 5-10 minutes to analyse the current API specification by Sally/Bob, and to (as a team) propose one (or a couple) of new "route(s)" (i.e. url) to the interface to add some cool functionality to the product. Find something that you as a team get excited about. You'll be sharing your answer with the class, and will be expected to provide for each route:
  * A route (i.e. /this/url/name)
  * A CRUD method (e.g. GET)
  * Input parameters
  * Return object
  * Description of what it does

## Exercise 3

Write a flask server `key.py` that has a single route `/getimg?tag=img` where it loads the unsw homepage and counts how many times the HTML tag "tag" property appears in the page.
```html
<div id="a"></div>
```

counts as 1 div tag.

```json
{
	"tag_count": 125
}
```

## Exercise 4

Convert the JSON file `widget.json` to a YAML file `widget.yaml` without the use of an online tool.

## Exercise 5

What are some real world examples of authentication and authorisation?

## Exercise 6 - Design

Modify `fettucine.py` to improve it in terms of its adherence to pythonic principles.w