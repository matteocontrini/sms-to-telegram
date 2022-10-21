Installation notes for Raspberry Pi OS (Debian 11 bullseye):

Add to `/etc/apt/sources.list`:

```
deb http://deb.debian.org/debian bullseye-backports main contrib non-free
```

Install Gammu dev files (gammu shouldn't be actually required):

```shell
sudo apt update
sudo apt install gammu libgammu-dev
```

Install Python dependencies:

```shell
pipenv install
```

Install `uhubctl`:

```shell
sudo apt install libusb-1.0-0-dev
git clone https://github.com/mvp/uhubctl
cd uhubctl
make
sudo make install
```

Run with:

```shell
export TELEGRAM_BOT_TOKEN=
export TELEGRAM_CHANNEL_ID=
pipenv run python3 app.py
```

Create the cron job:

```
* * * * * cd /home/pi/apps/sms-to-telegram && ./run.sh 2>&1 | tee -a sms.log
```

To make the Huawei K5160 modem work with this script, create the file `/etc/usb_modeswitch.d/12d1:1f1e`:

```
# Vodafone / Huawei K5160
TargetVendor=0x12d1
TargetProductList="157f,1592"
MessageContent=55534243123456780000000000000011063000000100000000000000000000
NoMBIMCheck=1
```
