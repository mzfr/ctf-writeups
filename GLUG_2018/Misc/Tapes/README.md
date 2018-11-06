# The Tapes

__PROBLEM__

Misha got deeply emotional after watching Hannah Baker's story in 13 Reasons why.She decided to summarize whole series in a folder. But,she lost a secret while doing so. Can you find it for us?

[13reasonwhy](13reasonswhy.zip)

__SOLUTION__

This problem was solved by my teammate [@ugtan](https://github.com/ugtan)

So this is another `git` related problem. This can be done by using a tool called [`Gittools`](https://github.com/internetwache/GitTools). Actually we only need one of the script in that tool called [`extractor.sh`](extractor.sh)
Just run this on the given directory and then you'll have lot's of preivous commits and files. After that use `grep` to find the flag.
So whole process would be
```bash
>>> ./extractor.sh HANNAH/ hannah_commit/
>>> grep GLUG
```

FLAG - `GLUG{3e72ome_10_9our_1@pe}`

P.S - I would just to use ripgrep instead of grep since ripgrep is way better.
