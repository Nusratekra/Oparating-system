reference_string = list(map(int, input("Enter reference string: ").split()))
frames = int(input("Enter number of frames: "))

memory = []
miss = 0
hits = 0
index = 0

for page in reference_string:
    if page in memory:
        hits += 1
    else:
        miss += 1
        if len(memory) < frames:
            memory.append(page)
        else:
            memory[index] = page
            index = (index + 1) % frames

    print(f"Page: {page} -> Memory: {memory}")

total = len(reference_string)
hit_ratio = hits / total
miss_ratio = miss / total

print("\nTotal Hits:", hits)
print("Total Misses:", miss)
print("Hit Ratio:", round(hit_ratio, 2))
print("Miss Ratio:", round(miss_ratio, 2))
