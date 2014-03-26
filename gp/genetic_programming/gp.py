'''
Created on 16/03/2014

@author: alex
'''
from numpy import math
from operator import itemgetter
import random

from genetic_programming.tree import Tree, mutation, crossover


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
    _population = []
    _operations = {0:"+", 1:"-", 2:"+", 3:"/"}
    _mutation_tax = 0
    _crossover_tax = 0
    _fitness_median = 0.0
    _num_zeros = 0
    _num_ones = 0
    _num_wrongs = 0
    _num_hits = 0
    _doing_train = False
    _threshold = 0.0
    _fitness = 0.0
    
    def __init__(self, args):
        pop_len = False
        max_it = False
        deph = False
        te = False
        tr = False
        mutation_tax = False
        crossover_tax = False
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
            elif arg == "mutation_tax":
                mutation_tax = True
            elif mutation_tax == True:
                self._mutation_tax = int(arg)
                mutation_tax = False
            elif arg == "crossover_tax":
                crossover_tax = True
            elif crossover_tax == True:
                self._crossover_tax = int(arg)
                crossover_tax = False
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
                
    def gp_facade(self):
        self._load_train_or_test_(self._train)
        self._load_train_or_test_(self._test)
        self._create_population_()
        self._doing_train = True
        self._fitness()
        the_most_adapted = 0
        max_it = 0
        while max_it < self._max_it:
            first_deph = 1
            individual1, index = self._select_individual()
            individual2, index = self._select_individual(index)
            if (random.randint(0,100) <= self._mutation_tax):
                mutation(self._operations, individual1["key"], first_deph, random.randint(1,self._deph))
                mutation(self._operations, individual2["key"], first_deph, random.randint(1,self._deph))
                new_individual1 = self._individual_restart(individual1["key"])
                new_individual2 = self._individual_restart(individual2["key"])
            else:
                tree1, tree2 = crossover(individual1["key"], individual2["key"])
                new_individual1 = self._individual_restart(tree1)
                new_individual2 = self._individual_restart(tree2)
            self._append_individual(new_individual1)
            self._append_individual(new_individual2)
            self._fitness()
            self._population = sorted(self._population, key=itemgetter("fitness"), reverse = True)
            if len(self._population) == 0:
                quit()
            print("%d %d %f")%(max_it, len(self._population), self._population[the_most_adapted]["fitness"])
            max_it += 1
        for individual in self._population:
            self._fitness_median += individual["fitness"]
        self._fitness_median /= len(self._population)
        self._doing_train = False
        self._threshold = self._population[the_most_adapted]["threshold"]
        self._fitness = self._population[the_most_adapted]["fitness"]
        self._classify_test(self._population[the_most_adapted])
        
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
                if "True_epitope" in line or "Class" in line:
                    line = line.split()[2]
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
            take_data = False
            f.close()
    
    def _create_population_(self):
        deph = 2
        num_features = len(self._train_set[0])
        for count in range(self._pop_len):
            if count < self._pop_len/2:
                individual = self._full(deph, num_features)
            else:    
                individual = self._grow(deph, num_features)
            self._population.append({"fitness": 0.0,
                                     "key": individual,
                                     "threshold": 0.0,
                                     "tp":0,
                                     "tn":0,
                                     "fp":0,
                                     "fn": 0,
                                     "calculou":False})
            if deph == self._deph:
                deph = 2
            else:
                deph += 1
    
    def _full(self, profundidade, num_features):
        if profundidade == 0:
            '''escolhe se vai ser uma constante ou uma variavel. Um tipo de uma 
            constante sera float e de uma variavel sera str'''
            aux = random.randint(0,100)
            if aux > 70:            
                atributo = random.uniform(-1000.0, 1000.0)
                return Tree(atributo)
            else:
                n = random.randint(0, num_features - 1)
                atributo = str(n)
                return Tree(atributo)
        else:
            n = random.randint(0, len(self._operations) - 1)
            operador = self._operations[n]
            filho_esquerda = self._full(profundidade - 1, num_features)
            filho_direita = self._full(profundidade - 1, num_features)
            return Tree(operador, filho_esquerda, filho_direita)
    
    def _grow(self, profundidade, num_features):
        if profundidade == 0:
            '''escolhe se vai ser uma constante ou uma variavel. Um tipo de uma 
            constante sera float e de uma variavel sera str'''
            aux = random.randint(0,100)
            if aux > 70:            
                atributo = random.uniform(-1000.0, 1000.0)            
                return Tree(atributo)
            else:
                n = random.randint(0, num_features - 1)
                atributo = str(n)
                return Tree(atributo)
        else:
            n = random.randint(0, len(self._operations) - 1)
            operador = self._operations[n]
            aux = random.randint(0, 2)
            if aux == 0:
                filho_esquerda = self._grow(profundidade - 1, num_features)
                return Tree(operador, filho_esquerda)
            elif aux == 1:    
                filho_direita = self._grow(profundidade - 1, num_features)
                return Tree(operador, filho_direita)
            else:
                filho_esquerda = self._grow(profundidade - 1, num_features)
                filho_direita = self._grow(profundidade - 1, num_features)
                return Tree(operador, filho_esquerda, filho_direita)
            
    def _fitness(self):
        count = 0
        for individual in self._population:
            function = {} #a chave eh o id do objeto, o item eh a funcao
            function_normalized = {} #normalizada entre 0 e 1  
            if individual["calculou"] == True:
                count += 1
                continue
            else:    
                #calcula funcao        
                self._function(individual, function)
                
                #normaliza        
                count_aux = self._normalized(function_normalized, function, count)
                if count_aux != count:
                    del self._population[count_aux]
                    continue
                #calcula threshold
                count_aux = self._threshold(function_normalized, function, count)
                if count_aux != count:
                    del self._population[count_aux]
                    continue
                #precision and recall
                precision, recall, tp, fp, fn, tn = self._matrix_confusion(function_normalized, function, count)
                try:
                    fitness = 2.0*(precision*recall)/(precision+recall)
                    self._population[count]["fitness"] = fitness
                    self._population[count]["tp"] = tp
                    self._population[count]["tn"] = tn
                    self._population[count]["fp"] = fp
                    self._population[count]["fn"] = fn
                    count += 1
                except:
                    del self._population[count]
                    continue
                
    def _normalized(self, function_normalized, function, count=-1):
        values = []
        for key, value in function.items():
            values.append(value)
        min_ = min(values)
        max_ = max(values)
    
        '''se o individuo atribuiu o mesmo valor de funcao para todos os individuos
        maximo - minimo = 0, logo, ele nao eh util'''
        if max_ == min_:
            del self._population[count]
            count -= 1
            return count
        for key, value in function.items():
            function_normalized[key] = float((value - min_)/(max_-min_))
        return count
    
    def _threshold(self, function_normalized, function, count):
        thresholds = []
        thresholds_options = []
    
        for i in range(50):
            thresholds_options.append(random.uniform(0.0, 1.0))
        
        first_class = 0
        second_class = 1
        for threshold in thresholds_options:
            thresholds_final = []
            for key, value in function_normalized.iteritems():
                if value < threshold:
                    thresholds_final.append({"key": key, "class": self._class_[first_class]})
                else:
                    thresholds_final.append({"key": key, "class": self._class_[second_class]})

            hit = 0
            for threshold_final in thresholds_final:
                if (threshold_final['class'] == self._class_data_train_[threshold_final["key"]] and \
                        self._class_data_train_[threshold_final["key"]] == self._class_[first_class]):
                    hit += 1
                elif(threshold_final['class'] == self._class_data_train_[threshold_final["key"]] and \
                        self._class_data_train_[threshold_final["key"]] == self._class_[second_class]):
                    hit += 1
            thresholds.append({"threshold": threshold, "hit": hit})

        thresholds = sorted(thresholds, key=itemgetter("hit"),reverse = True)
        first_threshold = 0
        if thresholds[first_threshold]["hit"] == 0:
            return count - 1
        threshold = thresholds[first_threshold]["threshold"]
        self._population[count]["threshold"] = threshold
        self._population[count]["calculou"] = True
        return count
    
    def _matrix_confusion(self, function_normalized, function, count):
        classified = {}
        
        first_class = 0
        second_class = 1
        
        threshold = self._population[count]["threshold"]
        for key, value in function_normalized.items():
            if value < threshold:
                classified[key] = self._class_[first_class]
            else:
                classified[key] = self._class_[second_class]

        tp = 0 #true positive
        fp = 0 #false positive
        fn = 0 #false negative
        tn = 0 #true negative

        for key, value in classified.iteritems():
            if (value == self._class_[second_class]) and (self._class_[second_class] == self._class_data_train_[key]):#tp
                tp += 1
            elif (value == self._class_[first_class]) and (self._class_[first_class] == self._class_data_train_[key]): #tn
                tn += 1
            elif (value == self._class_[second_class]) and (self._class_[first_class] == self._class_data_train_[key]): #fp
                fp += 1
            else: #fn
                fn += 1

        precision = float(tp)/float(tp+fp)
        recall = float(tp)/float(tp+fn)
        return(precision, recall,tp, fp, fn, tn)
    
    def _function(self, individual, function):
        functions = []
        set_ = {}
        self._InOrder(individual["key"], functions)
        '''para cada objeto, calcula a funcao correspondente a ele baseado no 
        individuo que chegou'''
        if self._doing_train == True:
            set_ = self._train_set
        else:
            set_ = self._test_set
        for key, value in set_.iteritems():
            function_ = 0
            count = 0
            operations = ""
            
            for node in functions:
                if node == "+" or node == "-" or node == "/" or node == "*":
                    operations = node
                    continue
                if type(node) is float:
                    if count == 0:
                        function_ = node
                        count = 1
                    else:
                        if operations == "+":
                            function_ += node
                        elif operations == "-":
                            function_ -= node
                        elif operations == "*":
                            function_ *= node
                        elif operations == "/":
                            if math.fabs(node) <= 0.001:
                                function_ = function
                            else:    
                                function_ /= node
                else:
                    if count == 0:
                        function_ = float(value[int(float(node))])
                        count = 1
                    else:
                        if operations == "+":
                            function_ += float(value[int(node)])
                        elif operations == "-":
                            function_ -= float(value[int(node)])
                        elif operations == "*":
                            function_ *= float(value[int(node)])
                        elif operations == "/":
                            if math.fabs(float(value[int(node)])) <= 0.001:
                                function_ = function_
                            else:
                                function_ /= float(value[int(node)])
            function[key] = function_
            
    def _InOrder(self, tree, functions):
        if tree == None: 
            return
        self._InOrder(tree.left, functions)
        functions.append(tree.cargo)
        self._InOrder(tree.right, functions)
        
    def _select_individual(self, first_index=-1):
        if len(self._population) == 0 or len(self._population) == 1:
            quit()
        while(1):
            individual_index1 = random.randint(0,len(self._population)-1)
            first = self._population[individual_index1]
            if first_index != -1 and individual_index1 == first_index:
                continue
            individual_index2 = random.randint(0,len(self._population)-1)
            second = self._population[individual_index2]
            if first_index != -1 and individual_index2 == first_index:
                continue
            if individual_index1 != individual_index2:
                break
        if first["fitness"] >= second["fitness"]:
            return first, individual_index1
        else:
            return second, individual_index2
    
    def _append_individual(self, individual):
        self._population.append(individual)
    
    def _individual_restart(self, tree):
        return {"fitness": 0.0, "key": tree, "threshold": 0, "tp":0, "tn":0, "fp":0, "fn": 0, "calculou":False}
    
    def _classify_test(self, individual_most_adapted):
        function = {} #a chave eh o id do objeto, o item eh a funcao
        function_normalized = {} #normalizada entre 0 e 1 
        self._function(individual_most_adapted, function)
        self._normalized(function_normalized, function)
        
        first_class = 0
        second_class = 1
        for key, value in function_normalized.items():
            if value < self._threshold:
                if self._class_data_test_[key] == self._class_[first_class]:
                    self._num_zeros += 1
                    self._num_hits += 1
                else:
                    self._num_wrongs += 1
            else:
                if self._class_data_test_[key] == self._class_[second_class]:
                    self._num_ones += 1
                    self._num_hits += 1
                else:
                    self._num_wrongs += 1

    def test(self):
        print (self._deph)
        print (self._max_it)
        print (self._pop_len)
        print (self._mutation_tax)
        print (self._crossover_tax)
        print (self._train_args)
        print (self._test_args)
        print (self._class_)
        print (self._class_data_train_)
        print (self._class_data_test_)
        print (self._train_set)
        print (self._test_set)
        print (self._population)
        print (self._fitness_median)
        print (self._fitness)
        print (self._threshold)
        print (self._num_zeros)
        print (self._num_ones)
        print (self._num_hits)
        print (self._num_wrongs)