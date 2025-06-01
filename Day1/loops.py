# for loop in python is written with range key word whereas other program languagues prefer for(i=0;condition:iteration)
for i in range(10):
    print("This is from for loop!!")
    print("Hello friends")
    

# loop that could be used for an array or list 
array = ["leapfrog", "is", "the best"]
for item in array:
    print(item)


#infinite loop using while loop
while True:
    name = input("Type 'meow' to quit: ")
    if name == "meow":
        break


#for loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished successfully!")
