#coding=utf-8
import Util;
import GlobalVariables;
import re;
import sys;
import math;

reload(sys);
sys.setdefaultencoding("utf-8");

class FileToDict:
    def __init__(self,dataFilePath):
        self.dataFilePath = dataFilePath;

    #process data into GlobalVariables
    def fileFrocess(self):
        self.input = Util.FileUtil(self.dataFilePath).getInput();
        searchKscByPagePattern = re.compile(r"searchKscByPage");
        userClickKscPattern = re.compile(r"userClickKsc");
        result = dict();

        for line in self.input:
            line = line.decode("utf-8");

            if(userClickKscPattern.search(line)):
                listWithTitle = line.split("\t");
                for data in listWithTitle:
                    temp  = data.split(":");
                    if(len(temp) == 2):
                        result[temp[0]] = temp[1];
                    elif(len(temp) > 2):
                        result["date"] = data[5:];

            if(result):
                if(result["userid"] == u"0"):
                    continue;

                #DictBasedOnUser
                if(GlobalVariables.DictBasedOnUser.has_key(result["userid"])):
                    if(result["songID"] not in GlobalVariables.DictBasedOnUser[result["userid"]]):
                        GlobalVariables.DictBasedOnUser[result["userid"]].append(result["songID"]);
                else:
                    GlobalVariables.DictBasedOnUser[result["userid"]] = [result["songID"]];

                #DictBasedOnSong
                if(GlobalVariables.DictBasedOnSong.has_key(result["songID"])):
                    if(result["userid"] not in GlobalVariables.DictBasedOnSong[result["songID"]]):
                        GlobalVariables.DictBasedOnSong[result["songID"]].append(result["userid"]);
                else:
                    GlobalVariables.DictBasedOnSong[result["songID"]] = [result["userid"]];

                #incase result is null,so the data remain in  result will be count multiple times
                result.clear();

    def getMatrixForSong(self):
        for u,songs in GlobalVariables.DictBasedOnUser.items():
            for i in songs:
                if(GlobalVariables.MatrixForSong.has_key(i)):
                    GlobalVariables.SongDownloadNum[i] += 1;
                else:
                    GlobalVariables.SongDownloadNum[i] = 1;
                for j in songs:
                    if(i == j):
                        continue;
                    if(GlobalVariables.MatrixForSong.has_key(i) and GlobalVariables.MatrixForSong[i].has_key(j)):
                        GlobalVariables.MatrixForSong[i][j] += 1;
                    elif(GlobalVariables.MatrixForSong.has_key(i) and not GlobalVariables.MatrixForSong[i].has_key(j)):
                        GlobalVariables.MatrixForSong[i][j] = 1;
                    else:
                        GlobalVariables.MatrixForSong[i] = dict();
                        GlobalVariables.MatrixForSong[i][j] = 1;

    def getMatrixForSimilarity(self):
        for i,related_songs in GlobalVariables.MatrixForSong.items():
            for j,countij in related_songs.items():
                if(GlobalVariables.MatrixForSimilarity.has_key(i)):
                    GlobalVariables.MatrixForSimilarity[i][j] = countij / math.sqrt(GlobalVariables.SongDownloadNum[i] * GlobalVariables.SongDownloadNum[j]);
                else:
                    GlobalVariables.MatrixForSimilarity[i] = dict();
                    GlobalVariables.MatrixForSimilarity[i][j] = countij / math.sqrt(GlobalVariables.SongDownloadNum[i] * GlobalVariables.SongDownloadNum[j]);

    #a function to geneate All needed dataset
    def generateAllData(self):
        self.fileFrocess();
        self.getMatrixForSong();
        self.getMatrixForSimilarity();


def test():
    a = FileToDict(Util.ConfigUtil.getValue("data","OriginalDataFilePath") + "test.log");
    #a.fileFrocess();
    #print GlobalVariables.DictBasedOnUser;
    # print '\n';
    # print GlobalVariables.DictBasedOnSong;

    #a.getMatrixForSong();
    # print "********************************"
    # print GlobalVariables.SongDownloadNum;
    # print "\n";
    # print GlobalVariables.MatrixForSong;
    #a.getMatrixForSimilarity();
    a.generateAllData();
    print  GlobalVariables.MatrixForSimilarity;

#test();

