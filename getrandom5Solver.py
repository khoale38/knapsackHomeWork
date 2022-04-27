from glob import glob
from traceback import print_tb
from ortools.algorithms import pywrapknapsack_solver
import numpy as np
import time
import os
import glob
import random
from multiprocessing import Pool
exportname = "ouputRandom/"
path = exportname
TIME_LIMIT = 10


def createfolder(dir):
    isExist = os.path.exists(path+dir)
    if not isExist:
        os.makedirs(path+dir)


def writeOutPut(folder, filename, amount, computed_value, total_weight, packed_items, packed_weights, runtime):
    createfolder(folder)
    f = open(os.path.join(exportname, folder+"/"+filename[0:4]+".json"), "w")
    #f.writelines('"File name":'+folder+"/"+filename+",\n")
    f.writelines('"Time limit": '+str(TIME_LIMIT)+",\n")
    f.writelines('"Amount of item": ' + amount+",\n")
    f.writelines('"Total value": ' + str(computed_value)+",\n")
    f.writelines('"Total weight": ' + str(total_weight)+",\n")
    f.writelines('"Packed items": ' + str(packed_items)+",\n")
    f.writelines('"Packed_weights": ' + str(packed_weights)+",\n")
    f.writelines('"Run time": '+str(runtime)+",\n")
    if runtime < TIME_LIMIT:
        f.writelines('"Optimal": true'+"\n")
    else:
        f.writelines('"Optimal": false'+"\n")


def main():
    list5kpDir = []
    rootFolder = 'input/'

    parent_list = os.listdir(rootFolder)

    for child in parent_list:

        N_dir = os.listdir(rootFolder+child)  # input/00Unrelated
        count = 0
        for N in N_dir:
            while count < 5:
                N = random.choice(os.listdir(rootFolder+child))
                R=os.listdir(rootFolder+child+"/"+N)[0]
                kp=random.choice(os.listdir(rootFolder+child+"/"+N+"/"+R))
                run(rootFolder+child+"/"+N+"/"+R+"/"+kp,child+"/"+N+"/"+R,kp)
               
                count = count+1
                


def run(dir, folder, filename):

    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    data = np.loadtxt(dir, dtype=int, skiprows=3)
    amount = np.loadtxt(dir, dtype='str', delimiter='\n')

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
    solver.set_time_limit(TIME_LIMIT)
    computed_value = solver.Solve()
    endtime = time.time()

    packed_items = []
    packed_weights = []
    total_weight = 0

    # print(dir)
    # print('Time limit:', TIME_LIMIT)
    # print('Amount of item :', amount[0])
    # print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    # print('Total weight:', total_weight)
    # print('Packed items:', packed_items)
    # print('Packed_weights:', packed_weights)
    # print('Run time: ', endtime-starttime)

    writeOutPut(folder, filename, amount[0], computed_value,
                total_weight, packed_items, packed_weights, (endtime-starttime))


if __name__ == '__main__':
    main()
