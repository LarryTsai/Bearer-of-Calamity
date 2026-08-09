# 設定工作區

本目錄只收錄本次重寫中重新確認的設定。

時間基準：小說開局時小荒一歲，陸沉尚未滿一歲、比荒小約一歲；兩人於百斷山初遇、三千州重逢。

## 權威規則

- 作者當前明確裁示最高；跨對談整理以 `AUTHOR_CORE_REQUIREMENTS.md` 為作者硬需求入口。若現行唯一來源或正文違反其中硬需求，須建立合理因果後回歸修正，不得用舊設定否決。
- 人物以 `characters/` 為唯一來源。
- 十雷與命圖體系以 `systems/` 為唯一來源。
- 團體與組織以 `factions/` 為唯一來源。
- `AUTHOR_SECRETS.md` 僅供作者與一致性檢查，正文需分階段揭露。
- 圖片只作視覺參考；圖片文字、檔名與舊版設定不得推翻 Markdown 正式資料。

## 文件索引

- `AUTHOR_CORE_REQUIREMENTS.md`：從 `new_story*.txt`、`basic_rule.txt` 與作者最新裁示提煉的硬需求及衝突解讀；所有開發與 closed-loop review 動筆前必讀。
- `AUTHOR_REQUIREMENTS_AUDIT_MATRIX.md`：作者裁示逐項對照現行唯一來源、正文驗證範圍與尚未關閉的卷章工作；用來區分「文件已一致」與「正文仍待驗證」。
- `CHECKLIST_PENDING_DECISIONS.md`：Codex／Claude 共同維護的待確認問題清單；核取前不視為正式設定。第 1～36 題已全數回填；第二輪第 37 題起持續擴充中，已回填項目見文中 ✅ 標記與 `CHECKLIST_RESOLVED_HISTORY.md`。
- `CHECKLIST_RESOLVED_HISTORY.md`：已回填項目的討論過程存檔（Codex 提案／Claude 意見／最終決定），僅供追溯，不作為設定依據。
- `WRITING_GUIDELINES.md`：正文視角、稱呼、戰鬥、揭密、原作邊界與提交前檢查規格。
- `REVEAL_TIMELINE.md`：作者真相、讀者線索、角色知情與公開揭露的分級控制表。
- `canon/PERFECT_WORLD_CANON_TIMELINE.md`：《完美世界》純原作主要事件鐵軌、境界硬錨與不可改寫功業；不混入陸沉原創事件。
- `world/WORLD_GEOGRAPHY_AND_ROUTES.md`：下界、上界、帝關的相對地理與跨界路線（起點／通道／終點／條件／時間／風險），只畫已用到的路線。

- `characters/`：人物設定集。
  - `characters/CHARACTER_LU_CHEN.md`：主角陸沉（稱號「劫」）的人物設定集。
  - `characters/CHARACTER_WITCH.md`：魔女的原作身分安全閥、與陸沉的長期知己／試探／道路對手關係及跨卷回收規則。
- `systems/`：力量系統唯一來源。
  - `systems/SYSTEM_TEN_CALAMITY_THUNDERS.md`：十雷正式名稱、進階與取得節奏。
  - `systems/SYSTEM_HEAVENLY_THUNDER_RANKING.md`：天地異雷榜前 thirty、完整場域威力、境界威脅、原生環境難度與陸沉九雷候選映射。
  - `systems/SYSTEM_LU_CHEN_FORMATION_SCOPE.md`：陸沉在太玄宗正式學陣、偏科專精、任意陣法威脅的處理層級、照命破陣流程與禁止陣道爭鋒邊界。
  - `systems/SYSTEM_CALAMITY_ORDER_AND_SELF_RECONSTRUCTION.md`：劫以人格驅動自我修正／重構、十雷承載矛盾、萬劫定序成長階段，以及只承接同一仙王《古神禁典》的傳承邊界。
  - `systems/SYSTEM_MYRIAD_CALAMITY_WEAPON_EMBRYO.md`：萬劫兵胎來源、形態學習限制、毀損重鑄規則、與無聲渡笛的關係。
  - `systems/SYSTEM_TAIXUAN_OLD_TOKEN.md`：太玄舊令基本性質、命印共鳴限制、合令畫面、太玄閣老人辨認依據。
  - `systems/SYSTEM_TAIXUAN_FATE_MAP_AND_JIE_REALM.md`：太玄命圖必要性、核心結構與能力、戰鬥運用；太古星天圖、劫藏與以劫為種。
  - `systems/SYSTEM_MYRIAD_BODY_FORGING_SCRIPTURE.md`：《萬體鑄身經》公開前四篇與鎮岳真傳後四篇。
  - `systems/SYSTEM_FORMLESS_SEPARATION_SCROLL.md`：《無相離身卷》、虛渡、雷身與分身前置。
  - `systems/SYSTEM_THUNDER_ALCHEMY.md`：雷煉丹原理、雷紋丹分級、丹劫機制與煉丹閣經濟制度。
  - `systems/SYSTEM_THUNDER_BODY_DIVISION.md`：太玄初期（一至三雷）本尊與雷身分工、雷核共鳴、承身命名。
  - `systems/SYSTEM_THUNDER_BODY_SCALING.md`：十雷齊備後雷身戰力比例、本尊化雷、三雷合體、九雷合一、十雷一體。
  - `systems/SYSTEM_CULTIVATION_TIMELINE.md`：原作事件、荒劫年齡／境界差、十雷成熟度與安全閥控制表。
  - `systems/SYSTEM_THUNDER_POOLS.md`：雷池四層結構、雷池類型，以及通過完整考驗後一次取得完整異雷本源的規則。
  - `systems/SYSTEM_THUNDER_COMMUNICATION_NETWORK.md`：雷訊令、雷訊臺／雷訊樁、鏈式中繼、安全限制與四階段發展。
  - `systems/SYSTEM_BATTLEFIELD_THUNDER_POOL_NETWORK.md`：戰雷母池、承雷樁、分雷臺、泄雷工事、能源守恆與五階段發展。
  - `systems/SYSTEM_MYRIAD_CALAMITY_SEALED_DOMAIN.md`：PW-26 終戰後固定公共災害封存域、三區四倉、共管制度與拆除方向。
- `factions/`：團體設定唯一來源。
  - `factions/FACTION_FOUR_COMPANION_STARS.md`：四伴星共同規則、排行與歸位。
  - `factions/FACTION_TAIXUAN_SECT.md`：太玄宗七峰、洛生衣歸屬、太玄舊令與收徒規則。
  - `factions/FACTION_JIE_CLAN.md`：劫族種族定位、沉雷谷、「劫」稱號古史、老族長。
- `AUTHOR_SECRETS.md`：作者層真相與揭露限制。
- `MACRO_OUTLINE.md`：全書現行大篇章骨架。
- `STORY_CAUSALITY_NETWORK.md`：陸沉全部原創故事的因果與伏筆總網；規定事件來源、能力所得、代價、跨篇回收、高潮層級與待補橋樑。
- `STORY_PACING_AND_WORLD_GUIDE.md`：陸沉線高潮波形、長程懸念、公平反轉、能力首秀、十雷標誌畫面與世界觀展示準則。
- `outlines/OUTLINE_TIANSHEN_ACADEMY.md`：天神書院篇四十八章六幕目錄；正文控制跨度約八至九個月，含書院生活、周晏殘陣案、荒劫排位、外圍七站、雷訊試網與第七雷雙戰場。
- `events/`：已定稿重大事件。
  - `events/EVENT_WITCH_LU_CHEN_LOWER_REALM_ARC.md`：魔女與陸沉在北海以前的六次相遇、三次招攬、百斷山互救、假殺荒委託與北海回收。
  - `events/EVENT_TIANSHEN_ACADEMY_AMBUSH.md`：荒初入書院遭王家特定旁支／異域外接組設局；周晏為唯一現場執行者，洛生衣承釘救人，劫於持續滅證威脅中斬周晏，孟天正定調「下次留活口」。
  - `events/EVENT_TIANSHEN_ACADEMY_HUANG_VS_JIE.md`：天神書院首席之爭，含院長（孟天正）認出劫之體修根基、排位前兩院首次招攬與排位後加碼重申、荒劫成長方式對照、司天鑑觀戰後的災源判定。
  - `events/EVENT_CHENLEI_VALLEY_NIGHT.md`：序篇沉雷谷血祭之夜，陸沉六歲時「劫」稱號成立事件，含族老會表決、母親三層後手、老族長結局與存活比例。
  - `events/EVENT_XIANGU_RUINS_ZHEXIAN.md`：仙古遺跡反敗謫仙，鎮無央首次顯化外環；含與《完美世界》原作銜接安全閥。
  - `events/EVENT_SOUL_DOMAIN_ZHENWUYANG.md`：陸沉主動追入外部雷魂域取得鎮魄；守墓獅鎮無央不贈雷，取雷後自主歸位。
  - `events/EVENT_DEADSTILL_DOMAIN_XUANHENG.md`：死寂雷域只留線索；陸沉分別由外部無聲雷池、定疆雷界取得歸寂與鎮界，玄衡不養雷而自主同行。
  - `events/EVENT_SCORCHED_NEST_JINCHANGMING.md`：陸沉主動追入燃身雷界取得外部本源；玄燼凰守池讓路，燼長明不贈火而自主歸位。
  - `events/EVENT_SECOND_THUNDER_JIEMING.md`：陸沉初入上界負傷期間，斬斷祭子命線，第二雷劫命歸位。
  - `events/EVENT_TWO_FALLEN_SECTS_ECHO.md`：三千州重逢後，補天閣與太玄閣兩座倒下山門的鏡像回音。
  - `events/EVENT_BORDER_RIFT_FRONT_CAMPAIGN.md`：帝關邊荒主線，裂界防線、血原巡獵、王家逼令、荒劫分守、焚羽古巢與天譴截矛。
  - `events/EVENT_PRIMORDIAL_CAPITAL_DESCENDANTS.md`：原始帝城後裔返關，陸沉祭子／罪血共鳴，鎮岳峰四位同門首次團隊行動面對制度性惡意。
  - `events/EVENT_MOTHER_FRACTURED_DOMAIN.md`：斷裂道域，洛清禾尋回，陸沉建替代承載結構，母親主動選擇解除綁定。
  - `events/EVENT_FINALE_TIMELINE_OVERVIEW.md`：終局三段結構唯一統籌來源——十二篇尾聲→銜接段「長息」→第十三篇大劫決裂，取代舊版「十三篇後延伸收尾」錯誤順序。
  - `events/EVENT_MINGZANG_FATE_MAP_ORIGIN.md`：太玄命藏，太玄命圖起源（無星古圖甦醒），劫厄穩定成實體。
  - `events/EVENT_TAIXUAN_PAVILION_SIEGE.md`：太玄閣滅閣雷劫、追雷入虛空，界海雷淵取照命雷雛形，劫厄界隙首次顯形，道天界命名起源。
  - `events/EVENT_TAIXUAN_TEN_THOUSAND_YEAR_THUNDER_POOL.md`：太玄宗近域萬年雷池、子母挪移陣與本尊／煌命身／承身夜間淬體日常。
  - `events/EVENT_TAIXUAN_ANCIENT_THUNDER_VEIN_RECONNECTION.md`：七峰古雷脈大難、擊碎主雷眼與小閣子陣永久熔毀。
  - `events/EVENT_TAIXUAN_THUNDER_MESSAGE_NETWORK.md`：雷訊原型、七峰基地臺試行事故與制度化後果。
  - `events/EVENT_LUO_SHENGYI_THUNDER_MESSAGE_DAILY_LIFE.md`：生與劫的雷身辨認、三身傷藥、第一對雷訊令、醫療碼與異域沉默。
  - `events/EVENT_LU_CHEN_LUO_SHENGYI_PROMISE_AND_CHOICE.md`：承諾、雷身共傷、共同承劫、醫療裁量與帝關多留一息。
  - `events/EVENT_FOREIGN_DOMAIN_COMPANION_RETURN_ROUTE.md`：陸沉主動陪荒入異域後分線、洛生衣守返程回路、荒先返與陸沉斷後。
  - `events/EVENT_JIN_WANG_INDIVIDUAL_TIANQIAN_TRIAL.md`：孟天正原作問罪後，金王新罪分案公審、逐人天譴與禁止血脈連坐。
  - `events/EVENT_FIRST_CALAMITY_FORBIDDEN_BATTLEFIELD.md`：PW-23D 後太古星天圖戰區首次被敵軍俗稱「劫禁區」，以及首次被破域代價。
  - `events/EVENT_CALAMITY_BEARING_DOMAIN_BECOMES_HOME.md`：帝關制度原型、終戰後建域、避難、藥田、碑林、聚落與「回家」。
- 鎮岳峰人物設定（現行設定）：
  - `characters/CHARACTER_YUE_CHENYUAN.md`：峰主岳沉淵，古嶽鎮身體。
  - `characters/CHARACTER_SHEN_SHANHE.md`：大師兄沈山河，玄極重域體。
  - `characters/CHARACTER_QIN_ZHAOXUE.md`：二師姐秦照雪，太陰映骨體。
  - `characters/CHARACTER_LU_XINGLIE.md`：三師兄陸行烈，赤陽焚身體。
  - `characters/CHARACTER_LIU_QINGTENG.md`：四師姐柳青藤，周天星脈體。
  - `characters/CHARACTER_HAN_TIEYI.md`：五師兄韓鐵衣，虛界不破體。
  - `characters/CHARACTER_GU_XIAOMAN.md`：六師姐顧小滿，剎那無痕體。
- 其他核心人物與四伴星：
  - `characters/CHARACTER_JIE_E.md`：四伴星之首劫厄。
  - `characters/CHARACTER_ZHEN_WUYANG.md`：鎮魄獅鎮無央。
  - `characters/CHARACTER_XUAN_HENG.md`：鎮界麒麟玄衡。
  - `characters/CHARACTER_JIN_CHANGMING.md`：玄燼凰燼長明。
  - `characters/CHARACTER_LUO_SHENGYI.md`：女主洛生衣，初見化名「生」，信物無聲渡笛。
  - `characters/CHARACTER_LUO_QINGHE.md`：陸沉之母洛清禾。
  - `characters/CHARACTER_LU_CHEN_FATHER.md`：陸沉之父陸承遠，未死、部分肉身與古雷道同化。
  - `characters/CHARACTER_TAIXUAN_ELDER.md`：下界太玄閣守閣人。
  - `characters/CHARACTER_SHI_HAO.md`：石昊與新版原創線的交會設定。
  - `characters/CHARACTER_RIVAL_TIANFA.md`：宿敵司天鑑，天罰一脈傳人，三階段登場節奏（仙古伏筆／天神書院登場／十凶血路死戰）。
