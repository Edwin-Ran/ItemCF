#coding=utf-8

import GlobalVariables;
import operator;

import DataProcessor;
import Util;

class BasedOnSongs:
    def __init__(self,userid,topK):
        self.userid = userid;
        self.topK = topK;

    def getRecommend(self):
        rank = dict();
        sortList = [];

        #get user downloaded songid
        userLikedSongs = GlobalVariables.DictBasedOnUser[self.userid];

        for songID in userLikedSongs:
            if(not GlobalVariables.MatrixForSimilarity.has_key(songID)):
                continue;

            for i,score in GlobalVariables.MatrixForSimilarity[songID].items():
                sortList.append((i,score));

            for j,wj in sorted(sortList,key=operator.itemgetter(1),reverse=True)[0:self.topK]:
                #if user downloaded this song continue
                if(j in userLikedSongs):
                    continue;
                if(rank.has_key(j)):
                    rank[j] += wj;
                else:
                    rank[j] = wj;

        return sorted(rank.items(),key=operator.itemgetter(1),reverse=True);


def test():
    #a = DataProcessor.FileToDict(Util.ConfigUtil.getValue("data","OriginalDataFilePath") + "test.log");
    a.generateAllData();

    b = BasedOnSongs(u"123456",10);
    print b.getRecommend();

test();



