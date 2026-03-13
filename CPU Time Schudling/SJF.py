
n = int(input("Enter the number of processes: "))

burstTime = []
for i in range(n):
    burstTime.append(int(input(f"Enter the burst time for process {i+1}: ")))

burstTime.sort()

waitingTime = [0] * n
for i in range(1, n):
    waitingTime[i] = waitingTime[i-1] + burstTime[i-1]

total_waitingtime = sum(waitingTime)
avg_wt = total_waitingtime / n

print("Average waiting time:", avg_wt)
