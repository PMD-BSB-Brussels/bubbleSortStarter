# The following code contains a number of logical errors and one run time error, please fix them.

numbers = [4,2,9,7,0,1,3,10]

def bubbleSort(numbers):
  sorted = True
  while not sorted:
    sorted = False
    for i in range(1,len(numbers):
      if numbers[i] > numbers[i+1]:
        temp = numbers[i]
        numbers[i] = temp
        numbers[i+1] = numbers[i]
        sorted = True
  return numbers

print(bubbleSort(numbers))
