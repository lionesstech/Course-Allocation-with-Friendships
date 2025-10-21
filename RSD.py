import random, hashlib

from itertools import permutations

from matplotlib import pyplot as plt

from RSD_INNER import RSD_round, generate_permutation, legal_sol
from evulation_function import my_loader, total_courses_value, myinnerproduct
from print_graph_capacity import gini, plot_line
from setting import my_setting
from solution_functions import create_tab, copy_sol
import numpy as np


def vector_sha(vector):
    str_vector = ""
    for v in vector:
        str_vector += "," + str(v)
    return hashlib.md5(str_vector.encode('utf-8'))


def weighted_index_selection(values):
    total = sum(values)
    cumulative_sum = 0
    r = random.uniform(0, total)
    for i, value in enumerate(values):
        cumulative_sum += value
        if r < cumulative_sum:
            return i


def ref_by_friendship_prob():
    friendship = my_loader.friendship_file #  read_course_file(False, my_setting.friendship_file_name)
    ssum = None
    N = len(friendship[0])
    for f in friendship:
        if ssum is None:
            ssum = []
            for ff in f:
                ssum.append(ff * 100 + 1)  # so they will not have prob 0
        else:
            for i in range(len(f)):
                ssum[i] += f[i]
    newarr = []
    # vls=[]
    while len(newarr) < N:
        ind = weighted_index_selection(ssum)
        if ind not in newarr:
            newarr.append(ind)
    return newarr


def neg(vec):
    newvec = []
    for i in vec:
        newvec.append(-1 * i)
    return newvec

def dif_by_cycle(sol1,sol2):
    count=0
    for i in range(len(sol1)):
        for i2 in range(len(sol1[i])):
            # print(" i i2",i , " ",i2 , " ",sol1[i][i2], " ",sol2[i][i2])
            if sol1[i][i2] != sol2[i][i2]:
                count+=1
    return  count
    # print(count)
    # exit('')


# add the options to choose all courses for student in is turn ( choose 3 courses)
def RSD(M, N, HBS=False, bundle=1, sameOrder=True, lim=60, w_factor=1, rp=None, showLog=my_setting.showlog, runDOA=False,algname=None):
    total_cnt = 0
    seats_left = lim * M
    sol = create_tab(N, M)
    rounds = 0
    change_courses = "DA-" in algname  # "(HBS or runDOA or my_setting.run_exp_on_q2)
    print(" change_courses " , change_courses)
    skipNumber = 0
    student_in_course = []
    for i in range(M):
        student_in_course.append(0)

    if rp is None:
        rp = generate_permutation(N)

    Tr= []

    shalist=[]
    diffrent_by_cycle=[]

    # skipNumber < N and
    while seats_left > 0 and rounds < my_setting.detarmine_is_deadlock_after_x_cycles:
        Tr.append([sol, skipNumber, student_in_course, total_cnt, seats_left, rp, rounds])
        # lastsol=copy_sol(sol)
        # print(student_in_course)
        sol, skipNumber, student_in_course, total_cnt, seats_left, rp, rounds = RSD_round(rounds, sol, lim, N, M,
                                                                                          w_factor, HBS, runDOA,
                                                                                          sameOrder, bundle,
                                                                                          change_courses,
                                                                                          student_in_course,
                                                                                          seats_left, total_cnt,
                                                                                          showLog, rp,algname)
        if my_setting.show_diffrent_by_cycle:
            diffrent_by_cycle.append( (rounds, N-skipNumber))
                #dif_by_cycle(lastsol,sol))
        shasol = vector_sha(sol).hexdigest()
        # exit(shasol)
        if shasol in shalist:
            print(" algorithm end by sha memory")
            break
            # is a loop
        shalist.append(shasol)
        print(" round ", rounds, " ", shasol)
    # for i in range(len(Tr)):
    #    print(Tr[i])
    # exit()
    if my_setting.show_diffrent_by_cycle:
        print("diffrent_by_cycle N",N , " ",diffrent_by_cycle)
        plot_line(diffrent_by_cycle,algname)
        plt.title(" number of changes by round "+algname + " N="+str(N)+"\n bundle=1, capacity="+str(lim)+ ", w="+str(w_factor))
        plt.legend()
        plt.savefig('./graphs/cycles/by_cycle_'+algname+"_N_"+str(N)+"_cap_"+str(lim)+"_w_"+str(w_factor)+'.png')
        plt.close()
        # plt.show()
        # exit()
    SUM_SOL = total_courses_value(sol, N, w_factor)
    print("gini_val at end is ", gini(SUM_SOL), " value ", sum(SUM_SOL))
    return sol, legal_sol(sol, lim),rounds
