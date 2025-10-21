import csv
from setting import my_setting
from solution_functions import print_tab, vector_inner_product, add_vectors, max_vectors


class my_loader:
    course_file = None  # Class Variable
    friendship_file = None
    friendshipmap = None
    friendshipmap_w = None
    frn_o=None


def delete_my_loader():
    my_loader.course_file = None
    my_loader.friendship_file = None
    my_loader.friendshipmap = None
    my_loader.friendshipmap_w = None


def myinnerproduct(vector_a, vector_b):
    vector_c = []
    for i in range(len(vector_a)):
        vector_c.append(vector_a[i] * vector_b[i])
    return sum(vector_c)


tables_store = {}
table_store_frn={}

def load_frn_table(name):
    # print("load friendship file: ", name)
    if name in table_store_frn:
        return table_store_frn[name]["table"],table_store_frn[name]["friendshipmap"],table_store_frn[name]["friendshipmap_w"]

    table = []
    # startlimit=1
    # if True: #"_3" in my_setting.friendship_file_name
    # startlimit=0
    # print(name + ".csv")
    with open(name + ".csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            # if True: # i >= startlimit:
            newline = []
            line = str(line).replace("'", "").replace("[", "").replace("]", "").split(",")
            for l in line:
                newline.append(int(l))
            table.append(newline)

    friendshipmap = []
    friendshipmap_w = []
    for l in table:
        addtofriendshipmap = []
        addtofriendshipmap_w = []
        for i in range(len(l)):
            if l[i] > 0:
                addtofriendshipmap.append(i)
                addtofriendshipmap_w.append(l[i])

        friendshipmap.append(addtofriendshipmap)
        friendshipmap_w.append(addtofriendshipmap_w)
    table_store_frn[name]={}
    table_store_frn[name]["table"]=table
    table_store_frn[name]["friendshipmap"]=friendshipmap
    table_store_frn[name]["friendshipmap_w"]=friendshipmap_w
    return table_store_frn[name]["table"], table_store_frn[name]["friendshipmap"], table_store_frn[name]["friendshipmap_w"]


def load_course_table(name):
    if name in tables_store:
        return tables_store[name]
    table = []
    with open(name + ".csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            # if i >= 1:
            newline = []
            line = str(line).replace("'", "").replace("[", "").replace("]", "").split(",")
            for l in line:
                newline.append(int(l))
            table.append(newline)
    tables_store[name] = table
    return tables_store[name]
    # print("load course file :", name)


def read_course_file(is_courses, name):  # change to courses
    # print(" name ", name)
    if is_courses:

        if True:  # my_loader.course_file is None:
            table = load_course_table(name)
            my_loader.course_file = table
        return my_loader.course_file
    else:

        if True:  # my_loader.friendship_file is None:
            table,friendshipmap , friendshipmap_w = load_frn_table(name)
            my_loader.friendshipmap = friendshipmap
            my_loader.friendshipmap_w = friendshipmap_w
            my_loader.friendship_file = table
            # print(my_loader.friendshipmap)
        return my_loader.friendship_file


def friendship_value(tab, i, tab2, w=1):  # student i

    # print(" user "+str(i))
    friendshipsum = 0
    for i2 in range(len(tab[0])):
        if tab[i][i2] == 1:
            addfriendshipsum = 0
            for i3 in range(len(tab)):
                if tab[i3][i2] == 1:
                    addfriendshipsum += tab2[i][i3] * w
                    # if tab2[i][i3] > 0:
                    # print("user "+str(i3))
            friendshipsum += addfriendshipsum
            # print("friendship sum for course "+str(i2)+ " is "+str(addfriendshipsum))

    return friendshipsum


def total_courses_value(tab, N, w=1, w_2=1):
    tab2 = my_loader.course_file  # read_course_file(True, my_setting.course_file_name)
    frn = my_loader.friendship_file  # read_course_file(False, my_setting.friendship_file_name)

    ssum = []
    for i in range(N):
        #print(len(tab2) , " ", len(tab))
        addsum = vector_inner_product(tab2[i], tab[i])
        addfrn = friendship_value(tab, i, frn, w)
        ssum.append(sum(addsum) * w_2 + addfrn)

    return ssum
