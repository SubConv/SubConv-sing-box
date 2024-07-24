#!/usr/bin/env python3
#coding=utf-8
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import FileResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

import httpx

from pathlib import Path
import os
import re
import argparse

DISALLOW_ROBOTS = bool(eval(os.environ.get("DISALLOW_ROBOTS", "False")))

if __name__ == "__main__":
    class GenerateConfigAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if values in ("default", "zju"):
                from config import generate_default_config
                generate_default_config(values)
                parser.exit(0)
            else:
                print("Invalid default config type")
                parser.print_help()
                parser.exit(1)

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", "-P", type=int, default=8000, help="port of the api, default: 8000")
    parser.add_argument("--host", "-H", type=str, default="0.0.0.0", help="host of the api, default: 0.0.0.0")
    parser.add_argument("--generate-config", "-G", type=str, choices=("default", "zju"), action=GenerateConfigAction, help="generate a default config file")
    args = parser.parse_args()

     # init config
    from config.config import config_instance
    if config_instance is None:
        print("Failed to load config.json, exiting")
        exit(1)

    module_name = __name__.split(".")[0]
    uvicorn.run(f"{module_name}:app", host=args.host, port=args.port, workers=4)

from generate import get_config
from parse import get_nodes
from type import outbound

import json

app = FastAPI()

# mainpage
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
async def mainpage():
    return FileResponse("static/index.html")

# /robots.txt
@app.get("/robots.txt")
async def robots():
    if DISALLOW_ROBOTS:
        return Response(content="User-agent: *\nDisallow: /", media_type="text/plain")
    else:
        return Response(status_code=404)
    
# subscription converter api
@app.get("/sub")
async def sub(request: Request):
    args = request.query_params

    # get the url of original subscription
    url = args.get("url")
    tun: bool = args.get("tun", True)

    url = re.split(r"[|\n]", url)
    # remove empty lines
    urls = list(filter(lambda x: x!="", url)) 

    # get the nodes from original subscription
    nodes = []
    for url in urls:
        if url.startswith("http://") or url.startswith("https://") and not url.startswith("https://t.me"):
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers={"User-Agent": request.headers["User-Agent"]})
                nodes.extend(get_nodes(response.text))
        else:
            nodes.extend(get_nodes(url))

    # get the config from nodes
    config = get_config(nodes=nodes, base_url=request.base_url, tun=tun)

    tmp = config.model_dump(exclude_none=True)

    # return Response(json.dumps(config.model_dump(exclude_none=True), indent=2, ensure_ascii=True), headers={"Content-Type": "application/json; charset=utf-8"})
    return Response(config.model_dump_json(exclude_none=True, indent=2), media_type="application/json; charset=utf-8")

# proxy
@app.get("/proxy")
async def proxy(request: Request, url: str):
    # file was big so use stream
    async def stream():
        async with httpx.AsyncClient() as client:
            async with client.stream("GET", url, headers={"User-Agent":request.headers["User-Agent"]}) as resp:
                yield resp.status_code
                yield resp.headers
                if resp.status_code < 200 or resp.status_code >= 400:
                    yield await resp.aread()
                    return
                async for chunk in resp.aiter_bytes():
                    yield chunk
    streamResp = stream()
    status_code = await streamResp.__anext__()
    headers = await streamResp.__anext__()
    if status_code < 200 or status_code >= 400:
        raise HTTPException(status_code=status_code, detail=await streamResp.__anext__())
    return StreamingResponse(streamResp, media_type=headers['Content-Type'])

# static files
@app.get("/{path:path}")
async def index(path):
    if Path("static/"+path).exists():
        return FileResponse("static/"+path)
    else:
        raise HTTPException(status_code=404, detail="Not Found")
