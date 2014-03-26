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
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/tr0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/tr1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/tr2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/tr3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/tr4.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/te0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te4.arff"
        second_test = "2"
        self._args[second_test] = "pop_len 500 \
                        max_it 100 \
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/monk/monks1_train.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/monk/monks1_test.arff"
    def args(self, args_num):
        return self._args[args_num]