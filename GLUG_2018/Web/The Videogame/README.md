# The Videogame

__PROBLEM__

One fine day,Rocket Raccoon found the video game that Groot was so obsessed with.Unfortunately,Groot had set a password on it. In the password hint,he had provided [link](http://104.248.49.223:7071/) to a website. Raccoon could not find anything in the website. Can you help him find it, so that he can play the videogame?

__HINT__

click [here](https://en.wikipedia.org/wiki/HTTP_cookie)

__SOLUTION__

As you can see that the hint takes you to `HTTP cookie` wiki page that means it has to do something with cookies. So Just open the developers tool in your browser and reload the page and then in `storage` section of the developer tools you'll see a `cookie` with name `user` which is set to `unknown`.

Okay we have the cookie now but how will this be helpful? well if you noticed that as you visit the given link it written `I am gROOT` see that capitalization on `ROOT` that means this will give acess to `ROOT` so just change the `user: unknown` in the cookie we found to `user: ROOT` and reload the page.

Flag - `GLUG{I_@m_7r55t}`
