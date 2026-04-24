student_data={}

def show_option():
    print(''' 
          Enter 1 for entering new students data.
          Enter 2 for identifying top student.
          Enter 3 for identifying weak student
          Enter 4 to check overall performance of the class.
          Enter 5 for the whole list of students
          Enter 6 to Exit.
          ''')

def add_student_data(name,sub_one,sub_two,sub_three):
    student_data.setdefault(name,{})
    student=student_data[name]
    student.setdefault("first_subject",sub_one)
    student.setdefault("second_subject",sub_two)
    student.setdefault("third_subject",sub_three)

def total_marks_of_each_student():
    students_list={}
    
    for key,value in student_data.items():
        total=0
        subjects=value

        for subject_mark in subjects.values():
            total=total+subject_mark
        total=round(total/3)
        students_list.setdefault(key,total)
    return students_list
   

def top_student():
    students_list=total_marks_of_each_student()
    
    maximum=0
    topper=None
    for student_name,student_mark in students_list.items():
         if student_mark > maximum:
             topper=student_name
             maximum=student_mark
    
    return topper

def weak_student():
    students_list=total_marks_of_each_student()
    
    minimum=999
    lower=None

    for student_name,student_mark in students_list.items():
        if student_mark < minimum:
            lower = student_name
            minimum = student_mark
    
    return lower

def overall_performance():
    students_list=total_marks_of_each_student()
    addition_of_all_the_values=0
    length=len(students_list)
    for marks in students_list.values():
        addition_of_all_the_values+=marks

    performance=addition_of_all_the_values/length

    return performance

def overwrite(name,sub_one,sub_two,sub_three):
    student_data[name]["first_subject"]=sub_one
    student_data[name]["second_subject"]=sub_two
    student_data[name]["third_subject"]=sub_three
    

show_option()
selected_number=int(input("Enter the suitable number among the above for the " \
"perticular action by the system\n"))


while selected_number!=6:

    if selected_number==1:

        name=input("Enter the name of the student\n").lower()
        if name in student_data:
            decesion=input("The entered student is already exist!. Do you want to overwrite?").lower()
            if decesion=="yes":
                subject_1_marks=int(input("Enter the marks(expects a integer) of 1st subject of that student\n"))
                subject_2_marks=int(input("Enter the marks(expects a inetger) of 2nd subject of that student\n"))
                subject_3_marks=int(input("Enter the marks(expects a integer) of 3rd subject of that student\n"))
                overwrite(name,subject_1_marks,subject_2_marks,subject_3_marks)
                show_option()
                selected_number=int(input("Enter the suitable number among the above for the " \
                                           "perticular action by the system\n"))
                continue
            else:
                show_option()
                selected_number=int(input("Enter the suitable number among the above for the " \
                                            "perticular action by the system\n"))
                continue
        else:
            subject_1_marks=int(input("Enter the marks(expects a integer) of 1st subject of that student\n"))
            subject_2_marks=int(input("Enter the marks(expects a inetger) of 2nd subject of that student\n"))
            subject_3_marks=int(input("Enter the marks(expects a integer) of 3rd subject of that student\n"))
            add_student_data(name,subject_1_marks,subject_2_marks,subject_3_marks)
    
    elif selected_number==2:
        
        print(f"{top_student()} is the TOPPER 🎉🎉")
    
    elif selected_number==3:
        print(f"{weak_student()}'s mark is lower among all the students in dictionary.")

    elif selected_number==4:
        if overall_performance()>90:
            print(f"Overall performance of the students is very good")
        elif overall_performance()>80:
            print("Overall performance of the students is good")
        elif overall_performance()>60:
            print("Overall performance of the students is average")
        else:
            print("Overall performance of the students is below average")
       
    elif selected_number==5:
        for students in student_data.items():
            print(students,"\n")

    show_option()
    selected_number=int(input("Enter the suitable number among the above for the " \
    "perticular action by the system\n"))