from RSD import vector_sha
from RSD_INNER import generate_permutation, RSD_round, legal_sol
from evulation_function import total_courses_value
from print_graph_capacity import gini
from setting import my_setting
from solution_functions import create_tab
import matplotlib.pyplot as plt

def print_graph(name,data,fold):
    x_values = [point[0] for point in data]
    y_values = [point[1] for point in data]
    # יצירת הגרף
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue')
    plt.title(name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    # שמירת הגרף כקובץ PNG
    #plt.show()
    #plt.plot()
    plt.savefig(fold + name + ".png", dpi=300)
    plt.close()
    #exit()



def meta_round( lim, N, M, w_factor, HBS, runDOA, sameOrder, bundle, rp, algname):
    print(algname, " cap ", str(lim))
    total_cnt = 0
    seats_left = lim * M
    sol = create_tab(N, M)
    rounds = 0
    change_courses = "DA-" in algname  # "(HBS or runDOA or my_setting.run_exp_on_q2)
    #print(" change_courses ", change_courses)
    skipNumber = 0
    student_in_course = []
    for i in range(M):
        student_in_course.append(0)
    Tr = []
    shalist = []

    TARGET_TREE=[] # GO BACK AND FORTH TO INCREASE UTILITY OR DEC GINI

#seats_left > 0 and
    while rounds < my_setting.detarmine_is_deadlock_after_x_cycles:
        Tr.append([sol, skipNumber, student_in_course, total_cnt, seats_left, rp, rounds])
        sol, skipNumber, student_in_course, total_cnt, seats_left, rp, rounds = RSD_round(rounds, sol, lim, N, M,
                                                                                          w_factor, HBS, runDOA,
                                                                                          sameOrder, bundle,
                                                                                          change_courses,
                                                                                          student_in_course,
                                                                                          seats_left, total_cnt,
                                                                                          False, rp, algname)
        shasol = vector_sha(sol).hexdigest()
        if shasol in shalist:
            print(" algorithm end by sha memory Loop at ",shasol)
            break
            # is a loop
        SUM_SOL = total_courses_value(sol, N, w_factor)
        shalist.append( shasol)
        TARGET_TREE.append([shasol,sum(SUM_SOL),gini(SUM_SOL)])
        print(" round ", rounds, " ", shasol," utility ",sum(SUM_SOL))


    if 0:
        tt=[]
        tt2=[]
        i=1
        for t in TARGET_TREE:
            tt.append([i,t[1]])
            tt2.append([i,t[2]])
            i+=1
        print_graph(algname+"_"+str(lim)+"_"+str(N)+"_"+str(w_factor)+"_"+my_setting.ratio,tt,"./improve_graph/")
        print_graph(algname+"_"+str(lim)+"_"+str(N)+"_"+str(w_factor)+"_"+my_setting.ratio,tt2, "./improve_graph2/")


    #print(Tr)
    #print(TARGET_TREE)
    #exit()
    return sol, legal_sol(sol, lim), rounds