#!/usr/bin/python2.7
# -*- coding: utf-8

from utils import Utils

import json
import logging
import random
logger = logging.getLogger(__name__)


class Miner:
    ut = Utils()

    def __init__(self, player):
        self.username = player.username
        self.password = player.password
        self.uhash = player.uhash
        self.p = player
        self.running = False
        self.useable = False
        self.energy = 0
        self._initminer()
        
    def _initminer(self):
    	career_data = self._carrerStatus()
        career = json.loads(career_data)
        if int(career['count']) > 0:
            self.energy = int(career['energy'])
            if self.strength >= 600:
                self.useable = True
    
    def _careerStatus(self):
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_getCareerStatus.php")
        return temp
    
    def start(self):
    	self.running = True
        while self.running:
        	