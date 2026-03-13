n= int(input("Enter number of processes: "))

pro = []

for i in range(n):
    pid = input(f"Enter Process ID for process {i+1}: ")
    bt = int(input("Enter Burst Time: "))
    pr = int(input("Enter Priority: "))
    pro.append([pid, bt, pr])


for i in range(n):
    for j in range(i+1, n):
        if pro[i][2] > pro[j][2]:
            temp = pro[i]
            pro[i] = pro[j]
            pro[j] = temp

wt = [0] * n
tat = [0] *n
for i in range(1, n):
    wt[i] = wt[i-1] + pro[i-1][1]


for i in range(n):
    tat[i] = wt[i] + pro[i][1]


print("\nProcess\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")

total_wt = 0
total_tat = 0

for i in range(n):
    total_wt += wt[i]
    total_tat += tat[i]
    print(pro[i][0], "\t", pro[i][1], "\t\t", pro[i][2],
          "\t\t", wt[i], "\t\t", tat[i])

print("\nAverage Waiting Time =", total_wt / n)
print("Average Turnaround Time =", total_tat / n)
