'''
Created on 16/03/2014

@author: alex
'''

class Genetic_Programming(object):
    _pop_len = 0
    _max_it = 0
    _deph = 0
    _train_args = []
    _test_args = []
    _train_set ={}
    _test_set = {}
    _train = 1
    _test = 2
    _class_ = []
    _class_data_train_ = {}
    _class_data_test_ = {}
    def __init__(self, args):
        pop_len = False
        max_it = False
        deph = False
        te = False
        tr = False
        for arg in args.split():
            if arg == "pop_len":
                pop_len = True
            elif pop_len == True:
                self._pop_len = int(arg)
                pop_len = False
            elif arg == "max_it":
                max_it = True
            elif max_it == True:
                self._max_it = int(arg)
                max_it = False
            elif arg == "deph":
                deph = True
            elif deph == True:
                self._deph = int(arg)
                deph = False
            elif arg == "tr":
                tr = True
            elif tr == True:
                if arg == "te":
                    tr = False
                    te = True
                else:
                    self._train_args.append(arg)
            elif te == True:
                self._test_args.append(arg)
                
    def gp(self):
        self._load_train_or_test_(self._train)
        self._load_train_or_test_(self._test)
    
    def _load_train_or_test_(self, train_or_test):
        count = 0
        load = []
        take_data = False
        if train_or_test == self._train:
            load = self._train_args
        else:
            load = self._test_args
        for arg in load:
            f = open(arg, "r")
            for line in f.readlines():
                line = line.replace("\n", "")
                line = line.replace("\r", "")
                if "Class" in line:
                    line = line.replace("{", "")
                    line = line.replace("}", "")
                    self._class_ = line.split(",")
                elif line == "@data":
                    take_data = True
                elif take_data == True:
                    data = line.split(',')
                    if train_or_test == self._train:
                        self._class_data_train_[count] = data[-1]
                        del data[-1]
                        self._train_set[count] = data
                    else:
                        self._class_data_test_[count] = data[-1]
                        del data[-1]
                        self._test_set[count] = data
                    count += 1
                f.close()
    
    def test(self):
        print (self._deph)
        print (self._max_it)
        print (self._pop_len)
        print (self._train_args)
        print (self._test_args)
        print (self._class_)
        print (self._class_data_train_)
        print (self._class_data_test_)