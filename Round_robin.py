n = int(input("Enter number of processes: "))

process = []
burst = []

for i in range(n):
    name = input("Enter process name: ")
    bt = int(input("Enter burst time: "))
    process.append(name)
    burst.append(bt)

quantum = int(input("Enter time quantum: "))

remaining = burst.copy()
waiting = [0] * n
time = 0

exec_process = []
exec_time = []

while sum(remaining) > 0:
    for i in range(n):
        if remaining[i] > 0:
            if remaining[i] <= quantum:
                time += remaining[i]
                waiting[i] = time - burst[i]
                remaining[i] = 0
                exec_process.append(process[i])
                exec_time.append(time)
            else:
                time += quantum
                remaining[i] -= quantum
                exec_process.append(process[i])
                exec_time.append(time)

print("Process  BT  WT  TAT")

for i in range(n):
    tat = waiting[i] + burst[i]
    print(process[i], burst[i], waiting[i], tat)

print("\nExecution Order:")
for i in range(len(exec_process)):
    print("Process", exec_process[i], "completed at time", exec_time[i])

print("Average WT =", sum(waiting)/n)
print("Average TAT =", sum(waiting[i] + burst[i] for i in range(n))/n)