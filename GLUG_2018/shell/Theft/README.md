# Theft

__PROBLEM__

They say comparison is the thief of joy.Do you want to steal some joy dealing with comparison?

Use the command below to login in this challenge server
ssh shell6@206.81.1.159 -p1333
Password - shell6

__SOLUTION__

After getting on the shell server first thing we do is checkout whats in the directory.
```bash
>>> ls
secretkey.new  secretkey.old
```
Okay so we are given two files and question was talking soemthing about `comparision` so let just compare them.
```bash
>>> diff secretkey.new secretkey.old
706c706
< GLUG{944086d1-6723-4540-aa7c-42fe34946725}
---
> GLUG{50650e01-be11-48d3-afb6-32a06a01a067}
```

FLAG - `GLUG{944086d1-6723-4540-aa7c-42fe34946725}`
