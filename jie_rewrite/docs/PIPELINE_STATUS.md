# 《劫》正文改寫產線狀態板

狀態：PM維護的活文件，每次重大進度變化就更新。/clear後先讀這份，不用使用者重講。

**2026-09-19大整理**：本檔案累積過多已完全結案的歷史敘事段落，PM已將其精簡為指標式紀錄（結論+commit/檔案指標），完整過程可查git log與對應commit message，不再於本檔重複展開。日後新增紀錄也維持這個精簡原則：結案的事只留「結論＋去哪裡查完整過程」，不留完整敘事。

## 目前角色↔session名稱對照

一律靠ListAgents查詢當下事實＋讀`docs/PIPELINE_WRITER1_LOG.md`／`docs/PIPELINE_WRITER2_LOG.md`自我識別，不記錄具體session名稱（每次重啟都會變，記錄了也是舊的）。角色只有四種：PM（本檔案維護者）、寫手1、寫手2、清道夫。

## 我是誰、在做什麼

我是這個正文改寫產線的PM，管理寫手1、寫手2、清道夫三個獨立session。工作內容：
1. 收到回報後立刻判斷並派發下一輪任務（優先序：先讓大家不idle，PM審查/commit在那之後做）。
2. 對回報成果做複核（讀正文、視情況跑額外review agent），複核通過後直接commit+push（不用再問使用者）。
3. 遇到需要作者裁決的設定/結構衝突（不是PM能自己拍板的），才停下來問使用者。
4. 記錄每位協作者的優缺點供互相參考。

**標準作業原則（持續有效）**：
- 每次對話開始（含重啟後）先ListAgents確認身分，再讀本檔案＋自己專屬的log檔接續工作，不依賴對話記憶。
- **commit前務必先跑`git status --short`確認完整暫存區內容**——共用working tree下，別人未完成的變更可能被誤掃進commit；看到不認識的staged檔案先`git restore --staged`退掉。
- **派出大範圍改寫`docs/`唯一來源檔案的background agent時，PM自己不要同時對同一檔案下Edit**，避免併發覆蓋遺失內容；等對方完成回報後再繼續，或先確認範圍完全不重疊才並行。
- 寫手交付正文前應自跑一輪jie-continuity/jie-canon/jie-character/jie-power-system審查，抓到問題自己用jie-writer修過再回報。
- 章綱分節/分章數量不是死的，可依實際寫作節奏調整，只要保留核心情節、安全閥與轉折順序。
- 遇到「已有正文但可能retcon衝突」的段落，先審查找真衝突才局部改寫，不要因為有新大綱就整章重寫已經寫得好的內容。
- **陸沉呈現原則**（`characters/CHARACTER_LU_CHEN.md`）：最不可取代的特質是「持續在想辦法」不是「很能忍」，同一組考驗要逐輪升級（硬扛→觀察→察覺不對→改變局面），不能讓「受傷/撐住/不叫苦」的份量長期壓過「觀察/理解/找線索」。
- **寫手1、寫手2為Remote Control連線，`clear_session`對他們結構性無效**，不用再嘗試；只有PM能自我清空。
- 使用者本人仍在重讀原作《完美世界》核對原作侵入程度，進度持續推進中，`jie-canon`關於原作後段時間軸的覆核結論一律視為「暫定」，被使用者事後修正時不需過度檢討重查。

## 任務分配現況（隨時更新，這是查現況最準的地方）

**2026-09-20 新工作線**：下界 v2 已完成 65 章，暫停修改、留待冷卻後回讀。`volume02_v2` 上界篇依 `outlines/OUTLINE_VOLUME02_V2_UPPER_REALM.md` 完成**全 89 章**：第八篇 ch001～011、第九篇 ch012～038、第十篇 ch039～060、命藏 ch061～064、百宗盟試 ch065～082、雷魂域與鑑月 ch083～089；清道夫已連讀修復接縫，開發版／published 89 對全文一致。出宗門後的人物驅動見 `outlines/OUTLINE_CROSS_ARC_CHARACTER_DRIVERS.md`。下一卷禁都舊 `volume03a/chapter001.md` 仍引用舊 ch085／鎮無央，須在新 v2 接續施工時改為 ch089／鑑月，不能把舊正文直接接到新版後。古界 Act5 交接工作線仍按下表記錄。

**2026-09-20 禁都 v2 完卷**：獨立 `novel/volume03a_v2/` 與 `novel/published/volume03a_v2/` 全28章已對 `outlines/OUTLINE_VOLUME03A_V2_FORBIDDEN_CAPITAL.md` 成文，含文家遭難四章；清道夫核正文雙版一致及逐章綱對位，ch018 同擊雙寫已修。卷二 ch089 的鑑月／初得七日冷卻與舊傷接新 ch001；ch028 經文家事件北行多日抵赤衢驛，`volume03_v2/chapter001.md` 已改承新版並修正唐野名次。舊 `volume03a/` 24章與只刊3章的舊 published 僅作素材。

**2026-09-20 禁都 v2 密度精修**：章數與章序維持28；ch005～010、020、022～023 將住戶用水用藥、商戶名譽、岑婆停令、維修交接、雙份紀錄簽認及夜路實測寫成現場選擇，已逐章回填同一份28章綱。清道夫核九章開發稿與 published 正文一致，章綱、時序、能力無 P1；ch010 扭傷者身分過度指定已修。

**2026-09-20 v2 卷冊對照**：`docs/V2_VOLUME_READING_MAP.md` 已將下界三卷後的上界89章分為閱讀卷四～六，禁都28章為卷七，三千州69章於 ch039／040 分為卷八、九。此為編輯卷號；施工資料夾不搬移，卷四～九獨立閱讀版與逐章來源表尚未生成。宏綱第十二篇與文家插段正文座標已更新至禁都 v2 28 章；第十三篇仍是三千州全69章，不因分卷改篇序。

| 寫手 | 目前任務 | 狀態 |
|---|---|---|
| 寫手1 | 古界Act1～4交稿；Act5不屬此分工 | ✅ `novel/volume04_v2/chapter001~046.md` 共46章（9／11／15／11）已完成四方審查；Act4末在望汐崖三人重會，轉入五島終局。詳見`PIPELINE_WRITER1_LOG.md`第44～49筆。 |
| 寫手2 | **接手Act5〈五島終局〉章節架構**；先把四格骨架、舊ch018～019與ch036～056可保留場景整合為逐章大綱，經PM審核後才落正文 | 既有評估、蒼梧「劃界失效」方案與殘鐧第五幕位置見`PIPELINE_WRITER2_LOG.md`第32～37筆；此階段尚未有新版Act5正文。 |
| 清道夫 | 待Act5章綱及首批正文交稿後審查 | 既有跨卷清理成果保留；古界Act1～4四方審查紀錄見寫手1 log。 |

**更新守則**：這張表跟兩份`PIPELINE_WRITERn_LOG.md`必須保持一致——寫手每完成一段就自己補log，PM每次收到回報/commit後就更新這張表，不要等整批任務結束才補記。

## 待使用者裁決事項（現存）

- **聽島＝陸沉未來「鎮界」（十雷之一）起源**：已轉呈使用者，未回覆，不影響寫手1/2繼續往下寫（暫依現狀不加深關聯）。
- **第213題**（古界只用陸沉本名不出現「劫」）：已使用者核可（`WRITING_GUIDELINES.md`第三節已回填）。
- **第214題**（潮會灘/柏灘部/祈叔三個世界背景設定最小追認）：待確認，不影響已完成正文。

## 已結案事項（指標式紀錄，完整過程查git log/對應doc）

- **三千州爭鋒v2.0整段重寫**：`novel/volume03_v2/chapter001~069.md`全69章完稿，全庫規模最大單項retcon，PM逐批複核commit。舊版`novel/volume03/`保留供查考，swap時機未定。
- **天神書院排位大會retcon（RC-V06）**：202~206題設計階段已關閉，UNBLOCK，12章大綱TRANSFORM完成，後續追蹤在`CHECKLIST_NOVEL_REVIEW_FIXES.md` RC-V06系列。
- **封寒與陸沉相識起點（第201題）**：`CHARACTER_FENG_HAN.md`四之4.1/4.2回填完成，`chapter040.md`/`chapter047.md`回溯修正完成。
- **古界篇長篇化擴建**：Canon Recovery→structural design→五幕重排→Scene Architecture（46章大綱）全部完成，「禁止開寫」已於2026-09-19解除（僅限Act1~4新寫，Volume04舊版56章retcon本體與Act5範圍不受影響），現正分批動筆。完整過程見`CHECKLIST_NOVEL_REVIEW_FIXES.md` 0.4節。
- **青璃混血/相界retcon（185題）**：`CHARACTER_QING_LI.md`升v1.3等已全部回填完成，僅RC-QL-04（P2）未完成不急。
- **volume01/02/03_v2/05/06/06b線性密度優化**：清道夫全卷掃完，抓到的所有bug詳見`CHECKLIST_NOVEL_REVIEW_FIXES.md` CB~CE節。

## 尚待排產的backlog（未開始，排期前先看這裡）

- **古世雙界遠行**：`OUTLINE_ANCIENT_WORLD_DUAL_REALMS.md`，雙線約50章，已完稿於`novel/volume06b/`（清道夫已掃完）。
- **帝關界路擴寫**：`OUTLINE_BORDER_ROAD_EXPANSION.md`，已完稿於`novel/volume07/`（清道夫掃描中）。
- **異域V08整卷重建**：`OUTLINE_FOREIGN_DOMAIN_REFORGING.md`，40→92章，規模最大，Act III約50章細節未逐章拆解，設定層級183~192題均已完成四方覆核回填，未動筆。排期時注意第265行舊版章節引用需訂正為`chapter071.md`。
- **書院寶庫插入**：`OUTLINE_ACADEMY_VAULT_INTROSPECTION.md`，2章，使用者已裁示整體後移編號，執行時volume06現有ch031~048要順移。
- **187禁都大篇擴充**（方案5全量組合，5~6章新增）：會重新打開已commit的`novel/volume03a/chapter005~020.md`，牽動`novel/README.md`等下游文件，尚未進入執行階段，larry-ad團隊會在啟動前通知PM。
- **189千年古界完整版**：內外時間流速差異解法已定案，理論上不牽動已發布內容，尚未進入章節設計階段。
- **ch080起（volume02）命藏/命圖初開新弧**：尚未排入正式篇號。
- `CHECKLIST_PENDING_DECISIONS.md`累積的其他待回填項目仍在等討論收斂。

## Production Pipeline系統性觀察（僅記錄不處理）

**2026-09-18使用者觀察**：Decision與Planning/Review這兩段很強，但Implementation tracking沒有形成真正的狀態機，導致「已決定」被誤讀成「已完成」。使用者明確表示現在不開工程線處理，等古界新版架構穩定後再回頭考慮，目前不需要任何session採取行動。
