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
        self._create_population_()
        self._fitness()
    
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
        dic_funcao = {} #a chave eh o id do objeto, o item eh a funcao
        funcao_normalizada = {} #normalizada entre 0 e 1    
        count = 0
        for individuo in populacao:
            if individuo["calculou"] == True:
                count += 1
                continue
            else:    
                #calcula funcao        
                calcula_funcao(individuo["key"], objeto_treino, dic_classe, dic_funcao)
            
                #normaliza        
                list_aux = []
                for k, v in dic_funcao.iteritems():
                    list_aux.append(v)
                minimo = min(list_aux)
                maximo = max(list_aux)
            
                '''se o individuo atribuiu o mesmo valor de funcao para todos os individuos
                maximo - minimo = 0, logo, ele nao eh util'''
                if maximo == minimo:
                    del populacao[count]
                    continue
                for k, v in dic_funcao.iteritems():
                    funcao_normalizada[k] = float((v - minimo)/(maximo-minimo))
            
                list_threshold = []
                list_opcoes = []
            
                for i in range(50):
                    list_opcoes.append(random.uniform(0.0, 1.0))
                #calcula threshold        
                for threshold in list_opcoes:
                    list_final = []
                    for k, v in funcao_normalizada.iteritems():
                        if v < threshold:
                            aux = {"key": k, "classe": classe[0]}
                        else:
                            aux = {"key": k, "classe": classe[1]}
                        list_final.append(aux)
    
                    acerto = 0
                    for j in list_final:
                        if (j['classe'] == dic_classe[j['key']] and dic_classe[j['key']] == classe[1]):
                            acerto += 1            
                        elif(j['classe'] == dic_classe[j['key']] and dic_classe[j['key']] == classe[0]):
                            acerto += 1
                    a = {"threshold": threshold, "acerto": acerto}
                    list_threshold.append(a)
    
                list_threshold = sorted(list_threshold, key=itemgetter("acerto"),reverse = True)
                threshold = list_threshold[0]["threshold"]
                populacao[count]["threshold"] = threshold
                populacao[count]["calculou"] = True
            
                #classifica os dados com a funcao dada
                dic_classificacao = {}
                for k, v in funcao_normalizada.iteritems():
                    if v < threshold:
                        dic_classificacao[k] = classe[0]
                    else:
                        dic_classificacao[k] = classe[1]
            
                #declara as variaveis que serao utilizadas para construir a matriz de confusao
                tp = 0 #true positive
                fp = 0 #false positive
                fn = 0 #false negative
                tn = 0 #true negative
    
                for k, v in dic_classificacao.iteritems():
                    a = v
                    b = dic_classe[k]
                    if (b == classe[1]) and (a == classe[1]):#tp
                        tp += 1
                    elif (b == classe[0]) and (a == classe[0]): #tn
                        tn += 1
                    elif (b == classe[1]) and (a == classe[0]): #fp
                        fp += 1
                    else: #fn
                        fn += 1
    
                precision = float(tp)/float(tp+fp)
                recall = float(tp)/float(tp+fn)
    
                try:
                    fitness = 2.0*(precision*recall)/(precision+recall)
                    populacao[count]["fitness"] = fitness
                    populacao[count]["tp"] = tp
                    populacao[count]["tn"] = tn
                    populacao[count]["fp"] = fp
                    populacao[count]["fn"] = fn
                    count += 1
                except:
                    del populacao[count]
                    continue
    def calcula_funcao(self, individuo, objeto_treino, dic_classe, dic_funcao):
        list_funcao = []
        '''para cada objeto, calcula a funcao correspondente a ele baseado no 
        individuo que chegou'''
        for k, v in objeto_treino.iteritems():
            funcao = 0
            count = 0
            operacoes = ""
            
            for i in list_funcao:
                if i == "+" or i == "-" or i == "/" or i == "*" or i == "/":
                    operacoes = i
                    continue
                if type(i) is float:
                    if count == 0:
                        funcao = i
                        count = 1
                    else:
                        if operacoes == "+":
                            funcao += i
                        elif operacoes == "-":
                            funcao -= i
                        elif operacoes == "*":
                            funcao *= i
                        elif operacoes == "/":
                            if math.fabs(i) <= 0.001:
                                funcao = funcao
                            else:    
                                funcao /= i
                else:
                    if count == 0:
                        funcao = float(v[int(float(i))])
                        count = 1
                    else:                    
                        if operacoes == "+":
                            funcao += float(v[int(i)])
                        elif operacoes == "-":
                            funcao -= float(v[int(i)])
                        elif operacoes == "*":
                            funcao *= float(v[int(i)])
                        elif operacoes == "/":
                            if math.fabs(float(v[int(i)])) <= 0.001:
                                funcao = funcao
                            else:
                                funcao /= float(v[int(i)])
            dic_funcao[k] = funcao
            
    def _InOrder(self, tree, list_funcao):
        if tree == None: 
            return
        self._InOrder(tree.left, list_funcao)
        list_funcao.append(tree.cargo)
        self._InOrder(tree.right, list_funcao)

    def test(self):
        print (self._deph)
        print (self._max_it)
        print (self._pop_len)
        print (self._train_args)
        print (self._test_args)
        print (self._class_)
        print (self._class_data_train_)
        print (self._class_data_test_)
        print (self._train_set)
        print (self._test_set)
        print (self._population)