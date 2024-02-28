num1 = input("Enter start : ")
num2 = input("Enter End   : ")
num1 = int(num1)
num2 = int(num2)
for i in range(num1,num2+1):
    print("Mea ",i)
    print("-------------------")
    for r in range(0,13):
      print(i," x ",r," = ",(i*r))
    print("-------------------")
    