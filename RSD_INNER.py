import random

import numpy as np

from evulation_function import total_courses_value, myinnerproduct, my_loader
from setting import my_setting


def studentValue(sol, student_i, w_factor):
    # print("course file ",my_setting.course_file_name)
    courses = my_loader.course_file  # read_course_file(True, my_setting.course_file_name)
    # print(student_i)

    M = len(courses[student_i])

    myfriend_list = my_loader.friendshipmap[student_i]
    myfriend_list_w = my_loader.friendshipmap_w[student_i]

    addfriendship = []
    for i in range(M):
        addsum = 0
        for t in range(len(myfriend_list)):
            friend_index = myfriend_list[t]

            if sol[friend_index][i] == 1:
                addsum += myfriend_list_w[t] * w_factor
        addfriendship.append(addsum)

    total_value = []
    for i in range(len(courses[student_i])):
        total_value.append(courses[student_i][i] + addfriendship[i])

    # print(student_i, " " ,total_value)
    # exit()
    # print("student ", student_i)
    # print("courses value ", courses[student_i])
    # print("friends ", myfriend_list, " ", myfriend_list_w)
    # print("friendship", addfriendship)
    # print("total_value",total_value)
    return total_value


def generate_permutation(N):
    # numbers = list(range(N))
    # random.shuffle(numbers)
    rndlist = []
    for i in range(N):
        rnd = random.randrange(N)
        while rnd in rndlist:
            rnd = random.randrange(N)
        rndlist.append(rnd)

    return rndlist


def legal_sol(sol, lim):
    for s in sol:
        if sum(s) != 3:
            return False
    ssum = []
    for i in range(len(sol[0])):
        ssum.append(0)
    for i in range(len(sol)):
        for i2 in range(len(sol[i])):
            ssum[i2] += sol[i][i2]
    for s in ssum:
        if s > lim:
            print(s, " > ", lim, " limit")
            return False
    return True


def add_random_to_same_value(indexs, values):
    # for i in indexs:
    # print("*",values[i])
    # print(indexs)

    last_index = None
    pairs = []
    for i in range(len(indexs)):
        if last_index is None:
            last_index = i
        else:
            if values[indexs[i]] != values[indexs[last_index]]:
                # print(last_index,"-",i-1)
                pairs.append([last_index, i - 1])
                last_index = i
            if i == len(indexs) - 1:
                pairs.append([last_index, i])
    newarr = []
    # print(pairs)
    for p in pairs:
        if int(p[0]) == int(p[1]):
            newarr.append(p[0])
            # print(values[indexs[p[0]]])
        else:
            n_arr = []
            for p in range(p[0], p[1] + 1):
                n_arr.append(p)

            n_arr_2 = []
            while len(n_arr_2) < len(n_arr):
                rr = random.randrange(0, len(n_arr))
                i_rr = n_arr[rr]
                if i_rr not in n_arr_2:
                    n_arr_2.append(i_rr)
                    newarr.append(i_rr)

    # print(newarr)
    # for i in newarr:
    # print(i , "  ---- ", values[indexs[i]])
    # exit()
    index_2 = []
    for i in newarr:
        index_2.append(indexs[i])

    return index_2



def addvec(vec,vec2):
    for i in range(len(vec2)):
        vec[i]+=vec2[i]
    return vec

def summat(mat):
    sum=0
    for i in mat:
        sum0=0
        for i2 in i:
            sum0+=i2
        sum += sum0
    return sum

def friendshiporder():
    if my_loader.frn_o is None:
        frn = my_loader.friendship_file
        frn_o=None
        for i in frn:
            if frn_o is None:
                frn_o = i.copy()
            else:
                frn_o=addvec(frn_o,i.copy())

        my_loader.frn_o =frn_o
        #print(sum(my_loader.frn_o) )
        #print(summat(frn))
        #exit()
    return my_loader.frn_o


def RSD_round(rounds, sol, lim, N, M, w_factor, HBS, runDOA, sameOrder, bundle, change_courses, student_in_course,
              seats_left, total_cnt, showLog, rp, algname):
    # print(student_in_course)

    skipNumber = 0

    # print(" round ", rounds)

    # order student by random order and let each chose by greedy choice

    # print("rounds", rounds)

    numberofchanges = 0
    if not "UBO" in algname and not "FBO" in algname:
        if "RO-" in algname:
            if "BF" in algname:
                if rounds % 2 == 0:
                    rp = generate_permutation(N)
            else:
                if True:  # rounds > 0
                    rp = generate_permutation(N)


    else:  # mvo
        HBS = True

        if rounds > 0:
            if (not "BF" in algname) or (rounds % 2 == 0):
                # print(" run mvo ")
                w_factor_send = w_factor
                cours_w = 1
                if "UBO_fn" in algname:
                    cours_w = 0
                if "UBO_cs" in algname:
                    w_factor_send = 0

                if "FBO" in algname:
                    #sol_by_cycle = total_courses_value(sol, N, w_factor_send, cours_w)
                    fr_o = friendshiporder()
                    arrc = []
                    for sbc in range(N):
                        arrc.append([sbc, fr_o[sbc] ] )
                        #, sol_by_cycle[sbc]])


                    #METHOD 4 arrc = sorted(arrc, key=lambda x: (x[2],-x[1], random.random()))
                    arrc = sorted(arrc, key=lambda x: ( -x[1], random.random()))

                    rp = []
                    for kk in arrc:
                        rp.append(kk[0])

                else:
                    sol_by_cycle = total_courses_value(sol, N, w_factor_send, cours_w)  # only friendships
                    # print(sol_by_cycle)
                    # print(np.std(sol_by_cycle))
                    if np.std(sol_by_cycle) > 0:
                        # print(sol_by_cycle)
                        arrc = []
                        for sbc in range(N):
                            arrc.append([sbc, sol_by_cycle[sbc]])
                        # print(arrc)

                        arrc = sorted(arrc, key=lambda x: (x[1], random.random()))

                        rp = []
                        for kk in arrc:
                            rp.append(kk[0])
                        # print(rp)
                        # exit()
                        # rp = np.sort(sol_by_cycle, kind='stable') #[::-1]

                        # rp = add_random_to_same_value(rp, sol_by_cycle)
                    else:
                        rp = generate_permutation(N)
                        # print(np.argsort(sol_by_cycle))
            # exit()

    # print("round" , rounds, " \n ",rp)
    # print(rp)
    # if runDOA:
    # print(rp)
    porder = []
    for i in range(N):

        if "BF" in algname or ("DA-" in algname and not "RR" in algname):
            if rounds % 2 == 0:
                student_i = rp[i]
            else:
                student_i = rp[N - 1 - i]
        else:
            student_i = rp[i]

        # turn of student rp[i]

        if "FDA" in algname:
            courses_per_student = 0
            for i2 in range(M):
                courses_per_student += sol[student_i][i2]
                if sol[student_i][i2] == 1:
                    sol[student_i][i2] = 0
                    student_in_course[i2] -= 1
                    seats_left += 1
            bundle = min(courses_per_student + 1, my_setting.numberofcourse_perstudent)
            #if i == 0:
            #    print("bundle", bundle)

        for b in range(bundle):

            porder.append(student_i)

            # ("student ",str(numberofrrr%my_setting.N_values[0]),str(student_i))

            # remove course hbs
            student_value_arr = studentValue(sol, student_i, w_factor)
            student_value = (myinnerproduct(student_value_arr, sol[student_i]))
            remove_index = -1
            if change_courses and sum(sol[student_i]) == my_setting.numberofcourse_perstudent:
                remove_value = 1000000000000000000000
                for r in range(M):
                    if student_value_arr[r] < remove_value and sol[student_i][r] == 1:
                        remove_value = student_value_arr[r]
                        remove_index = r
                sol[student_i][remove_index] = 0
                student_in_course[remove_index] -= 1
                seats_left += 1
            # remove course hbs

            # student choose best course

            if sum(sol[student_i]) == my_setting.numberofcourse_perstudent and not change_courses:
                skipNumber += 1
            else:

                # student choose course
                student_value_arr = studentValue(sol, student_i, w_factor)
                max_student_value = student_value
                student_choice = -1
                for i2 in range(M):
                    if (student_in_course[i2] < lim) and (sol[student_i][i2] == 0):
                        student_value2 = student_value + student_value_arr[i2]
                        if student_value2 >= max_student_value:
                            max_student_value = student_value2
                            student_choice = i2
                # student choose course

                if student_choice > -1:

                    sol[student_i][student_choice] = 1
                    student_in_course[student_choice] += 1
                    total_cnt += 1
                    seats_left -= 1
                    if remove_index == -1:
                        if my_setting.showlog:
                            print(total_cnt, " student", student_i, " choose course number ", student_choice)

                    if remove_index > -1:
                        if student_choice == remove_index:
                            if my_setting.showlog:
                                print("HBS student didn't change choice")
                            skipNumber += 1
                        else:
                            if my_setting.showlog:
                                print("HBS student change course ", remove_index, " to ", student_choice)
                else:
                    skipNumber += 1
    # print(porder)
    rounds += 1
    return sol, skipNumber, student_in_course, total_cnt, seats_left, rp, rounds
    # student choose best course
    # turn of student rp[i]
