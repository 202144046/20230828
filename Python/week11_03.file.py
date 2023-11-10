# file = open("c:/test_b/test01.txt", "r")

# while True:
#     line = file.readline()
#     if not line:
#         break
#     if line.strip() == "1학년":
#         break
#     print(line.strip())

# file.close()

file = open("c:/test_b/test01.txt", "r")

data = file.read()
print(data)