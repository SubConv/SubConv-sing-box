from .util import uniqueName, RandUserAgent
from type.common import Tls, Reality, Utls
from type.common.v2transport import Http, Websocket, Grpc, Httpupgrade
from type.outbound import Outbound

import urllib.parse as urlparse

def handleVShareLink(names: dict[str, int], url: urlparse.ParseResult, scheme: str, node: dict):
    # Xray VMessAEAD / VLESS share link standard
	# https://github.com/XTLS/Xray-core/discussions/716
    query = dict(urlparse.parse_qsl(url.query))
    node["tag"] = uniqueName(names, urlparse.unquote_plus(url.fragment))
    if url.hostname == "":
        raise Exception("hostname is empty")
    if url.port == "":
        raise Exception("port is empty")
    node["server"] = url.hostname
    node["server_port"] = url.port
    node["uuid"] = url.username
    tls = query.get("security", "").lower()
    if tls.endswith("tls") or tls == "reality":
        node["tls"] = Tls(
            server_name=query.get("sni"),
            alpn=query.get("alpn") and query.get("alpn").split(","),
            utls=Utls(fingerprint=query.get("fp", "chrome"))
        )
        if tls == "reality":
            node["tls"].reality = Reality(
                public_key=query.get("pbk"),
                short_id=query.get("sid")
            )
    
    switch = query.get("packetEncoding", "")
    if switch == "none" or switch == "":
        pass
    elif switch == "packet":
        node["packet_encoding"] = "packetaddr"
    elif switch == "xudp":
        node["packet_encoding"] = "xudp"

    network = query.get("type", "").lower()
    if network == "tcp":
        pass # not supported by sing-box
    if network == "http":
        headers = {}
        headers["User-Agent"] = RandUserAgent()
        host = query.get("host")
        path = query.get("path", "/")
        node["transport"] = Http(
            host=[host] if host else None,
            path=path,
            headers=headers
        )
    if network == "ws":
        headers = {}
        headers["User-Agent"] = RandUserAgent()
        if query.get("host"):
            headers["Host"] = query.get("host")
        node["transport"] = Websocket(
            path=query.get("path"),
            headers=headers,
            early_data_header_name=query.get("eh", "Sec-WebSocket-Protocol")
        )
        earlyData = query.get("ed")
        if earlyData:
            try:
                med = int(earlyData)
                node["transport"].max_early_data = med
            except:
                raise Exception(f"bad WebSocket max early data size: {earlyData}")
    if network == "httpupgrade":
        headers = {}
        headers["User-Agent"] = RandUserAgent()
        node["transport"] = Httpupgrade(
            host=query.get("host"),
            path=query.get("path"),
            headers=headers
        )
    if network == "grpc":
        node["transport"] = Grpc(
            service_name=query.get("serviceName")
        )
