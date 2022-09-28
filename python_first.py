name = input('Введите ваше имя:')
surname = input('Введите вашу Фамилию:')
age = int(input('Введите ваш возраст:'))
weight = int(input('Введите ваш вес:'))

if age <= 30 and weight>=50 and weight<=120:
    print('Пациент в хорошем состоянии')
elif age > 30 and age <=40 and (weight <=50 or weight>=120):
    print('Пациенту требуется заняться собой')
elif age > 40 and (weight <=50 or weight>=120):
    print('Пациенту требуется врачебный осмотр')

X = int(input())
H = int(input())
M = int(input())
N = (H*60) + M + X
print (N // 60)
print (N % 60)

a = True
b = False
a and b or not a and not b

A = int(input())
B = int(input())
H = int(input())
if A <= B and A <= H < B:
    print('Это нормально')
elif A>H:
  print('Недосып')
else: 
  print('Пересып')

N = int(input())
if 1900 <= N <= 3000 and ((N % 4 == 0) and (N % 100 != 0 or N % 400 == 0)):
  print('Високосный')
else:
  print('Обычный')

a = int(input())
b = int(input())
c = int(input())
p = ((a+b+c)/2)
print((p*(p-a)*(p-b)*(p-c))**0.5)

x = int(input())
print((-15 < x <= 12) or (14 < x < 17) or (19 <= x))

a = float(input())
b = float(input())
c = input()
if c == '+':
  print(a+b)
elif c == '-':
  print(a-b)
elif c == '*':
  print(a*b)
elif c == 'pow':
  print(a**b)
elif c == '/' and b == 0:
    print('Деление на 0!')
elif c == '/':
    print(a/b)
elif c == 'mod' and b == 0:
    print('Деление на 0!')
elif c == 'mod':
    print(a%b)
elif c == 'div' and b == 0:
    print('Деление на 0!')
elif c == 'div':
    print(a//b)
else:
    print('Не знаю такой функции!')

typ = input('')
if typ == 'треугольник':
  a = int(input())
  b = int(input())
  c = int(input())
  d = ((a+b+c)/2) 
  print((d*(d-a)*(d-b)*(d-c))**0.5)
elif typ == 'прямоугольник':
  a = int(input())
  b = int(input())
  print (a*b)
elif typ == 'круг':
  r = int(input())
  print (3.14*(r**2))
else:
  print('Шо за фигура, не пойму?!')

a=int(input())
b=int(input())
c=int(input())
x=max(a,b,c)
y=min(a,b,c)
print(x)
print(y)
print(a+b+c-x-y)

n=int(input())
if (n % 100) // 10 == 1:
  print(n, 'программистов')
elif (n % 10) == 0 or 9 >= (n % 10) >= 5:
  print(n, 'программистов')
elif (n % 10) == 1:
  print(n, 'программист')
elif (n % 10) == 2 or (n % 10) == 3 or (n % 10) == 4:
  print(n, 'программиста')
else: print(n, 'программистов')

if (x%100)//10==1:
  print (x, 'программистов')
else:
    if 5 <= x%10 <= 9 or x%10==0:
      print (x, 'программистов')
    if x%10 == 1:
      print (x, 'программист')
    if 2 <= x%10 <= 4:
      print (x, 'программиста')

a,b,c,d,e,f = input()
if int(a)+int(b)+int(c)==int(d)+int(e)+int(f):
  print('Счастливый')
else: print('Обычный')

x = int(input())
a = x%10 + (x%100)//10 + (x%1000)//100
b = (x%10000)//1000 + (x%100000)//10000 + (x%1000000)//100000
if a == b:
  print("Счастливый")
else:
  print("Обычный")

c = 0
while c <= 6:
  print ('*' * c)
  c+=1

for i in range(1, 8):
    print('*'*i)

n = int(input())
stars = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'

a = int(input())
s = 0
while a != 0:
  s += a
  a = int(input())
print(s)

a = int(input())
b = int(input())
d = max(a,b)
while d % a != 0 or d % b != 0:
  d+= 1
print(d)

for i in range(1, 8):
    print('*'*i)

#Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
#Для каждого введённого числа проверить:
#если число меньше 10, то пропускаем это число;
#если число больше 100, то прекращаем считывать числа;
#в остальных случаях вывести это число обратно на консоль в отдельной строке.
i = 1
while i > 0:
  i = int(input())
  if i < 10:
    continue
  elif i > 100:
    break
  else:
    print(i)

#Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range (c, d+1):
  print ('\t', i, end='')
print()
for j in range (a, b+1):
    print(j, end='\t')
    for k in range (c, d+1):
      print(j*k, end='\t')
    print()

#Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 33.
a = int(input())
b = int(input())
s = 0
t = 0
for i in range (a, b + 1):
  if i % 3 == 0:
    s += i
    t += 1
print(s/t)

#Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
#Например, в строке "acggtgttat" процентное содержание символов G и C равно \dfrac4{10} \cdot 100 = 40.0  где 4 -- это количество символов G и C,  а 10 -- это длина строки.
genom = input()
g = genom.upper()
a=int(g.count('G'))
b=int(g.count('C'))
c=int(len(g))
x=(a + b)/c *100
print(x)

genom = input()
g = genom.upper()
a=int(g.count('G'))
b=int(g.count('C'))
c=int(len(g))
x=(a + b)/c *100
print(x)

a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        s += i
print(s)

a=input()
x =len(a)
s=1
for i in range(x-1):
  if a[i] == a[i+1]:
    s+=1
  elif a[i] != a[i+1]:
    print(a[i]+str(s),end='')
    s=1
print(a[-1]+str(s))

a=[4,1,9,3]
n=len(a)
for i in range(n):
  print(i, a[i])
print(n)

nums= [int(i) for i in input().split()]
print(sum(nums))

nums= [int(i) for i in input().split()]
s=0
for i in nums:
  s+=i
print(s)

#Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
nums = [int(i) for i in input().split()]
#nums=list([1,3,5,6,10])
n = len(nums)
new=list([0]*n)
if n == 0:
  print(*nums)
elif n==1:
  new=nums
else:
  for i in range(0, n-1):
    new[i]=nums[i-1]+nums[i+1]
  new[n-1]=nums[n-2]+nums[0]
print(*new)

#уникальные записи
my_list1 = [4, 8, 0, 3, 4, 2, 0, 3]
my_list = list(set(my_list1))
print(my_list)

#уникальные записи
a=[4, 8, 0, 3, 4, 2, 0, 3]
b=[]
for i in a:
  if i not in b:
    
print(b)

#Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
a=[int(i) for i in input().split()]
b=sorted(a)
n=len(b)
c=[]
for i in range(n-1):
  if b[i]==b[i+1]:
    c.append(b[i])
print(*list(set(c)))

#Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
a = int(input())
s = a
x = (a**2)
while s != 0:
  a = int(input())
  s += a
  x += (a**2)
print(x)

#Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
s, d = 0, 0
while True:
    a = int(input())
    s += a
    d += a*a
    if s == 0:
        break
print(d)

#Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). 
x=7
s=x+1
for j in range(1, x+1):
  for i in range(j):
    s-=1
    if s > 0:
      print(j, end=' ')

#Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.
lst = [int(i) for i in input().split()]
x = int(input())
n=len(lst)
if lst.count(x) ==0:
  print('Отсутствует')
else:
  for i in range(n):
    if lst[i] == x:
      print(i, end= ' ')

#Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
def f(x):
    if x<= -2:
        return (1-(x+2)**2)
    elif -2<x<=2:
        return -(x/2)
    elif 2<x:
        return(x-2)**2 +1

#Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два.
def modify_list(l):
  lst1=[]
  for i in l:
    if i % 2 ==0:
      lst1.append(int(i/2))
  l.clear()
  l.extend(lst1)

  ###

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

#Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два.
def modify_list(l):
  global lst
  lst1=[]
  for i in lst:
    if i % 2 ==0:
      lst1.append(int(i/2))
  lst.clear()
  lst=lst1

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

#Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.
#Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
#Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].
def update_dictionary(d, key, value):
  if key in d:
    d[key]+=[value]
  elif 2*key in d:
    d[2*key]+=[value]
  else:
    d[2*key]=[value]

######
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}

#Посчитать повторяющиеся слова в Войне и мир
s = input().lower().split()
for i in set(s):
    print(i, s.count(i))

# a aa abC aa ac abc bcd a

#Найти все числа в строке
a='a3b4c2e10b1'
s=0
for y in range(len(a)):
  for i in range(0,9):
    if a[y] == str(i):
      print(a[y])

#Sample Input:a3b4c2e10b1
#Sample Output:aaabbbbcceeeeeeeeeeb
a=input()
let =[]
num = []
for y in range(len(a)-1):
  if a[y].isalpha():
    let.append(a[y])
  elif a[y].isdigit() and a[y+1].isdigit():      
    num.append(a[y]+a[y+1])
  elif a[y].isdigit() and a[y-1].isdigit():      
    continue
  else:
    num.append(a[y])
for y in range(len(a)-2,len(a)):
  if a[y].isdigit() and a[y-1].isdigit():      
    continue
  elif a[y].isdigit(): 
    num.append(a[y])
ab = [let[i]*int(num[i]) for i in range(len(let))]
print(*ab, sep ='', end='')

inf = open('file.txt', 'r') # открытие файла
s1 = inf.readline()  # введение (подходит для 1 строки)
inf.close()

with open('file.txt') as inf: # открытие файла, но не требуется последняя строка
    s1 = inf.readline()

# Построчное чтение файла
with open(r'C:\Users\etimchenko\Desktop\dataset_3363_3.txt') as inf:
    for line in inf:
        line=line.strip()
        print(line)

# Запись файла
with open('txt', 'w') as ouf:
    ouf.write('text\n')
    ouf.write(str(25))

# Чтение файла целиком
s = file.read()

# Чтение файла построчно
s = file.readline()


# Посчитать количество элементов в списке
a=['abc', 'a', 'bcd', 'bc', 'abc', 'bc', 'bcd', 'bcd', 'abc']
new=dict()
for i in a:
    new[i]=int(a.count(i))
print(new)

#Напишите программу, которая выводит самое частое слово в этом тексте и сколько раз оно встретилось.
with open(r'C:\Users\etimchenko\Desktop\dataset_3363_3 (1).txt') as file:
    text = file.read().replace('\n', ' ').lower().split()
import collections

new=collections.Counter(text).most_common()
print(new[0][0], new[0][1])

#popular_word = max(set(text), key=text.count)
#print(popular_word, text.count(popular_word))


#Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#Cчитает среднюю оценку по трём предметам на отдельной строке.
#Считает средние баллы по математике, физике и русскому языку,запись последней строкой.
with open(r'C:\Users\etimchenko\Desktop\dataset_3363_4.txt', 'r', encoding='utf8') as inf:
    text = []
    for line in inf:
        text.append(line.strip().split(';'))
#text =[['Петров','85','92','78'],['Сидоров','100','88','94'],['Иванов','58','72','85']]
for i in text:
    notes = ((int(i[1])+int(i[2])+int(i[3]))/3)
    print(notes)
sum_m, sum_f, sum_r = 0,0,0
for i in text:
    sum_m += int(i[1])
    sum_f += int(i[2])
    sum_r += int(i[3])
print(sum_m/len(text),sum_f/len(text),sum_r/len(text))

#Использование методов
import math

a=float(input())
print(2*math.pi*a)
