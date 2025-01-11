# Mark_student .08.01
import random
# Список учеников
students=['Надя','Ваня','Вова','Лена']
students.sort()
#Список предметов
classes=['математика','русский язык','физика']
#Пустой словарь с оценками по каждому предмету
students_marks={}
for student in students:
   students_marks[student]={}
   for classe in classes:
      marks=[random.randint(1,5) for i in range(3)]
      students_marks[student][classe]= marks  #Выводим получиывшийся словарь с оценками
      print(f'''{student}-{students_marks[student]}''')
   for student in students:
           print('''Список команд:
            1. Добавить оценки ученика по предмету
            2.Вывести средний балл по всем ученикам
            3.Вывести все оценки по всем ученикам
            4.Редактировать оценку
            5.Удалить оценку
            6.Добавить нового ученика
            7.Добавить новый предмет
            8.Удалить ученика 
            9.Удалить предмет
            10.Вывести средний балл ученика
            11.Вывести все оценки ученика
            12.Выход из программы''')


while True:
               command=int(input('Введите команду:')) 
#Если данные  введены верно
               if command == 1:
                 print('1.Добавить оценку ученика по предмету')
                 student=(input('Введите имя ученика:' ))
                 classe=(input('Введите предмет: '))
                 mark=int(input('Введите оценку: '))
                 if student in students_marks.keys() and classe in students_marks[student].keys():
                      students_marks[student][classe].append(mark)#Добавляем новую оценку
                      print(f'Для {student } по предмету {classe} добавлена оценка  {mark}')
                 else:#Неверные данные
                   print('Ошибка:неверное имя ученика или название предмета')   
               elif command ==2: 
                      print('2.Ввести средний балл по всем ученика:' )
                      for student in students:
                       if student in students_marks.keys() and classe in students_marks[student].keys():  
                          marks_count=len(students_marks[student][classe]) # выводим средний балл  
                          marks_sum=sum(students_marks[student][classe])
                          print(f'{student}-{classes}:{marks_sum//marks_count}')    
               elif command == 3:
                    print('3.Вывести все оценки по всем ученикам')
                    for student in student:
                     print(student)
                     for classe in classes:
                        print(f'\t{students_marks}')
                        print()
               elif command == 4:
                    print('4.Исправить оценку ученика по предмету')
                    student=(input('Введите имя ученика:'))
                    classes=(input('Введите предмет:'))   #Редактирование оценки
                    mark=int(input('Введите оценку которую нужно исправить:'))
                    new_mark=int(input('Введите оценку на которую нужно исправить:'))
                    def edit_mark(student, subject, index, new_mark): mark[student][subject][index] = new_mark
                    print(f'''Оценка {mark}  ученика  {student}  по предмету {classes}  исправлена на {new_mark}''') 
               elif command ==5: 
                    print('4.Удалить оценку:')
                    student=input('Введите имя ученика у которого нужно удалить оценку:')
                    classe=input('Введите предмет по которому нужно удалить оценку:')
                    print(f'''{student} оценки по :{classe}{marks}''')
                    delete_mark=int(input('Введите оценку которую нужно удалить:'))
                    for student in students:
                      for classe in classes:
                         for mark in marks:
                            if student in students_marks.keys() and classe in students_marks.keys():
                              if delete_mark in students_marks[student][classe]:students_marks[student][classe].remove(delete_mark)
                            print(f''''У ученика {student} по предмету {classe} оценка {delete_mark} удалена''''') 
               elif command==6:
                    print('6.Добавить нового ученика')
                    new_student=input('Введите имя нового ученика :')
                    if student in students:
                     students.append(new_student)
                     print(f'Новый ученик {new_student} добавлен в списки учеников')
                     print(students)
               elif command==7:
                    print('7.Добавить новый предмет ')
                    new_classe=input('Введите новый предмет ')
                    if classe in classes:
                      classes.append(new_classe)
                      print(f'''Новый предмет {new_classe} добавлен в список предметов''') 
                      print(classes)
               elif command==8:
                  print('8.Удалить ученика')
                  student_delete=input('Введите имя ученика которого нужно удалить:')
                  if student in students:
                     students.remove(student_delete)
                     print(f'Ученик {student_delete} удален')
                     print(students)
               elif command==9:
                  print('9.Удалить предмет из списка')
                  classe_delete=input('Введите предмет который нужно удалить из списка:')
                  if classe in classes:
                     classes.remove(classe_delete)
                     print(f'Предмет {classe_delete} удален из списка предметов')
                     print(classes)
                elif command==10:
                  print('10..Вывести средний балл ученика')
                  student=input('Введите имя ученкика:')
                  if student in students:
                       if student in students_marks.keys() and classe in students_marks[student].keys():  
                          marks_count=len(students_marks[student][classe]) # выводим средний балл  
                          marks_sum=sum(students_marks[student][classe])
                          print(f'''Ученик {student} по предметам -{classes}Имеет средний балл:{marks_sum//marks_count}''') 
                  else:
                   print(f"Ученик с именем {student} не найден.")      
               elif command==11:
                  print('11.Вывести все оценки ученика:') 
                  student=input('Введите имя ученика:')
                  if student in students_marks:
                    print(f"Оценки {student}:")
                    for subject, grades in students_marks[student].items():
                     print(f"  {subject}: {grades}")
                  else:
                   print(f"Ученик с именем {student} не найден.")
               elif command==12:
                  print('12.Выход из программы')
                  break 

