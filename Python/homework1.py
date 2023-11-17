import os

path_name = "c:/202144046"
full_filename = path_name + "/list.txt" # 저장할 파일의 전체경로

if not os.path.isdir(path_name):
    os.mkdir(path_name)

f = open(full_filename,'a')
while True:
    st_name = input("이름을 넣어주세요.(종료시:바로엔터) : ")

    if st_name == "":
        break

    st_korean = input("국어 점수:")
    st_english = input("영어 점수:")
    st_math = input("수학 점수:")
        
    f.write(f"{st_name},{st_korean},{st_english},{st_math}\n")


f.close()

