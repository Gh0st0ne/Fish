# Fish 1.0.0

![Fish](https://i.imgur.com/nQ45dEy.png "Fish")

[TOC]
## About
Fish is a phishing tool that inhabits a collection of webpages *(currently only Outlook)*. It tries to replicate webpages as closely as possible for a hard to distinguish phishing page.
## Features
#### Outlook
- Up-to-date outlook phishing page
- Easily configurable, with a startup script
- Has a menu that can be used to select the up-coming options.
- Can use any domain including but not limited to `Ngrok`, `Freenom`, `GoDaddy` etc.
- Has built-in option to install and use ngrok for a free public domain
- Uses flask. Has options in the start-up script to configure the host and port.

## Installation 
#### Clone the repo:
`$ git clone https://github.com/aarav2you/Fish.git`


------------

#### Go into the repo:
`$ cd Fish/`

------------

#### Run main.py
`$ pip install -r requirements.txt`

`$ python main.py`

------------

## Great! How do I use it?
You can specify the values it asks for when executing the `app.py`. Leaving the settings on default is the best option (just press ⏎). Refer to the table below for all values:

| `Enter redirect URL` 	| The link it will redirect the victim to after credentials have been logged in `Log.txt`. `Default: https://www.office.com/?auth=2` 	|
|----------------------	|-------------------------------------------------------------------------------------------------------------------------------------	|
| `Flask server host`  	| The local IP your flask server will run on. `Default: 127.0.0.1`                                                                    	|
| `Flask server port`  	| The port your flask server will run on. `Default: 80`                                                                               	|
| `Use ngrok`          	| This uses `nGrok`to to forward the phishing page to a public domain. More on this [here][1]. `Default: n`                                                   	|

## Contribution
We have built this with our ❤️. If you would like to contribute, please fork our project and send us a pull request for the [Dev][2] branch. If you would like to suggest, please open an issue with the label **Enhancement**.

## Authors
Made lovingly by [aarav2you][3] and [Kritagyaispro][4]
###### More to come soon...

[1]: https://ngrok.com "here"
[2]: https://github.com/aarav2you/Fish/tree/dev "Dev"
[3]: https://github.com/aarav2you "aarav2you"
[4]: https://github.com/Kritagyaispro "Kritagyaispro"