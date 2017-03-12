from incandescent import Client
import json
import re
import operator

def main(upload_image_url):
    #Nicolas
    #uid = "7093"
    #apikey = "838024ddaaa63db12d98ea3a16323cb6"

    #Benoit
    uid = "7092"
    apikey = "59189a0213476cc2b9396bca90e7f750"

    search = Client(uid, apikey)
    search.addImageUrl(upload_image_url)
    search.makeRequestData()
    search.makeRequest()

    res = search.getResults()
    if res is None:
        print" Try again, you have been kicked"
    else:
        return getGameName(res)

def parse_json():
    with open("./json.txt") as input:
        data = json.load(input, encoding="utf-8")
    names = []
    for line in data:
        for x in data[line]["pages"]:
            names.append(data[line]["pages"][x]["usage-image"])

def getGameName(urls):
    # Count words in the filename
    topterms = {}
    for url in urls:
        url = url.encode('utf-8')
        filename = url.split('/')[-1].split('#')[0].split('?')[0].split(".")[0]
        cleanfilename = re.sub('[^0-9a-zA-Z]+', ' ', filename)
        filenamewords = cleanfilename.split()
        for word in filenamewords:
            if (topterms.has_key(word)):
                topterms[word] += 1
            else:
                topterms[word] = 1

    # Create a list of the words sorted by importance
    sortedterms = sorted(topterms.items(), key=operator.itemgetter(1), reverse=True)

    # Select list of the most important words
    biggestDrop = 0
    biggestDropLoc = 0
    prec = 0
    for i in range(1,len(sortedterms)):
        drop = sortedterms[prec][1] - sortedterms[i][1]
        if (drop > biggestDrop):
            biggestDrop = drop
            biggestDropLoc = prec
        prec = i
    gameNameList= sortedterms[0: biggestDropLoc + 1]

    # Get the full name of the game (with "the", "of" and other little words in between)
    start = len(filenamewords)
    end = 0
    for url in urls:
        url = url.encode('utf-8')
        filename = url.split('/')[-1].split('#')[0].split('?')[0].split(".")[0]
        cleanfilename = re.sub('[^0-9a-zA-Z]+', ' ', filename)
        filenamewords = cleanfilename.split()
        gameNameArray = []
        for i in gameNameList:
            gameNameArray.append(i[0])
        if set(gameNameArray).issubset(set(filenamewords)):
            for word in gameNameList:
                if len([i for i, x in enumerate(gameNameList) if x == word]) == 1:
                    if gameNameList.index(word) < start:
                        start = gameNameList.index(word)
                    if gameNameList.index(word) > end:
                        end = gameNameList.index(word)
            break

    output = ""
    for i in gameNameList[start:end + 1]:
        output += i[0] + " "

    return output