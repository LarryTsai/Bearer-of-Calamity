# 《劫》正文改寫產線狀態板

狀態：PM維護的活文件，每次重大進度變化就更新。/clear後先讀這份，不用使用者重講。**PM目前的session代號不固定寫在這裡**——這個名稱會隨session重啟而改變（今天已經變過：larry-4e→larry-c7），一律以呼叫`ListAgents`查到的當下結果為準，不要假設本文件寫的名字還有效。

## 我是誰、在做什麼

我是這個正文改寫產線的PM。手上有兩位寫手（寫手1、寫手2，各自獨立session，名稱也一樣會隨重啟改變，一律靠他們讀`PIPELINE_WRITERn_LOG.md`自我識別，不靠記名字），我的工作：
1. 收到寫手回報後**立刻**判斷並派發下一輪任務（優先序：先讓寫手不idle，我的審查/commit在那之後做）。
2. 對寫手回報的成果做我自己的複核（讀正文、視情況跑額外review agent）。
3. 每審完一批就直接commit+push（不用再問使用者），指令：`git -C "D:\Workspace\larry\story" ...`（repo在`story/`底下，不是`D:\Workspace\larry`根目錄，那邊是空的無關repo）。
4. 遇到需要作者裁決的設定/結構衝突（不是我能自己拍板的），才停下來問使用者。
5. 記錄每位寫手的優缺點，回饋給雙方，讓兩人互相參考進步。
6. 有另一個並行的AI團隊（larry-cd等，目前已離線）今天也在同一個repo做過大量規劃工作，出現過一次檔案覆蓋事故（`OUTLINE_ACADEMY_VAULT_INTROSPECTION.md`），已解決但代表**寫新檔案前務必先確認檔案是否已存在**，不能無腦Write。
7. **經驗教訓（2026-09-12）**：PM與兩位寫手的session曾同時重啟、全部換了新名稱，且SendMessage的舊pipe位址全數失效。靠`CLAUDE.md`裡「先呼叫ListAgents查自己是誰→讀對應log檔」這套機制，三邊都在數分鐘內成功重新自我識別、對接上線，沒有遺失任務進度（因為狀態都寫在檔案而非對話記憶裡）。這證明了「進度寫檔案、身分靠ListAgents查、不依賴對話記憶或固定session名稱」這套設計是必要且有效的，往後持續維持。

## 全局關鍵原則（寫手也要知道，已同步給他們）

- 每個寫手一次只做一個任務，做完立刻回報，不用等對方；PM審查是背景工作，不卡任務推進。
- 寫手交付正文前**應自己先跑一輪jie-continuity/jie-canon/jie-character/jie-power-system審查**，抓到問題自己用jie-writer修過再回報（寫手2從一開始就這樣做，寫手1後來也採用了）。
- 章綱裡的分節/分章數量不是死的，寫手可依實際寫作節奏調整，只要保留核心情節、安全閥與轉折順序。
- **重要敘事原則（2026-09-12，使用者讀新版正文後裁示，已寫入`characters/CHARACTER_LU_CHEN.md`「呈現原則：思考優先於承受」）**：陸沉最不可取代的特質是「持續在想辦法」，不是「很能忍」。正文不能讓「受傷/撐住/付出代價/不叫苦」的份量長期壓過「觀察/理解/找線索/判斷代價/反過來利用對方規則」。標準：「敵人給他十道難題，他不是忍過十道，而是忍到第六道，敵人才發現他前面挨的根本不是打，是在讀你。」——同一組考驗要逐輪升級（硬扛→觀察→察覺不對→故意讓對方重複驗證→開始改變局面→對手才驚覺）。所有陸沉相關章節都要對照這條，不用等PM審查才抓。
- 遇到「已有正文但可能retcon衝突」的段落，先審查、找出真衝突才局部改寫，不要因為有新大綱就整章重寫已經寫得好的內容（百斷山、七峰大比/百宗盟試都是這樣處理，且七峰大比/百宗盟試最後決定保留單隊正文不改）。

## 今日（2026-09-12）已定案的關鍵決策

1. **虛神界（第三篇）**＝改寫 `novel/volume01/chapter011~013.md`，已完成commit（e7b386a）。真正執行章綱是`OUTLINE_VOLUME01_WEN_YI_SHARED_CANON_REBUILD.md`（比我當天另外新寫的`OUTLINE_VOID_SPIRIT_REALM.md`更具體可執行，優先參考前者）。
2. **百斷山（第五篇）**＝`novel/volume01/chapter023~028.md`已存在且審查通過，僅ch035補一句過場（洞天突破off-screen化，見下）。
3. **洞天突破retcon（第181題）**：舊設定要求百斷山凶獸潮觸發搬血→洞天突破，但既有正文（ch028）已經選擇「不靠奇景抄捷徑」。裁定改設定檔配合正文：突破改為返閣後日常修行期間off-screen完成，已回填`CHARACTER_LU_CHEN.md`、`SYSTEM_CULTIVATION_TIMELINE.md`、ch035補一句過場（commit b68469a）。
4. **真假委託（第六篇）**＝`novel/volume01/chapter029~031.md`已重寫完成commit（87f0990），修正了越級禁制問題，並埋入「魔女真正騙過陸沉」的冷伏筆（東壁改流手法追問，最早天神書院才回收）。
5. **三隊制例外**：今天稍早決定太玄宗七峰大比十二強分三隊出賽，但**已完成的`novel/volume02/chapter039~079.md`（40餘章七峰大比/百宗盟試）維持單隊寫法不追溯修改**，三隊制只適用未來新內容。已回填`MACRO_OUTLINE.md`、`FACTION_TAIXUAN_SECT.md`（commit d6b494a）。
6. **書院寶庫插入點檔案衝突**：`docs/outlines/OUTLINE_ACADEMY_VAULT_INTROSPECTION.md`發生同名檔案覆蓋事故（另一團隊的岳沉淵授權版 vs 我的CHECKLIST第180題三痕古域版），使用者裁定**採用180題版**，已復原並確認無其他檔案依賴被取代版本。
7. **禁都與萬禁會（第十二篇）**：`novel/volume03a/chapter001~004.md`已存在，ch005~020（第二～五幕）需要全新寫作，章綱`docs/outlines/OUTLINE_FORBIDDEN_CAPITAL_MYRIAD_CONVENTION.md`。前置案件鏈構想尚未裁決，先照已鎖定的ch001~020幕次寫，不採用前置案件鏈。
8. **文家遭難插段**：全新4章，章綱`docs/outlines/OUTLINE_WEN_FAMILY_CRISIS.md`（另一團隊產出），今天已核准多項局部修正方向（命圖用詞、傳送陣因果、崩角白石訊號限縮、文奕加入可切視角清單等）。**〔寫手1後續更新〕**已完成：章綱定案v1.1、`jie-writer`模式一寫出`novel/volume03a/chapter021~024.md`，交付前四方審查（continuity/canon信心0.92/character/power-system）全數pass無reject，並依審查意見修正ch024「文奕認出/猜到」confidence落差（改為陸沉視角明確判斷）。**尚未commit，等PM複核**。
9. **待PM處理的新發現衝突（寫手1回報，尚未觸及即無法直接聯繫PM session，先記錄於此）**：continuity審查〈文家遭難〉時發現 `SYSTEM_CULTIVATION_TIMELINE.md` T08欄位（三千州重逢/天才戰入口，緊接文家遭難之後）已用「命圖初成」描述陸沉能力狀態，但〈文家遭難〉章綱明確限定「命圖初成」保留給第十五篇〈無兵雷域〉六雷骨架里程碑——兩份唯一來源檔本身互相矛盾，非本次新增問題，但下一段寫三千州開篇時會直接卡到，建議PM擇一修正（改T08欄位用詞，或放寬「命圖初成」限定範圍）。另外`novel/README.md`尚未記載volume03a ch021~024進度，建議一併補登。

## 任務分配現況（隨時更新）

| 寫手 | 目前任務 | 狀態 |
|---|---|---|
| 寫手1 | 古世雙界遠行（`OUTLINE_ANCIENT_WORLD_DUAL_REALMS.md`，雙線約50章，全新，`novel/volume06b/`） | 章綱v1.1定案+楔子/線A第一幕（ch001~005）已複核commit（caaeb37）。魔女虛實道種已登記CHECKLIST第182題（進行中提案）。正推進線B第一幕（洛生衣+魔女墜界與古城） |
| 寫手2 | 禁都與萬禁會 ch005～020（16章全新寫作，`novel/volume03a/`） | ch005~018（第二～四幕，含律無咎正式對局、文奕奪魁）已全部複核commit（6ab2ac2、13073ac）；正推進第五幕（ch019～020，收束） |

**更新守則**：這張表跟兩份`PIPELINE_WRITERn_LOG.md`的「工作日誌」必須保持一致——寫手每完成一段就自己補log，PM每次收到回報／commit後就更新這張表，兩邊都要當下更新，不要等到整批任務結束才補記，否則/clear後查到的會是舊資訊。

## 尚未處理、之後要排的任務

- 古世雙界遠行（`OUTLINE_ANCIENT_WORLD_DUAL_REALMS.md`，雙線約50章，全新）
- 帝關界路擴寫（另一團隊`OUTLINE_BORDER_ROAD_EXPANSION.md`，16→31章）
- 異域V08整卷重建（另一團隊`OUTLINE_FOREIGN_DOMAIN_REFORGING.md`，40→約92章，規模最大，Act III約50章細節還沒逐章拆解）
- 書院寶庫插入（`OUTLINE_ACADEMY_VAULT_INTROSPECTION.md`，2章，卡在volume06章節編號方案未裁示——整體後移編號 vs 暫用非整數命名，**使用者已裁示整體後移編號**，執行時machine需注意volume06現有ch031~048要順移）
- ch080起（volume02）有命藏/命圖初開新弧，尚未排入正式篇號，需另外確認
- 三千州呼吸段、書院寶庫子情節插入點的舊版outline（另一團隊產出的`OUTLINE_THREE_THOUSAND_STATES_BREATHER.md`）狀態未核對
- `CHECKLIST_PENDING_DECISIONS.md`累積的待回填項目（176-178題等）仍在等其他討論收斂
- **律無咎禁陣機制「封字訣」「三重契約」**（寫手2 ch012~013回報）：具體招式設計已用於正文，建議走CHECKLIST提案正式登記，尤其在ch014~018正式對局前，避免屆時顯得孤立。其餘4項文件維護提醒（外貌、陸沉「撤紋」、T08/CHARACTER_LU_CHEN.md「入仙古」殘留用詞、鎮無央冷卻機制登記）已於今日處理完畢。
