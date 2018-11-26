# APL

__PROBLEM__

Dr. W gave me an old program of his... Can you tell me what it does? (Difficulty: Easy)

```
mx←7 0↓14 9⍴⍳132
a←mx[(3 3)(3 4)(1 4)(3 3)(1 7)(7 6)(7 2)(3 1)(5 6)(3 3)(5 2)(4 5)(2 7)(6 2)(2 4)(7 4)(4 5)(2 1)(6 7)(4 5)(1 9)(4 7)(3 1)(5 1)(4 5)(3 3)(6 3)(4 5)(3 1)(5 2)(1 2)(5 1)(7 8)]
```

__SOLUTION__

Just google the name of the task and you'll find that it's a programming language. I used [tryapl](https://tryapl.org/) to solve this.

After printing the values of `a` you'll get decimal value
```
84 85 67 84 70 123 119 82 105 84 101 95 79 110 76 121 95 73 115 95 72 97 82 100 95 84 111 95 82 101 65 100 125
```

change those decimal to ascii and you'll have the flag.

FLAG - `TUCTF{wRiTe_OnLy_Is_HaRd_To_ReAd}`
