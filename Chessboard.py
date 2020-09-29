#https://repl.it/repls/HappyBisqueCarat#main.py

import numpy as np
import random  
from random import randint
import math
 #!/usr/bin/python import signal signal.signal(signal.SIGINT, signal.SIG_IGN) signal.signal(signal.SIGTSTP, signal.SIG_IGN) 
 #! -*- coding: utf-8 -*-


# Создание матрицы чисел (массив массивов чисел) размером *size* x *size*
# Возвращает созданную матрицу
def createMatrix(size):
  matrix = []

  for i in range(size):
      matrix.append([])
      for j in range(size):
          matrix[i].append(random.randint(0,100))

  return matrix

# Вывод матрицы *matrix* в консоль в виде шахматной доски
def printPrettyMatrix(matrix):
  print("     %s" % 'A   B   C   D   E   F   G   H')

  for row in range(len(matrix)):
    print(row+1, end=" |")

    for col in range(len(matrix[row])):
      print("%3d" % matrix[col][row], end=" ")
    print()

# Просит пользователя ввести координаты начала и конца диагонали
# Возвращает массив, состоящий из координат этих двух точек, например ['A1', 'H8']
def inputCoordinate1():
  print('Начало диагонали: Введите сначала координату столбца, затем строки:')
  try:
    cr1 = input()
  
  except Exception: 
    cr1 = input()
    return cr1
  except KeyboardInterrupt: 
    cr1 = input()
    return cr1
  except EOFError:
    cr1 = input()
    return cr1
  except TypeError:
    cr1 = input()
    return cr1
  except NameError:
    cr1 = input()
    return cr1
  except IndexError:
    cr1 = input()
  else:  
    return cr1

def inputCoordinate2():
  print('Конец диагонали: Введите сначала координату столбца, затем строки:')
  try:
    cr2 = input()
  except KeyboardInterrupt: 
    cr2 = input()
    return cr2
  except IndexError:
    cr2 = input()
    return cr2
  except EOFError:
    cr2 = input()
    return cr2
  except TypeError:
    cr2 = input()
    return cr2
  except NameError:
    cr2 = input()
    return cr2
  else:  
    return cr2
  




# Проверка координат на диапазон
def validateRange(coordi):
  c = [coordi]
  letters = ['A','B','C','D','E','F','G','H']
  numbers = ['1','2','3','4','5','6','7','8'] 
  
  usercoordi = c[0]
  letter = usercoordi[0]
  number = usercoordi[1:] 

  if (letter in letters and number in numbers): 
    return True
  else:
    return False 

def inputCoordinates(coordinate1, coordinate2):
  coor1 = coordinate1
  coor2 = coordinate2
  return [coor1, coor2]
# Переводит массив userCoordinatesArray (массив координат точек, введенных пользователем) в числовые
# Возвращает полученный массив числовых координат
# Например ['A1', 'H8'] -> [(0,0), (7,7)]
def transformUserCoordinatesToDigits(userCoordinatesArray):
  letterMap = {'A': 0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7} 
  numberMap = {'1': 0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7}

  result=[]

  for i in range(len(userCoordinatesArray)):
    coordinate = userCoordinatesArray[i] 
    
    transformed = (
      letterMap.get(coordinate[0]),
      numberMap.get(coordinate[1])
    )

    result.append(transformed)
  return result

# Проверка принадлежности числовых координат к одной диагонали
def validateCoordinates(coordinates):
  col_1 = coordinates[0][0]
  row_1 = coordinates[0][1]

  col_2 = coordinates[1][0]
  row_2 = coordinates[1][1]
  
  if ((row_2 - row_1) == (col_2 - col_1)):
    return True
  elif ((row_2 - row_1) == -(col_2 - col_1)): 
    return True
  else:
    return False

 

# Возвращает массив координат значенией на диагонали

def findDiagonalCoordinates(coordinates):
  diagonal = []

  col_1 = coordinates[0][0]
  row_1 = coordinates[0][1]

  col_2 = coordinates[1][0]
  row_2 = coordinates[1][1]

  if (row_1 < row_2):
    if(col_2 > col_1):
      for i in range((col_2-col_1) + 1 ):
        column = col_1 + i
        row = row_1 + i 
        
        diagonal.append((column, row));
    else:
      for i in range((col_1 - col_2) + 1 ):
        column = col_1 - i
        row = row_1 + i  
        diagonal.append((column, row)); 
  elif (row_1 > row_2): 
    if(col_1 > col_2):
      for i in range((col_1-col_2) + 1):
        column = col_1 - i
        row = row_1 - i 
        diagonal.append((column, row));
    else:
      for i in range((col_2-col_1) + 1):
        column = col_1 + i
        row = row_1 - i  
        diagonal.append((column, row));
  else:
    column = col_1
    row = row_1
    diagonal.append((column, row));
  return diagonal




# Возвращает массив координат значенией на диагонали между точками из массива coordinates (координат начальной и конечной точки)
# [(0,0), (7,7)] -> [3, 76, 2, 77, 98, 53, 29, 80]

def transformDiagonalCoordinatesToNumbers(matrix, diagonalCoordinates):
  diagonalNumbers = []  

  for i in range(len(diagonalCoordinates)):
    col = diagonalCoordinates[i][0]
    row = diagonalCoordinates[i][1]
    diagonalNumbers.append(matrix[col][row])

  return diagonalNumbers

  #return [3, 76, 2, 77, 98, 53, 29, 80]
  
def quicksort(nums):
  if len(nums) <= 1:
      return nums
  else:
      q = random.choice(nums)
      s_nums = []
      m_nums = []
      e_nums = []
      for n in nums:
          if n < q:
              s_nums.append(n)
          elif n > q:
              m_nums.append(n)
          else:
              e_nums.append(n)
      return quicksort(s_nums) + e_nums + quicksort(m_nums)

def setValuesToMatrix(matrix, coordinates, values):
  
  for index in range(len(coordinates)):
    col = coordinates[index][0]
    row = coordinates[index][1]  
    matrix[col][row] = values[index]


  return matrix

# Зануляет все числа матрицы matrix кроме стоящих на заданной диагонали
# diagonalCoordinates - координаты точек, значения которых НЕ нужно занулять
def setZeroes(matrix, diagonalCoordinates):
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      if (col, row) not in diagonalCoordinates:
        matrix[col][row] = 0
  return matrix

##############################################################

# 1. Создание матрицы
matrix = createMatrix(8)

# 2. Печать матрицы в консоль в виде шахматной доски
prettymatrix = printPrettyMatrix(matrix)


areCoordinatesValid = False
while areCoordinatesValid == False:
  #3. Вввод пользователем координат:
  #Ввод первой координаты  
  chr1 = inputCoordinate1()
  #Проверка первой координаты
  areCoordinatesValid = validateRange(chr1)
  print(areCoordinatesValid)
  if (areCoordinatesValid == False):
    continue
  #Ввод второй координаты 
  areCoordinatesValid = False
  while areCoordinatesValid == False:
    chr2 =inputCoordinate2()
  #Проверка второй координаты
    areCoordinatesValid = validateRange(chr2)
    if(areCoordinatesValid == False):
      continue 
    print(areCoordinatesValid)
    userCoordinates = inputCoordinates(chr1, chr2)
    print (userCoordinates)
  
  # 5. Преобразование пользовательских координат в числовые
  startAndFinishPointDigitCoordinates = transformUserCoordinatesToDigits(userCoordinates)
  # 6. Проверка принадлежности числовых координат к одной диагонали
  areCoordinatesValid = validateCoordinates(startAndFinishPointDigitCoordinates)
  

print(startAndFinishPointDigitCoordinates)

# 7. Составление координат диагонали
coordinatesOfDiagonal = findDiagonalCoordinates(startAndFinishPointDigitCoordinates)

# 8. Вывод координат диагонали на экран.
print('Координаты диагонали: ', coordinatesOfDiagonal)
######
# 9. Вывод значений на диагонали
numbers = transformDiagonalCoordinatesToNumbers(matrix, coordinatesOfDiagonal)
print('Значения на диагонали: ', numbers)



# 9. Сортировка значений на диагонали
sortedDiagonalValues = quicksort(numbers) # массив значений

# 10. Вывод отсортированной диагонали на экран
print('=================')
print('Отсортированные значения на диагонали: ', sortedDiagonalValues)

# 11. Заполнение матрицы отсортированными значениями
matrix = setValuesToMatrix(matrix, coordinatesOfDiagonal, sortedDiagonalValues)

# 12. Обнуление значений матрицы, лежащих вне диагонали
arr = setZeroes(matrix, coordinatesOfDiagonal) # нужно передать массив координат

# 13. Вывод результата на экран
printPrettyMatrix(matrix)
