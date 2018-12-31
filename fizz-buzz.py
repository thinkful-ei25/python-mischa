import sys

def valid_input(input_value = None):
    while True:
            try:
                number = int(input('input a number for fizz-buzz: '))
                return number
            except ValueError:
                print("please enter an integer!!")


number = None
if len(sys.argv) > 1:
    number = valid_input(sys.argv[2])
else:
    number = valid_input()
    
number = float(number)

counter = 1
printOut = []
while counter <= number:
    if (counter % 3.0 == 0.0) & (counter % 5.0 == 0.0):
        printOut.append('fizzbuzz')
    elif counter % 3.0 == 0.0:
        printOut.append('fizz')
    elif counter % 5.0 == 0.0:
        printOut.append('buzz')
    else:
        printOut.append(counter)
    counter += 1
print(printOut)