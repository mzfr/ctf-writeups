# Referals

__PROBLEM__

Misha recently got placed at Google.So she started refering her friends for incoming job posts in the company.She hid a secret in this [website](104.248.49.223:8081) for those who got the job after her referal.The secret contains the place where she and her friends will be having party for their new jobs.

Minan is Misha's boyfriend.Minan wants to reach Misha asap.Since Minan didnt get a job at google and is a noob,Can you help him figure out the location?

__HINT__

click [here](https://en.wikipedia.org/wiki/HTTP_referer)

__SOLUTION__

After checking out the hint you'll see that it has to something to do with `Referer` value in the `HEADERS` of the requests send. So for that we just open the `Networks` tab in our developers tool of browser, reload the page edit the requests send from
```
Host: 104.248.49.223:8081
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: user=unknown
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
```

to
```
Host: 104.248.49.223:8081
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: user=unknown
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Referer: https://www.google.com
```

then send this request and you'll have the flag. All we did was add a `Referer`value in the request.

Flag - `GLUG{Refendrum_@_007}`
