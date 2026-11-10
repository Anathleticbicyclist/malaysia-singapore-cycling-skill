# 情报源与开源项目索引

## 一、先说结论

- **GitHub 上没有"新马骑行 GPX 专仓"**。真实 GPX 集中在 RideWithGPS / Bikemap / Wikiloc / Strava；GitHub 的价值是**工具链**（路由、GPX 编辑清洗、离线导航）。
- **马来西亚没有官方骑行路网开放数据**（本轮检索 data.gov.my 与州级 GIS 均未见成体系的 cycle lane 数据集，只见研究机构文档与地方规划材料）。马来西亚侧只能靠 OSM + 联邦公路编号 + 骑友 GPX。
- **新加坡是唯一有官方骑行路网 GeoJSON 的地方**，LTA 与 NParks 各有一套，可直接下载。
- 标 `[已验证]` = 本轮实际打开过页面/文档；`[沿用]` = 早期记录，未本轮复核，用前自己点开确认。

## 二、路由引擎（按用途选，别混着用）

| 项目 | 用途 | 地址 | 状态 |
|---|---|---|---|
| **BRouter** | 自行车路由主力。可配 profile、考虑坡度、支持 via/nogo 点、可跑长距离自行车路线；有网页版与离线版 | https://brouter.de/brouter/ ；仓库 https://github.com/abrensch/brouter | 官网 [已验证]；仓库 [沿用] |
| **brouter-web / bikerouter 实例** | 网页画线导 GPX，拖拽调线最顺手；m11n 实例 profile 更多 | https://bikerouter.de ；https://brouter.m11n.de | [已验证] |
| **BRouter 社区 profile** | 官方 profile 不够用时换别人的 `.brf`（trekking/racebike 各种变体） | https://github.com/poutnikl/Brouter-profiles | [已验证]（看过其 Trekking-hilly-paths.brf 原文） |
| **OsmAnd** | 手机端离线导航，可挂 BRouter 做离线算路；无网也能用 | https://github.com/osmandapp/osmand | [已验证] |
| **GraphHopper** | Java 路由引擎，要批量算几百条或做服务端时用 | https://github.com/graphhopper/graphhopper | [已验证] |
| **Valhalla** | 多模式路由，含 elevation-aware bicycle costing、isochrone | https://github.com/valhalla/valhalla | [已验证] |

**本行程怎么用**：路线出 GPX 用 BRouter（bikerouter.de 网页版，选 trekking 或 fastbike profile，避开 motorway）；出发前把该段 routing 数据下到手机 + OsmAnd，跨境当天断网也不慌。

## 三、GPX 编辑与清洗

| 项目 | 用途 | 地址 | 状态 |
|---|---|---|---|
| **gpx.studio** | 在线 GPX 编辑器，可视、可切段、可加途经点，最像"能用的工具" | https://github.com/gpxstudio/gpx.studio | [已验证] |
| **WTracks** | 轻量轨迹编辑器：压缩、反转、裁剪、高程填充、分享链接 | https://opoto.github.io/wtracks/doc/ | [已验证] |
| **GPX-Route-Planner** | 浏览器端点图出线、剖面、导 GPX，无账号、纯前端 | https://github.com/patricklmarie/GPX-Route-Planner | [已验证]（作者自述） |
| **gpxpy** | Python 读写/简化/合并 GPX，脚本化首选 | https://github.com/tkrajina/gpxpy | [沿用] |
| **gpxcsv** | GPX → CSV，便于用表格分析某段速度/爬升 | https://github.com/astrowonk/gpxcsv | [已验证] |
| **gpxtidy** | 发布前去掉时间戳与个人标识、抽稀轨迹 | https://codeberg.org/pbarker/gpxtidy | [已验证] |
| **OSMnx** | Python 拉取/建模 OSM 路网，做"这段有没有自行车道"的统计 | https://github.com/gboeing/osmnx | [已验证] |
| **CyclOSM** | OSM 自行车专用底图样式，肉眼能看出车道/路面/坡度 | https://github.com/cyclosm/cyclosm-cartocss-style | [沿用] |
| **Overpass API** | 按 bbox 拉车店、水源、加油站、禁行标志 | https://overpass-api.de | [沿用] |

## 四、路线规划类项目（参考思路，不建议直接依赖）

| 项目 | 说明 | 地址 | 状态 |
|---|---|---|---|
| **DirtGenie** | AI 生成 bikepacking 逐日行程 + GeoJSON，MIT。**依赖 OpenAI 与 Google Maps API key，且 Google 自行车路由会给出载重车不宜的路** | https://github.com/a20r/dirtgenie | [已验证] |

结论：这类工具可以借"逐日节奏怎么排"的思路，结论仍要用 BRouter 重算里程爬升，别直接采信 AI 给的路线。

## 五、开放数据集

| 数据 | 提供方 | 用途 | 地址 | 状态 |
|---|---|---|---|---|
| Cycling Path Network (GEOJSON) | 新加坡 LTA / data.gov.sg | 新加坡骑行路网（含 PCN 与镇议会车道），半年更新 | https://data.gov.sg/datasets?agencies=Land+Transport+Authority+(LTA)&resultId=d_8f468b25193f64be8a16fa7d8f60f553 | [已验证] |
| Park Connector Loop | 新加坡 NParks | PCN 各环线分段（Eastern Coastal / Northern Explorer 等） | https://data.gov.sg/datasets/d_a69ef89737379f231d2ae93fd1c5707f/view | [已验证] |
| Central Nature Reserve Biking Route | 新加坡 NParks | 自然保护区山地骑行线（本行程公路车不适用，但可判"哪里别骑"） | https://data.gov.sg/datasets/d_147e0d9d2f38453d2aa58d52716b78f1/view | [已验证] |
| 自行车停车点 | LTA DataMall + 社区补充 | 找停车/锁车点，2 万条 | https://bicycle-park-where.vercel.app | [已验证] |
| 高速禁行车辆清单 | 新加坡 LTA OneMotoring | 确认 bicycle 属 expressway excluded vehicles | https://onemotoring.lta.gov.sg/content/onemotoring/home/driving/road_safety_and_vehicle_rules/driving-in-expressway-and-tunnel.html | [沿用] |

## 六、现成路线（可直接参考或下载 GPX）

| 来源 | 内容 | 地址 |
|---|---|---|
| RideWithGPS 公开路线 | Kluang→SG（70mi/2831ft）、Kluang→Mersing 等 | https://ridewithgps.com/users/1297946 |
| Bikemap 集合 | Bangkok–Singapore 10 段 2134km；Borneo 4 段；Singapore PCN 集合 3 条 | https://www.bikemap.net/en/c/470632/ ；https://www.bikemap.net/de/c/421196/ |
| Wikiloc | 马来西亚 bikepacking 70+ 条 | https://gl.wikiloc.com/rutas/bikepacking/malaisia |
| sengkangbabies | 5D4N Cycle to KL，含 GPX、POI（补给/地标） | https://sengkangbabies.com/tag/cycling-batu-pahat-slopes-and-watermelon/ |
| momentumcyclesg | 新加坡 27 条路线，含 GPX | https://momentumcyclesg.com/cycling-routes-singapore/ |
| SportPlus.sg | Johor Cycling Series 136km 环线，含分段与补给建议 | https://sportplus.sg/blogs/news/cross-border-cycling-riding-johor-from-singapore |

## 七、社区（经验值最高）

- Facebook 群 **"Cycling SG to Malaysia"**：跨境骑行一手经验、当日关卡拥堵实况。
- 8264 骑行天下：中文长线游记（新马泰骑行 20+ 天实录，含关卡细节）。
- 结论：**关卡走法与拥堵只能靠社区当日信息**，官方页面不会写"推车走哪个闸口"。

## 八、官方入口（写进方案时优先引用这些）

| 事项 | 官方来源 |
|---|---|
| 机场行李/航站楼 | https://www.malaysiaairports.com.my ；https://www.klia2.info |
| 机场寄存 | https://www.klia2.info/klia2/facilities/luggage-storage-and-locker/ ；https://kliasmartstorage.com |
| 新加坡入境/关卡 | https://www.ica.gov.sg |
| 新加坡骑行法条 | https://sso.agc.gov.sg/SL/RTA1961-R3 ；https://www.lta.gov.sg |
| 新加坡海关免税与 GST | https://www.customs.gov.sg/at-customs/arriving-in-singapore/duty-free-concession-gst-relief/ |
| 马来西亚海关旅客指南 | https://www.customs.gov.my/en/individu/pengembara/travelers-guide |
| 中国进境物品征税与申报 | https://www.customs.gov.cn ；南京海关征税规定页 |
| 马来西亚高速禁行 | https://www.rmp.gov.my （JSPT 公告） |
| MDAC | https://ims.gov.my |
| 中马免签/协定 | https://my.china-embassy.gov.cn ；https://www.kln.gov.my |
| 中新免签 | https://www.mfa.gov.cn ；https://sg.china-embassy.gov.cn |
| 青岛航空行李条款 | https://www.qdairlines.com/articles?cur=354&par=19 |
| 航班落哪座航站楼 | 飞常准 / Trip.com 航班状态页（最可靠，逐日更新） |

## 九、检索纪律

1. 先查官方条文，再看商业指南，最后用社区经验补"只能现场知道"的部分。
2. 单一来源的关键结论（如"某关口禁自行车"）必须找到第二来源或法律链条，否则标"待核实"。
3. 航站楼、航班时刻这类会变的信息，**每次任务重新查**，不要用旧结论。
4. 工具类项目**先确认能不能跑起来**（有没有 key、要不要自建服务、数据是否覆盖该区域）再写进方案；只记名字不算验证。
5. 马来西亚骑行路网无官方数据集这一条，是"检索过没有"的结论，不是"懒得查"。若日后要补，从州级 GIS 门户（如 mygdispatial）与 OSM 变更集入手，别指望 data.gov.my。
