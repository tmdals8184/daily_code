#include <stdio.h>

int main(void)
{
    char word[101];
    int arr[26], idx;
    for (int i = 0; i < 26; i++) arr[i] = -1;
    scanf("%s", word);
    for (int i = 0; word[i] != '\0'; i++)
    {
        idx = word[i] - 'a';
        if (arr[idx] == -1) arr[idx] = i;        
    }
    for (int i = 0; i < 26; i++) printf("%d ", arr[i]);    
    return 0;
}