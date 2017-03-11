import transformations


class SearchResult(object):
    def __init__(self):
        self.tags = {}
        self.highestCertitude = 0
        self.correspondingTag = None

    def addData(self, tag, certitude):
        if not self.tags[tag]:
            self.tags[tag] = certitude
        else:
            self.tags[tag] = transformations.getTransformation(self.tags[tag], certitude)
        if self.tags[tag] > self.highestCertitude:
            self.highestCertitude = self.tags[tag]
            self.correspondingTag = tag

    def getHighestCertitude(self):
        return self.highestCertitude
    def getCorrespondingTag(self):
        return self.correspondingTag



class Database(object):
    def __init__(self):
        self.db = {}

    def addData(self, client, tag, certitude):
        if not self.db[client]:
            self.db[client] = SearchResult()
        self.db[client].addData(tag, certitude)
        return self.db[client].getHighestCertitude()

    def removeClient(self, client):
        c = self.db[client].getHighestCertitude()
        t = self.db[client].getCorrespondingTag()
        self.db[client] = None
        return t, c
