path = list(map(int, input("Enter all requests: ").split()))
head = path[0]
requests_rest = path[1:]
min_req = min(requests_rest)
max_req = max(requests_rest)
queue = [r for r in requests_rest if r != min_req and r != max_req]
requests = queue + [min_req, max_req]

direction = input("Enter direction (increasing/decreasing): ").lower()

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

if direction == 'increasing':
    for r in right:
        move = abs(head - r)
        seek_count += move
        print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r

    if left:
        jump_distance = abs(head - left[0])
        seek_count += jump_distance
        head = left[0]
        print(f"{head} -> {jump_distance}, total = {seek_count}")

        for r in left:
            if r != left[0]:
                move = abs(head - r)
                seek_count += move
                print(f"{head} -> {r} = {move}   total = {seek_count}")
                seek_sequence.append(r)
                head = r

else:
    for r in reversed(left):
        move = abs(head - r)
        seek_count += move
        print(f"{head} -> {r} = {move}   total = {seek_count}")
        seek_sequence.append(r)
        head = r

    if right:
        jump_distance = abs(head - right[-1])
        seek_count += jump_distance
        head = right[-1]
        print(f"{head} -> {jump_distance}, total = {seek_count}")

        for r in reversed(right[:-1]):
            move = abs(head - r)
            seek_count += move
            print(f"{head} -> {r} = {move}   total = {seek_count}")
            seek_sequence.append(r)
            head = r

print("\nSeek Sequence:", seek_sequence)
print("Total Seek Operations:", seek_count)