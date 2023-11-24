import score as sc

scores = []
scores.append(sc.Score(kor=20, eng=30, math=40))
scores.append(sc.Score(kor=20, eng=30))
scores.append(sc.Score(kor=20, math=40))

for score in scores:
    print(score.get_average())           # 약식
    # print(sc.Score.get_average(score)) # 정식
    # avg = (score.scores.values()) / len(score.scores)
    # print(avg)

score[0].scores["kor"] = 10
print(scores[0].add_subject("kor", 10))
print(scores[0].add_subject("sci", 10))

