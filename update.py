from utils import Utils
import json


class Update:
    ut = Utils()

    def __init__(self, player):
        self.username = player.username
        self.password = player.password
        self.uhash = player.uhash

    def getrunningtasks(self):
        """
        '{"data":[{"type":"sdk","start":"1495356942","end":"1495359788","wto":"1186","taskid":"110610282"}],
        "fAllCosts":"23","money":"17798567","inet":"10","hdd":"10","cpu":"10","ram":"14","fw":"350","av":"747",
        "sdk":"1185","ipsp":"151","spam":"204","scan":"575","adw":"210","netcoins":"9544","urmail":"0","score":"16254",
        "energy":"262260372","useboost":"2","boost":"336","status":"1","stime":"1495357017"}'
        ['data']
        [{u'start': u'1495356942', u'end': u'1495359788', u'type': u'sdk', u'taskid': u'110610282', u'wto': u'1186'},
         {u'start': u'1495357175', u'end': u'1495360024', u'type': u'sdk', u'taskid': u'110612494', u'wto': u'1187'}]
        :return: string, as above if tasks.
        """
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_tasks.php")
        return temp

    def SpywareInfo(self):
        """
        < type 'list' >: ['local:0', 'data:[{av:392', 'fw:417', 'money:42793029', 'spam:467', 'user:ShittyGame',
                           'ip:23.93.18.103', 'next:now.}]', 'remote:1', 'result:0']
        """
        arr = self.ut.requestArray(self.username, self.password, self.uhash, "vh_spywareInfo.php")
        return arr

    def removeSpyware(self):
        arr = self.ut.requestArray(self.username, self.password, self.uhash, "vh_removeSpyware.php")
        return arr

    def runningtasks(self, tasks=None):
        """
        Return the number of running tasks.
        :return: int
        """
        if not tasks:
            tasks = self.getrunningtasks()
        j = json.loads(tasks)
        try:
            return len(j["data"])
        except KeyError:
            return "0"

    def getTaskIDs(self, tasks=None):
        """
        Return a list of task ids
        [u'110610282', u'110612494']
        :param tasks string of json data
        :return: list
        """
        if not tasks:
            tasks = self.getrunningtasks()
        j = json.loads(tasks)
        return [x['taskid'] for x in j['data']]

    def startTask(self, type):
        """
        Start a task.
        :param type: string variable of task type, "adw","fw" etc. See config file.
        :return:
        """
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_addUpdate.php", utype=type)
        j = json.loads(temp)
        if "result" in temp:
            return temp.split('result":"')[1].split('"')[0], j[j['type']]
        return "2", False

    def fillWithTask(self, type):
        """
        Fill the queue with a task type.
        :param type: string variable of task type, "adw","fw" etc. See config file.
        :return:
        """
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_fillTasks.php", utype=type)
        if "result" in temp:
            return temp.split('result":"')[1].split('"')[0]
        return "2"

    def finishTask(self, taskID):
        """
        Finish single task of taskID
        :param taskID:
        :return:
        """
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_finishTask.php", taskid=taskID)
        if "4" in temp:
            return True
        else:
            return False

    def finishAll(self):
        """
        Finish all tasks currently running.
        :return:
        """
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_finishAll.php")
        if "0" in temp:
            return True
        else:
            return False

    def useBooster(self):
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_tasks.php", boost="1")
        return temp

    def infoUpdate(self, name, types=None):
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_updateInfo.php", utype=name)
        j = json.loads(temp)
        if types is None:
            return j["costs"]
        else:
            return j[types]

    def infoVersion(self, name):
        temp = self.ut.requestString(self.username, self.password, self.uhash, "vh_update.php")
        j = json.loads(temp)
        return j[name]