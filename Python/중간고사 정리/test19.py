def avg_score(avg_list):
    if avg_list != None:
        ScoresValue = avg_list.values()
        return sum(ScoresValue) / len(ScoresValue)

scores={"kim":95, "lee":65}

avg=avg_score(scores)

if avg !=None:
    print(f"평균:{avg}")
else:
    print("점수가 없음")
