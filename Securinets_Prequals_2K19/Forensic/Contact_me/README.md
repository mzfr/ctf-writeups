# Contact me

__PROBLEM__

People think it's hard to stay without a phone, but I don't! My computer has everything a smartphone has like browsers, notes, calendars, and a lot more.

[Link](http://www.mediafire.com/file/1x0ynlrcg3gc0t1/contact_me.zip/file)

__SOLUTION__

First I was trying lot of big guns like volatility and testdisk and all of those were failing and then admin said stick to the basics.

So basics of forensics are `exiftool` or `strings`, now exiftool didn't gave anything worth so I tried `strings`

```bash
➜ strings contact_me | grep -i -C 20 "securinets"

 Tuuid^teamIdentifierWoptionsWversionZwebpageURL_
eligibleForSearch_
dynamicActivityType\activityType_
eligibleForPublicIndexingTtypeUtitle]contentAction^expirationDateXkeywords_
eligibleForHandoffV$class\payloadError_
eligibleForReminders
012WNS.keysZNS.objects
4567Z$classnameX$classes\NSDictionary
68XNSObject_
;c2VjdXJpbmV0c3szMTAxMmUxNmMzZTVkZmE3ZTY3MzYxMmQ3ZDA3NTcxNX0_
com.apple.Notes.sharesheetP
45=>_
UAUserActivityInfo
UAUser_
--

```

There's this base64 strings which is long enough to be the flag.

```bash
➜ echo "c2VjdXJpbmV0c3szMTAxMmUxNmMzZTVkZmE3ZTY3MzYxMmQ3ZDA3NTcxNX0" | base64 -d
securinets{31012e16c3e5dfa7e673612d7d075715}
```
FLAG - `securinets{31012e16c3e5dfa7e673612d7d075715}`
