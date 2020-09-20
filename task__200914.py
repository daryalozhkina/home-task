import random
student_marks = []
while True:
    mark = input('Введите оценку: ')
    if mark:
        student_marks.append(mark)
    else:
        break

i = 0
avg_mark = 0
avg_mark += int(student_marks[i])
i += 1
avg_mark /= len(student_marks)
print ('средний балл', avg_mark)

for i in range(1, 5):
    print('подходит')
else:
    print('не подходит')




