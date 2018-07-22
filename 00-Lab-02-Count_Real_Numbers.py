nums = list(map(float, input().split(' ')))
counts = {}
for num in nums:
   if num in counts:
      counts[num] += 1
   else:
      counts[num] = 1
for num in sorted(counts.keys()):
    print(f"{num} -> {counts[num]} times")