> **Note** This is not an industry standard database application. I just made it for fun to improve my coding skills

# AVL-DB

This is an implementation of _in memory_ database which uses AVL-Tree as its backend to store the data. The search, insert and delete operations work in `O(log n)` time where `n` represents the number of data points.

## Why AVL-Tree?

**Property**: AVL Tree is a self balancing binary search tree (BBST)
**Property**: The difference between the heights of left and right subtree is almost 1, aka balancing factor of a node. 

It means that whenever the tree goes out of balance we perform rotations and make it balanced. All these rotations take constant amount of time, so there is no degradation in performance.

## Why not a BST?

In worst case a binary search tree can be skewed as shown in the figure below. In such cases searching a data point can take `O(n)` time where `n` is the number of data points.

## What are other BBST's?

There are many of them, most used ones in industries for implementing databases are

1. [B Trees](https://en.wikipedia.org/wiki/B-tree)
2. [B+ Trees](https://en.wikipedia.org/wiki/B%2B_tree)

## How to run the code

1. Clone the repository.
2. Go to the directory and run `python cli.py`

### Found a bug? or Have a suggestion to improve the project?

Please make a PR. I am always open to suggestions and constructive criticism.