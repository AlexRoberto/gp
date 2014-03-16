'''
Created on 16/03/2014

@author: alex
'''

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