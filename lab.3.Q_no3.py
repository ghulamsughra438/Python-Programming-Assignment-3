# Question  No.3
numbers = []

for i in range(1, 11):
  num = int(input(f'Enter number {i}: '))
  numbers.append(num)

total_sum = sum(numbers)
average = total_sum / len(numbers)
largest = max(numbers)
smallest = min(numbers)

even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = len(numbers) - even_count

print('\n Number Analysis')
print(f'Sum: {total_sum}')
print(f'Average: {average:.2f}')
print(f'Largest Number: {largest}')
print(f'Smallest Number: {smallest}')
print(f'Number of Even Numbers: {even_count}')
print(f'Number of Odd Numbers: {odd_count}')
