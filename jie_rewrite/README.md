# 《劫》重新撰寫工作區

本目錄是《劫》的全新寫作工作區。

## 當前狀態

- 正文尚未開始。
- 開局時間錨點：《完美世界》中小荒一歲。
- 主角：劫。
- 舊設定僅作參考，未重新確認前不自動視為正式設定。
- 所有新增設定應先整理至 `docs/`，正文放入 `novel/`。

## 目錄

- `docs/`：重新確認後的世界觀、人物、能力與時間線。
- `novel/`：正式正文與卷章內容。
- `docs/MACRO_OUTLINE.md`：現行不綁章數的大篇章骨架與時間線卡點。

## 下一步

1. 依 `docs/MACRO_OUTLINE.md` 鎖定第一篇的事件拆分與章節節奏。
2. 將第一篇所需人物、勢力、功法與事件設定整理成正文可直接引用的場景卡。
3. 確認第一章視角、開場畫面與第一個懸念。
4. 開始撰寫正文，新增設定同步回填 `docs/`，避免正文與設定檔分岔。

## Agent 自動化工作流

本專案已在 `.claude/agents/`（repo 根目錄）建立七個 Claude Code 專家 agent：`jie-creative`、`jie-canon`、`jie-continuity`、`jie-character`、`jie-power-system`、`jie-chapter-editor`、`jie-writer`。完整呼叫順序與總控原則見 `CLAUDE.md`。
