#include <stdio.h>

int main(void)
{
    int n, m, a, b, tmp;
    int arr[100];
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) arr[i] = i + 1;
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d", &a, &b);
        tmp = arr[a - 1];
        arr[a - 1] = arr [b - 1];
        arr[b - 1] = tmp;
    }
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    putchar('\n');
    
    return 0;
}