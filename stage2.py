print("write how many ml of water the machine needs ?")
water=int(input())
print("write how many ml of milk the machine needs ?")
milk=int(input())
print("write how many g of coffe beans the machine needs?")
coffee=int(input())

no_of_coffee=int(input())
k=int(min(water//50,milk//20,coffee//15))
if no_of_coffee==k:
    print("yes,I can make that amount of coffee")
 elif no_of_coffee>k:
        print("No,I cant make that amount only",k,"cups of coffee")
elif no_of_coffee<k:
    print("yes,I can make that amount of coffee(and even",k -no_of_coffee,"more than that)")