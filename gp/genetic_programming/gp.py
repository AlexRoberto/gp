'''
Created on 16/03/2014

@author: alex
'''
from numpy import math
from operator import itemgetter
import random

from genetic_programming.tree import Tree


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
        self._fitness()
        
        max_it = 0
        while max_it < self._max_it:
            first_individual = 1
            second_individual = 2
            first_deph = 1
            individual1 = self._select_individual()
            individual2 = self._select_individual(individual1)
            self._append_individual(individual1)
            self._append_individual(individual2)
            if (random.randint(0,100) <= self._mutation_tax):
                self._mutation(individual1, first_deph, random.randint(1,self._deph))
                self._mutation(individual2, first_deph, random.randint(1,self._deph))
            else:
                individual1, individual2 = self._crossover(individual1, individual2)
                new_individual1 = self._individual_restart(individual1["key"])
                new_individual2 = self._individual_restart(individual2["key"])
                self._append_individual(new_individual1)
                self._append_individual(new_individual2)
            self._fitness()
            #TODO
        self.test()
        
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
        function = {} #a chave eh o id do objeto, o item eh a funcao
        function_normalized = {} #normalizada entre 0 e 1    
        count = 0
        for individual in self._population:
            if individual["calculou"] == True:
                count += 1
                continue
            else:    
                #calcula funcao        
                self._function(individual, function)
                
                #normaliza        
                self._normalized(function_normalized, function, count)
                
                #calcula threshold
                self._threshold(function_normalized, function, count)

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
                
    def _normalized(self, function_normalized, function, count):
        values = []
        for key, value in function.items():
            values.append(value)
        min_ = min(values)
        max_ = max(values)
    
        '''se o individuo atribuiu o mesmo valor de funcao para todos os individuos
        maximo - minimo = 0, logo, ele nao eh util'''
        if max_ == min_:
            del self._population[count]
            return
        for key, value in function.items():
            function_normalized[key] = float((value - min_)/(max_-min_))
            
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
                if (threshold_final['class'] == function[threshold_final['key']] and \
                        function[threshold_final['key']] == self._class_[first_class]):
                    hit += 1
                elif(threshold_final['class'] == function[threshold_final['key']] and \
                        function[threshold_final['key']] == self._class_[second_class]):
                    hit += 1
            thresholds.append({"threshold": threshold, "hit": hit})

        thresholds = sorted(thresholds, key=itemgetter("hit"),reverse = True)
        first_threshold = 0
        threshold = thresholds[first_threshold]["threshold"]
        self._population[count]["threshold"] = threshold
        self._population[count]["calculou"] = True
        
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
            if (classified[key] == self._class_[second_class]) and (value == self._class_[second_class]):#tp
                tp += 1
            elif (classified[key] == self._class_[first_class]) and (value == self._class_[first_class]): #tn
                tn += 1
            elif (classified[key] == self._class_[second_class]) and (value == self._class_[first_class]): #fp
                fp += 1
            else: #fn
                fn += 1

        precision = float(tp)/float(tp+fp)
        recall = float(tp)/float(tp+fn)
        return(precision, recall,tp, fp, fn, tn)
    
    def _function(self, individual, function):
        functions = []
        self._InOrder(individual["key"], functions)
        '''para cada objeto, calcula a funcao correspondente a ele baseado no 
        individuo que chegou'''
        for key, value in self._train_set.iteritems():
            function_ = 0
            count = 0
            operations = ""
            
            for node in functions:
                if node == "+" or node == "-" or node == "/" or node == "*" or node == "/":
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
        
    def _select_individual(self, individual=None):
        if len(self._population) == 0 or len(self._population) == 1:
            quit()
        while(1):
            first = self._population[random.randint(0,len(self._population)-1)]
            if individual != None and individual["fitness"] == first["fitness"]:
                continue
            second = self._population[random.randint(0,len(self._population)-1)]
            if individual != None and individual["fitness"] == second["fitness"]:
                continue
            if first["fitness"] != second["fitness"]:
                break
        if first["fitness"] >= second["fitness"]:
            return first
        else:
            return second
    
    def _append_individual(self, individual):
        self._population.append(individual)
        
    def _mutation(self, individual, deph, level):
        if individual == None or deph > level:
            return
        else:
            if individual.cargo == "+" or individual.cargo == "-" or individual.cargo == "*" or individual.cargo == "/":
                individual.cargo = self._operations[random.randint(0, len(self._operations) - 1)]
            else:
                individual.cargo = random.uniform(-1000.0, 1000)
        self._mutation(individual.left, self._operations, deph+1, level)
        self._mutation(individual.right, self._operations, deph+1, level)
        
    def _overlap(self, individual1, individual2):
        if individual1["key"] is not None and individual2["key"] is not None:
            left = self._overlap(individual1["key"].left, individual2["key"].left)
            right = self._overlap(individual1["key"].right, individual2["key"].right)
            return 1 + left + right
        else:
            return 0
    
    def _make_crossover(self, individual1, individual2, position):
        left_overlap = self._overlap(individual1["key"].left, individual2["key"].left)
        right_overlap = self._overlap(individual1["key"].right, individual1["key"].right)
        assert position <= left_overlap + right_overlap + 1
        assert position >= 1
        if position <= left_overlap:
            assert left_overlap >= 1
            left1, left2 = self._make_crossover(individual1["key"].left, individual2["key"].left, position)
            right1, right2 = individual1["key"].right, individual2["key"].right
            individual1["key"] = Tree(individual1["key"].cargo, left1, right1)
            individual2["key"] = Tree(individual2["key"].cargo, left2, right2)
            return individual1, individual2
        elif position == left_overlap + 1:
            individual2["key"] = Tree(individual1["key"].cargo, individual1["key"].left, individual1["key"].right)
            individual1["key"] = Tree(individual2["key"].cargo,individual2["key"].left, individual2["key"].right)
            return individual1, individual2
        else:
            new_position = position - (left_overlap + 1)
            assert new_position >= 1
            assert right_overlap >= 1
            left1, left2 = individual1["key"].left, individual2["key"].left
            right1, right2 = self._make_crossover(individual1["key"].right, individual2["key"].right, new_position)
            individual1["key"] = Tree(individual1["key"].cargo, left1, right1)
            individual2["key"] = Tree(individual2["key"].cargo, left2, right2)
            return individual1, individual2
        
    
    def _crossover(self, individual1, individual2):
        s = self._overlap(individual1, individual2)
        position = random.randint(1, s)
        (individual1, individual2) = self._make_crossover(individual1, individual2, position)
        return individual1, individual2
    
    def _individual_restart(self, tree):
        return {"fitness": 0.0, "key": tree, "threshold": 0, "tp":0, "tn":0, "fp":0, "fn": 0, "calculou":False}

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