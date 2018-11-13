import numpy as np
import random
from numpy.distutils.command.config import GrabStdout

class Graph:
    l_path = []
    l_cost = []
    l_select = []
    l_all = []
    index_select = []
    child_final = []
    chk_random = 0
    check_stop = 0
    #constructor
    def __init__(self,V,SIZ):
        self.V = V
        self.SIZ = SIZ
        Graph.arr = np.zeros((V,V),dtype=list);
        Graph.l_all=range(0,self.V)
    #for add edge
    def addEdge(self,src,dest,w):
        Graph.arr[ord(src)-65][ord(dest)-65] = w
        Graph.arr[ord(dest) - 65][ord(src) - 65] = w
    # for print matrix of graph represent
    def print_Graph(self):
        print Graph.arr

    #calculate random number from 0 to number of node
    def get_random(self):
        Graph.l_path = []
        for i in range(self.SIZ):
            x = random.sample(range(0, self.V), self.V)
            Graph.l_path.append(x)

        return Graph.l_path

    #check if two path or more equal in random
    def check_random(self):
        chk_random = 0
        for j in range(self.SIZ):
            for k in range(self.SIZ):
                if (j == k):
                    continue

                if (Graph.l_path[j] == Graph.l_path[k]):
                    chk_random = 1
                    break
        return chk_random
    #calculate cost for pathes choses
    def cal_cost(self):
        Graph.l_cost = []
        for i in range(self.SIZ):
            cnt = 0
            for j in range(self.SIZ - 1):
                cnt += Graph.arr[Graph.l_path[i][j]][Graph.l_path[i][j + 1]]
            Graph.l_cost.append(cnt)

        #print "cost %s"%(Graph.l_cost)
        return Graph.l_cost

    #print last pathes after check on it
    def print_population(self):
        self.get_random()
        while(self.check_random()):
            self.get_random()

        return Graph.l_path
    def check_cost(self):
        chk_cost = 0
        for j in range(self.SIZ):
            for k in range(self.SIZ):
                if (j == k):
                    continue

                if (Graph.l_cost[j] == Graph.l_cost[k]):
                    chk_cost = 1
                    break
        return chk_cost

    def get_last_path_cost(self):
        self.print_population()
        self.cal_cost()
        self.check_cost()
        while(self.check_cost()):
            self.print_population()
            self.cal_cost()
            self.check_cost()

        #print "initial pop %s"%(Graph.l_path)
        print "initial population"
        for i in Graph.l_path:
            print map(chr, (item + 65 for item in i))

        #print "path cost %s"%(Graph.l_cost)

    def print2Smallest(self,arr):
        # There should be atleast two elements
        Graph.index_select = []
        arr_size = len(arr)
        if arr_size < 2:
            print "Invalid Input"
            return

        first = second = float('inf')
        for i in range(0, arr_size):

            # If current element is smaller than first then
            # update both first and second
            if arr[i] < first:
                second = first
                first = arr[i]

            # If arr[i] is in between first and second then
            # update second
            elif (arr[i] < second and arr[i] != first):
                second = arr[i];

        if (second == float('inf')):
            Graph.check_stop = 1;
        else:
            Graph.index_select.append(arr.index(first))
            Graph.index_select.append(arr.index(second))

    #Step1 : Selection Operator
    def selection(self):
        Graph.l_select = []
        self.print2Smallest(Graph.l_cost)
        Graph.l_select.append(Graph.l_path[Graph.index_select[0]])
        Graph.l_select.append(Graph.l_path[Graph.index_select[1]])
        print "selection population"
        for i in Graph.l_select:
            print map(chr, (item + 65 for item in i))
        print "we select pathes which index is %s"%(Graph.index_select)
    # Step2 : Crossover Operator
    def crosover(self):
        final_child = []
        child = []
        mid1 = random.sample(range(1,self.V/2),1)
        mid2 = random.sample(range(self.V/2,self.V-1),1)

        child.append(list(set(Graph.l_all).difference(Graph.l_select[0][mid1[0]:mid2[0]])))
        child.append(list(set(Graph.l_all).difference(Graph.l_select[1][mid1[0]:mid2[0]])))

        #print child
        Graph.child_final = []
        for i in range(len(Graph.l_select)):
            l = [None] * self.V
            l[mid1[0]:mid2[0]] = Graph.l_select[i][mid1[0]:mid2[0]]

            l[mid2[0]:self.V] = child[i][0:self.V-mid2[0]]

            l[0:mid1[0]] = child[i][self.V-mid2[0]:]

            Graph.child_final.append(l)

        #print "new child %s"%(Graph.child_final)

    # Step 4 : Mutation Operator
    def mutation(self):
        self.crosover()
        x = random.sample(range(0,self.V),4)
        #print "new child from mutation %s"%(Graph.child_final)
        print "new child before mutation"
        for i in Graph.child_final:
            print map(chr, (item + 65 for item in i))

        j = 0
        for i in range(len(Graph.child_final)):
            Graph.child_final[i][x[i+j]],Graph.child_final[i][x[i+j+1]] = Graph.child_final[i][x[i+j+1]],Graph.child_final[i][x[i+j]]
            j = j+1
        #print "new child after  mutation %s" % (Graph.child_final)
        print "new child after mutation"
        for i in Graph.child_final:
            print map(chr, (item + 65 for item in i))

        print "end"
        print "--------------------------------------"

    def new_child(self):
        loc = 0
        for i in range(self.V):
            if (i in Graph.index_select):
                continue
            else:
                if(loc >= len(Graph.index_select)):
                    break
                else:
                    Graph.l_path[i] =  Graph.child_final[loc]
                    loc = loc+1
        #print Graph.l_path
        print "new population"
        for i in Graph.l_path:
            print map(chr, (item + 65 for item in i))

        print "cost"
        print Graph.l_cost




    def genetic_algorithm(self):
        self.get_last_path_cost()
        print Graph.l_cost
        x = 10
        for i in range(x):
            self.selection()
            self.crosover()
            self.mutation()
            self.new_child()
            self.cal_cost()

gh = Graph(6,4)
gh.addEdge('A','B',1)
gh.addEdge('A','C',2)
gh.addEdge('A','D',1)
gh.addEdge('A','E',4)
gh.addEdge('A','F',3)
gh.addEdge('B','F',2)
gh.addEdge('B','E',3)
gh.addEdge('B','D',2)
gh.addEdge('B','C',4)
gh.addEdge('C','D',3)
gh.addEdge('C','E',2)
gh.addEdge('C','F',1)
gh.addEdge('D','E',1)
gh.addEdge('D','F',5)
gh.addEdge('E','F',6)
gh.genetic_algorithm()

