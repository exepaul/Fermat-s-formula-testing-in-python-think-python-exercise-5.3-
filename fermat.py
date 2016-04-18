def fermat():
    print("enter any no")
    a=int(input())
    b=int(input())
    c=int(input())
    n=int(input())

    if  c**n == (a**n)+(b**n):
       print("found")
    else:
       print("no wrong")

fermat()



#try with 0,0,0,3 :)
