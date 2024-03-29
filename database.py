STARTING_CERTITUDE = 0.3


class SearchResult(object):
    def __init__(self):
        self.tags = {}
        self.highestCertitude = 0
        self.correspondingTag = None
        self.size = 0

    def addData(self, tag):
        if tag is None:
            return
        self.size += 1
        if tag not in self.tags:
            self.tags[tag] = 1
        else:
            self.tags[tag] += 1
        cert = self.tags[tag]/float(self.size+3)
        if cert > self.highestCertitude:
            self.highestCertitude = cert
            self.correspondingTag = tag

    def getHighestCertitude(self):
        return self.highestCertitude

    def getCorrespondingTag(self):
        return self.correspondingTag

    def getData(self):
        return map((lambda x: (x[0], x[1]/float(self.size+3.0))),
                   sorted(self.tags.items(), key=(lambda x, y: x[1] > y[1])) if len(self.tags.keys()) > 1
                                                                             else self.tags.items())


class Database(object):
    def __init__(self):
        self.db = {}

    def addData(self, client, tag):
        if tag is None:
            return
        if client not in self.db:
            self.db[client] = SearchResult()
        self.db[client].addData(tag)
        return self.db[client].getHighestCertitude()

    def removeClient(self, client):
        c = self.db[client].getHighestCertitude()
        t = self.db[client].getCorrespondingTag()
        self.db[client] = None
        return t, c

    def getResults(self, client):
        return self.db[client].getData()

    def hasClient(self, appId):
        return appId in self.db
