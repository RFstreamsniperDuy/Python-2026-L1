#1
n = int(input("Enter circle radius? "))
print("Circle area =", (n**2)*3.14)

#2
C = int(input("Enter the temperature in Celcius? "))
print(f"{C} (C) = {(C*1.8)+32}(F)")

#3
prime_or_not = int(input("Enter a number? "))
condition = True
for i in range(2,prime_or_not):
    if prime_or_not % i == 0:
        condition = False
        break
if condition == False or prime_or_not < 2:
    print(f"{prime_or_not} is not a prime number")
else:
    print(f"{prime_or_not} is a prime number")

#4
perfect_number = int(input("Enter a number? "))
divisible_list = []
for i in range(1,perfect_number):
    if perfect_number % i == 0:
        divisible_list.append(i)
if sum(divisible_list) == perfect_number:
    print(f"{perfect_number} is a perfect number!")
else:
    print(f"{perfect_number} is not a perfect number!")

#5
existed_color = ["red","black","purple","blue"]
color = str(input("What is your favourite color? "))
if color in existed_color:
    print(f"your color is at index {existed_color.index(color)} in my list!")
else:
    print("Sorry, i could not find your color")
    
#6
print("range1")
for i in range(0,7,1):
    print(f"{i},", end=" ")
print("\nrange2")
for i in range(1,11,3):
    print(f"{i},", end=" ")
print("\nrange3")
for i in range(5,0,-1):
    print(f"{i},", end=" ")
print("\nrange4")
for i in range(6,-3,-2):
    print(f"{i},", end=" ") 

#7
#remove dollar sign => insert a string, 
# split them into letters, 
# find $ sign and remove  
str_test = str(input("Input a string consist of at least 1 dollar sign:"))
def remove_dollar_sign(s):
    letter_list = []
    for i in s:
        letter_list.append(i)
        if i == "$":
            letter_list.remove(i)
    return ''.join(letter_list) #there is a method to join list character together is to use the .join() method
print(remove_dollar_sign(str_test))

#8
num_list_example = []
n = 1
while n != 0:
    n = int(input("Input a number for list: "))
    num_list_example.append(n)
def extract_even(l):
    ans_list=[]
    for i in l:
        if i % 2 == 0 :
            ans_list.append(i)
    return ans_list
print(extract_even(num_list_example))

#9
inp_num = int(input("Input a number to calculate factorial of it: "))
def factorial_num(num):
    factorial_ans = 1
    if num < 1:
        print("The number cant be 0 or negative")
    else:
        for i in range(1,inp_num+1,1):
            factorial_ans *= i
    print (f"The factorial of {num}:",factorial_ans)
factorial_num(inp_num)

#10
inp_num = int(input("Input a number: "))
def divisors_finder(num):
    divisors_list= []
    for i in range(1,num+1):
        if num % i == 0:
            divisors_list.append(i)
    return divisors_list
print(divisors_finder(inp_num))

#11
# split into 2 points A and B (using (x,y))
# A(2,3) - B(5,6)
import math
A1 = int(input("Input x of point A: "))
A2 = int(input("Input y of point A: "))
B1 = int(input("Input x of point B: "))
B2 = int(input("Input y of point B: "))
print("The distance between A and B is: ",math.sqrt((A1-B1)**2+(A2-B2)**2))

#12
m = int(input("length of graph: "))
n = int(input("width of graph: "))
def pattern(m,n):
    for k in range(m):
        for i in range(n):
            if k == 0 or k == m-1 or i == 0 or i == n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print() 
pattern(m,n)

