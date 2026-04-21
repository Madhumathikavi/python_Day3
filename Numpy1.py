import numpy as np
marks = np.array([45, 67, 89, 32, 76])
print("Total students:", len(marks))
pass_students = marks[marks>=50]
print("pass students:", pass_students)
print("Number of pass students:", len(pass_students))
fail_students = marks[marks<50]
print("fail students:", fail_students)
print("Number of fail students:", len(fail_students))
average =marks.mean()
print("Average marks:",average)
Max_marks = marks.max()
print("Maximum marks:",Max_marks)
Min_marks = marks.min()
print("Minimum marks:",Min_marks)
