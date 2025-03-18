#Loops are used to repeat instructions
count = 1               #This is an iterator
while count<=5 :
    print("hello", count)
    count+=1            #this whole process of going on and on until condition is false is known as iteration.
print(count)            #value of count at the end of the loop.

#printing numbers from 1--5 and 5---1
i = 1
while i<=5 :
    print(i)
    i = i+1
print("Loop ended")

j = 5
while j>=1:
    print(j)
    j -= 1
print("Loop Ended")

#WAP to print numbers from 1 to 100
k = 1
while (k<=100):
    print(k)
    k = k+1
print("End of the Loop")

#WAP to print numbers from 100 to 1
m = 100
while m>=1 :
    print(m)
    m -= 1
print("End of the loop")

#WAP for the multiplication table of number n
n = int(input("Enter a number of your choice: "))
m = 1
while (m<=10):
    print(n*m)
    m += 1
print("Thanks")

#WAP to print the following list using loop [1,4,9,16,25,36,49,64,81,100]           #called as traversing over the list
list = []                                   #nums  = [1,4,9,16,25,36,49,64,81,100]
o = 1                                       #idx = 0
p = 1                                       #while idx < len(nums):
while o<=10 and p<=10:                      #print(nums[idx])   
    list.append(o*p)                        #idx += 1
    o += 1
    p += 1

print(list)         #if we want gradual increase of each element in this list then we can place the print command inside the loop


#WAP to search for a number x in this tuple using loop (1,4,9,16,25,36,49,64,81,100)
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i< len(nums):
    if(nums[i] == x):
        print("FOUND'EM @ idx: ", i)
    else:
        print("finding...")
    i += 1

#Break (used to terminate the loop) and continue (terminates execution in current iteration and continues execution with next iteration) statements
i = 0
while i<=5:
    if(i == 3):
        i += 1
        continue    #the loop starts with i=0, increases value and runs normally until i=3 where the if condition is satisfied and the entry is omitted due to continue statement
    print(i)
    i += 1

#WAP to print odd/even numbers
i = 1
while i <= 10:
    if(i%2 == 0):
        i+=1
        continue            #Skips
    print(i)
    i+=1

#For loops (used for sequential traversal) (eg. traversing list, tuples, strings)
veggies = ["potato", "brinjal", "radish", "cucumber"]
for val in veggies:
    print(val)

#To work on an iterator (updating values) use while loop, whereas use for loop when we have to traverse throgh a data type

str = "JavedKhan"

for char in str:
    if(char == "K"):
        print("K found")
        break           #Since break is used here therefore rest of the code won't be executed (not even else and print statements below)
    print(char)
else:                   #completely optional (can be used when we want some task to be executed after the loop has finished it's work)
    print("END")

#WAP to print the elements [1,4,9,16,25,36,49,64,81,100] using for loop
nums = [1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print(el)

#WAP to search for a nmber in the tuple (1,4,9,16,25,36,49,64,81,100) using for loop  
tup = (1,4,9,16,25,36,49,64,81,100,49)
x = 49
idx = 0
for el in tup:
    if(el == x):
        print("number found at idx", idx)
    idx +=1
#Optionally if you want to stop the process after first occcurance of 49 then use a break statement at line 114 (after print)


