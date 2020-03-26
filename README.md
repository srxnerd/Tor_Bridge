# Tor Bridge

## about
You can get new bridges with Tor Bridges. bypassing tor captcha and get bridges

## config file torrc and config_add.py
-  `tor --hash-password my_password`
-  `sudo gedit /etc/tor/torrc`
-  ```
    # add to config file
    ControlPort 9051
    HashedControlPassword YOUR_HASH_PASSWORD
    CookieAuthentication 1
    ```
- ```
    ## Debian
    sudo service tor restart 
    ## arch
    sudo systemctl restart tor.service
    ```
 - `you must add my_password to file  config_add.py`
 ## for run app
 - ```
      cd TorBridges
      python Tor.py number 
      ## Example:
      python Tor.py 10
      ```
![photo_2020-03-26_12-44-49](https://user-images.githubusercontent.com/46731929/77625011-69c0ad80-6f60-11ea-8f0a-6b113bd27d4a.jpg)
