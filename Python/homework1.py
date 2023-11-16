import os

path_name = "c:/202144046"
full_filename = path_name + "/list.txt" # 저장할 파일의 전체경로

if not os.path.isdir(path_name):
    os.mkdir("path_name")

f = open