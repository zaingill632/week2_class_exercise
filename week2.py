#student_dict = {"Zain": "A"}
student_dict={}
name=""
menu=1

def search_name(student_dict):
    name = input("Enter student name: ")
    if (student_dict):
        print(student_dict.get(name, "No data available for " + name + ", please add student data"))
    else:
        print("No student data available, please add records to start using this program")
        
def add_name(student_dict):
    name = input("Enter student name: ")
    grade = input("Enter student grade (for example: A, B, C): ")
    student_dict[name] = grade
    print("Data has been added")
    print(student_dict)
    
def delete_name(student_dict):
    name = input("Enter student name: ")
    if (student_dict):
        if(name in student_dict):
            del student_dict[name]
            print(name + "'s data has been deleted")
            print("Updated data")
            print(student_dict)
        else:
            print(name + "'s data does not exist, please add data")
    else:
        print("No student data available, please add records to start using this program")
    

while (menu != "0"):
    menu = input("\nPress 1 for search, 2 for add, 3 for delete and 0 to end program: ")
    if (menu == "1"):
        search_name(student_dict)
    elif(menu == "2"):
        add_name(student_dict)
    elif(menu == "3"):
        delete_name(student_dict)
    elif(menu == "0"):
        print("Program ended!")
    else:
        print("Please enter a valid option")