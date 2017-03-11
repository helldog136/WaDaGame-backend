from incandescent import Client
import json
import re
import operator

def main(upload_image_url):
    # Config
    uid = "7093"
    apikey = "838024ddaaa63db12d98ea3a16323cb6"

    search = Client(uid, apikey)
    #search.addImageUrl("http://i.skyrock.net/8989/70868989/pics/2813975768_1.png")
    search.addImageUrl(upload_image_url)
    #search.addImageUrl("http://i.imgur.com/KztFRBv.jpg")
    search.makeRequestData()
    search.makeRequest()


    #print(search.data)

    #if 'project_id' in search.data:
    res = search.getResults()
    print "res : "
    print res
    print "------------"
    return getGameName(res)
"""
    return getGameName([u'http://download.gamezone.com/uploads/image/data/1182115/Rogue_Legacy.JPG',
     u'http://i1.article.fd.zol-img.com.cn/t_s640x2000_w1/g4/M0B/05/0D/Cg-4zFTu41aIb7WWAARLe8i_NBQAAVlzwKaFzoABEuT987.jpg',
     u'https://farm4.staticflickr.com/3857/14424998087_fc2d6fa796_b.jpg',
     u'https://fanbolt-fanbolt.netdna-ssl.com/wp-content/uploads/2014/07/14454459905_2c30ec09c5_o.jpg',
     u'https://fanbolt-fanbolt.netdna-ssl.com/wp-content/uploads/2014/07/14454459905_2c30ec09c5_o.jpg',
     u'https://farm4.staticflickr.com/3857/14424998087_fc2d6fa796_b.jpg',
     u'http://www.godisageek.com/wp-content/uploads/Rogue-Legacy-Screenshot.png',
     u'https://articles-images.sftcdn.net/wp-content/uploads/sites/2/2014/08/02-568x319.jpg',
     u'https://cdn0.vox-cdn.com/thumbor/ISBwmoxqbZTRJx8N6eNyDSQIhTc%3D/176x77:1100x597/1600x900/cdn0.vox-cdn.com/uploads/chorus_image/image/35396670/14454459905_2c30ec09c5_o.0.jpg',
     u'http://static.betazeta.com/www.niubie.com/up/2014/07/Rogue-Legacy1-320x210.jpg',
     u'http://static.betazeta.com/www.niubie.com/up/2014/07/Rogue-Legacy1-320x210.jpg',
     u'http://www.bluegamer.net/wp-content/uploads/2013/07/RogueLegacy-2013-06-28-21-29-29-16.jpg',
     u'http://8.pic.paopaoche.net/up/2015-12/201512614720986080.jpg',
     u'http://8.pic.paopaoche.net/up/2015-12/201512614720986080.jpg',
     u'http://mos.futurenet.com/techradar/art/games/Best%2520laptop%2520games/rogue-legacy-420-90.jpg',
     u'http://o.aolcdn.com/hss/storage/midas/4cd5f03b417a0e87e4ac4cdf234f9e72/200393229/rogue-legacy-PS.jpg',
     u'http://o.aolcdn.com/hss/storage/midas/4cd5f03b417a0e87e4ac4cdf234f9e72/200393229/rogue-legacy-PS_thumbnail.jpg',
     u'http://o.aolcdn.com/hss/storage/midas/4cd5f03b417a0e87e4ac4cdf234f9e72/200393229/rogue-legacy-PS_thumbnail.jpg',
     u'http://file.lostresistance.blog.shinobi.jp/bb7c1293.jpeg',
     u'http://file.lostresistance.blog.shinobi.jp/bb7c1293.jpeg',
     u'http://psaddict.gr/wp-content/uploads/2015/12/14424998087_fc2d6fa796_b-1024x576.jpg',
     u'https://cf.geekdo-images.com/images/pic2199151_md.png',
     u'http://www.fansshare.com/image/roguelegacy/rogue-legacy-transistor-game-1430345018.jpg',
     u'http://icdn9.digitaltrends.com/image/14-7-1920x1080.png%3Fver%3D2',
     u'http://icdn8.digitaltrends.com/image/14-7-800x533-c.png%3Fver%3D2', u'http://s1.dmcdn.net/CBxkq/x240-Qyz.jpg',
     u'https://farm6.staticflickr.com/5193/14454459905_2c30ec09c5_o.jpg',
     u'https://i1.wp.com/3.bp.blogspot.com/-ItsUWDr3BTg/UdoqiEVAEjI/AAAAAAAAAdM/7_3vyGH_hxs/s400/rogue-legacy-pc-creenshot-02.jpg',
     u'https://c2.staticflickr.com/6/5193/14454459905_87d9329ea7_b.jpg',
     u'https://c2.staticflickr.com/4/3857/14424998087_fc2d6fa796_b.jpg',
     u'http://www.gamespark.jp/imgs/ogp_f/68300.jpg', u'http://www.gamespark.jp/imgs/ogp_f/68300.jpg',
     u'https://gamercaduco.files.wordpress.com/2015/06/09-rogue-legacy-summary-review-ferreiro-e-feiticeira.jpg',
     u'http://r3.ykimg.com/0541040854FEAB656A0A47046D6F98B2',
     u'http://nichegamer.com/wp-content/uploads/2014/07/rogue-legacy-07-09-14-1.jpg',
     u'https://static.betazeta.com/www.niubie.com/up/2014/07/Rogue-Legacy1-320x210.jpg',
     u'https://static.betazeta.com/www.niubie.com/up/2014/07/Rogue-Legacy1-320x210.jpg',
     u'http://cft2.igromania.ru/upload/iblock/821/518f99/detail.jpg',
     u'https://psmedia.playstation.com/is/image/psmedia/rogue-legacy-ps4-2-column%3F%24Icon%24',
     u'http://www.uplooder.net/img/image/26/0452dbf5a72963a3ca2b32e95a25d8af/4fziad.jpg',
     u'http://wallpapers.fansshare.com/photograph/roguelegacy/rl-sprite-1109635178.jpg',
     u'http://metrouk2.files.wordpress.com/2014/08/1080678611.jpg%3Fquality%3D80%26strip%3Dall%26w%3D1024%26h%3D576',
     u'http://images.akamai.steamusercontent.com/ugc/355024907210868091/91FB594DDD5CA185C25F5EA132DCB83F915D7E60/%3Finterpolation%3Dlanczos-none%26output-format%3Djpeg%26output-quality%3D95%26fit%3Dinside%257C1024:*',
     u'http://images.akamai.steamusercontent.com/ugc/355024907210868091/91FB594DDD5CA185C25F5EA132DCB83F915D7E60/%3Finterpolation%3Dlanczos-none%26output-format%3Djpeg%26output-quality%3D95%26fit%3Dinside%257C1024:*',
     u'https://s.aolcdn.com/hss/storage/midas/4cd5f03b417a0e87e4ac4cdf234f9e72/200393229/rogue-legacy-PS.jpg',
     u'https://s.aolcdn.com/hss/storage/midas/4cd5f03b417a0e87e4ac4cdf234f9e72/200393229/rogue-legacy-PS.jpg',
     u'http://nichegamer.com/wp-content/uploads/2014/07/rogue-legacy-07-09-14-1.jpg',
     u'http://nichegamer.com/wp-content/uploads/2014/07/rogue-legacy-07-09-14-1.jpg',
     u'https://game-guide.fr/wp-content/uploads/2013/08/2013-08-02_00004.jpg',
     u'http://o.aolcdn.com/hss/storage/midas/4cd5f03b417a0e87e4ac4cdf234f9e72/200393229/rogue-legacy-PS.jpg',
     u'http://ps4.tgbus.com/UploadFiles/201502/20150204093732126.jpg',
     u'http://livedoor.blogimg.jp/monoton3/imgs/f/e/fee600cb.jpg',
     u'http://livedoor.blogimg.jp/monoton3/imgs/f/e/fee600cb.jpg',
     u'http://8.pic.paopaoche.net/up/2015-12/201512614720986080.jpg',
     u'http://mos.futurenet.com/techradar/art/games/Best%2520laptop%2520games/rogue-legacy-420-90.jpg',
     u'http://mos.futurenet.com/techradar/art/games/Best%2520laptop%2520games/rogue-legacy-420-90.jpg',
     u'http://cfile3.uf.tistory.com/image/240F9C415235B82E32BAE5',
     u'http://i-1.497.com/2014/7/10/73ec86bf-2c3b-42ad-814c-20c67c1784a0.jpg',
     u'http://gamingtrend.com/wp-content/screenshots/rogue-legacy/roguelegacy-2013-06-28-01-23-43-57.png',
     u'http://gamingtrend.com/wp-content/screenshots/rogue-legacy/roguelegacy-2013-06-28-01-23-43-57.png',
     u'https://farm4.staticflickr.com/3857/14424998087_fc2d6fa796_b.jpg',
     u'https://3dnews.ru/assets/external/illustrations/2014/07/10/823764/2.jpg',
     u'https://3dnews.ru/assets/external/illustrations/2014/07/10/823764/2.jpg',
     u'http://www.pujia8.com/static/uploads/20150411111938_4.jpg',
     u'https://s-media-cache-ak0.pinimg.com/originals/41/68/9e/41689ebe67117d0ec7af55625f48fab0.jpg',
     u'http://www.gamingunion.net/newsimg/rogue-legacy-arrives-at-playstation-platforms-later-this-month.jpg',
     u'http://www.gamingunion.net/newsimg/rogue-legacy-arrives-at-playstation-platforms-later-this-month.jpg',
     u'http://blog-imgs-96-origin.fc2.com/c/v/c/cvcv152/20160901181239838.png',
     u'https://apollo2.dl.playstation.net/cdn/EP4488/NPEJ00386_00/FREE_CONTENTW3dLQaMPdISU56PI2OYv/PREVIEW_SCREENSHOT2_425754.jpg',
     u'https://i.ytimg.com/vi/HAbae4drunI/maxresdefault.jpg',
     u'http://2.bp.blogspot.com/-uRw8uQ9vBWI/Ud8ULp_-vGI/AAAAAAAADt4/y4dK1iPeoz0/s1600/RogueLegacy%2B2013-07-12%2B00-00-25-31.jpg',
     u'http://mos.futurenet.com/techradar/art/games/Best%2520laptop%2520games/rogue-legacy-420-90.jpg',
     u'http://www.ladebalken.net/wp-content/uploads/2014/07/14424998087_fc2d6fa796_b.jpg',
     u'http://www.tups4.com/wp-content/uploads/2014/08/2014-08-24-204447.jpg',
     u'http://8.pic.paopaoche.net/up/2015-12/201512614720986080.jpg',
     u'http://vitameanslife.esy.es/wp-content/uploads/2016/04/roguelegacy-1024x576.jpg',
     u'http://3.bp.blogspot.com/-ItsUWDr3BTg/UdoqiEVAEjI/AAAAAAAAAdM/7_3vyGH_hxs/s400/rogue-legacy-pc-creenshot-02.jpg',
     u'http://www.4gamer.net/games/040/G004096/20130709086/TN/008.jpg',
     u'http://www.4gamer.net/games/040/G004096/20130709086/SS/008.jpg',
     u'http://mos.futurenet.com/techradar/art/games/Best%2520laptop%2520games/rogue-legacy-420-90.jpg',
     u'http://mos.futurenet.com/techradar/art/games/Best%2520laptop%2520games/rogue-legacy-420-90.jpg',
     u'http://image.gamer.ne.jp/news/2015/20150408/0047cc70feadcb3f0aecebf20f6b62df3f8a/m/21.jpg',
     u'http://8.pic.paopaoche.net/up/2015-12/201512614720986080.jpg',
     u'http://gimmedigital.gimmedigital.netdna-cdn.com/wp-content/uploads/2014/08/RogueLegacy_PSVITA1.jpg',
     u'http://cfile8.uf.tistory.com/image/216A013954F6E7E510E082',
     u'http://livedoor.blogimg.jp/ysokuhou/imgs/3/d/3dd2e87b-s.jpg',
     u'http://www.quartertothree.com/fp/wp-content/uploads/2013/07/Body-1.jpg',
     u'http://imagenes.es.sftcdn.net/blog/es/2014/08/02-568x319.jpg',
     u'http://static.blog.playstation.com/wp-content/uploads/2014/07/roguelegacy.jpg',
     u'http://cdn1-www.playstationlifestyle.net/assets/uploads/2014/07/roguelegacyscreenshot2.jpg',
     u'http://cdn1-www.playstationlifestyle.net/assets/uploads/2014/07/roguelegacyscreenshot2.jpg',
     u'http://o.aolcdn.com/hss/storage/midas/4cd5f03b417a0e87e4ac4cdf234f9e72/200393229/rogue-legacy-PS.jpg',
     u'http://mos.futurenet.com/techradar/art/games/Best%2520laptop%2520games/rogue-legacy-420-90.jpg',
     u'http://thefreecheese.com/wp-content/uploads/2014/07/14454459905_2c30ec09c5_o.jpg',
     u'http://nichegamer.net/media/2014/07/rogue-legacy-07-09-14-1.jpg',
     u'http://o.aolcdn.com/hss/storage/midas/4cd5f03b417a0e87e4ac4cdf234f9e72/200393229/rogue-legacy-PS.jpg'])
"""
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

    # print(names)

def getGameName(urls):
    print urls
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
    #print topterms
    sortedterms = sorted(topterms.items(), key=operator.itemgetter(1), reverse=True)
    biggestDrop = 0
    biggestDropLoc = 0
    prec = 0
    for i in range(1,len(sortedterms)):
        drop = sortedterms[prec][1] - sortedterms[i][1]
        if (drop > biggestDrop):
            biggestDrop = drop
            biggestDropLoc = prec
        prec = i
    print biggestDrop
    print biggestDropLoc
    print sortedterms
    gameNameList= sortedterms[0: biggestDropLoc + 1]

    gameName = ""
    for i in gameNameList:
        gameName += i[0] + " "
    print gameName

    print "FULL NAME (with The)"
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
    print str(start) + " " + str(end) + " --> " + str(gameNameList[start:end + 1])

    output = ""
    for i in gameNameList[start:end + 1]:
        output += i[0]

    print "output of getGameName()"
    print output

    return output

#if __name__ == "__main__":
    #print(main("http://i.imgur.com/CaFjhJB.png"))
    #parse_json()