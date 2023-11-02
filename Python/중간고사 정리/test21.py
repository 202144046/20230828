def add_dict(stdict,stname,stscores):
    
    if stname in stdict:
        return False
    else:
        stdict[stscores] = stname
        return True


scores = {"kim":95, "lee":65}

if add_dict(scores, "park", 100):

    print("입력 완료")

else:
    print("동일 학생 있음")

if add_dict(scores, "kim", 100):

    print("입력 완료")

else:
    print("동일 학생 있음")

