# fact-collector

Autocomplete interface powered by Tries. Can insert records and insert into itself.

* Type "I ate a"  then use arrow keys to control selected item. Press enter to insert into textarea.
* When you have fulfilled all variables, press tab and press enter on save.

* [Mirrored](https://jsfiddle.net/8nat61g5/13/)

# Install

Create a database called `forum` with password `forum`:

```
virtualenv -p $(which python3) venv
source venv/bin/activate
python install.py # once for database population
pip install -r requirements.txt
./run.sh
```
