# 《劫》正文改寫產線狀態板（2026-09-25 重整）

狀態：PM維護。舊版（369行歷史敘事）已歸檔於 `docs/archive/PIPELINE_STATUS_until_20260925.md`。**2026-09-25 已恢復運作；寫手1／2／3均完成本輪階段。目錄改版已commit `abdfe94`，現行新版驗證通過；舊材料已依作者裁示完成分類清理，必要資料13份移至docs。原 Claude sessions 未連接，不代表那些 sessions 已被喚醒。**

### 現行目錄與本輪提交
- 正文入口以 `docs/STORY_STRUCTURE.json` 為準：28個篇章群、867章，各層三位數排序；可讀對照見 `docs/STORY_STRUCTURE.md`。本板以下保留的 volume／arc 編號是歷史定位，派工須先用 manifest 的 `legacy_source` 對到現行 `source`／`published`，不能直接沿舊路徑施工。
- PM已推送：`25cd0cb`共同規則、`f6dda22`鏡像10檔修復、`bbe2e28`百斷山8章審查、`9d6dcfc`古界083／085／086局部修訂。目錄重整與工具變更已提交 `abdfe94`；遠端同步狀態以Git收尾查核為準。
- 現行驗證命令為 `python scripts/build_story.py --check`，核對867章正文、閱讀版、934個生成檔與28篇大綱；舊稿已清除，不使用舊檔例外。
- 依作者最新裁示，248個殘留舊路徑已清除；235份淘汰，13份必要材料移至docs並標明用途。詳見 [清理紀錄](STORY_LEGACY_CLEANUP.md)。

### 本次恢復交接
- PM：本次 Codex `/root`，統籌派工、範圍與交叉依賴；重大創作／設定決定仍交作者。
- 寫手1 `/root/writer1`：古界083／085／086本輪局部修訂完成；顧問獨立驗收無新增P0／P1，尚非全段定稿，向 PM 回報。
- 寫手2 `/root/writer2`：百斷山（舊下界arc05）ch001～008修士邏輯審查完成，未確認P0／P1，2項P2未修；與清道夫分區，向 PM 回報。
- 寫手3 `/root/writer3`：鏡像10檔修復與本輪版本盤點完成；鏡像唯一重建者，向 PM 回報；volume10的G節窄查為後續階段。
- 清道夫 `/root/scavenger`：volume03a_v2 起修士邏輯審查、因果與基準缺口，向 PM 回報。
- 顧問 `/root/advisor`：創作把關，與寫手討論並由 PM 彙整作者待裁問題；不直接改正文與唯一來源設定。
- 接班核對完成後，作者已授權正式開工：寫手1修 ch085～086；寫手2審下界 arc05；寫手3修復鏡像並盤點版本。角色識別僅適用本次對話，不沿用為其他 session 的身分。
- 作者再次強調：**任何開發、故事內容及世界觀都須從仙人／修士角度推演**，已補入 `XIANXIA_PERSPECTIVE_CHARTER.md` 第一節，所有派工共同遵守。
- 作者追加：**境界越高，人物感知、思考、行動、代價與世界文明越應呈現差異**；不可只放大戰力，已同步共同守則。
- 號段衝突：寫手2舊日誌「360起」不可沿用，360～379已屬寫手3；新登記先由 PM 核對未用號段。
- 本輪寫手3發現的鏡像落後已修復並推送（`f6dda22`，10檔）；舊交接的全庫零差異僅為歷史結果，目錄重整後須以現行builder重新驗證。
- 作者最新工作方式：每個階段完成並檢查後，由 PM commit 並 push；最終工作樹只留新版。已被新版完整取代的舊稿應移除並修正有效入口／引用，歷史由 Git 保留；尚未完整取代的內容先完成承接，避免刪掉唯一正文。開發稿與其同步閱讀鏡像屬同一新版的不同用途，不依檔名無 `v2` 就判為舊版。

## 一、現況摘要
- 主線大部已寫至第十九篇＋戰後沉封域；**古界N-2末段／N-3仍未完成**。古界入口 `novel/002_上界成道/009_界潮與古界/README.md`；ch080~086已寫，N2-7〈窗〉、N2-8未落筆，N-3亦未寫，不得標成全書完稿。
- N-2依據：作者2026-09-24/25裁決方案6（出口早就存在、難處在誰願意用它）；章綱`docs/outlines/ANCIENT_REALM_N2_CHAPTER_OUTLINE_DRAFT.md`、骨架`ANCIENT_REALM_N2_PLAN6_SKELETON.md`、CHECKLIST 231/320。ch080~084已審修（083/084為標竿）；本輪依原五審彙整修訂083／085〈沒有門〉／086〈告別〉，顧問獨立驗收無新增P0／P1，已推送`9d6dcfc`。記錄見`docs/drafts/N2_CH085_086_REVISION_20260925.md`；原`N2_CH085_086_REVIEW_SUMMARY.md`為歷史審查依據。窗口選日、封寒對側獨處、修士送傷者替代手段等未決，不能標成全段定稿。
- 已完成：volume02_v2/03/03a_v2/05/06/06b/07/08/09仙俠質感；causality全庫審查（`docs/drafts/CAUSALITY_DEBT_MASTER_TABLE.md`）與T0/T1補句；蒼梧代詞「牠→他」全書；終局人物歸宿表（`docs/outlines/OUTLINE_FINALE_CHARACTER_DESTINATIONS.md`）；洛生衣觀生錨點；舊published/upper_realm_v2曾通過鏡像稽核（歷史結果；現行目錄仍以本輪builder檢查為準）。
- 修士邏輯審查已恢復並完成本輪階段：歷史已審下界arc01~04、volume02_v2、volume03；本輪新增百斷山8章（未確認P0／P1，2項P2未修）。基準表`docs/systems/CULTIVATOR_LOGIC_BASELINE.md` v0.2、agent `.claude/agents/jie-cultivator-logic.md`、共同守則`docs/XIANXIA_PERSPECTIVE_CHARTER.md`仍有效。volume10~12質感改寫未開始（volume10審查報告已產出）。

## 二、待作者裁定（依重要度）
1. 空中救殿/救宗大型場面六題：`docs/drafts/BIG_SCENE_AIR_RESCUE_FLOWC_ROUND1.md`（位置已定後續卷/番外）。
2. volume03 P1：ch023荒獨去硬拆矛盾（三方向見`CULTIVATOR_LOGIC_AUDIT_VOLUME03.md`#1）；ch031補「四所互不統屬」一句；劫厄在三千州行蹤。
3. 465天譴射程、467黑旗來源、468周回女兒走位、370（203題對話）、345（已定「蒼梧」）、347鑑月/分身「牠」、閣老傷在胸口回填角色檔、442黑水城撞名、440人名撞字、CHARACTER_LU_CHEN L128慢半拍。
4. 下界arc03~04 B/D類一句補丁（已授權有限解凍：僅補一句專屬理由＋機械修正）；P1：arc04 ch009、arc03 ch007 L79。
5. 340 volume05前提：已採方案A止血；B/C待N-2完稿後裁。
6. 單卷承諾確認清單：`docs/drafts/SINGLE_VOLUME_PROMISES_CONFIRMATION_LIST.md`；原作待核項（御空/儲物/傳訊、461/462暫定口徑）等作者讀原作。

## 三、下一階段順序（由PM另派，以下舊編號先查manifest）
1. PM完成本輪必要性清理、標準驗證及commit／push；下一階段依未決事項與現行manifest派工。
2. 寫手1：本批修訂已完成；N2-7動筆前處理窗口與對側獨處等未決，再接〈窗〉（蒼梧自己決定不把窗口做更穩更久）、N2-8與N-3。不得把未裁新設定自行補成定案。
3. 寫手3：目錄重整後依現行builder核對閱讀版，再接volume10的G節窄查及後續質感工程。
4. 寫手2／清道夫：百斷山本批2項P2仍待處置；後續審查按manifest重新界定分區，既有候選範圍為03a_v2、04_v2至ch079、05起及已核可補句。
5. 全書完成後：`docs/FINAL_REVIEW_PIPELINE_MANUAL.md` 的最終審查pipeline。

## 四、協作規則（持續有效）
- 每次對話開始先ListAgents確認身分，讀本檔＋自己的`PIPELINE_WRITERn_LOG.md`。
- **git commit/push只由PM統一做**；寫手回報附「檔案清單＋一行摘要」。
- CHECKLIST號段：清道夫304~319/380~459、寫手1 320~339、寫手2 340~359、寫手3 360~379/460~479。
- 閱讀鏡像只由寫手3重建；現行映射以`docs/STORY_STRUCTURE.json`為準，使用`scripts/build_story.py`及其`--check`。舊`upper_realm_v2`與舊builder說明只作歷史參考。
- 作者指示原則：「階段完成就停手」；創作/設定重大決定（角色道、悲劇本質、新能力）交作者，連續性/對表由PM裁決。

## 五、角色↔session
ListAgents查當下事實，不記名字。角色：PM、寫手1、寫手2、寫手3、清道夫、顧問（創作面諮詢、與作者多輪討論）。

## 六、2026-09-24/25 作者決定索引（唯一來源檔在括號內；細節查CHECKLIST_PENDING_DECISIONS.md對應題號）
- **古界N-2**：方案6；先驗者封寒；殘鐧放N-3；不放寬蒼梧定位；隔日第二次代界（用第二次即走不了＝當樁）；骨刺顫固定兩次（N2-2/N2-7）；封寒折損三日；劃掉黎母阿荇（離界名冊）；聽島令歸還阿磯；轄域前因補在ch006/018/027；章數8~10不壓縮；N2-7高潮＝蒼梧自己決定不把窗口做更穩更久（CHECKLIST 231/320、`outlines/ANCIENT_REALM_N2_*`）。
- **蒼梧代詞**：敘事一律「他」，僅陌生人第一印象/獸群/物種描述可用「牠」；對他說話用「你」（CHECKLIST 343；盤點`drafts/pronoun_xuanheng_audit/`）。稱呼定「蒼梧」不用「梧」（345）。
- **268/269太玄閣**選C：閣後倒、三人只入簿待查、陸沉自認、宋知微守閣簿筆跡；306「劫瘫」→「雷者」；318選B（volume07古世回望）；315~317、319（06b時間帳）已施工。
- **通則**：雷身重凝（`systems/SYSTEM_THUNDER_BODY_DIVISION.md`五之二）；年數三十年硬錨；終局歸宿表；單卷收束清單（`drafts/CAUSALITY_DEBT_MASTER_TABLE.md`第七節）。
- **洛生衣誤判聞硯**：第三種（道沒有說謊、錯在把看得見的範圍當成全部；volume09 ch049保持全卷第一次）。
- **封寒終局近況**：volume12 ch024石片界石＋青璃一句；魔女容器＝後續卷；文奕落事件點C（volume12 ch013）。
- **修仙視角全書**（`XIANXIA_PERSPECTIVE_CHARTER.md`）：三層（詞/修士邏輯/仙人文明）；第三層第一輪決定：錨地承限（場域限制、相對語、不寫下界通則）、有限解凍lower_realm_v2（僅一句專屬理由＋機械修正）、大型場面（空中救一殿/一宗）放後續卷或番外，走流程C（`drafts/XIANXIA_CIVILIZATION_ROUND1_RECOMMENDATIONS.md`第七節、`drafts/RULE_ANCHOR_BOUNDARY_LIMIT_DRAFT.md`、`drafts/BIG_SCENE_AIR_RESCUE_FLOWC_ROUND1.md`）。
- 各人交接：`PIPELINE_WRITER1/2/3_LOG.md`、`PIPELINE_SCAVENGER_LOG.md`、`PIPELINE_ADVISOR_LOG.md`（2026-09-25新增一節）。
