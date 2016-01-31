# check-kimsufi

A *minimal* Python script that checks continuously if a server is available to buy, and executes a command when it is.

Requires [`requests`](http://docs.python-requests.org/en/latest/). Tested with Python 3.5.

# Quickstart

```bash
cp sample.conf kimsufi.conf
vim kimsufi.conf # change the configuration options at ease
python kimsufi.py
```

# Other projects worth checking:

* [kimsufi-crawler](https://github.com/MA3STR0/kimsufi-crawler), full-fledged script with many more features

* [This fork](https://github.com/castanley/kimsufi-crawler) in particular has a up-to-date server [alias list](https://github.com/castanley/kimsufi-crawler/blob/master/mapping/server_types.json)
