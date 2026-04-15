reference_string = list(map(int, input("Enter reference string: ").split()))
frames = int(input("Enter number of frames: "))

memory = []
order = []   
hits = 0
miss = 0

print("\nPage\tFrames\tStatus")

for page in reference_string:

    if page in memory:
        hits += 1
        status = "Hit"

        order.remove(page)
        order.append(page)

    else:
        miss += 1
        status = "Miss"

        if len(memory) < frames:
            memory.append(page)
            order.append(page)
        else:
            lru_page = order.pop(0)
            index = memory.index(lru_page)

            memory[index] = page
            order.append(page)

    print(f"{page}\t{memory}\t{status}")

total = len(reference_string)
print("\nTotal Hits:", hits)
print("Total Misses:", miss)