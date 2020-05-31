# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:27:32 2020

@author: Rahul
"""
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1. Build a Blockchain

"""
Genesis block is marked by create_block() function
with previous hash as '0'
"""


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 }
        self.chain.append(block)
        return block
