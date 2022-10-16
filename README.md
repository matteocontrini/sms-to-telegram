Installation notes for Raspberry Pi OS (Debian 11 bullseye):

Add to `/etc/apt/sources.list`:

```
deb http://deb.debian.org/debian bullseye-backports main contrib non-free
```

Install Gammu dev files (gammu shouldn't be actually required):

```
sudo apt update
sudo apt install gammu libgammu-dev
```

Install Python dependencies:

```
pipenv install
```

Install `uhubctl`:

```
sudo apt install libusb-1.0-0-dev
git clone https://github.com/mvp/uhubctl
cd uhubctl
make
sudo make install
```

Run with:

```
export TELEGRAM_BOT_TOKEN=
export TELEGRAM_CHANNEL_ID=
pipenv run python3 app.py
```
