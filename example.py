from incandescent import Client
import json
import re


def main():
    # Config
    uid = "7093"
    apikey = "838024ddaaa63db12d98ea3a16323cb6"

    search = Client(uid, apikey)
    #search.addImageUrl("http://i.skyrock.net/8989/70868989/pics/2813975768_1.png")
    search.addImageUrl("http://i.imgur.com/CaFjhJB.png")
    #search.addImageUrl("http://i.imgur.com/KztFRBv.jpg")
    search.makeRequestData()
    search.makeRequest()


    #print(search.data)

    #if 'project_id' in search.data:
    getGameName(search.getResults())

    #else:
        #print "No Project ID"


def parse_json():
    with open("./json.txt") as input:
        data = json.load(input, encoding="utf-8")
    names = []
    for line in data:
        for x in data[line]["pages"]:
            names.append(data[line]["pages"][x]["usage-image"])
            #print(data[line]["pages"][x]["usage-image"])

    print(names)

def getGameName(urls):
    print urls
    topterms = {}
    for url in urls:
        filename = url.split('/')[-1].split('#')[0].split('?')[0].split(".")[0]
        cleanfilename = re.sub('[^0-9a-zA-Z]+', ' ', filename)
        filenamewords = cleanfilename.split()
        for word in filenamewords:
            if (topterms.has_key(word)):
                topterms[word] += 1
            else:
                topterms[word] = 1
    print topterms

if __name__ == "__main__":
    main()
    #parse_json()