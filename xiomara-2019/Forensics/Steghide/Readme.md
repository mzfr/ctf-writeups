# Steghide

__PROBLEM__

While going through bash history of one of our developers account, we found that "steghide" was used to hide something inside an image. We have tried all possible password combinations but no luck. I hope you could help us.

__SOLUTION__

Since the name of the challenge suggest that we should use [steghide](https://github.com/StefanoDeVuono/steghide) so we simply save the image and use steghide on it.

```bash
✦ ➜ steghide extract -sf stego.jpg
Enter passphrase:
wrote extracted data to "README.md".
```
Again for the passphrase I tried `xiomara` and simply got the README.md file

FLAG - `xiomara{SteGhide_is_For_Beginnners_1024!!!}`
