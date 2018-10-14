# environ

__PROBLEM__

Sometimes you have to configure environment variables before executing a program. Can you find the flag we’ve hidden in an environment variable on the shell server?

__HINT__

unix [env](https://www.tutorialspoint.com/unix/unix-environment.htm)

__SOLUTION__

This is the introduction to linux `environment variables`.
Run
```
> printenv | grep "picoCTF"
```

Here `printenv` prints all the environment variables and the we use our friend `grep` to get us the flag.

FLAG - `picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}`
