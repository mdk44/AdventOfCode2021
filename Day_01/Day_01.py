input_file = 'Day_01\\Input.csv'
# input_file = 'Day_01\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split()

nums = []

for line in lines:
    nums.append(int(line))

# Part 1
p1_count = 0
for x in range(1, len(nums)):
    if nums[x] > nums[x - 1]:
        p1_count += 1

# Part 2
p2_count = 0
for x in range(3, len(nums)):
    if nums[x] + nums[x - 2] + nums[x - 1] > nums[x - 1] + nums[x - 2] + nums[x - 3]:
        p2_count += 1

print("Part 1: " + str(p1_count))
print("Part 2: " + str(p2_count))