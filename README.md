# Wordpress-FastApi
<p align="center">

</p>
<p align="center">
    <em>FastAPI To Consime woocomerce API , high performance, easy to learn, fast to code, ready for production</em>
</p>



## Installation

<div class="termy">

```console

$ python3 -m virtualenv -p python3 .
$ source bin/activate
$ pip install -r requirements.txt

---> 100%
```

</div>



</div>



### Create it

* Create a file `main.py` with:



```Python hl_lines="9  14"
from fastapi import FastAPI
from woocommerce import API
import os
import json
import base64 # the easieast way to send a url as param :)

app = FastAPI()
@app.get("/wordpress/{consumerKey}/{consumerSecret}/{site}")
def  getter(consumerKey,consumerSecret,site):
	try:
		wcapi = API(
			url=base64.b64decode(site),
			consumer_key=consumerKey,
			consumer_secret=consumerSecret,
			version="wc/v3"
		)
		return {"products": wcapi.get("products").json()}
	except:
		return {"Error": " Please verify parameters"}
```

**Note**:

This is used by calling 
http://server:port/wordpress/consumer_key/consumer_secret/url_encoded
where
	server = ip address ( 127.0.0.1 in dev mode )
	port 	= fast api operating port ( 8000 by default )
	consumer_key = obtained from WooCommerce API in wordpress 
	consumer_secret = obtained from WooCommerce API in wordpress 
	url_encoded = base64.encode(URL_TO_Wordpress)
	

</details>

### Run it

Run the server with:

<div class="termy">

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>About the command <code>uvicorn main:app --reload</code>...</summary>

The command `uvicorn main:app` refers to:

* `main`: the file `main.py` (the Python "module").
* `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
* `--reload`: make the server restart after code changes. Only do this for development.

</details>


The server should reload automatically (because you added `--reload` to the `uvicorn` command above).



## License

This project is licensed under the terms of the GPL license.