#include <stdio.h>

int main(void)
{
    int n, x;
    int arr[10000];
    scanf("%d", &n); scanf("%d", &x);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    for (int i = 0; i < n; i++)
        if (arr[i] < x) printf("%d ", arr[i]);
    return 0;
}