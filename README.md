# Run this script

## Modify the script and add your public key to it

## Create a virtual environment

```bash
python3 -m venv /path/to/your/directory/where/the/script/is
```

### Run the virtual environment

```bash
source ./bin/activate
```

### Install the dependencies

```bash
pip install -r requirements.txt
```

### Test run

```bash
python3 ./airdroptokens.py
```

You should see a response with a timestamp, if there are any errors you will see it too and just ping me in the discord.

## MacOS

## create a .plist file

I'm not gonna share it here, you can google how to do that or ask chat gpt.

## launch the script

Open a terminal.
Run the following command to load the service:

```bash
sudo launchctl load <p.list> file
```

You need to unload the file first and then load it again before you make changes

```bash
sudo launchctl unload <p.list> file
```

# solanadevnetautomaticairdrop
