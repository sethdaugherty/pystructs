# Red-black trees are a self-balancing binary search tree. Each node contains a extra piece of information - it's "color" - which is used to maintain balance during use.
# Balancing is not perfect, but is good enough to guarantee searching in O(logn) time. Insertion and deletion is also in O(logn).

# Reference: https://www.cs.auckland.ac.nz/software/AlgAnim/red_black.html
# A red-black tree is a binary search tree which has the following red-black properties:
#   1. Every node is either red or black.
#   2. Every leaf (NULL) is black.
#   3. If a node is red, then both its children are black.
#   4. Every simple path from a node to a descendant leaf contains the same number of black nodes

class Node:
    def __init__(self, value, color):
        self.value = value;
        self.color = color;



