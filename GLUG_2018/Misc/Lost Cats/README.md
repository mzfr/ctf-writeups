# Lost Cats

__PROBLEM__

May Lost her cat ,"Gittiy". Hope you can help her.

Here is a archive, You may help her with it.
[lostcat](lostcat-masterqs.zip)

__SOLUTION__

Extracting the given archive we get a [folder](lostcat/). There's an image but it's not the complete flag.
If you'll read the problem properly it is referring to [`git`](https://git-scm.com/).
Not just follow
```bash
>>> git show
commit 9e982686c7ae3672020e1093cf9b7a6a445fb714 (HEAD -> master, origin/master, origin/HEAD)
Author: @realsdx <realsdx@protonmail.com>
Date:   Thu Oct 18 14:51:52 2018 +0530

    Deleted a secret file

diff --git a/gitcat_full.png b/gitcat_full.png
deleted file mode 100644
index 162e002..0000000
Binary files a/gitcat_full.png and /dev/null differ

>>> git reset --soft @~1
>>> git status
On branch master
Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        deleted:    gitcat_full.png
>>> git reset HEAD gitcat_full.png
Unstaged changes after reset:
D       gitcat_full.png
>>> git checkout gitcat_full.png
```
After this you should have a file named [`gitcat_full.png`](/Lost%20Cats/lostcat/gitcat_full.png). Then you can either use [`OCR`](https://www.newocr.com/) or just write the flag out.

What happened there?
1) `git show` - we see what has been done in this repository.
2) `git reset --soft @~1` - we reset the last commit.
3) `git status` - we check what did we `undone` in 2nd step
4) `git reset HEAD gitcat_full.png` - We hard reset as in to undo the changes that were made
5) `git checkout gitcat_full.png` - we get back the deleted file.

FLAG - `GLUG{17_15_345y_70_5h007_y0ur_f007_0ff_w17h_617,_bu7_4l50_345y_70_r3v3r7_70_4_pr3v10u5_f007_4nd_m3r63_17_w17h_y0ur_curr3n7_l36}`
