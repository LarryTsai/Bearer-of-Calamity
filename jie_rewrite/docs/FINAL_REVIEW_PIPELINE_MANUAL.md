# 《劫》最終回顧審查 Pipeline 使用手冊（Final Review Agent Blueprint v1）

本文件記錄 2026-09-13 建置的一套「全書／大篇章完成後」專用的多層審查 Agent 群，目的是在正式收尾前做一次比日常寫作流程更徹底的總體檢查。

**這套 pipeline 目前只完成建置，尚未執行過任何一次。** 使用前請重讀本文件一次，尤其是「實務執行建議」一節——直接把全部 agent 對全書跑一輪，會產生遠超單次對話可處理的輸出量與成本，必須分批。

## 一、這套 pipeline 跟 `CLAUDE.md` 既有工作流的關係

`story/jie_rewrite/CLAUDE.md` 描述的是**日常產出流程**：每次寫一段新劇情或處理一批新正文時，跑 `jie-creative → 平行審查 → jie-chapter-editor → jie-writer → 最終審查三件套`。那套流程管的是「這一批新東西有沒有問題」。

這份 pipeline 管的是**全書或大篇章尺度的總體健檢**：適合在以下時機使用——

- 某個大篇（依 `docs/MACRO_OUTLINE.md` 分篇）全部正文完成後，做一次收尾前總審。
- 完成一輪大規模 retcon（例如 `VOLUME04_RETCON_CHAPTER_PLAN.md` 這類跨章改寫）之後，需要確認沒有「修 A 壞 B」。
- 全書（或已完成的卷冊）累積到一定量之後，做一次跨卷角色與世界一致性總體檢。
- 準備對外發布／完稿前的最後一輪品質把關。

**不要**把這套 pipeline 當成每章都要跑的日常流程——那樣做只會拖慢產出速度，也不是這些 agent 的設計目的。

## 二、Agent 總表

### 既有沿用（不需新建，行為與 `CLAUDE.md` 描述一致）

| Agent | 在這套 pipeline 中的角色 |
| --- | --- |
| `jie-continuity` | 世界一致性層：時間線/境界/稱呼/物品/地點 |
| `jie-canon` | 世界一致性層：《完美世界》原作相容性 |
| `jie-power-system` | 世界一致性層：境界、十雷、命圖、伴星戰力狀態 |
| `jie-causality` | 世界一致性層：單一事件的前因後果鏈（場景級） |
| `jie-chapter-editor`（模式二） | 故事品質層：單章節奏與禁用寫法 |
| `jie-reader` | 讀者體驗層：第一次讀某段的即時直覺反應（＝藍圖中的「reader-first-pass」） |

### 新建：角色人生層

| Agent | 是否為通用模板 | 說明 |
| --- | --- | --- |
| `jie-character-life-simulator` | 是（每次指定一位角色） | 單一角色從頭到尾的第一人稱人生模擬 |
| `jie-character-crosscheck` | 否 | 比對多位角色人生軌跡的矛盾 |
| `jie-relationship-arc` | 否（每次指定一組關係） | 特定關係組的演變曲線 |

### 新建：世界一致性層（既有四個的補充）

| Agent | 說明 |
| --- | --- |
| `jie-knowledge-state` | 每個角色在每個時間點知道什麼 |
| `jie-world-state` | 世界背景是否隨主角離場持續運作 |
| `jie-foreshadowing-payoff` | 全書尺度的伏筆帳本（與 `jie-causality` 的場景級因果鏈互補） |

### 新建：故事品質層

| Agent | 說明 |
| --- | --- |
| `jie-arc-structure` | 單一「篇」的起承轉合（比 `jie-chapter-editor` 大一級） |
| `jie-global-structure` | 全書篇與篇之間的節奏/類型分布 |
| `jie-pacing` | 連續多章疊加的密度曲線與疲勞感 |
| `jie-battle` | 純戰鬥：戰術、辨識度、大招鋪墊、體系一致性 |
| `jie-dialogue-voice` | 純對話：角色聲音是否趨同 |
| `jie-emotional-continuity` | 重大事件後的情緒延續與消退 |
| `jie-protagonist-balance` | 陸沉是否什麼都會、配角是否仍不可替代 |
| `jie-supporting-cast-agency` | 全體配角是否有自己的目標（橫向掃描版） |
| `jie-mystery-reveal` | 秘密揭露節奏是否過早或過晚 |
| `jie-originality` | 是否過度近似其他靈感來源作品 |

### `jie-arc-structure` 方法論修正（2026-09-23，回應第257/253題，使用者裁定，呼叫時務必內建在prompt裡）

因257題〈百宗盟試〉的試跑結果（65章硬算成一篇，必要卡點18章/28%處就已完整兌現，後面72%其實是另外兩組獨立命題）暴露出這個agent原本的判斷方式有兩處系統性問題，使用者要求所有後續呼叫都要修正：

1. **先判斷篇界是否切對，再判斷高潮位置**：不要一拿到章節範圍就直接算「高潮在第幾%」。若這個範圍其實橫跨了兩個以上主題、場域、核心衝突完全不同的獨立故事（不是同一條主線的前後失衡，是根本不該算同一篇），「高潮前置」很可能是假問題——真正的問題是篇界本身沒切對。判斷篇界是否需要拆分時，可比照`docs/MACRO_OUTLINE.md`已有的「篇間插段」先例（如第十二、十三篇間插段〈文家遭難〉）。
2. **不再硬性要求「至少一位主角不可逆變化」，改為「故事結束後，世界不能完全回到起點，必須存在至少一項有敘事意義的不可逆結果」**——這個不可逆結果不必是角色本身的變化，可以是：讀者知道了一個無法忘記的真相／世界狀態改變／一個地方毀掉／一群人的命運改變／某條未來因果被啟動／主角雖未升級但第一次看見下一個高度／角色自己沒變但世界第一次知道他們存在。**明確禁止**：若一段內容本來就沒有這類問題（例如`OUTLINE_ANCIENT_BATTLEFIELD_DEEP_V2.md`明文刻意讓主線四人不產生不可逆變化，是有意的設計選擇），不得為了通過這條硬指標，反過來替內容發明一個不需要的永久傷勢/能力/關係轉折——**方向反了：不能為了通過結構檢查而修改原本沒有問題的故事**。

呼叫`jie-arc-structure`（不論總控或寫手）時，請把以上兩點原則寫進prompt本身一併提供給agent，因為此agent定義本身不在本repo內、無法直接編輯，只能靠呼叫時的指示覆蓋舊方法論。

### 新建：讀者體驗層（`jie-reader` 之外的其他讀者視角）

| Agent | 是否為通用模板 | 說明 |
| --- | --- | --- |
| `jie-reader-binge` | 否 | 完本讀者：整體疲勞與風格斷裂 |
| `jie-reader-serialized` | 否 | 追更讀者：記憶負擔與章尾吸引力 |
| `jie-reader-character-fan` | 是（每次指定代入哪個角色的粉絲） | 專抓角色是否只被拿來服務主角 |
| `jie-reader-huang-fan` | 否 | 原作荒粉視角：陸沉是否搶了荒的功業 |
| `jie-reader-newcomer` | 否 | 沒看過原作的新讀者：是否過度依賴原作知識 |

### 新建：最終裁決層

| Agent | 說明 |
| --- | --- |
| `jie-line-editor` | 文字級（重複句式/過度解說/旁白越界/形容詞堆疊），只在內容穩定後才跑 |
| `jie-regression` | 修改完成後掃描「修 A 壞 B」 |
| `jie-final-editorial-board` | 彙整所有審查報告，分 P0/P1/P2 |
| `jie-author-intent-guard` | 最後一道：防止其他 agent 把作者刻意的設計當成缺陷改掉 |

## 三、核心必跑 vs 選配

作者原訂「不能省」的核心清單：`character-life-simulator`、`character-crosscheck`、`knowledge-state`、`continuity`、`canon`、`power-system`、`causality`、`arc-structure`、`global-structure`、`reader-first-pass`（＝`jie-reader`）、`regression`、`final-editorial-board`，共 12 個。

**待確認事項**：作者同時把 `author-intent-guard` 稱為「最後一道」，語氣上也是不能省的，但沒被列進上述 12 個核心清單。實務上這道關卡的作用（防止其他 agent 用「標準寫法」誤改作者刻意的設計）跟 `final-editorial-board` 一樣是全域性、不特定於某個檢查角度，建議視為**第 13 個事實上的核心步驟**，除非作者本人確認可以省略。

其餘 12 個（角色關係層的 `relationship-arc`、世界層的 `world-state`/`foreshadowing-payoff`、故事品質層全部、讀者層除 `jie-reader` 外的其他四個、以及 `line-editor`）屬於選配，依下列情況決定是否加開：

- 這一輪明顯涉及多角色感情或友情線大幅推進 → 加開 `relationship-arc`
- 這一輪主角長時間離開某個場景／勢力 → 加開 `world-state`
- 已經好幾篇沒有正式盤點伏筆 → 加開 `foreshadowing-payoff`
- 這一輪包含大量新戰鬥設計 → 加開 `battle`
- 懷疑角色對話開始像同一人在說話 → 加開 `dialogue-voice`
- 準備發布／即將完稿，需要壓力測試讀者觀感 → 加開讀者層其餘四個
- 內容已經穩定、準備最後定稿 → 加開 `line-editor`

## 四、固定執行順序

```
第一階段｜人物各自活一次
  jie-character-life-simulator × N（逐位主要角色，各自獨立呼叫、獨立 context）
        │
        ▼
第二階段｜人物互相比對
  jie-character-crosscheck
  （＋ jie-relationship-arc，若這輪涉及重要關係推進）
        │
        ▼
第三階段｜世界一致性總查（可平行呼叫，彼此不依賴）
  jie-continuity / jie-canon / jie-power-system / jie-causality
  jie-knowledge-state
  （＋ jie-world-state / jie-foreshadowing-payoff，視需要）
        │
        ▼
第四階段｜每篇結構
  jie-arc-structure（逐篇呼叫）
        │
        ▼
第五階段｜全書結構
  jie-global-structure
        │
        ▼
第六階段｜戰鬥／情緒／對話（可平行呼叫）
  jie-battle / jie-emotional-continuity / jie-dialogue-voice
  （＋ jie-protagonist-balance / jie-supporting-cast-agency / jie-mystery-reveal / jie-originality，視需要）
        │
        ▼
第七階段｜多種讀者盲讀（可平行呼叫）
  jie-reader（＝reader-first-pass）
  （＋ jie-reader-binge / jie-reader-serialized / jie-reader-character-fan × N /
     jie-reader-huang-fan / jie-reader-newcomer，視需要）
        │
        ▼
   使用者／總控依前六階段的發現，決定哪些內容要實際修改
        │
        ▼
第八階段｜regression（只有在真的有修改內容時才需要）
  jie-regression
        │
        ▼
（可選）內容穩定後才做文字定稿
  jie-line-editor
        │
        ▼
第九階段｜最終裁決
  jie-final-editorial-board（彙整全部報告，分 P0/P1/P2）
        │
        ▼
第十階段｜作者意圖守門
  jie-author-intent-guard（防止 P0/P1 建議誤傷作者刻意設計）
        │
        ▼
   使用者最終裁決：哪些一定修、哪些可接受、哪些是刻意設計
```

## 五、通用模板 Agent 怎麼呼叫

`jie-character-life-simulator` 與 `jie-reader-character-fan` 不是「一個角色一個 agent 檔」，而是同一份 agent 定義，靠每次呼叫時的任務描述指定角色。用 `Agent` 工具呼叫時，把角色名稱與範圍寫進 `prompt`，例如：

```
Agent({
  subagent_type: "jie-character-life-simulator",
  description: "模擬封寒人生軌跡（Volume07-09）",
  prompt: "這次請你模擬「封寒」這個角色，範圍限定 Volume07 到 Volume09（帝關與異域返本段落）。
           先讀 docs/characters/CHARACTER_FENG_HAN.md 掌握他的設定，再依 agent 定義的模擬方法逐章檢查。"
})
```

`jie-reader-character-fan` 同理，例如「這次請代入瘋（封寒）粉絲的視角」「這次請代入生（洛生衣）粉絲的視角」。

**每個角色、每個範圍都是獨立的一次 Agent 呼叫**（獨立 context），不要在同一次呼叫裡要求它模擬多位角色——那樣會失去「站在自己立場」的沉浸效果，變回一般化的全局審查（那是 `jie-supporting-cast-agency` 該做的事）。

## 六、實務執行建議：務必分批，不要一次跑全書

全書已經十二卷以上，若對每一位主要角色（`docs/characters/` 下有 26 個檔案）在全書範圍跑一次 `jie-character-life-simulator`，單一次呼叫的上下文會遠超合理範圍，結果也會失焦。建議：

1. **依大篇分批**：以 `docs/MACRO_OUTLINE.md` 的分篇為單位，一次只處理一到三篇的範圍。
2. **只模擬該範圍內真正重要的角色**：不必every次都跑滿 26 人；先看這幾篇誰是核心，誰只是路過。
3. **跨批次累積成一份摘要**：每個角色每跑完一個範圍，把「人生時間軸摘要」保留下來（可存成臨時筆記），下一批次呼叫時作為背景提供給該角色的下一次模擬，避免每次從零開始。
4. **`jie-arc-structure`、`jie-relationship-arc` 同理**：逐篇／逐關係組個別呼叫，不要要求一次涵蓋全書。
5. 只有 `jie-global-structure`、`jie-reader-binge` 這類本質上就是「全書尺度」的 agent，才需要讀完全書——即便如此，也建議先確認 `novel/` 實際章節數量與長度，評估是否需要再拆成上下卷分兩次跑。

## 七、彙整與裁決：怎麼餵資料給最後兩關

`jie-final-editorial-board` 與 `jie-author-intent-guard` 不會自己去跑前面所有審查——它們是**整合者**，需要使用者（或總控）把前面各階段實際收到的審查輸出貼給它們，或至少告訴它們去哪裡找這些輸出。實務上：

1. 每個階段跑完後，把各 agent 的結構化輸出保留下來（貼在對話裡，或存成臨時檔案）。
2. 全部階段跑完後，把這些輸出整理後一次交給 `jie-final-editorial-board`，明確告知「本輪審查來源包含哪些 agent」，讓它能在輸出中誠實標記是否有缺漏。
3. 把 `jie-final-editorial-board` 的 P0/P1/P2 清單交給 `jie-author-intent-guard` 覆核。
4. 最終的 P0/P1 清單與 `jie-author-intent-guard` 的覆核結果一起交給使用者本人裁決——這兩個 agent 都不能代替作者定案，只能整理與提醒。

## 八、什麼情況該停下來問作者，不要自動往下走

比照 `CLAUDE.md` 既有的停止原則，這套 pipeline 也一樣：

- `jie-canon` 或 `jie-author-intent-guard` 判定某項發現「風險高」或「疑似誤傷作者刻意設計」。
- `jie-final-editorial-board` 標記的 P0 項目會牽動已定稿的重大事件、人物生死或身分。
- 多個 reader 層 agent 給出彼此矛盾的觀感（例如 `jie-reader-huang-fan` 認為某段壓低了荒，`jie-reader-character-fan`〔代入陸沉粉絲〕卻認為這段正好平衡）——這是創作取捨，不是總控能代選的。
- `jie-regression` 發現新矛盾，且修正方式會影響到本輪之外、還沒送審的其他章節。

其餘情況（例如挑選要不要加開某個選配 agent、批次怎麼拆）可以由總控依現況自行判斷，不必每一步都問。

## 九、目前狀態

- 25 個新 agent 檔案已建置於 `.claude/agents/`，工具權限均為 `Read, Glob, Grep`（純審查，不會修改任何檔案）。
- 尚未執行過任何一次呼叫，也沒有排入 `CLAUDE.md` 的日常流程——這是刻意的，避免與既有的高頻寫作流程混淆。
- 第一次正式使用前，建議先挑一個範圍最小的既完成篇章（例如已定稿的某一篇）做小規模試跑，確認各 agent 輸出品質與檔案路徑引用是否正確，再逐步擴大範圍。
