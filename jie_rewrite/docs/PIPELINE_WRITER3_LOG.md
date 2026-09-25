# 寫手3 工作日誌

## 現行接班：百斷山鏡像同步完成（2026-09-25）

- PM確認寫手2的002／004／006正文已凍結、顧問独立覆核通過後，執行 `python scripts/build_story.py`：Built 934 story files；續跑 `python scripts/build_story.py --check`：Verified 934 story files。
- manifest獨立計數為28組、867章；來源與published各867個唯一檔案，缺檔0。生成後實際內容diff僅新增百斷山002〈兩條撤路〉、004〈繩在那頭〉、006〈雷火淬骨〉三份published變更（10行增加、8行刪除）；其餘是生成前已有的三章來源與預期文件，無索引或其他鏡像內容變更。
- 本批只生成官方鏡像並更新本日誌，未改來源正文、未提交或推送；交PM整批驗收與Git收尾。長息G报告仍是窄查結論，未施工正文。

## 現行接班：長息 G 窄查已交（2026-09-25）

- 現行長息為 manifest group `long_breath`：`novel/003_邊荒承劫/004_長息/`，001～040；舊volume10只作來源識別。
- 已完成代表例前 power／character／canon 窄查，報告 `docs/drafts/XIANXIA_TEXTURE_VOLUME10_AUDIT_G.md`。確認固定鐧變形與位置錯誤、020成道里程碑未依現行系統落實、蒼梧雷羽／咬袖／代詞、赤翎轉贈餘命越界、劫厄叼人呈現、顧小滿慢半拍及024→038重複交印。
- 重要收窄：黑洞成道已有203題正式系統定案，非作者尚未選邊；修法需局部場景設計，不能只改「掌握」二字。四掌與伏臥不自動等於舊形態錯誤；前卷前掌傷後限制不自動外推長息多年後。罪州車梯／載人尺度仍有能力基準留白，不捏造禁飛或儲物通則。
- 007觀生句保護不動；001／008僅為有界候選，其他候選未批准。下一批先做報告所列已裁最小修法；020場景與罪州救援可行性先交PM窄審，新增能力／改既定成道時點才交作者。
- PM補核020章綱：G02驗收已明列「手部精細重量感知／操控永久受損」，不得降成暫時疲勞或泛稱有限承載，後續場景須持續承認此代價。
- 本批僅寫報告與本日誌，未改正文／設定／共用狀態板，未生成鏡像、未操作Git、未開agent。待PM另通知鏡像批次。

## 2026-09-25 恢復首批：鏡像修復完成

- 已讀 commit-and-push-story 技能及最新共同守則；仙人／修士視角涵蓋人物思維、因果與文明制度，境界差異不限於戰力。此批僅同步已定 dev，未新增情節或設定。
- 實查發現舊「912 對零差異」已過時：volume02_v2 ch001／013／053／075／093 的同號 published 及 upper 共 10 檔落後，各 1 處正文。以現行 dev 同步，同號鏡像保留既有 BOM／換行；upper 由官方腳本整體重建。
- 持久化工具 `scripts/audit_story_mirrors.py`：預設唯讀，檢查現有同號鏡像及兩份 SOURCE_MANIFEST 的映射；`--sync` 僅從 dev 更新同號／lower 鏡像，upper 仍交官方 builder。讀取時移除開發註記、自檢段，不忽略正文差字。
- 驗證：`python scripts/build_upper_realm_reading_v2.py --check` 通過 236 章及來源表；`python scripts/audit_story_mirrors.py` 檢查 1036 對，0 差異。此數包含目前仍存在的舊稿及其鏡像，不表示新版有 1036 章；未檢驗索引完整性或缺少整個映射的章節。
- 交 PM：10 個鏡像章檔＋上述腳本＋本日誌。未改 dev、未搬移／刪除／改名、未操作 Git；volume10 G 節尚未開工。
- 新舊替代附註：`novel/volume03a/` 與 `published/volume03a/` 是已由 `docs/STORY_STRUCTURE.md`（28 章，閱讀卷八）取代的舊禁都稿；`novel/volume04/` 與 `published/volume04/` 是失效舊仙古稿，新古界在 `novel/002_上界成道/009_界潮與古界/README.md`，仍須完成 N-2 並定閱讀卷界。這兩組是日後清理候選，非本批刪除指令。引用依賴包含 novel/README、CHECKLIST、角色／世界／事件／大綱中的舊章號，不能直接全域替換章號。
- 現行閱讀鏡像須與舊稿區別：`novel/published/001_下界成根/README.md`、`novel/published/002_上界成道/README.md` 是重編卷章的閱讀版；`docs/STORY_STRUCTURE.md`、`novel/002_上界成道/008_三千州爭鋒/README.md`、`docs/STORY_STRUCTURE.md`、`novel/002_上界成道/010_無兵雷域/README.md`～`novel/003_邊荒承劫/005_大劫決裂/001_萬劫沉封域・劫後有家/README.md`（含06b）是現行同號鏡像。volume05～12 沒有 _v2 名稱不代表過期，volume03 已完成新版扶正。古戰域 deep 源稿也被 upper builder 使用。官方 upper builder 另核對同號 published，不能單以「重複」刪除。drafts／work_in_progress 為工程材料，本批不判為可刪舊正文。

## 角色
- 從 PM 接工作，手上沒事就主動找 PM 要。也支援寫手1、寫手2，分工先協調好，不碰對方的檔案。
- 只存檔，不 git add/commit/push（一律由 PM 做）。新設定走 `docs/CHECKLIST_PENDING_DECISIONS.md` 提案；範圍外的 bug 另報 PM，不混進當下的工程。
- 正文每次修改都要同步所有鏡像：`novel/published/<卷>/`，以及 **`novel/published/002_上界成道/README.md`**（閱讀版，分卷編號不同，部分段落是舊版）。保留 BOM 與換行；不跑 make_clean_copy.pl（它會把 CRLF 疊成 \r\r\n），改用同段精確替換，最後檢查每檔增刪行數相等。

## 鏡像對照（已查證）
- ancient_battlefield_deep_v2：ch001～019 → upper volume06/ch(N+24)（025～043）；ch020～040 → upper volume07/ch(N−19)。（舊記「+18、ch019無鏡像」是鏡像重建前的編號，已失效；**upper 會被重建而改號，動手前一律先查 SOURCE_MANIFEST.md**。）
- volume03：published/volume03 同號；upper volume09/同號（ch001～039）、upper volume10/chapter(N−39)（ch040～069）。
- volume02_v2：ch011～022 → upper volume04 同號；ch042～068 → upper volume05/ch(N−38)；ch069～081 → upper volume06/ch(N−68)；ch086/089 upper 為舊版（改句不存在）；ch094～099 upper 未收錄。

## 已完成（2026-09-24，皆已 commit）
- 仙俠質感：volume05、volume06、volume06b（含215題落地）、ancient_battlefield_deep_v2（14例＋約90處機械替換＋14個bug）。產出在 `docs/drafts/XIANXIA_TEXTURE_*`、`novel/drafts/xianxia_texture_*`。
- 維護 `docs/drafts/XIANXIA_TEXTURE_ROLLOUT_SPEC.md`（方案c、角色錨點表、五之一十條教訓）。
- volume06b 補做：制度骨架補掃（歸寧司措辭、恤例）與卷尾 ENRICH（ch053 L21）。歸寧司兩個新機制提案登記為 CHECKLIST 294（留白）。
- volume02_v2（與寫手2分工）：制度骨架三例 ch064/065/075/076＋連動 ch069/076/077/081；新機制9條為 CHECKLIST 295「已落筆待核可」，退回時連動句要一起退。Phase 2 機械掃除 ch050/051/056/057/068/073/080。
- volume03（69章）：審查＋canon/power窄查（AUDIT G節）→10代表例＋5處路過奇觀（076c050）→第二輪現代詞約100、半息類約45、章尾套語、作者解釋句約40、F節bug 19條、複核再修14處（7160560）；CHECKLIST 296（荒不佩刀、石村、重逢、異獸坐騎、ch063短紋石、ch001恢復「與厄」、ch038連打一夜樁）。留給總控：資格賽／賽區、CHECKLIST 303（灰印牌措辭、驗印廳位置）。
- volume03a_v2（28章）完成（待PM commit）：G節窄查→15代表例→四方審查→FINAL_FIX回寫→PASS2三段機械掃除→輕量regression→劫厄落腳ENRICH方案3（CHECKLIST 360）→兩份鏡像全卷同步。EB-002撞區ch026未動、ch015/025只詞級。登記361（鑑月新月印負荷徵兆，留白）。
- 鏡像工具：scratchpad 的 sync_mirror.py（base＝鏡像檔最後一次commit；只套正文差異、略過章首「>」行與章末自檢；雙向驗證不過就不寫）＋body_cmp.py（dev與鏡像整章正文逐行比對）。每次新session要重寫。
- 已同步鏡像（他人dev改動）：v07 ch027、v10 ch003/022/037、v11 ch036、v12 ch021/025、v06b 24檔、v08 ch024/038/039/040/043/050/052/053。volume04_v2 無鏡像。
- 2026-09-24晚／25凌晨：①身份→身分全庫統一（104處56檔，跳過lower_realm_v2／archive／author_directives／drafts）；②published全目錄 \r\r\n 雙重換行修正41檔；③CHECKLIST 360標核可、登記362～366（v03a_v2範圍外）；④volume08：G節完成（AUDIT_G.md）、15代表例示範稿 novel/drafts/xianxia_texture_v08/REWRITES_A/B/C.md、審查 canon＋power 完成、**character 因API用量上限中斷待重跑、continuity 待確認**，彙整在 docs/drafts/XIANXIA_TEXTURE_VOLUME08_FINAL_FIX.md（草稿，未回寫）。⑤與清道夫約定：他 volume08 因果補句等我全卷掃完再做。⑥寫手2蒼梧代詞全批完成，鏡像同步進行中（v05/06/06b/09/10/11/12 共25檔；v07/v08 經 \r\r 修正後已一致）。
- 2026-09-25 volume08（97章）質感全流程完成：G節→15代表例（四方）→PM裁決367/368/369(收窄:翼羽為物件)/371/372回寫→PASS2五段約570處→ENRICH ch004/007/023保守版（CHECKLIST 373～375建議不採，只落退回寫法）→ch039/040/042/043坦白濃縮（PM核可，提案V08_CH040_042_CONDENSE_PROPOSAL.md）→三方regression→17項修正→published/volume08全卷以rebuild_mirror.py整章重生。370（203題對話）留作者。交PM清單見FINAL_FIX末節「交PM」。
- 工具新增：scratchpad/rebuild_mirror.py（dev整章重生鏡像，已與既有published做8章round-trip逐位元組一致）；upper_realm_v2 一律用 scripts/build_upper_realm_reading_v2.py（逐段替換套不上舊版段落）。
- 鏡像稽核腳本 scratchpad/audit_mirrors.py：全庫 dev↔published（含 upper，upper 標題編號不同會誤報 2 行差，忽略）。
- 進行中（2026-09-25）：volume09（56章）——審查 PART1～3 已 commit；G節 AUDIT_G.md（PM 裁決 376B/377A/378A/379A/460A/461A/462A/463/464、洛生衣誤判第三種、邵檀改名、劫厄 ch043～046 原形）；15 代表例四方審查定稿 docs/drafts/XIANXIA_TEXTURE_VOLUME09_FINAL_FIX.md 已回寫；ch005 依 PM 裁決(a) 退回推演／讀數、ch049 保持第一次、ch050 L69 等小修已落；PASS2 三段機械掃除進行中。之後：regression→鏡像（published/volume09 整章重生）→回報 PM 一次 commit→volume10～12。PM 要求 volume09 全部完成後一次回報。CHECKLIST 號段 360～379 已用完，新號段 460～479（已用 460～464）。

## 做法心得
- **agent 回報「三份都改好」不可信**，鏡像一律自己同步、自己驗證：以開發稿對 HEAD 的差異套到鏡像（整段比對、插入找錨點），再做雙向驗證（新增行都在、刪除行都不在）。腳本在 scratchpad 的 sync_v03b.py（每次開新 session 要重寫）。
- 鏡像重建目前只由寫手3做（PM規則）；他人改 dev 後通知我，我依批重建。

## 待辦／提醒
- **volume10～12 保護清單（寫手2 觀生句，2026-09-25 PM核可已commit）**：volume10 ch007 L13、volume11 ch022 L17、volume11 ch030 L25、volume12 ch024 L9、volume12 ch032 L11——質感改寫、機械掃除、regression 一律不動；改寫以最新 dev 為準。
- ROLLOUT_SPEC 教訓彙整：PM 指示等更多卷跑完再做。候選教訓：「X順着Y傳回手上」句型全卷限量；制度／程序骨架也要過核心測試；觀生只看生念、只限視線內與近處，不讀元素（那是青璃的領域）；封寒古界前是劍修「勢」，但 FH-03 已核准「敲地比較回震／辨重量影」，不可誤判為越界；不同卷有不同的時序錨點（292題只管古界後的 volume06）。
- volume02_v2 → upper_realm_v2 全卷比對同步：PM 已排在這輪落地之後。
- CHECKLIST 294、295 等使用者裁定。

## 2026-09-25 交接（session 清空前，接手所需的一切）

### ① 角色與流程要點
- 寫手3：只存檔，**不自己 git add/commit/push**（一律由 PM 做）；完成一批就回報 PM「檔案清單＋一行摘要＋剩餘未做項」。
- **published/ 與 upper_realm_v2 鏡像重建的唯一負責人**（PM 規則）：重建前先廣播 PM；他人改 dev 後通知我，我依批重建；收尾一律全庫稽核。
- CHECKLIST 號段：360～379（已用完）、460～479（已用 460～468）。新機制／新設定一律登記、附 2～3 方向與建議、不預選、不直接落稿。
- **仙人視角守則**（作者指示，`docs/XIANXIA_PERSPECTIVE_CHARTER.md`）：每場景問「如果他真是這境界的修士，為什麼這樣做？」「這世界已有修士幾萬年，為何還沒解決？」；「有禁制」單獨不算理由；不憑空發明；升級必附代價；陸沉不成唯一解。ROLLOUT_SPEC 已註明守則為共同前提、質感工程是其第一層。
- 每卷質感流程（ROLLOUT_SPEC）：審查 PART（18～20 章一段並行，general-purpose 寫報告）→ G 節窄查（power／character／canon，必要時 cultivator-logic）→ 定選約 15 代表例＋路過奇觀（G-4）→ jie-writer 示範稿 REWRITES_A/B/C → 四方審查（continuity／character／power／canon）→ FINAL_FIX（跨審查衝突在「定稿彙整」裁定）→ jie-writer 回寫 dev → PASS2 全卷機械掃除（分段並行）→ 三方 regression → 修正 → 鏡像整章重生 → 全庫稽核 → 回報 PM 一次 commit。
- 教訓：agent 回報不可盡信，鏡像一律自己同步自己驗證；各 PASS2 寫手不會彙總配額（例：v08「咬」超配額），需我在 FINAL_FIX 寫明全卷配額；API 用量上限會中斷 agent，重跑前先把已完成審查寫進 FINAL_FIX 草稿。

### ② 本輪完成事項
- **仙俠質感已完成卷冊**：volume02_v2、03、03a_v2、05、06、06b、07、08、09（皆已 commit）。v08／v09 產出：`docs/drafts/XIANXIA_TEXTURE_VOLUME0{8,9}_AUDIT_PART*.md`、`_AUDIT_G.md`、`_FINAL_FIX.md`；`novel/drafts/xianxia_texture_v0{8,9}/`（REWRITES、PASS2）；`docs/drafts/V08_CH040_042_CONDENSE_PROPOSAL.md`、`V03A_V2_JIE_E_LODGING_OPTIONS.md`。
- **v09 關鍵裁決已落實**：376B／377A（監察使＝司天鑑，全卷統一）／378A（機構稱「天罰一脈」、首次出場「天律」）／379A（模型→推演、聲紋→音紋、生機指標只指儀器）／460A；洛生衣誤判聞硯採「第三種」（道沒說謊、錯在把看得見的範圍當全部；ch049 保持首次，ch005 依 (a) 退回推演與讀數）；蘇檀→邵檀（464）；劫厄 v09 ch043～046 原形；星位帳 A；照命進階後全卷稱煌命（依 SYSTEM_TEN_CALAMITY_THUNDERS L166）；461／462／463 唯一來源已改並標「暫定，待作者讀原作後核」。
- **ROLLOUT_SPEC 第四節**新增錨點列：文奕、律無咎、岑婆、聞栩、赤翎、陸行烈、韓鐵衣、季垣、烏迭、監劫使、褚姊、莫渡、司天鑑、天罰一脈執行者、聞硯、v09 倖存者群、程岸、骨羅、秤書人；顧小滿補醫營期；蒼梧用「他」。
- **全庫機械統一**：身份→身分（104 處 56 檔，跳過 lower_realm_v2／archive／author_directives／drafts）。
- **\r\r bug**：published 下 41 檔 `\r\r\n` 雙重換行已修（make_clean_copy.pl 舊 bug，**不要再用那支腳本**）。
- **鏡像現況**：2026-09-25 收尾時全庫稽核 912 對 dev↔published（含 upper）**0 差異、無 \r\r**；lower_realm_v2 四章（v01 ch014/015/018、v03 ch016）已同步。
- **鏡像工具（在 session scratchpad，session 清空後需重寫）**：
  - `rebuild_mirror.py DEV MIRROR`：以 dev 整章重生鏡像＝標題行＋空行＋正文（略過章首「>」行、章末 `## 一致性自檢／本章自檢／修訂記錄／待確認提案／自檢／章末自檢` 之後全部，並去掉緊鄰的 `---`），保留鏡像原有 BOM 與 CRLF。已與既有 published 做 8 章 round-trip 逐位元組一致。**published/<卷>/ 同號鏡像首選此法**。
  - `sync_mirror.py BASE DEV MIRROR`：以 dev（BASE→現行）正文差異逐段套到鏡像，雙向驗證（新增行都在、刪除行都不在）不過就不寫；BASE＝鏡像檔最後一次 commit。用於標題編號不同的鏡像（lower_realm_v2）。
  - `body_cmp.py DEV MIRROR`：整章正文逐行比對（略過「>」、標題、空行、`---`、footer），印 SAME／DIFF。
  - `audit_mirrors.py [略過卷...]`：全庫配對（published/<卷>/ 同號＋依 upper_realm_v2/SOURCE_MANIFEST.md 解析 upper 對應），upper 比對忽略標題行，列出不一致清單。
  - **upper_realm_v2 一律用官方 `scripts/build_upper_realm_reading_v2.py`（先 `--check`）整體重建**，逐段替換套不上舊版段落。volume04_v2 目前沒有鏡像。

### ③ volume10～12
- **volume10 審查**：已產出 `docs/drafts/XIANXIA_TEXTURE_VOLUME10_AUDIT_PART1.md`（ch001～020）、`PART2.md`（ch021～040）。PART1 重點：ch020 封寒「兵胚」化暗影（L7/L27/L47/L49/L77）與 2026-09-16 鐧外形不變 retcon 衝突、黑洞是否已掌握各文件矛盾（先交總控定準）；ch019 L7 顧小滿「慢了半拍」違反慢半拍規則；蒼梧舊麒麟殘留（ch009 雷羽、ch010 咬袖口、ch013 L19「它」）且度量之道缺席；17/20 章章末格言；ch017/018 制度戲缺修士身體（C-5～C-8）。PART2 重點：病灶在敘述層（大綱「不得／不是」條件寫成旁白、每章「沒有」5～13 次、格言收尾，最重 ch039 L27）；ch025 L25／ch027 L29 糧車墊階梯需過 power-system 並登記 CHECKLIST（仙人視角）；伴星寵物化（ch026 L39 劫厄叼人＝硬禁忌、ch026 L45 赤翎續命超出角色檔、ch034 L27／ch035 L35 鑑月犬化），劫厄三訊號／鑑月喚名定魄／蒼梧頸段全段缺席；F-2 物件 bug：ch024 已交出上界端正印，ch038 L27 又交一次。**依作者「階段完成就停手」，未接續**。
- volume10 後續（未開始）：G 節窄查→代表例→四方→FINAL_FIX→回寫→PASS2→regression→鏡像→回報。volume11（56 章）、volume12（32 章）完全未開始。
- **保護清單**（寫手2 觀生句，PM 核可已 commit；質感改寫／掃除／regression 一律不動）：volume10 ch007 L13、volume11 ch022 L17、ch030 L25、volume12 ch024 L9、ch032 L11。
- **全卷規則沿用**：「慢半拍」只屬洛生衣；監察使＝司天鑑、機構＝天罰一脈；巡天令（司天鑑手上）≠巡天印（陸沉腕上，只追粗訊號）；模型→推演、聲紋→音紋；照命進階後稱煌命；蒼梧用「他」、鑑月／赤翎用「她」、劫厄用「牠」；劫厄三訊號（一暗一亮＝估量／整體轉暗＝耗損／胸口劫核＝失控）不可互換、不犬化；焦黑紋只在陸沉自己身上；不立「掌骨雷痕」專名；荒台詞不用「算」字（CHARACTER_LU_CHEN L220）。

### ④ 待作者／PM 裁定
- 465：天譴射程與同時目標數（基準表缺口；正文已做措辭消歧，射程留作者定）。
- 467：v09 ch049 醫營黑旗來源（建議 A 補一句）。
- 468：v09 ch033 周回女兒走位（建議 A 轉給無名孩子）。
- 466：v09 ch034 神識／肉身同時行動缺口（交清道夫 causality）。
- 370：v08 ch043 未落實 203 題黑洞誕生對話（留作者）。
- 361：鑑月新月印負荷徵兆（留白）。
- 伴星工具化（赤翎／劫厄／鑑月各補一筆）：PM 裁示併入「道的尺度」試點報告一起裁。
- v08 交 PM 清單（FINAL_FIX 末節）與 v09 交 PM 清單（FINAL_FIX「交 PM」）中其餘小項。
