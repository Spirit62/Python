""" Welcome to Mini School Management System """


student_details=[#{"id":1,"name":"ram","mark":77},
                 #{"id":2,"name":"hari","mark":89}
                 ]


while True:
        
    print("Choose a number from 1 to 5\n")
    print("1. Add Student\n2. View Student\n3. Passed Student\n4. Failed Student\n5. Exit\n")

    choice=int(input("Enter your choice"))

    match choice:
        case 1:
            id= int(input("Enter the Student ID"))
            name=input("Enter the name of student:")
            mark=float(input("Enter the mark of the Student"))



            studentadd={
                "id":id,
                "name":name,
                "mark":mark
            }

            student_details.append(studentadd)
            print("Student Added Successfully")


        case 2:
            print("Id\tName\tMark")

            for i in student_details:
                print(f"{i['id']}\t{i['name']}\t{i['mark']}")


        case 3:
            passed=0
            for i in student_details:
                if i["mark"]>=40:
                    print(i["name"])
                    passed=passed+1
            print(f"The total no of passed students are:{passed}")

        case 4:
            failed=0
            for i in student_details:
                if i["mark"]<40:
                    print(i["name"])
                    failed=failed+1
            print(f"The total no of Failed students are:{failed}")
        case 5:
            print("Thank you for using Mini Studement Management System")