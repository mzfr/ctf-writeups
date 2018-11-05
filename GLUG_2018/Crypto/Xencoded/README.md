# Xencoded

__PROBLEM__

Can you decode this message?
23262a233d1a3418331b19322f181b2f1a37322f1b181b2f181b3e

__HINT__

Lost in the shift

__SOLUTION__

number/ascii-hex-bin-dec-converter.html) we get the decimal values from the given hex.
we'll get `35 38 42 35 61 26 52 24 51 27 25 50 47 24 27 47 26 55 50 47 27 24 27 47 24 27 62`.

```python
>>> t = ''

>>> for i in s:
         t = t+ chr((i<<1))
>>> t
'FLTFz4h0f62d^06^4nd^606^06|'
```
Now this is a random string and no it's not in base64 or soemthing like that. It is just soemthing random meaning we did something wrong. so instead of getting characters out of shift, we can get the decimal values out of shift and then do some manipulation our self.

```python
>>>t = []
>>> for i in s:
        t.append(i<<1)
>>> t
[70, 76, 84, 70, 122, 52, 104, 48, 102, 54, 50, 100, 94, 48, 54, 94, 52, 110, 100, 94, 54, 48, 54, 94, 48, 54, 124]
```

Now we have values that we can change into ascii character using [ascii tables](https://homepage.cs.uri.edu/faculty/wolfe/book/Readings/R02%20Ascii/completeASCII.htm).

one thing we know is that first 4 character has to `GLUG` meaning change 70 to 71, also we know that ascii/leet characters in flag will be connected by `_` meaning all the `94` will be changed to `95` and then in the same way you can try to amke sense out of the whole flag.
Now I don't think so this is the ideal way of getting this flag but it worked.

FLAG - `GLUG{5h1f73d_17_4nd_607_17}`
