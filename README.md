# Recursion and Dynamic Programming

## Instructions:

*Write a method to return all subsets of a set*

## Using the program:

### Installation

Clone this git repository:

```

```

### Activation!

Navigate to the repo:

```

```

Run the script

```
python subsets.py
```

<img src=http://i.imgur.com/328fre1.png>

----

This ended up being trickier in practice than it first seemed. Surprised?

## Mistakes I made:

1. Tried to handle/manipulate sets like lists
2. GOTO 1

In practice I understood that sets don't care about the order of their items. When I worked through this on the whiteboard, the algorithm I arrived at didn't seem to care about the order of the items, so I thought I was fine.

When I put it into code, however, I realized that if I were to subsitute lists in for the sets, it would still work. "That's fine," I thought.

I took me a bit to realize this contradiction.

I am thankful that Python refused to let me get away with this.

I had to learn how some of the tools that Python gives us to work with sets. These set-specific tools helped me avoid treating a set like a list.

In the end, this problem exercised my algorithmic muscles the way I hoped it would. And then, in actually implementing what I wrote on the whiteboard, it exercised my Python-muscles, letting me work with a data structure I've usually let sit in an rather lifeless form (though admittedly, still very useful):

```
if item in set:
    do action
```

## TODO

- Let the user input a set
- Change the set's __repr__
- Change the for-loop on line 23 to a set comprehension

```
subs = {set.union(item, to_apply) for item in result}
```