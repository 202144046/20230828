import os

path_name = "c:/202144046"
full_filename = path_name + "/list.txt"

if os.path.isfile(full_filename):
    f = open(full_filename, "r")

    result = []

    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        datas = line.split(",")

        if len(datas) == 4:
           result_dic = {}
           result_dic['이름(name)'] = datas[0]
           result_dic['국어점수(kor)'] = datas[1]
           result_dic['영어점수(eng)'] = datas[2]
           result_dic['수학점수(mat)'] = datas[3]
           result.append(result_dic)

    f.close()

    for result_dic in result:
        st_name = result_dic['이름(name)']
        st_kor = int(result_dic['국어점수(kor)'])
        st_eng = int(result_dic['영어점수(eng)'])
        st_mat = int(result_dic['수학점수(mat)'])
        st_avg = round((st_kor + st_eng + st_mat) / 3, 2)
        print(f"이름:{st_name} 국어:{st_kor} 영어:{st_eng} 수학:{st_mat} 평균:{st_avg:.2f}")




