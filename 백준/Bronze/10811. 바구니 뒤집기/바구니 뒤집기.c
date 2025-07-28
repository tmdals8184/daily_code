#include <stdio.h>
#define MAX 100

void reverse(int arr[], int start, int end);
int main(void)
{
    int n, m, a, b;
    int arr[MAX];
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) arr[i] = i + 1;
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d", &a, &b);
        reverse(arr, a - 1, b - 1);       
    }
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}

void reverse(int arr[], int start, int end)
{
    while (start < end)
    {
        int tmp = arr[start];
        arr[start] = arr[end];
        arr[end] = tmp;
        start++; end--;
    }
}

