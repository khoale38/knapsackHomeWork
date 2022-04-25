from glob import glob
from traceback import print_tb
from ortools.algorithms import pywrapknapsack_solver
import numpy as np
import time
import os
import glob
foldername = "R01000/"
filename = "s000"
exportname = "json/"
path = exportname+foldername
TIME_LIMIT = 10


def createfolder():
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)


def writeOutPut(amount, computed_value, total_weight, packed_items, packed_weights, runtime):
    f = open(os.path.join(exportname, foldername + filename+'.json'), "w")
    f.writelines(foldername+filename+"\n")
    f.writelines('Time limit:'+str(TIME_LIMIT)+"\n")
    f.writelines('Amount of item :' + amount+"\n")
    f.writelines('Total value =' + str(computed_value)+"\n")
    f.writelines('Total weight:' + str(total_weight)+"\n")
    f.writelines('Packed items:' + str(packed_items)+"\n")
    f.writelines('Packed_weights:' + str(packed_weights)+"\n")
    f.writelines('Run time: '+str(runtime)+"\n")


def main():
    list5kpDir = []
    rootFolder = 'input/'
    
    parent_list = os.listdir(rootFolder)

    for child in parent_list:
        child_list = os.listdir(rootFolder+child)
        for R in child_list:
            R_list = os.listdir(rootFolder+child+"/"+R)
            for kp in R_list:
                kp=os.listdir(rootFolder+child+"/"+R+"/"+kp)
                count =0
                for item in kp:
                   
                    if count<5:
                        list5kpDir.append(rootFolder+child+"/"+R+"/"+str(kp)+"/"+item)
                        count=count+1
                    else:
                        break
  

                
                


def run(child):

    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    data = np.loadtxt(child, dtype=int, skiprows=3)
    amount = np.loadtxt(child, dtype='str', delimiter='\n')

    values = [

    ]
    weights = [[

    ]]
    for each in data:
        values.append(each[1])
        weights[0].append(each[0])

    capacities = [int(amount[1])]
    starttime = time.time()
    solver.Init(values, weights, capacities)
    solver.set_time_limit(180)
    computed_value = solver.Solve()
    endtime = time.time()

    packed_items = []
    packed_weights = []
    total_weight = 0

    print(foldername+filename)
    print('Time limit:', TIME_LIMIT)
    print('Amount of item :', amount[0])
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)
    print('Run time: ', endtime-starttime)


if __name__ == '__main__':
    main()
