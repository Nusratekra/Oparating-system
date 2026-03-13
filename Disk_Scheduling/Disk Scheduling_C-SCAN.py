queue = list(map(int, input("Enter request queue: ").split()))
disk_size = int(input("Enter disk size: "))
direction = input("Enter direction (increasing/decreasing): ").lower()

head = queue[0]
requests = queue[1:]

left = []
right = []
seek_sequence = []
seek_count = 0

for r in requests:
    if r < head:
        left.append(r)
    else:
        right.append(r)

left.sort()
right.sort()

if direction == "increasing":
    right.append(disk_size - 1)  
    left.insert(0, 0)           

    for r in right:
        move = abs(head - r)
        seek_count += move
        print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r

    jump_distance = abs(head - 0)
    seek_count += jump_distance
    print(f"{head} -> 0 = {jump_distance}   total = {seek_count}")
    seek_sequence.append(0) 
    head = 0

    for r in left[1:]: 
        move = abs(head - r)
        seek_count += move
        print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r

else: 
    left.insert(0, 0)
    right.append(disk_size - 1)

    for r in reversed(left):
        move = abs(head - r)
        seek_count += move
        print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r

    jump_distance = abs(head - (disk_size - 1))
    seek_count += jump_distance
    print(f"{head} -> {disk_size - 1} = {jump_distance}   total = {seek_count}")
    seek_sequence.append(disk_size - 1)  
    head = disk_size - 1

    for r in reversed(right[:-1]):  
        move = abs(head - r)
        seek_count += move
        print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r

print("\nSeek Sequence:", seek_sequence)
print("Total Seek Operations:", seek_count)
