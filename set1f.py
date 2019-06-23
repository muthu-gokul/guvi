ye= int(input())
if (ye%4 == 0):
    if (ye%100 == 0):
        if(ye %400 == 0) :
            print('yes')
        else :
            print('no')
    else :
        print('yes')
else :
    print('no')
