from os import getcwd, walk, path
import re
import time


class Searcher(object):


    def __init__(self, udir):
        self.udir = udir
        self.searchtype = "variable"
        self.query = "#include <stdio.h>[\w]*"
        self.sfile = "/root/redis-unstable/utils/lru/lfu-simulation.c"

    def matcher(self, line):
        pattern = re.compile(self.query)
        return line, re.search(pattern, line)

    def allonce(self):
        try:
            t = time.time()
            result = {}
            for root, dirs, filenames in walk(path.join(getcwd(),self.udir)):
                for files in filenames:
                    with open(path.join(root, files),'r') as freader:
                        lines = freader.readlines()
                        x = map(self.matcher, lines)
                        x = filter((lambda x:x[1]!=None), x)
                        if len(x)!=0:
                            result[path.join(root, files)] = zip(*x)[0]
            first = {"This is how much time your query took to execute":time.time() - t}
            return result, first
        except Exception as e:
            return str(e)

    def twostep0(self):
        try:
            t = time.time()
            result = {}
            for root, dirs, filenames in walk(path.join(getcwd(),self.udir)):
                for files in filenames:
                    with open(path.join(root, files),'r') as freader:
                        x = re.findall(self.query, freader.read())
                    if len(x)!=0:
                        result[path.join(root, files)] = x
            second = {"This is how much time your query took to execute":time.time() - t}
            return result, second
        except Exception as e:
            return str(e)
		
	
    def twostep1(self):
        try:
            t = time.time()
            with open(self.sfile,'r') as freader:
                lines = freader.readlines()
            x = map(self.matcher, lines)
            x = filter((lambda x:x[1]!=None), x)
            third = {"This is how much time your query took to execute":time.time() - t}
            return zip(*x)[0], third
        except IndexError:
            return "No matches found"
        except Exception as e:
            return str(e)

