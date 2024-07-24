import logging
logger = logging.getLogger(__name__)

from type.common import Tls, Utls, Udp_over_tcp
# from type.common.v2transport import Websocket, Grpc, Http, Httpupgrade
from type.common import v2transport
from type.outbound import Outbound, Hysteria, Hysteria2_obfs, Hysteria2, Tuic, Trojan, Vless, Vmess, Shadowsocks, Socks, Http

from .util import RandUserAgent, uniqueName
from .v import handleVShareLink

import json
import base64
import urllib.parse as urlparse
import distutils.util
from typing import Optional

def ConvertsV2Ray(buf) -> Optional[list[Outbound]]:
    try:
        data = base64.b64decode(buf).decode("utf-8")
    except:
        try:
            data = buf.decode("utf-8")
        except:
            data = buf

    arr = data.splitlines()

    nodes = []
    names = {}

    for line in arr:
        if line.strip() == "":
            continue

        if "://" not in line:
            continue
        else:
            scheme, body = line.split("://", 1)

        scheme = scheme.lower()

        if scheme == "hysteria":
            try:
                urlHysteria = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlHysteria.query))
            name = uniqueName(names, urlparse.unquote_plus(urlHysteria.fragment))
            hysteria = {}

            hysteria["tag"] = name
            hysteria["server"] = urlHysteria.hostname
            hysteria["server_port"] = urlHysteria.port
            hysteria["up_mbps"] = query.get("up", query.get("upmbps"))
            hysteria["down_mbps"] = query.get("down", query.get["downmbps"])
            hysteria["obfs"] = query.get("obfs", "")
            hysteria["auth_str"] = query.get("auth")
            # tls = {}
            # tls["server_name"] = query.get("peer")
            # tls["insecure"] = bool(
            #     distutils.util.strtobool(query.get("insecure"))
            # )
            # tls["alpn"] = query.get("alpn") and query.get("alpn").split(",")
            # hysteria["tls"] = Tls(**tls)
            hysteria["tls"] = Tls(
                server_name=query.get("peer"),
                insecure=bool(distutils.util.strtobool(query.get("insecure"))),
                alpn=query.get("alpn") and query.get("alpn").split(",")
            )

            nodes.append(Hysteria(**hysteria))

        if scheme == "hysteria2" or scheme == "hy2":
            try:
                urlHysteria2 = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlHysteria2.query))
            name = uniqueName(names, urlparse.unquote_plus(urlHysteria2.fragment))
            hysteria2 = {}

            hysteria2["tag"] = name
            hysteria2["server"] = urlHysteria2.hostname
            hysteria2["server_port"] = urlHysteria2.port or 443
            if query.get("obfs"):
                hysteria2["obfs"] = Hysteria2_obfs(
                    type=query.get("obfs"),
                    password=query.get("obfs-password")
                )
            hysteria2["password"] = urlHysteria2.username + (f":{urlHysteria2.password}" if urlHysteria2.password else "")
            hysteria2["tls"] = Tls(
                server_name=query.get("peer") or query.get("sni"),
                insecure=bool(distutils.util.strtobool(query.get("insecure"))),
                alpn=query.get("alpn") and query.get("alpn").split(",")
            )

            nodes.append(Hysteria2(**hysteria2))

        if scheme == "tuic":
            try:
                urlTUIC = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlTUIC.query))

            tuic = {}
            
            tuic["tag"] = uniqueName(names, urlparse.unquote_plus(urlTUIC.fragment))
            tuic["server"] = urlTUIC.hostname
            tuic["server_port"] = urlTUIC.port
            tuic["uuid"] = urlTUIC.username
            tuic["password"] = urlTUIC.password
            tuic["congestion_control"] = query.get("congestion_control")
            tuic["udp_relay_mode"] = query.get("udp_relay_mode")
            tuic["tls"] = Tls(
                server_name=query.get("sni"),
                disable_sni=bool(distutils.util.strtobool(query.get("disable_sni"))),
                alpn=query.get("alpn") and query.get("alpn").split(",")
            )

            nodes.append(Tuic(**tuic))

        if scheme == "trojan":
            try:
                urlTrojan = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlTrojan.query))

            name = uniqueName(names, urlparse.unquote_plus(urlTrojan.fragment))
            trojan = {}

            trojan["tag"] = name
            trojan["server"] = urlTrojan.hostname
            trojan["server_port"] = urlTrojan.port
            trojan["password"] = urlTrojan.username
            trojan["tls"] = Tls(
                server_name=query.get("sni"),
                insecure=bool(distutils.util.strtobool(query.get("allowInsecure"))),
                alpn=query.get("alpn") and query.get("alpn").split(","),
                utls=Utls(fingerprint=query.get("fp", "chrome"))
            )

            network = query.get("type", "").lower()
            if network == "ws":
                headers = {}
                headers["User-Agent"] = RandUserAgent()
                trojan["transport"] = v2transport.Websocket(
                    path=query.get("path"),
                    headers=headers
                )
            elif network == "grpc":
                trojan["transport"] = v2transport.Grpc(
                    service_name=query.get("serviceName")
                )

            nodes.append(Trojan(**trojan))

        if scheme == "vless":
            try:
                urlVless = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlVless.query))
            vless = {}

            try:
                handleVShareLink(names, urlVless, scheme, vless)
            except Exception as e:
                logger.debug(f"handleVShareLink: {e}")
                continue
            vless["flow"] = query.get("flow")

            nodes.append(Vless(**vless))

        if scheme == "vmess":
            # V2RayN-styled share link
			# https://github.com/2dust/v2rayN/wiki/%E5%88%86%E4%BA%AB%E9%93%BE%E6%8E%A5%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E(ver-2)
            try:
                dcBuf = base64.b64decode(body)
            except:
                # Xray VMessAEAD share link
                try:
                    urlVMess = urlparse.urlparse(line)
                except:
                    continue
                query = dict(urlparse.parse_qsl(urlVMess.query))
                vmess = {}
                try:
                    handleVShareLink(names, urlVMess, scheme, vmess)
                except:
                    continue
                vmess["security"] = query.get("security", "auto")
                vmess["alter_id"] = 0
                nodes.append(Vmess(**vmess))
                continue

            values = {}
            try:
                values = json.loads(dcBuf)
            except:
                continue

            try:
                tempName = values["ps"]
            except:
                continue
            vmess = {}
            vmess["tag"] = uniqueName(names, tempName)
            vmess["server"] = values["add"]
            vmess["server_port"] = values["port"]
            vmess["uuid"] = values["id"]
            vmess["security"] = values.get("scy", "auto")
            vmess["alter_id"] = values.get("aid", 0)

            # not sure how to get this value
            # behave the same as hihomo
            vmess["packet_encoding"] = "xudp"

            tls = values.get("tls")
            if tls and tls.endwith("tls"):
                vmess["tls"] = Tls(
                    server_name=values.get("sni"),
                    alpn=values.get("alpn") and values.get("alpn").split(","),
                    utls=Utls(fingerprint=values.get("fp", "chrome"))
                )

            network = values.get("net", "").lower()
            # not sure how to handle "h2"
            if network == "http" or network == "h2":
                headers = {}
                headers["User-Agent"] = RandUserAgent()
                host = values.get("host")
                path = values.get("path", "/")
                vmess["transport"] = v2transport.Http(
                    host=[host] if host else None,
                    path=path,
                    headers=headers
                )
            elif network == "ws":
                headers = {}
                headers["User-Agent"] = RandUserAgent()
                if values.get("host"):
                    headers["Host"] = values.get("host")
                vmess["transport"] = v2transport.Websocket(
                    path=values.get("path"),
                    headers=headers
                )
                if values.get("path"):
                    pathURL = urlparse.urlparse(values.get("path"))
                    query = dict(urlparse.parse_qsl(pathURL.query))
                    earlyData = query.get("ed")
                    try:
                        med = int(earlyData)
                        vmess["transport"].max_early_data = med
                        vmess["transport"].early_data_header_name = query.get("eh", "Sec-WebSocket-Protocol")
                    except:
                        continue
            elif network == "httpupgrade":
                headers = {}
                headers["User-Agent"] = RandUserAgent()
                vmess["transport"] = v2transport.Httpupgrade(
                    host=values.get("host"),
                    path=values.get("path"),
                    headers=headers
                )
            elif network == "grpc":
                vmess["transport"] = v2transport.Grpc(
                    service_name=values.get("path")
                )

            nodes.append(Vmess(**vmess))

        if scheme == "ss":
            try:
                urlSS = urlparse.urlparse(line)
            except:
                continue

            ss = {}
            ss["tag"] = uniqueName(names, urlparse.unquote_plus(urlSS.fragment))

            port = urlSS.port
            if not port:
                try:
                    dcBuf = base64.base64RawStdDecode(urlSS.hostname)
                except:
                    continue

                try:
                    urlSS = urlparse.urlparse(f"ss://{dcBuf}")
                except:
                    continue

            cipherRaw = urlSS.username
            cipher = cipherRaw
            password = urlSS.password
            if not password:
                try:
                    dcBuf = base64.base64RawStdDecode(cipherRaw)
                except:
                    try:
                        dcBuf = base64.base64RawURLDecode(cipherRaw)
                    except:
                        continue
                try:
                    cipher, password = dcBuf.split(":", 1)
                except:
                    continue

            ss["server"] = urlSS.hostname
            ss["server_port"] = urlSS.port
            ss["method"] = cipher
            ss["password"] = password

            query = dict(urlparse.parse_qsl(urlSS.query))
            plugin = query.get("plugin")
            if plugin:
                plugin = plugin.split(";", 1)
                if plugin not in ("obfs-local", "v2ray-plugin"):
                    continue
                ss["plugin"] = plugin[0]
                if len(plugin) > 1:
                    ss["plugin_opts"] = plugin[1]
            if query.get("udp-over-tcp") == "true" or query.get("uot") == "1":
                ss["udp_over_tcp"] = Udp_over_tcp()

            nodes.append(Shadowsocks(**ss))

        if scheme == "ssr":
            # not supported
            continue

        if scheme == "tg":
            try:
                urlTG = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlTG.query))

            tg = {}
            remark = query.get("remark")
            if not remark:
                remark = query.get("remarks")
            if not remark:
                remark = urlTG.hostname
            tg["type"] = urlTG.hostname
            tg["tag"] = uniqueName(names, remark)
            tg["server"] = query.get("server")
            tg["port"] = query.get("port")
            tg["username"] = query.get("user")
            tg["password"] = query.get("pass")

            nodes.append(eval(f"{tg['type'].capitalize()}")(**tg))

        if scheme == "https":
            try:
                urlHTTPS = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlHTTPS.query))

            if not urlHTTPS.hostname.startswith("t.me"):
                continue
            
            tg = {}
            remark = query.get("remark")
            if not remark:
                remark = query.get("remarks")
            if not remark:
                remark = urlHTTPS.path.strip("/")
            tg["type"] = urlHTTPS.path.strip("/")
            tg["tag"] = uniqueName(names, remark)
            tg["server"] = query.get("server")
            tg["port"] = query.get("port")
            tg["username"] = query.get("user")
            tg["password"] = query.get("pass")

            nodes.append(eval(f"{tg['type'].capitalize()}")(**tg))

    return nodes if nodes else None
