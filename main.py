#Import statements
import hashlib as hasher
import random as rand
import time
import datetime as date
import ipyparallel as ipp
import numpy as np
import matplotlib.pyplot as plt

# In this section we will define the class "Block" and create an init function that creates a new block given some parameters,
# as well as a function hash_block, that computes the hash of this block based on its class variables.
#
#    Index --> the index of the block on the chain (zero indexed)
#    Timestamp --> time that the block was added on to the chain
#    data --> The data the block contains (Usually points to root of merkel tree, but we can fill it with whatever for this)
#    previous_hash --> The hash value of the previous block
#    hash --> hash of this block computed using the hash_block function
#    nonce --> the variable value that we change to alter the hash output (Default value = 0, irrelevant in this section)

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce #set to zero as default not applicable in first section
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    # question 1 : implementing hash_block()
    #Concatenate string representations of all the class variables
    #Computes the SHA256 hash of this concatenation

    def hash_block(self):
        #Your code for QUESTION 1 Here
        return  ""

    # question 2 : Functions for building chain --->
    # lets figure out how to make a chain out of them. For a chain, we need to first have a function that creates a genesis block,
    # which serves as the first block of our chain, and then create the function next_block() which builds a new block on top of a given block.

    # Creates the first block with current time and generic data
    def create_genesis_block(self):
        # Manually construct a block with
        # index zero and arbitrary previous hash
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    # Function that creates the next block, given the last block on the chain you want to mine on
    #We need to implement the function next_block() which takes in 1 parameter:
        #Last_block = an instance of class Block that is the block that we're building our next block on top of
        #nonce = Dont do anything with this right now - just pass it in to the Block that you create using the default

    def next_block(self,last_block, nonce=0):
        # Your code for QUESTION 2 here
        return  ""

#Spinning up the chain : Now that we've created the data structure as well as the functions needed to create the chain,
# lets see how spinning up an actual instance of this would work. Below we initialize three different variables :

    #blockchain - this is a python list which we initialize with one block inside (the genesis block)
    #previous_block - this points to our genesis block (since it references the first element in blockchain)
    #num_blocks - this specifies the number of additional blocks we want to add to our chain

# Create the blockchain and add the genesis block
blockchain = [Block.create_genesis_block()]

# Create our initial reference to previous block which points to the genesis block
previous_block = blockchain[0]

# How many blocks should we add to the chain after the genesis block
num_blocks = 20


#We want to complete the implementation of the function complete_chain().
# This function takes in three inputs, which correspond to the initializations that we made.
# It returns nothing, however by the time we are done running it,
# the list 'blockchain' that we initialized earlier has been turned into an array of length num_blocks + 1 in
# which each element is an instance of class Block and each element's self.previous_hash == the previous element's self.hash.
# Therefore we have created our own mini blockchain!!

#The for loop and the print statements of complete_chain have been implemented for you,
# you need to add the statements that create a new block on top of previous_block, add it to the block chain,
# and edit previous block so that the for loop can continue correctly

def complete_chain(num_blocks, blockchain, previous_block):
    # Add blocks to the chain
    for i in range(0, num_blocks):
        # Your code for QUESTION 3 Here

        # Your code for QUESTION 3 ends Here
        # Tell everyone about it!
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))


complete_chain(num_blocks, blockchain, previous_block)




