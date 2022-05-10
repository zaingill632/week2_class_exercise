#student_dict = {"Zain": "A"}
student_dict={}
name=""
menu=1

while (menu != "0"):
    menu = input("\nPress 1 for search, 2 for add, 3 for delete and 0 to end program: ")
    if (menu == "1"):
        name = input("Enter student name: ")
        if (student_dict):
            print(student_dict.get(name, "No data available for " + name + ", please add student data"))
        else:
            print("No student data available, please add records to start using this program")
    elif(menu == "2"):
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        student_dict[name] = grade
        print("Data has been added")
        print(student_dict)
    elif(menu == "3"):
        name = input("Enter student name: ")
        if (student_dict):
            if(student_dict.get(name, "No data available for " + name + ", please add student data")):
                del student_dict[name]
                print(name + "'s data has been deleted")
        else:
            print("No student data available, please add records to start using this program")
        
    else:
        print("Program ended!")