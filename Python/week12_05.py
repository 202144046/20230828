# p.377

list_score = [10, 20, 30, 40, 50, 60]

while True:

    try:

        # 실행하고자 하는 코드
        
        number1 = input("분자:")
        number1 = int(number1)

        number2 = input("분모:")
        number2 = int(number2)

        result = number1 // number2
        print(result)

        print(list_score[result])
        break

    except:

        # try에서 실행한 코드가 오류가 나면 여기로 점프

        print("예외가 발생하였습니다.")
        print("비정상 종료")

print("전체 종료")

