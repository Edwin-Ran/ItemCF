#coding=utf-8
import ConfigParser;
import os;
import codecs;

#read config from ini file
class ConfigUtil:
	def __init__(self,configFilePath):
		self.cf = ConfigParser.ConfigParser();
		self.cf.read(configFilePath);

	def getConfigParser(self,section,key):
		return self.cf.get(section,key);

	@staticmethod
	def getValue(section,key):
		return ConfigUtil(os.getcwd() + os.sep + "Config.ini").getConfigParser(section,key);


#class DateUtil:

# read or write file
class FileUtil:
    def __init__(self,filePath):
        self.filePath = filePath;

    def getInput(self):
        return codecs.open(self.filePath,'r',"utf-8");
        #return open(self.filePath,'r');

def test():
    path =  ConfigUtil.getValue("data","OriginalDataFilePath");
    a = FileUtil(path + u"test.log").getInput();

test();
