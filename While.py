start = int(input("Input the first number from 100 to 9999: "))
end = int(input("Input the second number from 100 to 9999: "))

if 100 <= start <= 9999 and 100 <= end <= 9999:
    print("CORRECT1")
else:
    print("ERROR!!! Please INPUT numbers in the range from 100 to 9999!")
    exit()

if start > end:
    start += end
    end = start - end
    start -= end

print("Odd numbers in the range:")
count = 0
if start % 2 == 0:
    num = start + 1
else:
    num = start
while num <= end:
    print(num, end=" ")
    count += 1
    num += 2
print()

print(f"Total number of odd numbers in the range = {count}")