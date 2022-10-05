// C program for the above approach
#include <stdio.h>

// Driver Code
int main(){
    char c;
    int count = 0, temp = 0, money = 100;
    while ( (c = getchar()) != '\n'){
        if (c != ' '){
            temp *= 10;
            temp += (c - '0');
        }
        else{
            money -= temp;
            if(money <= 0) {
                printf("%d", count);
                return 0;
            }
            temp = 0;
            count++;
        }
    }
    money -= temp;
    if (money < 0) {
        printf("%d", count);
    }
    else{
        count++;
        printf("%d", count);
    }

    return 0;
}