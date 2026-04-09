queue = list(map(int, input("Enter request queue: ").split()))                
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



print("\nHead Movement:")

if direction == "decreasing":
    for r in reversed(left):
        if head != r: 
            move = abs(head - r)
            seek_count += move
            print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r
    for r in right:
        if head != r:
            move = abs(head - r)
            seek_count += move
            print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r
else:  
    for r in right:
        if head != r:
            move = abs(head - r)
            seek_count += move
            print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r
    for r in reversed(left):
        if head != r:
            move = abs(head - r)
            seek_count += move
            print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r

print("\nSeek Sequence:", seek_sequence)
print("Total Seek Operations:", seek_count)
