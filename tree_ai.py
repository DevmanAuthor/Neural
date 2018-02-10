from itertools import count
from enum import Enum
import string
import random

##helper functions###
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):   # randomly generates characters
        return ''.join(random.choice(chars) for _ in range(size)) 
def assess(node, action, type="node"):                                    # asseses the situation of a node
    print(type + " " + str(node.id) + ": ", action)                       # with a printed statement
##helper functions##


class node(object):                                     # This is a Node. Nodes are cell-like part of the tree that
    status = Enum('status', 'READY HOLD SYNC')          # recieves data from the world carries data to other nodes
    _ids = count(0)                                     # and processes it
    def __init__(self, head=None, load=None):
            self.id = next(self._ids)                   # Each node has an simple static counter that acts as an [id] on creation 
            self.head = head                            # Each node is responsible for sending data to the [head] node-pointer 
            self.load = load                            # The [load] is the immidiate data recieved
            self.memory = []                            # The property [memory] is a list of all data ever recieved
            self.carry = self.status.READY              # A [carry] value determines a node's current state of operation
            self.tier = None                            # The [tier] determines if the node is head or another kind of node
    def switch(self):
            if self.carry is self.status.READY:
                self.carry = self.status.HOLD           # The switch function switches the Node's carry state between the 
            if self.carry is self.status.HOLD:          # READY and HOLD signals -- aka boolean "availability" signals 
                self.carry = self.status.READY
    def bind(self, head):                               # bind() the node to a specific head node and make sure the
            self.head = head                            # head knows itself to be a head node
            if self.head.tier is not self.status.SYNC:  
                self.head.tier = self.status.SYNC       
            else:
                pass
    def forget_swath(self, start, end):                 # forget_swath() destroys a specified range of data in node's memory
            for _ in range(start, end):                 
                del(self.memory[_])
    def forget(self, index):                            # forget() destroys a specifc index of data in node's memory                           
                del(self.memory[index])                 
    def flush(self):                                    # flush() copies a node's load to its head node, and prints detailed results
        if self.tier is self.status.SYNC:               
            assess(self, "flushed data upward " + str(self.load), "node [HEAD]")
            self.head.listen(self.load)
        else:
            assess(self, "flushed data upward " + str(self.load))
            self.head.listen(self.load)
    def listen(self, load):                             # listens() intercepts data when the node/head is ready
        if self.carry is self.status.READY:
            self.memory += [load]
            if self.tier is self.status.SYNC:
                assess(self, "has intercepted data: " + str(load) + " to memory " + str(self.memory), "node [HEAD]")
            else:
                assess(self, "has intercepted data: " + str(load) + " to memory " + str(self.memory))
            return True
        else:
            assess(self, "is unable to intercept memory: " + str(load))
            return False
        

class layer(object):                                    # The is a Layer. A Layer consists of a nodes and heads
    nodes = [] 
    heads = []
    def __init__(self, numofnodes=None, *params):       # Initializes a new layer with an optional number of nodes created
        for _ in range(0, numofnodes):                  # You can initialize these swaths of created nodes with specific properties
            self.nodes.append(node(*params))
    def bind(self, head, name=None):                    # Binds() several nodes to head node and gives the head
        if name is None:                                # an optional name
            name = id_generator()
        for n in range(0, len(self.nodes)):
            self.nodes[n].bind(head)
        self.heads.append(head)
    def fill(self,w_nodes, data):                          # Fills() node(s) with data(s)
        if isinstance(w_nodes, list) and isinstance(data, list):  
            for n in range(0,len(w_nodes)):
                for o in range(0, len(data)):           # These set of if/elif statements check to see if the node(s) and data(s)
                    self.nodes[n].load = data[o]           # are lists or not
                    break
        elif isinstance(w_nodes, list) and not isinstance(data, list):
            for n in range(0,len(w_nodes)):
                self.nodes[n].load = data
        elif isinstance(data, list) and not isinstance(w_nodes, list):
            for n in range(0,len(data)):
                self.nodes.load = data
    def flush_all(self):                                # Calls all nodes in its layer to flush data to their head(s)
        for n in range(0, len(self.nodes)):
            self.nodes[n].flush()
    def list_heads(self):                               # Prints out id's of all the heads in its layer
        print("-------Heads in this layer:---------\n")
        for _ in range(0, len(self.heads)):
            print("Head id: " + str(self.heads[_].id))
    def deactivate(self,head):                          # Deactivate() and cleanup() respectively stop a node from being a head
        head.tier = None                                # and deletes the node from the layer
    def clean_up(self):
        for _ in range(0, len(self.heads)):
            if self.heads[_].tier is not node.status.SYNC:
                del(self.heads[_])

class tree(object):                                     # A simple Tree of nodes. On initialization you can decide layer and node
    Root = node()                                 # specifc properties all in one statement
    layers = []
    def __init__(self, numoflayers, *params):
        self.Root.head = self.Root
        self.Root.tier = self.Root.status.SYNC
        self.layers = [layer(*params) for i in range(numoflayers)]
        pass

Tree = tree(4,5,12, "asdasd")

Tree.layers[2].fill([1,2,3,4,5],1231)
Tree.layers[2].bind(Tree.Root)
Tree.layers[2].flush_all()
'''
layer1 = layer()
layer1.create(5)
layer1.bind(layer1.nodes[1])
layer1.list_heads()
layer1.fill(layer1.nodes, 1)
layer1.flush_all()
layer1.nodes[4].load = 0
layer1.nodes[4].flush()

Nupta = Node()
Nupta.load = 0
Nupta.bind(layer1.nodes[0].head)
Nupta.flush()'''