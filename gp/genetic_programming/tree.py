'''
Created on 16/03/2014

@author: alex
'''
import random


class Tree(object):
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right
        
    def __str__(self):
        if self.left and self.right:
            return "%s %s %s" % (str(self.left), str(self.cargo), str(self.right))
        else:
            return str(self.cargo)
        
def mutation(operations, tree, deph, level):
        if tree == None or deph > level:
            return
        else:
            if tree.cargo == "+" or tree.cargo == "-" or tree.cargo == "*" or tree.cargo == "/":
                tree.cargo = operations[random.randint(0, len(operations) - 1)]
            else:
                tree.cargo = random.uniform(-1000.0, 1000)
        mutation(operations, tree.left, deph+1, level)
        mutation(operations, tree.right, deph+1, level)
        
def _overlap(tree1, tree2):
    if tree1 is not None and tree2 is not None:
        left = _overlap(tree1.left, tree2.left)
        right = _overlap(tree1.right, tree2.right)
        return 1 + left + right
    else:
        return 0

def _make_crossover(tree1, tree2, position):
    left_overlap = _overlap(tree1.left, tree2.left)
    right_overlap = _overlap(tree1.right, tree1.right)
    assert position <= left_overlap + right_overlap + 1
    assert position >= 1
    if position <= left_overlap:
        assert left_overlap >= 1
        left1, left2 = _make_crossover(tree1.left, tree2.left, position)
        right1, right2 = tree1.right, tree2.right
        t1 = Tree(tree1.cargo, left1, right1)
        t2 = Tree(tree2.cargo, left2, right2)
        return t1, t2
    elif position == left_overlap + 1:
        t2 = Tree(tree1.cargo, tree1.left, tree1.right)
        t1 = Tree(tree2.cargo,tree2.left, tree2.right)
        return t1, t2
    else:
        new_position = position - (left_overlap + 1)
        assert new_position >= 1
        assert right_overlap >= 1
        left1, left2 = tree1.left, tree2.left
        right1, right2 = _make_crossover(tree1.right, tree2.right, new_position)
        t1 = Tree(tree1.cargo, left1, right1)
        t2 = Tree(tree2.cargo, left2, right2)
        return t1, t2
    

def crossover(tree1, tree2):
    s = _overlap(tree1, tree2)
    position = random.randint(1, s)
    (t1, t2) = _make_crossover(tree1, tree2, position)
    return t1, t2