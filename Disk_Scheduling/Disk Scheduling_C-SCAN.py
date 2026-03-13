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
    head = 0
    print(f"{head} -> {jump_distance}, total = {seek_count}")

    for r in left:
        if r != 0:  
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
    head = disk_size - 1
    print(f"{head} -> {jump_distance}, total = {seek_count}")

    for r in reversed(right):
        if r != disk_size - 1:  
            move = abs(head - r)
            seek_count += move
            print(f"{head} -> {r} = {move}   total = {seek_count}")
            seek_sequence.append(r)
            head = r

print("\nSeek Sequence:", seek_sequence)
print("Total Seek Operations:", seek_count)
