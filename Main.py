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


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
