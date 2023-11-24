# studentpy
class Student1:
    pass


class Student2:
    def __init__(self) -> None:
        pass


class Student3:
    def __init__(self) -> None:
        self.name = ""
        self.number = ""
        self.major = ""


class Student4:
    def __init__(self, name, number, major="") -> None:
        self.name = name
        self.number = number
        self.major = major

    def __str__(self) -> str:
        return f"{self.name}/{self.number}/{self.major}"


#score.py

class Score1:
    def __init__(self) -> None:
        self.kor = 0
        self.eng = 0
        self.math = 0


class Score2:
    def __init__(self, kor=0, eng=0, math=0) -> None:
        self.kor = kor
        self.eng = eng
        self.math = math


class Score3:
    def __init__(self, kor=0, eng=0, math=0) -> None:
        self.scores = dict()
        self.scores["kor"] = kor
        self.scores["eng"] = eng
        self.scores["math"] = math

    def __str__(self) -> str:
        if len(self.scores) > 0:
            avg = sum(self.scores.values()) / len(self.scores)
            return f"평균:{avg:0.1f}"

        return "0"
    
class Score4:
    # * 가변 매개변수 => List
    def __init__(self, *scores) -> None:
        self.scores = dict()
        for score in scores:
            self.scores[score] = 0

    def __str__(self) -> str:
        if len(self.scores) > 0:
            avg = sum(self.scores.values()) / len(self.scores)
            return f"평균:{avg:0.1f}"

        return "0"    
    
class Score5:
    # ** 키워드 가변 매개변수 => dic
    def __init__(self, **scores) -> None:
        self.scores = scores

    def __str__(self) -> str:
        if len(self.scores) > 0:
            avg = sum(self.scores.values()) / len(self.scores)
            return f"평균:{avg:0.1f}"

        return "0"    
    

# 절차지향 : C언어 (기능 <-> 데이터)
# 객체지향 : C++, Python, Javascript, Java, C#,....
#           (기능 + 값) => class

class Score:
    def __init__(self, **scores) -> None:
        self.scores = scores

    def add_subject(self, subject, score=0):
        if None == self.scores.get(subject):
            self.scores[subject] = score
            return True
        return False

    def get_average(self):
        s = sum(self.scores.values())
        l = len(self.scores)

        if l == 0:
            return 0.0
        else:
            return s / l

    def __str__(self) -> str:
        if len(self.scores) > 0:
            return f"평균:{self.get_average:0.1f}"

        return "0"
    
