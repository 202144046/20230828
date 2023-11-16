# p.385

list_score = [10, 20, 30, 40, 50, 60]

try:

    # 실행하고자 하는 코드
    
    number1 = input("분자:")
    number1 = int(number1)

    number2 = input("분모:")
    number2 = int(number2)

    result = number1 // number2
    print(result)

    print(list_score[result])

except ValueError as ex:
    # print(type(ex))
    # print(ex)
    print("정수만 입력하시오.")

except IndexError as ex:
    # 밑에 정보는 보통 로그 파일에 출력한다.
    # print(type(ex))
    # print(ex)
    print("결과가 6 이하가 되게 입력하시오.")

except Exception as ex:
    # 밑에 정보는 보통 로그 파일에 출력한다.
    # print(type(ex))
    # print(ex)
    print("관리자에게 문의 하시오.")

