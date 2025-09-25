number=int(input('enter your number: '))
if number % 2 == 0:
    print(number,'is even number')
else:
    print(number,'is odd number')

total=0
for i in range(1,51):
   total += i
print("the sum of the numbers 1 to 50 is:", total)
