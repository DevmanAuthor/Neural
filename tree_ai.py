from itertools import count
from enum import Enum
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
def assess(node, action):
    print("node ", node.id, " ", action)

class Node(object):
    status = Enum('status', 'READY HOLD SYNC')
    _ids = count(0)
    def __init__(self):
            self.id = next(self._ids)    
            self.head = None
            self.load = None
            self.memory = []
            self.carry = self.status.READY
            self.tier = None
    def switch(self):
            if self.carry is self.status.READY:
                self.carry = self.status.HOLD
            if self.carry is self.status.HOLD:
                self.carry = self.status.READY
    def bind(self, head):
            self.head = head
    def forget_swath(self, start, end):
            for _ in range(start, end):
                del(self.memory[_])
    def forget(self, index):
                del(self.memory[index])
    def flush(self):
            assess(self, "flushed data upward " + str(self.load))
            self.head.listen(self.load)
    def listen(self, load):
        if self.carry is self.status.READY:
            self.memory += [load]
            assess(self, "has intercepted data: " + str(load) + " to memory " + str(self.memory))
            return True
        else:
            assess(self, "is unable to intercept memory: " + str(load))
            return False
        

class layer(object):
    nodes = []
    heads = []
    def __init__(self):
        pass
    def create(self, numofnodes):
        for _ in range(0, numofnodes):
            self.nodes.append(Node())
    def bind(self, head, name=None):
        if name is None:
            name = id_generator()
        for n in range(0, len(self.nodes)):
            self.nodes[n].bind(head)
        self.heads.append(head)
        head.tier = head.status.SYNC
    def fill(self,node, data):
        if isinstance(node, list) and isinstance(data, list):
            for n in range(0,len(node)):
                for o in range(0, len(data)):
                    node[n].load = data[o]
                    break
        elif isinstance(node, list) and not isinstance(data, list):
            for n in range(0,len(node)):
                node[n].load = data
        elif isinstance(data, list) and not isinstance(node, list):
            for n in range(0,len(data)):
                node.load = data
    def flush_all(self):
        for n in range(0, len(self.nodes)):
            self.nodes[n].flush()
    def list_heads(self):
        print("-------Heads in this layer:---------\n")
        for _ in range(0, len(self.heads)):
            print("Head id: " + str(self.heads[_].id))
    def deactivate(self,head):
        head.tier = None
    def clean_up(self):
        for _ in range(0, len(self.heads)):
            if self.heads[_].tier is not Node.status.SYNC:
                del(self.heads[_])
    

layer1 = layer()
layer1.create(5)
layer1.bind(layer1.nodes[0])
layer1.list_heads()
layer1.fill(layer1.nodes, True)
layer1.flush_all()
layer1.nodes[4].load = id_generator()
layer1.nodes[4].flush()

Nupta = Node()
Nupta.load = 13123
Nupta.bind(layer1.nodes[0].head)
Nupta.flush()