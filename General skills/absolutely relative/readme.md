# absolutely relative

__PROBLEM__

In a filesystem, everything is relative ¯_(ツ)_/¯. Can you find a way to get a flag from this [program](absolutely-relative)? You can find it in /problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6 on the shell server. [Source](absolutely-relative.c).

__HINT__

Do you have to run the program in the same directory? (⊙.☉)7

Ever used a text editor? Check out the program 'nano'

__SOLUTION__

Looking at the source:
```c
#include <stdio.h>
#include <string.h>

#define yes_len 3
const char *yes = "yes";

int main()
{
    char flag[99];
    char permission[10];
    int i;
    FILE * file;


    file = fopen("/problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6/flag.txt" , "r");
    if (file) {
        while (fscanf(file, "%s", flag)!=EOF)
        fclose(file);
    }

    file = fopen( "./permission.txt" , "r");
    if (file) {
        for (i = 0; i < 5; i++){
            fscanf(file, "%s", permission);
        }
        permission[5] = '\0';
        fclose(file);
    }

    if (!strncmp(permission, yes, yes_len)) {
        printf("You have the write permissions.\n%s\n", flag);
    } else {
        printf("You do not have sufficient permissions to view the flag.\n");
    }

    return 0;
}

```
We can see that this program is looking for a file called `permission.txt` for granting us the permission to see the flag.

So go to `~/` on shell by typing `cd ~/` and then make a file called `permission.tx` in that directory `echo "yes">permission.txt` and then run the program from this directory
```
> problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6/absolutely-relative
> You have the write permissions.
picoCTF{3v3r1ng_1$_r3l3t1v3_befc0ce1}
```

FLAG - picoCTF{3v3r1ng_1$_r3l3t1v3_befc0ce1}
