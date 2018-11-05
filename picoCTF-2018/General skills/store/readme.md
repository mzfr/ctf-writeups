# store

__PROBLEM__

We started a little [store](store), can you buy the flag? [Source](source.c). Connect with 2018shell2.picoctf.com 43581.

__HINT__

Two's compliment can do some weird things when numbers get really big!

__SOLUTION__

Looking at the source
```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int con;
    con = 0;
    int account_balance = 1100;
    while(con == 0){

        printf("Welcome to the Store App V1.0\n");
        printf("World's Most Secure Purchasing App\n");

        printf("\n[1] Check Account Balance\n");
        printf("\n[2] Buy Stuff\n");
        printf("\n[3] Exit\n");
        int menu;
        printf("\n Enter a menu selection\n");
        fflush(stdin);
        scanf("%d", &menu);
        if(menu == 1){
            printf("\n\n\n Balance: %d \n\n\n", account_balance);
        }
        else if(menu == 2){
            printf("Current Auctions\n");
            printf("[1] I Can't Believe its not a Flag!\n");
            printf("[2] Real Flag\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){
                printf("Imitation Flags cost 1000 each, how many would you like?\n");

                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 1000*number_flags;
                    printf("\nYour total cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour new balance: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds\n");
                    }
                }
            }
            else if(auction_choice == 2){
                printf("A genuine Flag costs 100000 dollars, and we only have 1 in stock\n");
                printf("Enter 1 to purchase");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);

                if(bid == 1){

                    if(account_balance > 100000){
                        printf("YOUR FLAG IS:\n");
                        }

                    else{
                        printf("\nNot enough funds for transaction\n\n\n");
                    }}

            }
        }
        else{
            con = 1;
        }

    }
    return 0;
}

```
From this code main thing to look for is:
```c
scanf("%d", &number_flags);
if(number_flags > 0){
    int total_cost = 0;
    total_cost = 1000*number_flags;
    printf("\nYour total cost is: %d\n", total_cost);
    if(total_cost <= account_balance){
        account_balance = account_balance - total_cost;
```

In this we have to give the value of `number_flags` in such a way that it's greater than `0` but also make the value such way that it increases our balance. So basically it is an integer overflow.

So when you are prompted to enter the number of flag enter a big integer value like `123456789` and that would wrap around the number and instead will make it a negative, adding it to our balance instead or subtracting from it.


FLAG - `picoCTF{numb3r3_4r3nt_s4f3_6bd13a8c}`
