# Tor Bridge

## about
You can get new bridges with Tor Bridges. bypassing tor captcha and get bridges

## run
-  `tor --hash-password my_password`
-  `sudo gedit /etc/tor/torrc`
-  ```
    ControlPort 9051
    HashedControlPassword YOUR_HASH_PASSWORD
    CookieAuthentication 1
    ```
