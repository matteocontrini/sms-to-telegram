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
