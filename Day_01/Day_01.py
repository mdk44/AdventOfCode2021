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

print(p1_count)

# Part 2
# for x in range(0, len(nums)):
#     for y in range(x + 1, len(nums)):
#         for z in range(y + 1, len(nums)):
#             if nums[x] + nums[y] + nums[z] == 2020:
#                 print("Part 2: " + str(nums[x] * nums[y] * nums[z]))