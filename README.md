# 新马跨境骑行 Skill

一套按**真实行程**逐条打磨的 AI Agent 技能包：**青岛 → 吉隆坡 → 新加坡 → 折返吉隆坡 → 青岛**，三人、三台公路车、三只大纸箱、两次陆路跨境。

它不做"路线推荐"，只做**作业规范**：每个环节都写明依据哪条规则、数字是多少、哪些不确定、不确定的怎么去落实。

> 行程序号取自真实计划：12/25 青岛航空 QW907（09:40 → 16:00，落 KLIA **T2**）；骑行吉隆坡—新加坡—折返；1/3 由 KUL T2 飞回青岛。纸箱在机场寄存约 9 天。

## 一、它到底解决哪些真实难点

| 环节 | 难在哪 | 对应文件 |
|---|---|---|
| 大纸箱托运 | 公路车箱三边和 210–230cm，必然超规；青岛航空国际经济舱只 1 件 ≤23kg、三边和 ≤158cm，超限且不能改善者可拒运 | `references/airline-bike-logistics.md` |
| 落地提超规件 | 不在普通转盘，要去超规交付区；门位与柜台随排班变 | `references/kila-baggage-storage.md` |
| 纸箱存 9 天 | 谁能存、按什么价、要不要护照、能不能夜间接、空箱怎么计价 | `references/kila-baggage-storage.md` |
| 三人三箱怎么走 | 落地当天就要开箱装车，空箱要折平再送回寄存，Grab 上车点在 Level 1 | `references/kila-baggage-storage.md` |
| 骑自行车过关 | Woodlands 是唯一可骑的口岸，Tuas 不可行（有法条链条）；通道怎么走、推车多久 | `references/border-crossing.md` |
| 三次入境的申报 | 马来西亚去程、新加坡入境、马来西亚**陆路**回程，额度还不一样 | `references/customs-declaration.md` |
| 回国被征税 | 自行车属"拟复带进境自用物品"，出境不申报，回国按不可分割单件**全额征 20%** | `references/customs-declaration.md` |
| 新加坡骑行合规 | 头盔强制、单车道禁并排、PCN 限速、夜间开灯、非折叠车不得上地铁巴士 | `references/singapore-road-rules.md` |
| 马来西亚骑行合规 | 高速公路禁自行车（LN167/59 第 17 条，罚至 RM5,000 或 12 个月监禁） | `references/malaysia-road-rules.md` |
| 队伍与家属 | 掉队三原则、18:00 强制收工、报平安机制、家属问答 | `references/route-corridor.md`、`references/contingency-playbook.md` |
| 保险与后勤 | 保险四覆盖、投保六问、通信离线化、支付、药品、证件备份 | `references/trip-support.md` |
| 待确认项怎么落地 | 六档渠道分级、三段电话脚本、留证规范、A1–A8 落实记录表 | `references/verification-channels.md` |

## 二、仓库结构

```text
malaysia-singapore-cycling-skill/
├── README.md                 # 本文件：如何调用、致谢、边界
├── LICENSE                   # MIT（本项目原创文本与脚本）
└── skill/                    # 真正的技能目录，可整体复制到 Agent 的 skills 目录
    ├── SKILL.md              # 主文件：六步工作流 + 23 条铁律 + 交付五件套 + 自检 11 项
    ├── references/           # 18 份专题参考（按需读取，渐进披露）
    │   ├── airline-bike-logistics.md   航司条款、158cm 矛盾、打包、禁运品
    │   ├── kila-baggage-storage.md     T2 动线、超规提取、寄存阶梯价、住宿、地面运输
    │   ├── border-crossing.md          Woodlands 走法、违禁品、卡关预案、现金与药品
    │   ├── customs-declaration.md      中/马/新三国申报与免税额度、复带进境
    │   ├── visa-entry.md               免签依据、MDAC/SGAC、三次跨境动作表
    │   ├── singapore-road-rules.md     法条名称、硬性义务、PCN、公共交通
    │   ├── malaysia-road-rules.md      高速禁行、联邦公路实务、补给与车店
    │   ├── route-corridor.md           西海岸走廊、8 天排法、跳段方案、掉队规则
    │   ├── time-axis-checklist.md      T-45 到 T+0 倒排、三人分工、费用分摊
    │   ├── contingency-playbook.md     七类故障树、理赔材料、家属问答、应急电话
    │   ├── trip-support.md             保险、通信、支付、医疗、证件备份
    │   ├── verification-channels.md    待确认项的落实途径与号码总表
    │   ├── capability-matrix.md        23 项能力 → 执行动作 → 数据源
    │   ├── sources-open-data.md        开源工具、开放数据集、现成 GPX
    │   └── role-review-2026-11.md      十角色审查记录（含未覆盖项）
    ├── assets/               # 可直接打印/发送的模板
    │   ├── pocket-card.md               A5 随身流程卡
    │   ├── packing-list.md              打包清单（含随身小件袋）
    │   ├── daily-card.md                每日行程卡
    │   └── inquiry-templates.md         中英文询价话术与邮件
    └── scripts/
        └── storage_cost.py   # 寄存费用测算（支持阶梯价与人均分摊）
```

## 三、如何调用这个 Skill

### 方式一：装进支持 Skills 的 Agent（推荐）

```bash
git clone https://github.com/Anathleticbicyclist/malaysia-singapore-cycling-skill.git
mkdir -p ~/.claude/skills
cp -r malaysia-singapore-cycling-skill/skill ~/.claude/skills/malaysia-singapore-cycling
```

Windows PowerShell：

```powershell
git clone https://github.com/Anathleticbicyclist/malaysia-singapore-cycling-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse .\malaysia-singapore-cycling-skill\skill "$env:USERPROFILE\.claude\skills\malaysia-singapore-cycling"
```

要点：**`SKILL.md` 必须位于技能目录根部**。不同 Agent 的 skills 目录位置不同，按其文档放置即可；目录名建议与 `SKILL.md` 里的 `name` 一致。

注意：**目标父目录必须先存在**。`~/.claude` 或 `~/.claude/skills` 尚未创建时，`cp -r` 会直接报错而不是自动创建——所以上面两条命令都先建目录。若目标目录已存在旧版本，`cp -r` 是合并式覆盖，不会先清空，重装前建议先删掉旧目录。

装好后无需手动点名，用自然语言描述任务就会命中。可直接这么说：

- "12/25 青岛飞吉隆坡，三个人三台公路车装纸箱要托运，纸箱有点大，怎么弄？"
- "KLIA T2 落地怎么提取超规行李？纸箱想存 9 天，回来再取"
- "从马来西亚骑自行车去新加坡怎么过关？要准备什么？"
- "新加坡骑行要注意什么？"
- "帮我把三人三箱寄存 9 天的费用算一下"
- "1/3 从吉隆坡飞回青岛，什么时候取箱打包？"

### 方式二：不装，直接把内容喂给模型

把 `skill/SKILL.md` 全文贴进对话，再按其中"参考文件导航"表按需贴入对应 `references/*.md`。这套结构就是为渐进加载设计的，不必一次贴完。

### 方式三：当人类手册用

不需要任何 Agent。直接读 `skill/references/` 下的文件即可——每份都标注了依据来源与"待确认"项。

### 脚本：寄存费用测算

```bash
python skill/scripts/storage_cost.py --items 3 --days 9 --rate 48 --tier2 42 --tier2-from 7 --people 3
```

实测输出（三件、9 个 24 小时段、第 7 天起降档）：

```text
单件: RM414   三件: RM1,242   人均: RM414   ≈ ¥2,111（按 1 MYR ≈ 1.7 CNY）
```

## 四、几条最容易被忽略的结论

1. **落点是 KLIA T2，不是 T1。** 寄存柜台就在 T2 的 Gateway@klia2 商场（Baggage Solutions，L1-08 / L2-136A，24 小时），不必进城。
2. **自行车托运能不能过，取决于事先获批**，不是"买了票就能带"。青岛航空条款把"超规且旅客不能或拒绝改善"列为可拒运情形。
3. **纸箱按阶梯计价**：自行车 RM48（1–6 天）/ RM42（7–14 天）/ RM40（15 天起）。按全段 48 算会算高。
4. **出境必须做复带进境申报。** 否则回国时自行车作为不可分割单件被全额征 20%（自行车在 20% 税率档），三台可能上万元。
5. **马来西亚陆路入境免税额度只有 RM500**（空路 RM1,000）；**备胎内胎属"轮胎与内胎"，必须申报**。
6. **新加坡：从马来西亚到达的旅客酒类零免税；香烟零免税、零 GST 减免。**
7. **Woodlands 是唯一可骑的口岸。** Tuas 侧接 AYE，自行车属 expressway excluded vehicle。
8. **超规件在货舱优先级低于普货**，载重或天气受限时第一批被卸——证件、药品、当日必需品一律随身。

## 五、内容边界

- 法规、价格、航班与柜台信息都会变。文中凡标"**待确认**"的项，都配了落实路径（电话、WhatsApp、邮箱、话术、留证要求），**必须自己核实后再据此行动**。
- 本仓库是行程作业参考，不构成法律、税务、医疗或保险建议；正式决定请以官方原文与持牌专业人士意见为准。
- 十角色审查记录（`references/role-review-2026-11.md`）如实标注了仍未覆盖的项，请连同"未覆盖"一起读，不要把缺席当成没有缺陷。

## 六、致谢

这套东西是站在很多人的肩膀上整理出来的。以下项目、数据与作者提供了工具、数据、事实依据或一手经验，在此致谢；第三方内容的版权与许可归各自作者所有。

### 开源工具与项目

| 项目 | 作者 / 组织 | 本项目的用法 | 链接 |
|---|---|---|---|
| BRouter | BRouter 项目与贡献者（@abrensch） | 自行车路由与 GPX 生成主力 | https://github.com/abrensch/brouter |
| bikerouter.de | 实例维护者（@mjaschen） | 网页画线导 GPX 的常用入口 | https://bikerouter.de |
| BRouter 社区 profile | @poutnikl | 官方 profile 不够用时替换 | https://github.com/poutnikl/Brouter-profiles |
| OsmAnd | OsmAnd 团队（@osmandapp） | 手机端离线导航，可挂 BRouter 算路 | https://github.com/osmandapp/osmand |
| GraphHopper | GraphHopper GmbH | 批量/服务端路由 | https://github.com/graphhopper/graphhopper |
| Valhalla | Valhalla 项目与贡献者 | 多模式路由、坡度感知 | https://github.com/valhalla/valhalla |
| gpx.studio | gpx.studio 组织（@gpxstudio） | 在线 GPX 编辑、切段、加途经点 | https://github.com/gpxstudio/gpx.studio |
| WTracks | @opoto | 轻量轨迹编辑：压缩、反转、裁剪、高程 | https://opoto.github.io/wtracks/doc/ |
| GPX-Route-Planner | @patricklmarie | 纯前端点图出线、剖面、导 GPX | https://github.com/patricklmarie/GPX-Route-Planner |
| gpxpy | @tkrajina | Python 读写/简化/合并 GPX | https://github.com/tkrajina/gpxpy |
| gpxcsv | @astrowonk | GPX → CSV，便于逐段分析 | https://github.com/astrowonk/gpxcsv |
| gpxtidy | Paul Barker（@pbarker） | 发布前去除时间戳与个人标识、抽稀 | https://codeberg.org/pbarker/gpxtidy |
| OSMnx | Geoff Boeing（@gboeing） | 拉取/建模 OSM 路网做统计 | https://github.com/gboeing/osmnx |
| CyclOSM | CyclOSM 贡献者 | 自行车专用底图样式 | https://github.com/cyclosm/cyclosm-cartocss-style |
| DirtGenie | @a20r | 借其"逐日节奏怎么排"的思路（结论仍需自算） | https://github.com/a20r/dirtgenie |

### 开放数据

| 数据 | 提供方 | 许可 |
|---|---|---|
| Cycling Path Network (GeoJSON) | 新加坡陆路交通管理局 LTA / data.gov.sg | Singapore Open Data Licence |
| Park Connector Loop (GeoJSON) | 新加坡国家公园局 NParks / data.gov.sg | Singapore Open Data Licence |
| Central Nature Reserve Biking Route | 新加坡国家公园局 NParks | Singapore Open Data Licence |
| 自行车停车点 | LTA DataMall + 社区补充 | 见原项目说明 |
| OpenStreetMap 数据 | © OpenStreetMap contributors | ODbL |

### 一手经验与路线

RideWithGPS、Bikemap、Wikiloc 上的公开路线作者；sportplus.sg 的跨境骑行指南；sengkangbabies 的新加坡—吉隆坡骑行记录；momentumcyclesg 的新加坡路线合集；8264 骑行天下的中文长线游记。关卡怎么走、拥堵什么时段，这些"只能现场知道"的部分主要来自他们。

### 官方与商业资料

青岛航空（qdairlines.com）行李运输条款；青岛胶东国际机场服务信息；klia2.info 与 KLIA Smart Storage、Talasco Dagang（Baggage Solutions）公开价目；马来西亚皇家关税局《Traveler's Guide》与马来西亚皇家警察 JSPT 公告；新加坡海关（Singapore Customs）、IRAS、ICA、LTA、Singapore Statutes Online；中国海关总署与南京海关、国务院关税税则委员会公告 2024 年第 11 号、海关总署公告 2024 年第 176 号。

## 七、许可证

- 本项目**原创文本与脚本**：MIT，见 [LICENSE](LICENSE)。
- **第三方内容**（引用的条款原文、价格、数据集、路线）版权归各自权利人，本项目仅作事实引用与出处标注，MIT 不覆盖这些第三方内容。
- 若你是上述项目的作者，希望调整署名方式或移除某项引用，请开 issue，会尽快处理。

## 八、更新与贡献

- 欢迎补真实案例、纠正过期数字：请开 issue 并附**来源链接**（不接受"听说"）。
- 提交前请遵守本项目的核心纪律：**数字必须有据，不确定就标待确认，并给出落实路径**。
