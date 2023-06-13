# Twitter Royale with [Supabase](https://supabase.com/)
## Install libraries
The libraries installed in this project are 

 ![pyVersion310](https://img.shields.io/badge/Tweepy-4.10.0-blue.svg) 
 ![pyVersion310](https://img.shields.io/badge/Supabase-0.5.6-green.svg)
 ![pyVersion310](https://img.shields.io/badge/Pillow-9.1.1-red.svg)
 ![pyVersion310](https://img.shields.io/badge/Python-3.10-yellow.svg)

You can install all dependecies with
``` bash
pip install -r requireInstall.txt
```

#  Supabase database table
Column of table  *EXAMPLE_TABLE*
* id [ bigint, int8 ] NOT NULL
* character_id [ bigint int8 ] NOT NULL
* season [ bigint, int8 ] NULL
* name [ character varying, varchar ] NOT NULL
* image [ character varying, varchar ] NOT NULL
* killer_id [ bigint, int8 ] NULL

# Fill the keys 
Please fill all the json from *royale_example.json* or create another file with this dicts, then locate the file. The next step explain how to do it. 
# How to call the keys
The file *call_keys.py* need the keys via arguments or path, you can do either
###  Way 1 - 'paths' variable
``` bash
paths = "example/royale_example.json"
keys = getKeysFromPath(paths)
```
Terminal:
``` bash
python supabaseRoyale.py
```
###  Way 2 - arguments
``` bash
keys = getKeysFromArguments()
```
Terminal:
``` bash
python supabaseRoyale.py ./royale_example.json
```
