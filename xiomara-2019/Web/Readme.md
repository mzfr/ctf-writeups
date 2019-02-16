# URL

__PROBLEM__

This web server has been behaving weirdly. Might be a hacker left something there.

IP: http://34.73.70.190/


__SOLUTION__

This is the challenge that was taken from OTA without their permission and the creator didn't even cleared the source.

```html
<!DOCTYPE HTML>

<html>
  <head>
    <title>EZ Flag Reloaded</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <style>
      body, html { height: 100%; }
      .corb-centered {
        position: relative;
        left: 50%;
        /* bring your own prefixes */
        transform: translate(-50%, 25%);
      }
      .corb-ez-flag {
        max-width: 50%;
      }
      .corb-big-ass-button {
        width: 50%;
      }
    </style>
   <meta charset="UTF-16">
  </head>
  <body>
    <div class="corb-centered corb-ez-flag text-center">
      <h1>Xiomara 2k19</h1>
      <br/>
      <h2>Do you want another flag ???</h2>
      <br/>
      <h3>I think you do! ✯⸜(ّᶿ̷ധّᶿ̷)⸝✯ </h3>
      <br/>
      <br/>
      <h2>Ok then... Click here to get your flag! (－ｏ⌒)</h2>
      <br/>
      <a href="/can_y#u_get_the_flag?!" class="corb-big-ass-button btn btn-lg btn-success">Get the flag!</a>
    </div>
  </body>
</html>
```

there's `corb-big-ass-button` and lot of other `corb` hint.


Okay so the solution to this one is simple. When you click on the `Get the flag` button you'll  get `Not found` page but if you look at the URL you'll see `http://34.73.70.190/can_y#u_get_the_flag?!`. Since I already solved this challenge in OTA I knew that it simple URL decoding.

So all you have to do is replace the special symbols like:

```
# = %23
? = %3F
! = %21
```

so the URL will become: http://34.73.70.190/can_y%23u_get_the_flag%3F%21

FLAG: `xiomara{URi_Syn7@x_1s_@_g00D_thing_t0_lOOk_@t}`
