FunnyMan = int( input(" Insert a number that is higher than 20 and is also an odd: "))

while ( FunnyMan <= 20 or FunnyMan % 2 == 0):
    print("Acess denied")
    FunnyMan = int( input(" Insert a number that is higher than 20 and is also an odd: "))
else:
    print("Congratulations")

# if (FunnyMan % 2 == 1):
#     print("Congratulations")
# else:
#     print("Imagine")
#     FunnyMan = int( input(" Insert a number that is higher than 20 and is also an odd: "))
