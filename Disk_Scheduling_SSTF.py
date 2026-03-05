
path = list(map(int, input("Enter disk queue (1st element = head position): ").split()))

head = path[0]        
Queue = path[1:]  

current = head
total_distance = 0
step = 1

print("\nInitial Head Position:", head)
print("Request Queue:", Queue)

print("\nStep by Step Movement:\n")

while len(Queue) > 0:
    closest = Queue[0]
    min_distance = abs(closest - current)

    for r in Queue:
        distance = abs(r - current)
        if distance < min_distance:
            min_distance = distance
            closest = r

    total_distance = total_distance + min_distance

    print("Step", step)
    print("Move from", current, "->", closest)
    print("Distance =", "|", closest, "-", current, "| =", min_distance)
    print("Running Total =", total_distance)
    print()

    current = closest
    Queue.remove(closest)
    step = step + 1

print("Total Head Movement =", total_distance)