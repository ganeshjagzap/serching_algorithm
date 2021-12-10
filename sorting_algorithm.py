# practical number 1


se=['karan','jitu','sanket','komal','chhakuli','lalita','virat','ganesh','sagar','abhi','vivek','tejas','vikas','rohit','kiran']
futball=['ganesh','sagar','tejas','vikas','abhi','rohit','virat','jitu']
cricket=['karan','jitu','sanket','komal','chhakuli','lalita','virat','ganesh']
badminton=['vivek','rohit','virat','sagar','kiran','jitu','tejas','chhakuli','sanket']

# list of student who play both cricket and badminton
A=[]
for i in cricket:
    for j in badminton:
        if i==j:
            A.append(i)
print("the se student : ", se)
print("the student who play both cricket and badminton : ",A)

# list of the student who play either cricket or badminton but neither both
B=[]
for i in cricket:
    if i not in badminton:
        B.append(i)
print("the list of the student who play either cricket or badminton ",B)

# list of the student who play neither cricket and nor badminton
C=[]
for i in se:
    if i not in cricket:
        if i not in badminton:
            C.append(i)
print("the student who do not play cricket or badminton : ",C)

# number of student who play cricket and football but not badminton
D=[]
for i in se:
    if i not in badminton:
        D.append(i)
print("the number of student who play cricket and football but not badminton : ",D)









'''
# practical number two


nofstudent = int(input('enter the number of student : '))
subject = input('enter the subject : ')
list1 = []
for i in range(nofstudent):
    marks = int(input('enter the marks of the student : '))
    list1.append(marks)
print(f'the marks of the student : {list1}')

# the average of the student's marks
sum = 0
count = 0
for i in list1:
    sum += i
    count += 1
    avg = sum / count
print(f"the average of the student's marks {avg}")

# the max score of the class
max = 0
for i in list1:
    if max < i:
        max = i
print(f'the maximum score of the clas : {max}')

# the minimum score of the class
min = 100
for i in list1:
    if min > i and i>0:
        min = i
print(f'the minimum score of the class is : {min}')

#the student who are absent for the test

count=0
for i in list1:
    if i==0:
        count+=1
        i+=1
print(f'the number of student who are absent for the test : {count}')
# the maximum frequency of the score
print('most frequent marks :')
count = 0
temp = 0
index = 0
for i in range(0, len(list1)):
    temp = list1.count(list1[i])
    if (temp > count) and list1[i]>0:
        count = temp
        index = i
mostfrequentnumber = list1[index]
print(mostfrequentnumber)
print('marks repeated are', count, 'times')
'''





# practical array operations

from array import *
nofstudent = int(input('enter the number of student : '))
subject = input('enter the subject : ')
arr = array('i',[])
for i in range(nofstudent):
    marks = int(input('enter the marks of the student : '))
    arr.append(marks)
print(f'the marks of the student : {arr}')

# the average of the student's marks
sum = 0
count = 0
for i in arr:
    sum += i
    count += 1
    avg = sum / count
print(f"the average of the student's marks {avg}")

# the max score of the class
max = 0
for i in arr:
    if max < i:
        max = i
print(f'the maximum score of the clas : {max}')

# the minimum score of the class
min = 100
for i in arr:
    if min > i and i>0:
        min = i
print(f'the minimum score of the class is : {min}')

#the student who are absent for the test

count=0
for i in arr:
    if i==0:
        count+=1
        i+=1
print(f'the number of student who are absent for the test : {count}')
# the maximum frequency of the score
print('most frequent marks :')
count = 0
temp = 0
index = 0
for i in range(0, len(arr)):
    temp = arr.count(arr[i])
    if (temp > count) and arr[i]>0:
        count = temp
        index = i
mostfrequentnumber = arr[index]
print(mostfrequentnumber)
print('marks repeated are', count, 'times')









# matrix calculation


row=int(input('enter the number of row : '))
col=int(input('enter the number of col : '))
m=[[int(input()) for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        print(m[i][j],end=" ")
    print()
n=[[int(input()) for i in range(col)]for j in range(row)]
for i in range(row):
    for j in range(col):
        print(n[i][j],end=" ")
    print()

# the addition of the matrix
print("the addition of the matrix m and n is : ")
add=[[int() for i in range(col)]for j in range(row)]
for i in range(row):
    for j in range(col):
        add[i][j]=m[i][j]+n[i][j]
for i in add:
    print(i)

# subtraction of the matrix m and n
print('the subtraction  of the matrix  m and n is ')
sub=[[int()for i in range(col)]for j in range(row)]
for i in range(row):
    for j in range(col):
        sub[i][j]=m[i][j]-n[i][j]
for i in sub:
    print(i)
# the multiplication of the matrix m and n is
print('the the multiplication of the matrix m and n is  ')
# for multiplication first create the null matrix
c=[[ int() for i in range(col)] for i in range(col)]
for i in range(row):
    for j in range(col):
        pass
for i in range(0,len(c)):
    for j in range(0,len(c[0])):
        for k in range(0,len(n)):
            c[i][j]+=m[i][k]*n[k][j]
for i in c:
    print(i)

# transpose
print('the transpose of the matrix m  is : ')
x=[[int() for i in range(col)]for j in range(row)]
for i in range(row):
    for j in range(col):
        pass
for i in range(len(x)):
    for j in range(len(x[0])):
        x[i][j]=m[j][i]
for i in x:
    print(i)




# sparse matrix

# program for creation of the sparse matrix and it's addition and it's transpose
row=int(input('enter the number of rows :'))
col=int(input('enter the number of col :'))
m1 = []
for i in range(row):
    n = []
    for j in range(col):
        n.append(int(input('enter the values in the matix 1')))
    m1.append(n)
for i in range(row):
    for j in range(col):
        print(m1[i][j], end=" ")
    print()

sparse1 = []
sparse2 = []
for i in range(len(m1)):
    for j in range(len(m1[0])):
        if (m1[i][j] == 0):
            pass
        else:
            x = []
            x.append(i)
            x.append(j)
            x.append(m1[i][j])
            sparse1.append(x)
print(sparse1)

m2 = []
for i in range(row):
    x = []
    for j in range(col):
        x.append(int(input('enter the vaues in the matrix 2 :')))
    m2.append(x)
for i in range(row):
    for j in range(col):
        print(m2[i][j], end=" ")
    print()
for i in range(len(m2)):
    for j in range(len(m2[0])):
        if (m2[i][j] == 0):
            pass
        else:
            n = []
            n.append(i)
            n.append(j)
            n.append(m2[i][j])
            sparse2.append(n)
print(sparse2)

# code for addition of the sparse matrix
def add(sparse1, sparse2):
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    print("addition of the sparse matrix 1 and 2 is :")
    for i in range(len(sparse1)):
        for j in range(len(sparse1[0])):
            result[i][j] = sparse1[i][j] + sparse2[i][j]
    print(result)


add(sparse1, sparse2)


def transposeofsparsematrix(sparse1):
    transpose = []
    print("transpose is: ")
    for i in sparse1:
        transpose.append([i[1], i[0], i[2]])
    print(transpose)

print('transpose of the matrix 1 is :')
transposeofsparsematrix(sparse1)
print('transpose of the matrix 2 is:')
transposeofsparsematrix(sparse2)




#practical number 4
balance=0
print('enter your bank transaction : ')
while True:
    s=input()
    if not s:
        break
    data=s.split(' ')
    Type=data[0]
    amount=int(data[1])
    if Type=="d":
        balance+=amount
    elif Type=="w":
        balance-=amount
    else:
        pass
print(f'your current balance is : {balance}')






# string operations


# the word with longest length is
def LongestWord():
    str = []
    n = int(input("How many words are there in the list?"))
    for word in range(0, n):
        element = input("Enter the words: ")
        str.append(element)

    max_len = len(str[0])
    temp = str[0]
    for word in str:
        if (len(word) > max_len):
            max_len = len(word)
            temp = word
    print("The word with maximum length is: ", temp)
    print("its length = ", max_len)
    return str
def Frequency():
    str = input("Enter some string: ")
    dict = {}
    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
def Palindrome():
    str = input("\n Enter some string: ")
    if(str == str[::-1]):
        print("\n The given string is palindrome")
    else:
        print("\n The given string is not palindrome")

def Find_Substr():
    str = input("\n Enter some statement: ")
    word = input("\n Enter the substring to be searched: ")
    for i in range(len(str) - len(word)+1):
        if (str[i:i+len(word)] == word):
            return i
    return 'Not Found'


def OccurWords():
    str = input("\n Enter some statement: ")
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word]+= 1
        else:
            counts[word] = 1
    print(counts)

#Driver code
print("\n Program for String operations")
ch=['1','2','3','4','5']
ans='ch'
while True :
        print("\n 1. To display word with the longest length")
        print("\n 2. To determine the frequency of occurrence of particular character in the string")
        print("\n 3. To check whether given string is palindrome or not")
        print("\n 4. To display index of first appearance of the substring")
        print("\n 5. To count the occurrences of each word in a given string ")
        ch=input("enter your choice : ")
        if ch=='1':
            print(LongestWord())
        elif ch=='2':
            print(Frequency())
        elif ch=='3':
            print(Palindrome())
        elif ch=='4':
            print(Find_Substr())
        elif ch=='5':
            print(OccurWords())
        else:
            break
