# openftm

Open-source implementation of FortiToken's TOTP algorithm.

You can extract the actual TOTP seed and use it with apps like [KeePassXC](https://keepassxc.org/) or [andOTP](https://github.com/andOTP/andOTP), make sure to set the period to 60 seconds.

## Prequisites

For this to work, you need to extract 3 things - [SSAID](https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID), UUID and encrypted seed.
This needs root access on your Android device.

### SSAID

#### Android 8.0+
For Android 8.0+ SSAID is unique for every installed app, to get value for FTM run this command in a rooted shell:
```
# grep com.fortinet /data/system/users/0/settings_ssaid.xml                                                                 
```

Output should look like this:
```xml
<setting id="32" name="10309" value="eefd7d4837294e94" package="com.fortinet.android.ftm" defaultValue="eefd7d4837294e94" defaultSysSet="false" tag="null" />
```

#### Android versions before 8.0

For previous versions of Android SSAID is the same for all apps to get it run following command
```
# grep android_id /data/system/users/0/settings_secure.xml
```

```xml
  <setting id="31" name="android_id" value="eefd7d4837294e94" package="android" />
```

Copy the value from quotes and paste it to the script as `DEVICE_ID`.

### UUID

The encrypted UUID is stored in the UUID key of the XML file stored at /data/data/com.fortinet.android.ftm/shared_prefs/FortiToken_SharedPrefs_NAME.xml.

```
grep UUID /data/data/com.fortinet.android.ftm/shared_prefs/FortiToken_SharedPrefs_NAME.xml
    <string name="UUID">N7gAr30eX72sR2owbVR4WrFiw4e3ignGBO6IcgA4qJjvBYjZvIxZXIMTHOix8QDt</string>
```

Copy the value paste it to the script as `UUID`.

### Seed

The seed is stored in app's database: `/data/data/com.fortinet.android.ftm/databases/FortiToken.db`
You can copy the file and open it with an SQLite3 editor,

```
$ sudo sqlite3 /data/data/com.fortinet.android.ftm/databases/FortiToken.db 'SELECT seed FROM Account WHERE type="totp"'
MNmAN7drtlNJxjFqo5bgSN/DZcdWVK9Qv1YyUP3OjuJkDXgV06siQYlQfO0678Lg
```

or run this command: (I know it's ugly, but does the job)
```
# grep -Eao 'totp.{64}' /data/data/com.fortinet.android.ftm/databases/FortiToken.db | cut -c5-
MNmAN7drtlNJxjFqo5bgSN/DZcdWVK9Qv1YyUP3OjuJkDXgV06siQYlQfO0678Lg
```

Copy the output and paste it as `SEED`.


## Usage

Install requirements with `pip3 install -U -r requirements.txt`, then run with `python3 generate.py`.

```
$ python3 generate.py
UUID KEY: eefd7d4837294e94unknown
UUID: bbc350195b88433dbcc7365cdbd130e5
SEED KEY: eefd7d4837294e94unknownbbc350195b88433dbcc7365cdbd130e5
TOTP SECRET: DEADBEEFDEADBEEFDEADBEEFDEADBEEF
Current TOTP: 779726
```

Printed TOTP SECRET is base32-encoded and can be used to setup TOTP codes in other authenticator applications like: KeePassXC, andOTP, SailOTP, Numberstation. Make sure to set the period to *60 seconds*.

## Disclaimer

All product and company names are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.
