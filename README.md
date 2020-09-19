# fact-collector

Autocomplete interface powered by Tries. Can insert records and insert into itself.

* Type "I ate a"  then use arrow keys to control selected item. Press enter to insert into textarea.
* When you have fulfilled all variables, press tab and press enter on save.

* prototype was written on js fiddle -> [Mirrored](https://jsfiddle.net/8nat61g5/13/)

# Prolog inference

* Prolog statements begin with "Logic"
* Prolog queries begin with "Inference"

# Install

Create a postgres database called `forum` with password `forum`:
```
CREATE DATABASE forum;
CREATE USER forum WITH PASSWORD 'forum';
GRANT ALL PRIVILEGES ON DATABASE forum to forum;
```



```
sudo apt install postgresql-server-dev-all python3-dev
virtualenv -p $(which python3) venv
source venv/bin/activate
python3 install.py # once for database population
pip install -r requirements.txt
./run.sh
```
