total=0
for num in range(1,10):
    print ("in the loop",num)
    if num %3 ==0 or num % 5 == 0:
        total += num
        print ("in the if block", num)
        print (total)