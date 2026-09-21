# 9/21 urgent 第三批交付與回歸

狀態：本批已交付並完成有限範圍驗收。使用者在第二批後指示「繼續」，沿原全角色配置→清冊→正文回填工作線推進；**不是五份顧問要求或全書工程全部完成**。

## 配置與清冊實際交付

- [陸沉戰技檔](CHARACTER_COMBAT_LU_CHEN.md)：LC-00～17，從殘紋／殘篇至古界真一；按關鍵取得切版本，不只按雷數。列每版手段、限制、套裝層次、體術／禁／雷身演化、首用證據與未核清單。
- [封寒戰技檔](CHARACTER_COMBAT_FENG_HAN.md)：FH-01～08，劍路、鈍劍、深層交重劍後空鞘、古界左右傷史及步法護送；入口特殊吞入有來源但常規可用資格待統一，未換鐧。
- [配置矩陣](CHARACTER_COMBAT_MATRIX.md)：角色排產、七峰四人同時期橫向對照、場次碼對接與顧問舊圖概念處置。未逐張看圖，不稱圖面已驗收；遠期概念不授早期能力。
- [戰鬥清冊](BATTLE_INVENTORY.md)：B組全文連讀02 ch039～060與038／061邊界，登錄26項已演出比賽／演習／自練。回述戰績、報名、名單不冒充完整戰鬥。下界、盟試、深層及其他篇尚未逐場入冊。

來源核稿：A、C分別對照各自證據複核個別檔，修正陸沉下界左肘是扣石縫而非肘擊、五息是早期自主停而非首次時長；045未用劫命限定當次傷脈風險，鎮魄僅取得後可用。封寒046只是決定去拆解、深層受力後不能追第二手，均已縮準。新檔相對連結檢查無缺失。未核首用／境界列證據待辦，不冒充正文P1。

## 正文修訂與獨立審查

| 工單／來源 | 問題與最後修法 | 保留的結果／验收 |
| --- | --- | --- |
| U-B6／02 ch040，閱讀卷五第2章 | 原文只有一個清楚命中便判兩擊；補常岳反推後陸沉收肘讓力、肩撞胸前符，兩符各亮 | 原勝者、常岳反制、陸沉胸肋／左腿傷不變。A與C各核039～041，未碰傷停線 |
| U-B4／02 ch050，卷五第12章 | 原先聽到青璃完整警告後仍打；改原案先壓右節，交界露出即警告、立即收掌撤槍。已有壓力沿槍回灼，木釘完整 | 槍手燙臂、江離失步分、青璃滴水驗證與替案主導、四人取牌／傷後限制均保留；C連讀049～051 |
| U-B7／02 ch055，卷五第17章 | 原先054知缺交接，隔日又像未學；改昨夜先排次序，第一門成功，第二門變頻／早回扣／反捲／折門才失效。陸沉在車後等、各人報未完成 | 洛側頂車的左臂傷、超時與「未接」碼保留；C核054～056及058～060，沒有重置已學知識 |
| U-B5／02 ch059～060，卷五第21～22章 | 兩息內塞護送穩脈往返；將安置兩人、穩脈與回箱旁放在起計前，两息只切帶／抽箱／撞劍卡角／肩接。059末及060回指改不再靠傷者肩接 | 人箱全過、四人耗傷、兩息上限與停手醫令、隊长讓權均不變；C核058～060及最後兩句diff |
| U-A2-N／03a ch001，閱讀卷八第1章 | 劫命身誤稱校為承身 | 本尊＋煌命身＋承身，不新加身體；A連讀02 ch089→03a001／002，鎮魄期限、鑑月未外顯及傷一致 |

C獨立連讀039～041、049～051、054～056、058～060，共12章，最後正文 **PASS，無未解P0/P1**。A另核040與禁都命名。PM連讀本批修訂段及後續回指，補核章綱。B為050／055寫手，其自審不充作唯一驗收；040／059／060與命名由PM修。

本批未替045乾砂累積等P2候選擴篇，亦未合併054～056章號；明列於清冊，無須為字數配額加新試錯。

## 發布與檢查

已同步發展稿與對應clean published：02 ch040／050／055／059／060，03a ch001；用既有生成器重建閱讀卷。禁都有定位與自檢，須用既有`clean_source`清除工程段，不能直接複製完整發展稿；第一次檢查抓到此格式差異後已修正。

- `build_upper_realm_reading_v2.py --check`：上界226章及來源表通過。
- `build_v2_reading_index.py --check`：十卷291章通過。
- 本批四份配置／清冊文件：相對連結零缺失。
- `git diff --check`：通過。

章名與章序未變；未新增古界閱讀卷，未改正式人物／系統能力設定。上批古界修稿與七峰044保留。驗收完成時尚未提交；使用者隨後明確要求每個修訂段落即commit／push，PM依此分段補交並核遠端，提交結果以Git歷史為準。

## 分段提交追蹤

依使用者最新指示，已將前述與上批未提交的正文補成13筆，**每筆commit後即push，origin/main均已接受**；下表含上批古界及七峰044。各筆均核暫存區只含指定章與相應發布版，不含快取或其他工作。配置、章綱、清冊、驗收與持續提交規則另作紀錄提交。

| Commit | 已推送內容 |
| --- | --- |
| `7860e14` | Clarify the second scoring hit against Chang Yue |
| `b7ba58a` | Expand Lu Chen and Feng Han semifinal exchanges |
| `47bad81` | Make Lu Chen stop when Qing Li warns of backlash |
| `5ef255d` | Preserve learned handoffs when the training route changes |
| `4461ac5` | Fit the mine rescue actions within the two-breath limit |
| `fc99326` | Restore Cheng Shen naming at the Forbidden Capital entrance |
| `764cc9e` | Stop the unsafe promise from sending the medicine team onward |
| `1b65f7b` | Carry the stopped promise into the fourth-marker inspection |
| `63b2cd3` | Keep personal responsibility when withdrawing the promise |
| `a019689` | Preserve the learned limits before the three-route evacuation |
| `4b309e6` | Make the east-dike setback arise from handoff timing |
| `856ff5b` | Separate accountability from the True One breakthrough |
| `3a7c046` | Remove an engineering chapter reference from the South Shore scene |

## 下一批入口

1. 陸沉：補02 ch022～036／064～082及下界突破全文，核後篇體修、虛渡、固定兵器鏈；分清外火促短線與正式活禁的「第一次」、03ch048「這輩子一次」究竟限制何者。
2. 封寒：核深層返宗後領劍／復健證據；對齊入口本能吞入例外與人物／Act4的無常規能力范围；殘鐧與天煞舊座標不直接套到現行。
3. 下一組洛生衣／青璃／雲行完整歷代配置，其他核心角色與長線敵手續排；七峰之外全文戰鬥清冊尚未完成。
4. 三龍台仍以C2已查窗口為下一步依據，新事件與雙鑰保管回填未施工。

方法回顧：此輪屬跨章學習、短時能力動作排程、來源與實績分離，既有審校技能已涵蓋，不新增通用skill規則。
