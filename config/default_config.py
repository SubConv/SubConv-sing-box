from .type import User_config_outbound, User_config_route, User_config
from type.inbound import Inbound, Mixed, Tun
from type.experimental import Experimental, Cache_file, Clash_api
from type.log import Log
from type.dns import Dns, Server, Rule

# inbounds
INBOUDS = [
    Mixed(
        tag="mixed-in",
        listen="0.0.0.0",
        listen_port=7890,
        sniff=True,
        domain_strategy="prefer_ipv6"
    ),
    Tun(
        tag="tun-in",
        auto_route=True,
        stack="system",
        sniff=True,
        # address=[
        #     "172.18.0.1/30",
        #     "fdfe:dcba:9876::1/126"
        # ],
        inet4_address=[
            "172.18.0.1/30",
        ],
        inet6_address=[
            "fdfe:dcba:9876::1/126"
        ],
        domain_strategy="prefer_ipv6",
    )
]

# some helper constants
NONE_RULE_TAGS = [
    "🚀 节点选择",
    "♻️ 自动选择",
    "🚀 手动切换1",
    "🚀 手动切换2",
    "🇭🇰 香港节点",
    "🇨🇳 台湾节点",
    "🇸🇬 狮城节点",
    "🇯🇵 日本节点",
    "🇰🇷 韩国节点",
    "🇺🇸 美国节点",
]

default_config = User_config(
    log=Log(
        level="info"
    ),
    dns=Dns(
        servers=[
            Server(address="https://223.5.5.5/dns-query", tag="AliDNS", detour="direct"),
            Server(address="https://1.1.1.1/dns-query", tag="CfDNS", detour="🚀 节点选择"),
        ],
        final="AliDNS",
        rules=[
            Rule(ip_cidr=["240.0.0.0/4"], server="CfDNS"),
            Rule(outbound=["direct"], server="AliDNS"),
            Rule(outbound=["any"], server="AliDNS"),
        ]
    ),
    experimental=Experimental(
        cache_file=Cache_file(enabled=True),
        clash_api=Clash_api(
            external_controller="localhost:9090",
            default_mode="Rule"
        )
    ),
    inbounds=INBOUDS,
    outbounds=[
        User_config_outbound(
            tag="🚀 节点选择",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS[1:],
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="♻️ 自动选择",
            type="selector",
            regex=r".*"
        ),
        User_config_outbound(
            tag="🚀 手动切换1",
            type="selector",
            regex=r".*"
        ),
        User_config_outbound(
            tag="🚀 手动切换2",
            type="selector",
            regex=r".*"
        ),

        # outbounds for rules
        User_config_outbound(
            tag="🤖 ChatBot",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="📲 电报消息",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="📹 油管视频",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎥 奈飞视频",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="📺 巴哈姆特",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="📺 哔哩哔哩",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🌍 国外媒体",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="🌏 国内媒体",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="📢 谷歌FCM",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="📢 谷歌服务",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="Ⓜ️ 微软Bing",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="Ⓜ️ 微软云盘",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="Ⓜ️ 微软服务",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🍎 苹果服务",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎮 游戏平台",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎶 网易音乐",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎶 Spotify",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎯 全球直连",
            type="selector",
            outbounds=[
                "direct",
                *NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🛑 广告拦截",
            type="selector",
            outbounds=[
                "block",
                "direct",
                *NONE_RULE_TAGS
            ]
        ),
        User_config_outbound(
            tag="🍃 应用净化",
            type="selector",
            outbounds=[
                "block",
                "direct",
                *NONE_RULE_TAGS
            ]
        ),
        User_config_outbound(
            tag="🛡️ 隐私防护",
            type="selector",
            outbounds=[
                "block",
                "direct",
                *NONE_RULE_TAGS
            ]
        ),
        User_config_outbound(
            tag="🐟 漏网之鱼",
            type="selector",
            outbounds=[
                *NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        
        # outbounds for region
        User_config_outbound(
            tag="🇭🇰 香港节点",
            type="urltest",
            regex=r"🇭🇰|HK|Hong|Kong|HGC|WTT|CMI|港"
        ),
        User_config_outbound(
            tag="🇨🇳 台湾节点",
            type="urltest",
            regex=r"🇹🇼|TW|Taiwan|新北|彰化|CHT|台|HINET"
        ),
        User_config_outbound(
            tag="🇸🇬 狮城节点",
            type="urltest",
            regex=r"🇸🇬|SG|Singapore|狮城|^新[^节北]|[^刷更]新[^节北]"
        ),
        User_config_outbound(
            tag="🇯🇵 日本节点",
            type="urltest",
            regex=r"🇯🇵|JP|Japan|Tokyo|Osaka|Saitama|东京|大阪|埼玉|日"
        ),
        User_config_outbound(
            tag="🇰🇷 韩国节点",
            type="urltest",
            regex=r"🇰🇷|KO?R|Korea|首尔|韩|韓"
        ),
        User_config_outbound(
            tag="🇺🇸 美国节点",
            type="urltest",
            regex=r"🇺🇸|US|America|United.*?States|美|波特兰|达拉斯|俄勒冈|凤凰城|费利蒙|硅谷|拉斯维加斯|洛杉矶|圣何塞|圣克拉拉|西雅图|芝加哥"
        ),
    ],

    route=User_config_route(
        final="🐟 漏网之鱼",
        remote_rule_set=[
            ["🤖 ChatBot", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/OpenAi.srs"],
            ["🤖 ChatBot", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/ChatBot.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/LocalAreaNetwork.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/UnBan.srs"],
            ["🛑 广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanAD.srs"],
            ["🍃 应用净化", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanProgramAD.srs"],
            ["🛑 广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanEasyList.srs"],
            ["🛑 广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanEasyListChina.srs"],
            ["🛡️ 隐私防护", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanEasyPrivacy.srs"],
            ["📢 谷歌FCM", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/GoogleFCM.srs"],
            ["📢 谷歌服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Google.srs"],
            # ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/GoogleCN.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Adobe.srs"],
            ["Ⓜ️ 微软Bing", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Bing.srs"],
            ["Ⓜ️ 微软云盘", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/OneDrive.srs"],
            ["Ⓜ️ 微软服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Microsoft.srs"],
            ["🍎 苹果服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Apple.srs"],
            ["📲 电报消息", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Telegram.srs"],
            ["🎶 网易音乐", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/NetEaseMusic.srs"],
            ["🎶 Spotify", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Spotify.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Epic.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Origin.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Sony.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Steam.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Nintendo.srs"],
            ["📹 油管视频", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/YouTube.srs"],
            ["🎥 奈飞视频", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Netflix.srs"],
            ["📺 巴哈姆特", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Bahamut.srs"],
            ["📺 哔哩哔哩", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/BilibiliHMT.srs"],
            ["📺 哔哩哔哩", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Bilibili.srs"],
            ["🌏 国内媒体", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ChinaMedia.srs"],
            ["🌍 国外媒体", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ProxyMedia.srs"],
            ["🚀 节点选择", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ProxyGFWlist.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ChinaIp.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ChinaDomain.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ChinaCompanyIp.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Download.srs"],
            # ["🎯 全球直连", "[]GEOIP,CN"],
        ],
    )
)

ZJU_NONE_RULE_TAGS = [
    "🚀 节点选择",
    "♻️ 自动选择",
    "🚀 手动切换1",
    "🚀 手动切换2",
    "🇨🇳 ZJU节点",
    "🇭🇰 香港节点",
    "🇨🇳 台湾节点",
    "🇸🇬 狮城节点",
    "🇯🇵 日本节点",
    "🇰🇷 韩国节点",
    "🇺🇸 美国节点",
]

default_zju_config = User_config(
    log=Log(
        level="info"
    ),
    dns=Dns(
        servers=[
            Server(address="https://223.5.5.5/dns-query", tag="AliDNS", detour="direct"),
            Server(address="https://1.1.1.1/dns-query", tag="CfDNS", detour="🚀 节点选择"),
            Server(address="10.10.0.21", tag="ZJUDNS", detour="✔ ZJU"),
        ],
        final="AliDNS",
        rules=[
            Rule(ip_cidr=["240.0.0.0/4"], server="CfDNS"),
            Rule(rule_set=["ZJU"], server="ZJUDNS"),
            Rule(outbound=["direct"], server="CfDNS"),
            Rule(outbound=["any"], server="AliDNS"),
        ]
    ),
    experimental=Experimental(
        cache_file=Cache_file(enabled=True),
        clash_api=Clash_api(
            external_controller="localhost:9090",
            default_mode="Rule"
        )
    ),
    inbounds=INBOUDS,
    outbounds=[
        User_config_outbound(
            tag="🚀 节点选择",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS[1:],
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="♻️ 自动选择",
            type="urltest",
            regex=r"^(?!.*(ZJU|浙大|内网|✉️)).*"
        ),
        User_config_outbound(
            tag="🚀 手动切换1",
            type="selector",
            regex=r".*"
        ),
        User_config_outbound(
            tag="🚀 手动切换2",
            type="selector",
            regex=r".*"
        ),

        # outbounds for rules
        User_config_outbound(
            tag="✔ ZJU-INTL",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="✔ ZJU",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="📃 ZJU More Scholar",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🤖 ChatBot",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="📲 电报消息",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="📹 油管视频",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎥 奈飞视频",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="📺 巴哈姆特",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="📺 哔哩哔哩",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🌍 国外媒体",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="🌏 国内媒体",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="📢 谷歌FCM",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="📢 谷歌服务",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="Ⓜ️ 微软Bing",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="Ⓜ️ 微软云盘",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="Ⓜ️ 微软服务",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🍎 苹果服务",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎮 游戏平台",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎶 网易音乐",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎶 Spotify",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        User_config_outbound(
            tag="🛸 PT站",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🎯 全球直连",
            type="selector",
            outbounds=[
                "direct",
                *ZJU_NONE_RULE_TAGS,
                "block"
            ]
        ),
        User_config_outbound(
            tag="🛑 广告拦截",
            type="selector",
            outbounds=[
                "block",
                "direct",
                *ZJU_NONE_RULE_TAGS
            ]
        ),
        User_config_outbound(
            tag="🍃 应用净化",
            type="selector",
            outbounds=[
                "block",
                "direct",
                *ZJU_NONE_RULE_TAGS
            ]
        ),
        User_config_outbound(
            tag="🛡️ 隐私防护",
            type="selector",
            outbounds=[
                "block",
                "direct",
                *ZJU_NONE_RULE_TAGS
            ]
        ),
        User_config_outbound(
            tag="🐟 漏网之鱼",
            type="selector",
            outbounds=[
                *ZJU_NONE_RULE_TAGS,
                "direct",
                "block"
            ]
        ),
        
        # outbounds for region
        User_config_outbound(
            tag="🇨🇳 ZJU节点",
            type="urltest",
            regex=r"ZJU|浙大"
        ),
        User_config_outbound(
            tag="🇭🇰 香港节点",
            type="urltest",
            regex=r"🇭🇰|HK|Hong|Kong|HGC|WTT|CMI|港"
        ),
        User_config_outbound(
            tag="🇨🇳 台湾节点",
            type="urltest",
            regex=r"🇹🇼|TW|Taiwan|新北|彰化|CHT|台|HINET"
        ),
        User_config_outbound(
            tag="🇸🇬 狮城节点",
            type="urltest",
            regex=r"🇸🇬|SG|Singapore|狮城|^新[^节北]|[^刷更]新[^节北]"
        ),
        User_config_outbound(
            tag="🇯🇵 日本节点",
            type="urltest",
            regex=r"🇯🇵|JP|Japan|Tokyo|Osaka|Saitama|东京|大阪|埼玉|日"
        ),
        User_config_outbound(
            tag="🇰🇷 韩国节点",
            type="urltest",
            regex=r"🇰🇷|KO?R|Korea|首尔|韩|韓"
        ),
        User_config_outbound(
            tag="🇺🇸 美国节点",
            type="urltest",
            regex=r"🇺🇸|US|America|United.*?States|美|波特兰|达拉斯|俄勒冈|凤凰城|费利蒙|硅谷|拉斯维加斯|洛杉矶|圣何塞|圣克拉拉|西雅图|芝加哥"
        ),
    ],

    route=User_config_route(
        final="🐟 漏网之鱼",
        remote_rule_set=[
            ["🛸 PT站", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/PrivateTracker.srs"],
            ["✔ ZJU-INTL", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ZJU-INTL.srs"],
            ["✔ ZJU", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ZJU.srs"],
            ["🤖 ChatBot", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/OpenAi.srs"],
            ["🤖 ChatBot", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/ChatBot.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/LocalAreaNetwork.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/UnBan.srs"],
            ["🛑 广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanAD.srs"],
            ["🍃 应用净化", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanProgramAD.srs"],
            ["🛑 广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanEasyList.srs"],
            ["🛑 广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanEasyListChina.srs"],
            ["🛡️ 隐私防护", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/BanEasyPrivacy.srs"],
            ["📢 谷歌FCM", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/GoogleFCM.srs"],
            ["📢 谷歌服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Google.srs"],
            # ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/GoogleCN.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Adobe.srs"],
            ["Ⓜ️ 微软Bing", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Bing.srs"],
            ["Ⓜ️ 微软云盘", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/OneDrive.srs"],
            ["Ⓜ️ 微软服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Microsoft.srs"],
            ["🍎 苹果服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Apple.srs"],
            ["📲 电报消息", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Telegram.srs"],
            ["🎶 网易音乐", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/NetEaseMusic.srs"],
            ["🎶 Spotify", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Spotify.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Epic.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Origin.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Sony.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Steam.srs"],
            ["🎮 游戏平台", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Nintendo.srs"],
            ["📹 油管视频", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/YouTube.srs"],
            ["🎥 奈飞视频", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Netflix.srs"],
            ["📺 巴哈姆特", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Bahamut.srs"],
            ["📺 哔哩哔哩", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/BilibiliHMT.srs"],
            ["📺 哔哩哔哩", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Ruleset/Bilibili.srs"],
            ["🌏 国内媒体", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ChinaMedia.srs"],
            ["🌍 国外媒体", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ProxyMedia.srs"],
            ["🚀 节点选择", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ProxyGFWlist.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ChinaIp.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ChinaDomain.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ChinaCompanyIp.srs"],
            ["🎯 全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/Download.srs"],
            ["✔ ZJU", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/sing-box/ZJU-IP.srs"],
            # ["🎯 全球直连", "[]GEOIP,CN"],
        ],
    )
)
