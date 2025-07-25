#include <stdio.h>

int main(void)
{
    int min = 0, max = 0;
    int arr[9];
    for (int i = 0; i < 9; i++)
        scanf("%d", &arr[i]);
    for (int i = 1; i < 9; i++)
        if (arr[i] > arr[max]) max = i;    
    printf("%d\n%d\n", arr[max], max + 1);
    return 0;       
}