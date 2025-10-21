def retu_arr(start, end):
    rr = []
    for i in range(start, end + 1):
        rr.append(i)
    return rr


class my_setting:

    pltcsv = "./plt_csv/"
    ratio = "" # ""
    course_file_name = "courses_pe/courses_84"#  "userdata"

        #"courses_pe/courses_84"


    # 'userdata'  # './courses_pe/courses_146' # 'courses_3.csv' #
    friendship_file_name =  "s1d"
    # "frn"


    # "s1d"  # "./friendships/f177_3" # "frn.csv" #

    algo_list = [

       # "RO-FDA-RR"


         "SO-FDA-RR",  "RO-FDA-RR", "UBO-FDA-RR", "FCO-FDA-RR",
         "SO-FDA-BF",  "RO-FDA-BF", "UBO-FDA-BF", "FCO-FDA-BF",

        
          "SO-SA-RR", "RO-SA-RR", "UBO-SA-RR", "FCO-SA-RR",
          "SO-SA-BF", "RO-SA-BF", "UBO-SA-BF","FCO-SA-BF" ,

         "SO-DA-RR", "RO-DA-RR", "UBO-DA-RR", "FCO-DA-RR",
         "SO-DA-BF", "RO-DA-BF", "UBO-DA-BF", "FCO-DA-BF",



        #"SO-FDA-RR", "RO-FDA-RR", "UBO-FDA-RR", "SO-FDA-BF", "RO-FDA-BF", "UBO-FDA-BF",
    ]

    bundle_list = [1,2,3]  # ,2,3]#,2,3]  #1,2,3
    M=9
    # [ i for i in range(20,136) ]
    # [20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135

    #bigarr = [20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135]  # [ i for i in range(10,60) ] # [10,15,20,25,30,35,40,45,50,55,60]

    limit_list = range(10, 85) # bigarr  # [60] # [40,45,50,55] #[60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130,135] # course max size
    # [20,25,30,35,40,45,50,55,60] #
    # 20,25,30,35, 40,45,50,55,60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130,135
    # 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130,135
    # 20, 25, 30, 35, 40, 45, 50, 55,
    w_list = [0, 1, 2, 3, 4, 5]  # ,1,2,3,4,5] #0, 1, 2, 3, 4, 5]  # []  #0, 1, 2, 3, 4, 5
    detarmine_is_deadlock_after_x_cycles = 100

    # , 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125
    # 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95,
    N_values = [84] # 8

    #177]  # bigarr # [177]#  20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95,  100, 105, 110, 115, 120, 125]
    #  20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125
    #  20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125,

    k = 100 # 50
    run_exp_on_q2 = True
    plot_in_stick_form = False
    showlog = False
    showGiniStd = False
    show_diffrent_by_cycle = False

    numberofcourse_perstudent = 3

    print_big_excel_file = True

    free_scale_graph_mode = False
