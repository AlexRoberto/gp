'''
Created on 16/03/2014

@author: alex
'''

class Utils(object):
    _args = {}
    
    def __init__(self):
        first_test = "1"
        self._args[first_test] = "pop_len 100 \
                        max_it 50 \
                        deph 5 \
                        tr \
                        gp/genetic_programming/database/tr0.arff \
                        database/tr1.arff \
                        database/tr2.arff \
                        database/tr3.arff \
                        database/tr4.arff \
                        te \
                        database/te0.arff \
                        database/te1.arff \
                        database/te2.arff \
                        database/te3.arff \
                        database/te4.arff"
    def args(self, args_num):
        return self._args[args_num]