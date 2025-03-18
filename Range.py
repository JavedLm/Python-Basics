#Range functions returns a sequence of numbers, starting form 0 by default, increments by 1 and stops before the specified input number
print (range(5))        #Initially the numbers from 0--5 won't be printed

seq = (range(4))        #but we can print the indices       #range(stop value)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

#Or optionally
seq = (range(6))                    #also for i in range[10]    is equally acceptable rather than creating a new variable seq
for i in seq:
    print(i)

#(range(start value (optional by default 0), stop value(compulsory), step index(optional by default 1))
for i in range(2,10,2):
    print(i)

#Step size can also be negative value for printing a series in reverse order
#WAP to print a table of number input by user

n = int(input("Enter the number:"))

for i in range(1,11):
    print(n*i)

#Pass statement is a null statement that does nothing. Placeholder for future code
for i in range(5):
    pass
print("Nothing done")

#WAP to find the sum of first n natural numbers (while)
n = 4
sum = 0 
for i in range(1, n+1):                 #while i <= n:
    sum +=i                             #sum += i
                                        #i += 1
print("Total sum is ", sum)

#WAP to find the factorial of first n numbers
n = 4
fact = 1
for j in range(1, n+1):
    fact *= j

print("the factorial is:", fact)

#06:04:00