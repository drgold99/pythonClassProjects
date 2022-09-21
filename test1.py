num=int(input("type a number?"))
while num!=1:
    #if odd 3x+1
    if num%2==1:
        num=num*3+1
        print(num)
    #if odd divid by 2
    elif num%2==0:
        num=num/2
        print(num)