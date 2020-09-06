from fastapi import FastAPI
from woocommerce import API
import os 
import json
import base64

app = FastAPI()


@app.get("/wordpress/{consumerKey}/{consumerSecret}/{site}")
def getter(consumerKey,consumerSecret,site):
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




