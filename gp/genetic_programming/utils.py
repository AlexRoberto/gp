'''
Created on 16/03/2014

@author: alex
'''

class Utils(object):
    _args = {}
    
    def __init__(self):
        first_test = "1"
        self._args[first_test] = "pop_len 100 \
                        max_it 100 \
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
        third_test = "3"
        self._args[third_test] = "pop_len 100 \
                        max_it 100 \
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr0-100.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr1-100.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr2-100.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr3-100.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr4-100.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/te0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te4.arff"
        fourth_test = "4"
        self._args[fourth_test] = "pop_len 100 \
                        max_it 100 \
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr0-200.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr1-200.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr2-200.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr3-200.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr4-200.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/te0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te4.arff"
        fifth_test = "5"
        self._args[fifth_test] = "pop_len 100 \
                        max_it 100 \
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr0-500.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr1-500.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr2-500.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr3-500.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr4-500.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/te0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te4.arff"
        sixth_test = "6"
        self._args[sixth_test] = "pop_len 100 \
                        max_it 100 \
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr0-1000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr1-1000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr2-1000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr3-1000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr4-1000.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/te0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te4.arff"
        seventh_test = "7"
        self._args[seventh_test] = "pop_len 100 \
                        max_it 100 \
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr0-1500.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr1-1500.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr2-1500.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr3-1500.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr4-1500.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/te0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te4.arff"
        eighth_test = "8"
        self._args[eighth_test] = "pop_len 100 \
                        max_it 100 \
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr0-2000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr1-2000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr2-2000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr3-2000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr4-2000.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/te0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te4.arff"
        ninth_test = "9"
        self._args[ninth_test] = "pop_len 100 \
                        max_it 100 \
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr0-3000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr1-3000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr2-3000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr3-3000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr4-3000.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/te0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te4.arff"
        tenth_test = "10"
        self._args[tenth_test] = "pop_len 100 \
                        max_it 100 \
                        deph 7 \
                        mutation_tax 40 \
                        crossover_tax 60 \
                        tr \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr0-4000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr1-4000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr2-4000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr3-4000.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/balanceado/tr4-4000.arff \
                        te \
                        /home/alex/git/gp/gp/genetic_programming/database/te0.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te1.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te2.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te3.arff \
                        /home/alex/git/gp/gp/genetic_programming/database/te4.arff"
    def args(self, args_num):
        return self._args[args_num]