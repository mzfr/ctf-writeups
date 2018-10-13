# Safe RSA

__PROBLLEM__

 Now that you know about RSA can you help us decrypt this [ciphertext](./ciphertext)? We don't have the decryption key but something about those values looks funky..

__HINT__

RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

Hmmm that e value looks kinda small right?

These are some really big numbers.. Make sure you're using functions that don't lose any precision!

__SOLUTION__

we are given:

```

N: 374159235470172130988938196520880526947952521620932362050308663243595788308583992120881359365258949723819911758198013202644666489247987314025169670926273213367237020188587742716017314320191350666762541039238241984934473188656610615918474673963331992408750047451253205158436452814354564283003696666945950908549197175404580533132142111356931324330631843602412540295482841975783884766801266552337129105407869020730226041538750535628619717708838029286366761470986056335230171148734027536820544543251801093230809186222940806718221638845816521738601843083746103374974120575519418797642878012234163709518203946599836959811

e: 3

ciphertext (c): 2205316413931134031046440767620541984801091216351222789180967130585669043554866325905770867150377611820746759815247778516899403229047066700396787852388511389893043279713280998235746440322483431305358901578692935378439077796777060321410661

```

Now going to the [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) given in the hint and keep the point about `small value of e` we find(in `Attacks against plain RSA` section of wikipedia page) out that RSA have a problem with e being small i.e

> When encrypting with low encryption exponents (e.g., e = 3) and small values of the m, (i.e., m < n1/e) the result of me is strictly less than the modulus n. In this case, ciphertexts can be easily decrypted by taking the eth root of the ciphertext over the integers.

So that means we just have to find the eth root of N and in our case we have to find the cube root of N.

Here's my small code for cube root:
```
def find_cube_root(n):
       low = 0
       high = n
       whighle low < high:
           mid = (low+high)//2
           if mid**3 < n:
               low = mid+1
           else:
               high = mid
    print(low)
```

Pass the value of N to this function. Then change that [DECIMAL to HEX](https://www.rapidtables.com/convert/number/decimal-to-hex.html) of the number you receive and then change that [hex to ASCII](https://www.rapidtables.com/convert/number/hex-to-ascii.html) and you'll get the flag.

FLAG - `picoCTF{e_w4y_t00_sm411_a5b5aaac}`
