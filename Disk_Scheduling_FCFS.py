
path = list(map(int, input("Enter disk queue (1st element = head position): ").split()))
    
requests = path[1:]   

current = path[0]
total_distance = 0
step = 1

print("\nInitial Head Position:", path[0])
print("Request Queue:", requests)

print("\nStep by Step Movement:\n")

for req in requests:
    distance = abs(req - current)
    total_distance = total_distance + distance

    print("Step", step)
    print("Move from", current, "->", req)
    print("Distance =", "|", req, "-", current, "| =", distance)
    print("Running Total =", total_distance)
    print()

    current = req
    step = step + 1

print("Total Distance =", total_distance)