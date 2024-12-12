x = input("Enter a password: ")
if len(x) < 8:
    print("strong password needed")
elif x == x.upper():
    print("Atleast one lowercase letter required")
elif x == x.lower():
    print("Atleast one uppercase letter required")                 
elif x != [0,1,2,3,4,5,6,7,8,9]:
    print("Atleast one digit is required")
    
# og = int(input("Enter the Original Price in dollar: $"))
# if og < 50:
#     print("No discount for prices below $50")
# elif og >= 50 and og <= 100:
#     print("$",og-(og/100*10),"Final price after discount")
# elif og > 100:
#     print("$",og-(og/100*20),"Final price after discount")        

# name = "devvrat"
# print(name[0:4])    