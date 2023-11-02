def get_students(students_list):
    if students_list != None:
        return students_list.keys()
    else:
        return []





scores={"kim":95, "lee":65}

students = get_students(scores)

if students:
    students = ",".join(students)
    print(f"명단:{students}")
else:
    print("학생이 없음")
