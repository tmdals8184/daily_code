#include <stdio.h>

int main(void)
{
    int n, m, a, b, c;
    int arr[100] = {0,};
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d %d", &a, &b, &c);
        for (int j = a - 1; j < b; j++) arr[j] = c;
    }
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    putchar('\n');
    
    return 0;
}