# Rotten

__PROBLEM__

Head over to the link below to find the flag.
[Link](https://rotplayer-glugctf.netlify.com/)

__SOLUTION__

Since nothing is given to first thing we check out is the source of theh page and what we see is:
```javascript
 document.getElementById("check").onclick = function () {
 var flag = document.getElementById("flag").value;
 var rotFlag = flag.replace(/[a-zA-Z]/g, function(c){
 return String.fromCharCode((c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26);});
 if ("TYHT{py13a7_51q3_y061a_j17u_e0713!}" == rotFlag) {
 alert("Correct flag!");
 } else {
 alert("Incorrect flag, rot again");
 }
 }
```

And here we can see that entered value is compared with `TYHT{py13a7_51q3_y061a_j17u_e0713!}`. Okay but this is not the correct flag, hey what was the name of the problem `rotten`? Well is that string encoded with `rot13`. We head over to [this](https://www.dcode.fr/rot-cipher) and gets our prize.

FLAG - `GLUG{cl13n7_51d3_l061n_w17h_r0713!}`
