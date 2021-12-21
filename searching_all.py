print('''\t\t\t1. linear search
            2. sentinel search
            3. binary search
            4. fibonacci search''')
def linear_search():
    n=int(input("enter the number of student"))
    list1=[int(input("enter the roll number of student "))for i in range(n)]
    print(f"students roll numbers are : {list1}")
    search=int(input("enter the roll number for the searching"))
    flag=0
    for i in range(n):
        if(search==list1[i]):
            flag=1
            print(f"roll number {search} attended the training program")
            break
    if(flag==0):
        print(f"roll number {search} not attended the training program")
def sentinel_search():
    n=int(input("enter the number of student"))
    list1=[int(input("enter the roll number of student "))for i in range(n)]
    print(f"students roll numbers are : {list1}")
    search=int(input("enter the roll number for the searching"))
    last=list1[n-1]
    list1[n-1]=search
    i=0
    while(list1[i]!=search):
        i+=1
    list1[n-1]=last
    if(i<n-1) or list1[n-1]==search:
        print(f"roll number {search} attended the training program")
    else:
        print(f"roll number {search} not attended the training program")

def binary_search():
    n = int(input("enter the number of student"))
    list1 = [int(input("enter the roll number of student ")) for i in range(n)]
    print(f"students roll numbers are : {list1}")
    search = int(input("enter the roll number for the searching"))
    flag=0
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(search==list1[mid]):
            flag=1
            print(f"roll number {search} attended the training program")
            break
        elif(search<list1[mid]):
            high=mid-1
        elif(search>list1[mid]):
            low=mid+1
    if(flag==0):
        print(f"roll number {search} not attended training program")

def fibonacci_search():
    n = int(input("enter the number of student"))
    list1 = [int(input("enter the roll number of student ")) for i in range(n)]
    print(f"students roll numbers are : {list1}")
    search = int(input("enter the roll number for the searching"))
    m1=1
    m2=0
    m=m1+m2
    while(m<n):
        m2=m1
        m1=m
        m=m1+m2
    flag=0
    offset=-1
    while(m>1):
        i=offset+m2
        if(list1[i]<search):
            m=m1
            m1=m2
            m2=m-m1
            offset=i
        elif(list1[i]>search):
            m=m2
            m1=m1-m
            m2=m-m1
        else:
            flag=1
            print(f"roll number {search} attended the training program")
            break
    if(flag==0):
        print(f"roll number{search} not attended the training program")

while True:
    ch=int(input("enter your choice :"))
    if(ch==1):
        linear_search()
    elif(ch==2):
        sentinel_search()
    elif(ch==3):
        binary_search()
    elif(ch==4):
        fibonacci_search()
    elif(ch==5):
        break