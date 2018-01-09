#!/usr/bin/python2.7
# -*- coding: utf-8

from utils import Utils

import json
import logging
import random
import config
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('logs/botnet.log')
formatter = logging.Formatter('%(asctime)s [%(threadName)10s][%(module)10s][%(levelname)8s] %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

class Botnet:
    ut = Utils()

    def __init__(self, player):
        self.username = player.username
        self.password = player.password
        self.uhash = player.uhash
        self.botNetServers = 3
        self.botnet = []
        self.p = player
        self.ofwhat = config.BotNet_updates
        self.energy = 0
        self.debug = config.debug
        self._initbot()

    def _initbot(self):
        """
        Grab the amount of bots in the botnet
        and populate and array of Bot class
        :return: none
        """
        if(self.ofwhat == "ALL"):
            self.ofwhat = ["fw", "av", "smash", "mwk"]
        data = self._botnetInfo()
        bots = json.loads(data)
        self.botnet = []
        if int(bots['count']) > 0:
            for i in bots['data']:
                bot = Bot(i['running'], self.ofwhat[random.randint(0,len(self.ofwhat)-1)], self.energy, i['hostname'],  self.username, self.password, self.uhash)
                self.botnet.append(bot)

    def printbots(self):
        """
        Print a list of player PCs in the botnet
        :return: None
        """
        for bot in self.botnet:
            logger.info(bot)

    def getbotnetdata(self):
        """
        Return an array of bot class.
        Contains all the bots in the botnet.
        :return: list of bot class
        """
        return self.botnet

    def getInfo(self):
        """
        Get info about the entire botnet.
        Including if you can attack bot net servers etc.
        Also botnet PC info.
        :return: list of vHack serves that can be hacked.
                 ['1','2','1']. '1' = can be hacked, '2' time not elapsed.
        """
        response = self.ut.requestString(self.username, self.password, self.uhash, "vh_botnetInfo.php")
        response = json.loads(response)
        return response

    def attack(self):
        """
        Check if vHack server botnet is attackable,
        then attack if can.
        :return: none
        """
        self._initbot()
        logger.info("Trying Bot Net")
        cinfo = self.getInfo()

        for i in range(1, self.botNetServers + 1):
            if cinfo[i - 1] == '1':
                logger.debug('attacking #{}'.format(i))
                if i == 1:
                    response = self.ut.requestString(self.username, self.password, self.uhash, "vh_attackCompany.php", company=str(i))
                else:
                    response = self.ut.requestString(self.username, self.password, self.uhash, "vh_attackCompany" + str(i) + ".php", company=str(i))
                logger.debug('attack #{} response {}'.format(i, response))
                if response == '0':
                    logger.info('#{} Netcoins gained'.format(i))
                else:
                    logger.info('#{} Failed! No netcoins...'.format(i))
            else:
                logger.info("Botnet #{} not hackable as yet".format(i))

    def upgradebotnet(self, hostname, running, count):
        """
        Check if there is enough money to upgrade a botnet PC.
        Cycle through and upgrade until no money.
        :return: None
        """
        ofwhat = self.ofwhat[random.randint(0,(len(self.ofwhat)-1))]
        
        if self.debug:
                logger.warning("L106; ofwhat = '%s'",ofwhat)
        
        logger.info("Prepare attempting to upgrade bot net PC '"+ hostname +"'")
        get_infobot = self.getInfo()

        if (int(get_infobot['data'][count]['strength']) == 1120 and int(get_infobot['data'][count]['stars']) == 4):
            logger.info("Bot '"+hostname+"' has max strength [1120] for level " + str(get_infobot['data'][count]['stars']))
            return  False

        elif (int(get_infobot['data'][count]['strength']) == 840 and int(get_infobot['data'][count]['stars']) == 3):
            logger.info("Bot '"+hostname+"' has max strength [840] for level " + str(get_infobot['data'][count]['stars']))
            return False

        elif (int(get_infobot['data'][count]['strength']) == 600 and int(get_infobot['data'][count]['stars']) == 2):
            logger.info("Bot '"+hostname+"' has max strength [600] for level " + str(get_infobot['data'][count]['stars']))
            return False

        elif (int(get_infobot['data'][count]['strength']) == 400 and int(get_infobot['data'][count]['stars']) == 1):
            logger.info("Bot '"+hostname+"' has max strength [400] for level " + str(get_infobot['data'][count]['stars']))
            return False

        elif (int(get_infobot['data'][count]['strength']) == 3000 and int(get_infobot['data'][count]['stars']) == 0):
            logger.info("Bot '"+hostname+"' has max strength [3000] for level " + str(get_infobot['data'][count]['stars']))
            return False

        if (int(get_infobot['data'][count]['running']) == 0 and int(get_infobot['energy']) > 0):

            if int(get_infobot['data'][count]['stars']) > 0:
                maxofwhat = 20 + (5*int(get_infobot['data'][count]['stars']))
            
            elif int(get_infobot['data'][count]['stars']) == 0:
                maxofwhat = 250

            remove = 0

            for a, i in enumerate(xrange(0, len(self.ofwhat))):
                if int(get_infobot['data'][count][unicode(self.ofwhat[i-remove])]) == int(maxofwhat):
                    self.ofwhat.remove(self.ofwhat[i-remove])
                    remove = remove + 1
                if i == 3:
                    break

            ofwhat = self.ofwhat[random.randint(0,(len(self.ofwhat)-1))]
            
            if self.debug:
                logger.warning("L151; ofwhat = '%s'",ofwhat)

            new_bal = self.upgradesinglebot(hostname, ofwhat)
            if new_bal:
                logger.info("Waiting! Doing updates for bot '" + hostname + "', [" + ofwhat + "]")
                return True

        elif (int(get_infobot['energy']) == 0):
            logger.info("You don't have enough energy to upgrade '" + hostname + "'! :(")
            return False

        elif (int(get_infobot['data'][count]['running']) == 1):
            logger.info("Waiting! Doing updates for bot '" + hostname + "', [" + ofwhat + "]")
            return False

        logger.debug("The bot '{}' is not upgradeable".format(hostname))
        return False

    def _botnetInfo(self):
        """
        Get the botnet information including vHack servers and PC data.
        :return: string
        '{"count":"14",
        "data":[{"bID":"1","bLVL":"100","bSTR":"100","bPRICE":"10000000"},
        {"bID":"2","bLVL":"100","bSTR":"100","bPRICE":"10000000"}],
        "strength":23,"resethours1":"","resetminutes1":"14","resethours2":"4","resetminutes2":"15",
        "resethours3":"3","resetminutes3":"15",
        "canAtt1":"2","canAtt2":"2","canAtt3":"2"}'
        """
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_botnetInfo.php")
        return temp
    
    def upgradesinglebot(self, hostname, ofwhat):
        """
        Pass in bot class object and call upgrade function based on bot ID.
        details :
        {u'strength': u'22', u'old': u'30', u'mm': u'68359859',
        u'money': u'66259859', u'costs': u'2100000',
        u'lvl': u'21', u'new': u'22'}
        current lvl, bot number, x, x, upgrade cost, lvl, next lvl
        :return: None 
        """
        response = self.ut.requestString(self.username, self.password, self.uhash, "vh_upgradePC.php", hostname=hostname, ofwhat=ofwhat, inst="0", much="1")
        jsons = json.loads(response)
        if int(jsons['result']) == 0:
            return True
        else:
            logger.error("Upgrade " + hostname + " Failed !")
            return False

    def __repr__(self):
        return "Botnet details: vHackServers: {0}, Bot Net PC's: {1}".format(self.botNetServers, self.botnet)


class Bot:
    ut = Utils()

    def __init__(self, running, ofwhat, energy, hostname, username, password, uhash):
        self.username = username
        self.uhash = uhash
        self.password = password
        self.running = int(running)
        self.ofwhat = ofwhat
        self.energy = energy
        self.hostname = hostname

    def botupgradable(self, running):
        """
        Determine if botnet PC is at max level or not.
        :return: Bool
        """
        if running == 0:
            return True
        else:
            return False

    def nextlevelcostenergy(self):
        """
        Return the cost of upgrading bot to the next level
        :return:int
        """
        return self.energy

    def parse_json_stream(self, stream):
        decoder = json.JSONDecoder()
        while stream:
            obj, idx = decoder.raw_decode(stream)
            yield obj
            stream = stream[idx:].lstrip()

    def upgradesinglebot(self, hostname, ofwhat):
        """
        Pass in bot class object and call upgrade function based on bot ID.
        details :
        {u'strength': u'22', u'old': u'30', u'mm': u'68359859',
        u'money': u'66259859', u'costs': u'2100000',
        u'lvl': u'21', u'new': u'22'}
        current lvl, bot number, x, x, upgrade cost, lvl, next lvl
        :return: None
        """
        response = self.ut.requestString(self.username, self.password, self.uhash, "vh_upgradePC.php", hostname=hostname, ofwhat=ofwhat)
        response = response.split('}{')[0] + '}'
        print(response)
        jsons = json.loads(response)
        logger.info(jsons)
        return True


    def __repr__(self):
        
        return "Bot details: running: {0}, energy: {1}, upgrade: {2}, botname: {3}".format(self.running, self.energy, self.ofwhat, self.hostname)
