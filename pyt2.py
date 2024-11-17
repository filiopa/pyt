# Practicing lists with tarrot!
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23' '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42']

# Print a random value from the list!
import random
random_value = random.choice(numbers)
print("Random value: ", random_value)

# Print all values in the list! + in a single line with 'end="something"'!
Number = len(numbers)
for steps in range(Number):
 print(numbers[steps], end="+")

# Same but with simpler code!
for σηθιτ in numbers:
 print(σηθιτ, end=" ")
  
# Print all values in the list in a single line using join
print(".".join(numbers))

# Print first number
print('\n' + numbers[0])
# Print last number
print(numbers[-1])