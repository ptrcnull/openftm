# openftm

Open-source implementation of FortiToken's TOTP algorithm.

You can extract the actual TOTP seed and use it with apps like [KeePassXC](https://keepassxc.org/) or [andOTP](https://github.com/andOTP/andOTP), make sure to set the period to 60 seconds.

## Prequisites

For this to work, you need to extract 2 things - [SSAID](https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID) and encrypted seed.
This needs root access on your Android device.

### SSAID

Run this command in a rooted shell:
```
# grep com.fortinet /data/system/users/0/settings_ssaid.xml                                                                 
```

Output should look like this:
```xml
<setting id="32" name="10309" value="12dddfc4a3b45678" package="com.fortinet.android.ftm" defaultValue="12dddfc4a3b45678" defaultSysSet="false" tag="null" />
```

Copy the value from quotes and paste it to the script as `android_ssaid`.

### Seed

The seed is stored in app's database: `/data/data/com.fortinet.android.ftm/databases/FortiToken.db`
You can copy the file and open it with an SQLite3 editor, or run this command: (I know it's ugly, but does the job)
```
# grep -Eao 'totp.{64}' /data/data/com.fortinet.android.ftm/databases/FortiToken.db | cut -c5-
```
Copy the output and paste it as `seed`.

## Usage

Install requirements with `pip3 install -U -r requirements.txt`, then run with `python3 generate.py`.

## Disclaimer

All product and company names are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.
