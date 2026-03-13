#include <stdio.h>
void findWaitingTime(int processes[], int n, int bt[], int wt[]) {
    wt[0] = 0;
    for (int i = 1; i < n; i++) {
        wt[i] = bt[i - 1] + wt[i - 1];
    }
}

void findAvgTime(int processes[], int n, int bt[]) {
    int wt[n];
    int total_wt = 0;
    findWaitingTime(processes, n, bt, wt);
    printf("\nProcess  BurstTime  WaitingTime \n");
    for (int i = 0; i < n; i++) {
        total_wt += wt[i];
        printf("  %d\t\t%d\t\t%d\n", processes[i], bt[i], wt[i]);
    }
    float avg = (float)total_wt / n;
    printf("\nAverage waiting time = %f\n", avg);
}

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    int processes[n], bt[n];
    for (int i = 0; i < n; i++) {
        processes[i] = i + 1;
    }
    for (int i = 0; i < n; i++) {
        printf("Enter the Burst Time for process %d: ", i + 1);
        scanf("%d", &bt[i]);
    }
    findAvgTime(processes, n, bt);
    return 0;
}

