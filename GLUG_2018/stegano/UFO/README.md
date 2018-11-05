# UFO

__PROBLEM__

Casper found this image on his Trash folder, he is not sure who is the creator.
Can you help him by finding it out ? We will reward you with a FLAG

[ufo.jpeg](ufo.jpeg)

__SOLUTION__

Well the first thing I tried was to see if our flag was in the strings and actually it was.

```
>>> strings ufo.jpeg | grep GLUG
GLUG{3x1f_15_n07_d34d}
```

FLAG - `GLUG{3x1f_15_n07_d34d}`
