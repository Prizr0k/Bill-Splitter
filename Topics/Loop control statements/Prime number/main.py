n = int(input())
count = 0
for i in range(2, n + 1):
    if n % i == 0:
        count += 1
    if count == 2:
        break
print(("This number is not prime", "This number is prime")[count == 1])

counter = 0
max_value = 0
while counter < 10:
    counter = counter + 1
    max_value = max_value + counter
    if max_value > 15:
        break
    counter = counter + 1

print(counter, max_value)
