# p.240

fruits = ["딸기", "귤", "키위", "키위", "키위", "복숭아"]

target = "키위"
while target in fruits:
    fruits.remove(target)

    print(fruits)
    print()

i = 0
while i < len(fruits):
    print(f"{i+1} 순위 {fruits[i]}")
    i+=1
    print()




# for i in range(len(fruits)):
    # print(f"{i+1} 순위 {fruits[i]}")
    # print()

infos = {
    "123" : ["김인하", 22],
    "124" : ["김인하", 21]
}

print("학생 검색 시스템")
number = input("학번:")
if number in infos:
    print(infos[number])

print("학생 검색 시스템")
while True:
    number = input("학번:")
    if number in infos:
        print(f"이름:{infos[number][0]}")
        break
    else:
        pass # continue
    print("학번을 다시 입력하시오")

print("학생 검색 시스템")
while True:
    number = input("학번:")
    if not (number in infos):
        print(f"이름:{infos[number][0]}")
        break
    else:
        yesorno = input("계속할래? (Y,N)")
        if yesorno.upper() == "Y":
        pass
        else:
        break
    print("학번을 다시 입력하시오")

print("학생 검색 시스템")
while True:
    number = input("학번:")
    if number in infos:
        print(f"이름:{infos[number][0]}")
    else:
        print("그런 애 없다")

        yesorno = input("계속할래? (Y,N)")
        if yesorno.upper() != "Y":
            break

