
# Pepal auto Signature

A simple python script to automaticly sign you presence on [pepal.eu](https://pepal.eu).<br />
Un script pour signer automatiquement votre présence sur [pepal.eu](https://pepal.eu).

<div id="header" align="center">
  <img src="https://www.pepal.eu/images/logo_login_2.png"> 
</div>

## Installation - Setup

1. Clone the repo

```bash
git clone https://github.com/Nv3l/Pepal.eu-Sign.git
```

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Replace the credentials variable within you own

```python
  username = "etu.callard"
  password = "CPasClaire1234"
```

> This script was tested on Python 3.8.5

## Run Automatically



Clone the project

> You can use different method depending on your operating system.

- **Linux / crontab**

```bash
4 9-11,13-15 * * * python /your/directory/Pepal.eu-Sign/pepalSign.py
```
 
---

 


- **Windows**

You can use the *Windows Task Scheduler* or alternatively **[Z-cron](https://z-dbackup.de/en/z-cron-scheduler/)**.

```bash
python C:\your\directory\Pepal.eu-Sign\pepalSign.py
```


---


However, you can compile it into a .exe file using pyinstaller

```bash
pip install -U pyinstaller
```

```bash
pyinstaller --onefile pepalSign.py
```
> It would generate a pepalSign.exe file that you can run directly. Or, specify it with your favorite application.

 
## Support

For support, you can contact me on Discord : `Chicoch#7678`
  
## Disclaimer

This script is for educational purposes only.

