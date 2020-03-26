# Tor Bridge

## about
You can get new bridges with Tor Bridges. bypassing tor captcha and get bridges

## run
-  `tor --hash-password my_password`
-  `sudo gedit /etc/tor/torrc`
-  ```
    # add to config file
    ControlPort 9051
    HashedControlPassword YOUR_HASH_PASSWORD
    CookieAuthentication 1
    ```
 - `you must add my_password to file  config_add.py` 
- ```
    # Debian
    sudo service tor restart 
    # arch
    sudo systemctl restart tor.service
    ```
