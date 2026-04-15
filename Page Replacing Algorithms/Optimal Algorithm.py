reference_string = list(map(int, input("Enter reference string: ").split()))
frames = int(input("Enter number of frames: "))

memory = []
miss = 0
hits = 0

print("\nPage\tFrames\tStatus")

for i in range(len(reference_string)):
    page = reference_string[i]

    if page in memory:
        hits += 1
        status = "Hit"
    else:
        miss += 1
        status = "Miss"

        if len(memory) < frames:
            memory.append(page)
        else:
            future_use = []

            for m in memory:
                if m in reference_string[i+1:]:
                    future_use.append(reference_string[i+1:].index(m))
                else:
                    future_use.append(float('inf'))

            index_to_replace = future_use.index(max(future_use))
            memory[index_to_replace] = page

    print(f"{page}\t{memory}\t{status}")

total = len(reference_string)
hit_ratio = hits / total
miss_ratio = miss / total

print("\nTotal Hits:", hits)
print("Total Misses:", miss)
print("Hit Ratio:", round(hit_ratio, 2))
print("Miss Ratio:", round(miss_ratio, 2))