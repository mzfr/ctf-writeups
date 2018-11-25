# Miss Scarlet's <br> Resume Requests

__PROBLEM__

Something is up with Miss's Scarlet's acting site. Maybe you can take a look?

http://18.220.239.106/

__SOLUTION__

We head over to the URL and then to `contact.php` and notice we have to find Mr. Boddy again. Remember `Mrs. White's messy maids`. The first thing we try is `http://18.220.239.106/Boddy/` and gets:

```
That was a really good try...Did you think it would be that easy?
```

Now looking at the source of this page:

```html
<html>
        <head>
                <title>Not a Clue</title>
                <style>
                        body {
                                background-color: #8B0000;
                                margin: 0;
                                padding: 0;
                                font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

                        }
                        div {
                                width: 600px;
                                margin: 5em auto;
                                padding: 50px;
                                background-color: #fff;
                                border-radius: 1em;
                        }
                        a:link, a:visited {
                        color: #38488f;
                        text-decoration: none;
                        }
                        @media (max-width: 700px) {
                                body {
                                        background-color: #fff;
                        }
                                div {
                                        width: auto;
                                        margin: 0 auto;
                                        border-radius: 0;
                                        padding: 1em;
                                }
                        }
                </style>
        </head>
    <body>
        <h2>That was a really good try...Did you think it would be that easy?
        <!--Maybe look into how easy it would be to receive some tissues in the 'post'--></h2>
    </body>
</html>
```

Notice in the last thing there is a word `post` and the name of this prblem also have something related to `requests`. So we send a `post` request to this URL .

FLAG - `TUCTF{1_4ccu53_m155_5c4rl37_w17h_7h3_kn1f3_1n_7h3_h77p_r3qu357}`
