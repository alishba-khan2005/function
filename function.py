#1
def city(city,country="pakistan"):
    print(city,"is in ",country)
city("Karachi",)
city("Canberra")
city("Tokyo","Japan")



#2
def fav_book(title):
    print("my favourite book is ",title)
fav_book("alice in the wonderland")




#3
def gcd(a,b):
    if a>b:
        min=b
    else:
        min=a
    for i in range(1,min+1):
        if a%i==0 and b%i==0:
            hcf=i
    print("the hcf is ",hcf)
gcd(16,8)


#4
def three_int(a,b,c):
    if a>b and a>c:
        max=a
    elif b>a and b>c:
        max=b
    else:
        max=c
    print("the max is ",max)
three_int(3,65,76)