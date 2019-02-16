# Elf Basic

__PROBLEM__

After analysing the server we found an executable. We suspect this executable may be a part of attack. Help us to identify the same.

Note: Make sure you add xiomara{} tag before submitting the flag.

[FILE](AnokhREV)
__SOLUTION__

When you'll run the given file you'll see that it asks for input and then tell's you right or wrong like
```bash
✦ ➜ ./AnokhREV
Welcome To Anokha 2k19 Please Enter the flag !
flag

Psst Wrong Try Again
```

With this flow it looks like it must be using something like `strcmp` so I started it with [ltrace](https://github.com/dkogan/ltrace)

```bash
✦ ➜ ltrace ./AnokhREV
puts("Welcome To Anokha 2k19 Please En"...Welcome To Anokha 2k19 Please Enter the flag !
)                                                                           = 47
malloc(18)                                                                                                            = 0x5573aeeea670
memset(0x5573aeeea670, '\0', 18)                                                                                      = 0x5573aeeea670
fgets(a
"a\n", 18, 0x7ff9e5c93860)                                                                                      = 0x5573aeeea670
strcmp("a\n", "jnhFClg2sv3uaBBxs")                                                                                    = -9
printf("\nPsst Wrong Try Again "
)                                                                                     = 22
free(0x5573aeeea670)                                                                                                  = <void>
Psst Wrong Try Again +++ exited (status 0) +++
```

And here we can see that it is comparing the input with `jnhFClg2sv3uaBBxs` so this time we run it and give that as input.

```bash
✦ ➜ ./AnokhREV
Welcome To Anokha 2k19 Please Enter the flag !
jnhFClg2sv3uaBBxs
Your flag is xiomara{jnhFClg2sv3uaBBxs}
```

FLAG - `xiomara{jnhFClg2sv3uaBBxs}`
