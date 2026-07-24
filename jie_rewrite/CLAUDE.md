# 《劫》Claude Code 多 Agent 工作流

本檔案給在 `story/jie_rewrite` 目錄下工作的 Claude Code 主對話（總控）用，說明如何呼叫 `.claude/agents/` 下的七個專家 subagent 來自動化後續故事產出。所有 agent 只用 Read/Grep/Glob 讀取設定並輸出審查結果或方案；只有 `jie-writer` 能寫檔（限 `novel/` 目錄），且只有使用者明確要求存檔時才寫入。

## 可用 Agent

| Agent | 職責 | 輸出 |
| --- | --- | --- |
| `jie-creative` | 提出劇情方案（3~5 種） | 方案清單 + 風險提示 |
| `jie-canon` | 《完美世界》原作相容性審查 | pass/warning/reject + 銜接分類 + 侵入程度 |
| `jie-continuity` | 設定一致性審查（時間線/境界/稱呼/物品等） | 明確衝突/潛在衝突/建議修正 |
| `jie-character` | 人物行為與關係審查 | 逐角色問題點 |
| `jie-power-system` | 境界、十雷、命圖、伴星狀態審查 | 目前狀態表 + 是否提前使用能力 |
| `jie-chapter-editor` | 大綱拆解（目標/阻力/轉折/結果/鉤子）或節奏審查 | 章節大綱 或 節奏問題清單 |
| `jie-writer` | 依核准大綱寫正文 | 正文 + 自檢 + 待確認提案 |

## 標準流程

```
使用者提出劇情需求
        │
        ▼
  jie-creative（提出方案）
        │
        ▼
  並行審查：jie-canon / jie-power-system / jie-character / jie-continuity
        │
        ▼
   使用者選定方案（總控不可代替使用者定案）
        │
        ▼
  jie-chapter-editor（拆解為章節大綱）
        │
        ▼
     jie-writer（寫正文，僅在使用者要求時存檔）
        │
        ▼
  最終審查：jie-continuity / jie-canon / jie-character
        │
        ▼
   使用者確認 → 若有新設定提案，由使用者決定是否回填
   docs/CHECKLIST_PENDING_DECISIONS.md（唯一來源檔不可由 agent 自行定稿）
```

## 總控（主對話）原則

- 總控負責決定流程順序與呼叫哪些 agent，不負責創作或審查本身。
- 不要讓 agent 之間無限來回辯論；每個審查 agent 只回報一次結構化結果，衝突由總控整理後交給使用者判斷。
- 審查類 agent（canon/continuity/character/power-system）可以平行呼叫，因為彼此不依賴對方輸出。
- `jie-chapter-editor` 依賴已核准的方案；`jie-writer` 依賴已核准的章節大綱——這兩步是序列的，不能跳過使用者確認直接往下走。
- 新設定一律先進 `docs/CHECKLIST_PENDING_DECISIONS.md` 當「提案」，經使用者核可後才回填對應的唯一來源檔（`characters/`、`systems/`、`factions/`、`events/`）。任何 agent 都不應直接改寫唯一來源檔。
- 涉及 `AUTHOR_SECRETS.md` 的秘密揭露節奏，一律依 `docs/REVEAL_TIMELINE.md` 的分級控制，不因單一章節需要而提前公開。

## 單輪全自動模式（預設觸發方式）

使用者只要在一則訊息中提出劇情需求（不必逐步下指令、不必自己點名要呼叫哪個 agent），總控就應該在**同一輪**內依「標準流程」把 `jie-creative` → 平行審查 → `jie-chapter-editor` → `jie-writer` → 最終審查全部跑完，中途不主動暫停等待使用者按讚。

只有以下情況才可以中途停下來問使用者，其餘一律由總控自行拍板並在最終回覆中簡述理由：

1. `jie-canon` 回報 `status: reject`，或銜接分類判定為需要新開安全閥卻尚未存在的原作事件衝突。
2. `jie-continuity` 回報「明確衝突」且沒有不影響設定的修正方式。
3. 流程中出現會實際變動唯一來源檔（`characters/`、`systems/`、`factions/`、`events/`、`AUTHOR_SECRETS.md`）的新設定，且該設定重要到會影響後續多篇章（例如新增能力、改變已定稿的死活/勝負/身分）——這類提案一律先停在 `CHECKLIST_PENDING_DECISIONS.md` 等使用者核可，不自動回填。
4. `jie-creative` 給出的多個方案彼此差異巨大，且審查結果都是 pass／沒有明顯優劣——這種「創作方向」的選擇權在使用者，不由總控代選。

其餘決策（例如挑選其中一個方案、章節怎麼拆、用字風格微調）由總控依審查 agent 的回饋自行選最合規的一個往下走，不需要每一步都問。

執行完後，總控應該在同一則回覆總結：選了哪個方案、為什麼、審查結果摘要、是否有留待確認的提案、正文是否已存檔。

## 何時可以跳過流程

- 單純查詢設定內容、不產出新劇情或正文：直接讀 `docs/` 對應檔案即可，不需要呼叫任何 agent。
- 只是想要腦力激盪、還沒打算定案：只呼叫 `jie-creative` 即可，不必自動觸發後續審查。
- 使用者已經給了完整、明確核准的大綱，且只是要落筆：可以跳過 `jie-creative` 與 `jie-chapter-editor`，直接呼叫 `jie-writer`，但寫完後仍建議跑最終審查三件套。
