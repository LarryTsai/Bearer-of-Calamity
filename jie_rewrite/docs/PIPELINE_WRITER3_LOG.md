# 寫手3 工作日誌

## 角色
- 從 PM 接工作，手上沒事就主動找 PM 要。也支援寫手1、寫手2，分工先協調好，不碰對方的檔案。
- 只存檔，不 git add/commit/push（一律由 PM 做）。新設定走 `docs/CHECKLIST_PENDING_DECISIONS.md` 提案；範圍外的 bug 另報 PM，不混進當下的工程。
- 正文每次修改都要同步所有鏡像：`novel/published/<卷>/`，以及 **`novel/published/upper_realm_v2/`**（閱讀版，分卷編號不同，部分段落是舊版）。保留 BOM 與換行；不跑 make_clean_copy.pl（它會把 CRLF 疊成 \r\r\n），改用同段精確替換，最後檢查每檔增刪行數相等。

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
