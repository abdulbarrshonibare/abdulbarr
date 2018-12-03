
#WHILE-LOOP ASSIGNMENT

x = 1 
while (x<=100):
    print(x)
    x+=1
    if(x%3==0):
        print(x,'fizz')
    elif(x%5==0):
            print(x,'buzz')
    if(x%3==0 and x%5==0):
            print(x,'fizzbuzz')
