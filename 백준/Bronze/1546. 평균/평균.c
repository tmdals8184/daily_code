#include <stdio.h>
#define MAX 1000

int main(void)
{
    int n, max = 0, sum = 0;
    int arr[MAX] = {0,};
    scanf("%d", &n);
    for (int i = 0; i < n; i++) 
    {
        scanf("%d", &arr[i]);
        if (arr[i] > max) max = arr[i];
    }
    for (int i = 0; i < n; i++) sum += arr[i];
    printf("%lf\n", (double)sum / (double)max * 100.0 / (double)n);
    return 0;
}