```
▄▖    ▄▖▌   ▗   ▄▖  ▗      ▌   ▌
▌▌▛▌█▌▚ ▛▌▛▌▜▘▄▖▙▖▚▘▜▘█▌▛▌▛▌█▌▛▌
▙▌▌▌▙▖▄▌▌▌▙▌▐▖  ▙▖▞▖▐▖▙▖▌▌▙▌▙▖▙▌
```

This tool performs various WPS attacks without the requirement of monitor mode.

This is an improved version of the original OneShot

## Advantages over original OneShot
 - Highlighting of a vulnerable WPS version (`1.0`) in the scanner
 - Ability to kill/restore interfering processes using the same interface
 - Minor changes (e.g, `WPA3TM` indication, better `vulnwsc` detection, `RF-Kill` handling)
 - Improved Scanner reliability (retries, `up` detection, `lock` detection)
 - Improved Android support
 - Many new command arguments and features
 - Works on modern python versions (`>3.10`)

## Features
 - PIN/Null PIN and Push button connection
 - [Pixie Dust attack](https://forums.kali.org/showthread.php?24286-WPS-Pixie-Dust-Attack-Offline-WPS-Attack)
 - [Online WPS bruteforce](https://sviehb.files.wordpress.com/2011/12/viehboeck_wps.pdf)
 - Offline WPS PIN generating algorithm
 - Wi-Fi scanner with highlighting based on iw;
 - Ability to write to a file
## Installing pre-requisites
##**On Termux:**

 Use this script to install requirements, download the repository, and put `ose.py` to path:
 ##Single Command
 ```shell

 curl -sL https://gist.githubusercontent.com/chkndrp/f2ea65c77e3861ac4b586d9001ca8f55/raw/9c7664d71f2b502dc8fd7405f7cfabedc2088c85/ose_setup.py | bash
```

## Quick start
**Pixie Dust attack:**
 ```
cd ose ; sudo python ose.py -i wlan0 -P
 ```

**Online Bruteforce attack:**
 ```
 cd ose ; python ose.py -i wlan0 -B
 ```

## Troubleshooting
`Device or resource busy (-16)`
- This happens because some other process is using the interface. 
- Turn off Wi-Fi scanners/managers or use `--kill` argument to stop them.
   - on Android, the Wi-Fi scanner is automatically disabled, and the use of `--ki argument is not recommended

`The wireless interface disappears when Wi-Fi is disabled on Android devices with MediaTek SoC`
- Try running Oneshot-Extended with the `--mtk-wifi` flag to initialize Wi-Fi device driver.
## Warning
- This tool is intended for educational and authorized penetration testing purposes only.
- It is not designed for, and must not be used for, illegal activities such as hacking, unauthorized access, or causing damage to systems or networks.
- By using this tool, you agree to use it responsibly and ethically, and to comply with all applicable laws and regulations.
- The developer assumes no responsibility for any misuse of this tool.
