#include <stdio.h>

int main(void)
{
    int n, r;
    char word[21];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d %s", &r, word);
        for (int j = 0; word[j] != '\0'; j++)
        {
            for (int k = 0; k < r; k++)
                printf("%c", word[j]);
        }
        putchar('\n');
    }
    return 0;
}