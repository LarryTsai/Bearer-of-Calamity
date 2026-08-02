# 《劫》重新撰寫工作區

本目錄是《劫》的全新寫作工作區。

## 當前狀態

- 正文已開發至 Volume12；development 與 `novel/published/` 並行維護，實際卷章狀態見 `novel/README.md`。
- 開局時間錨點：《完美世界》中小荒一歲。
- 主角：劫。
- 舊設定、原始對談與歷史 checklist 僅供追溯；現行作者裁示以 `docs/AUTHOR_CORE_REQUIREMENTS.md` 為最高入口。
- 所有新增設定應同步整理至 `docs/`，正文放入 `novel/`，發布版放入 `novel/published/`。

## 目錄

- `docs/`：重新確認後的世界觀、人物、能力與時間線。
- `novel/`：正式正文與卷章內容。
- `docs/AUTHOR_CORE_REQUIREMENTS.md`：作者不可被舊設定否決的核心硬需求；開發與 review 前必讀。
- `docs/MACRO_OUTLINE.md`：現行不綁章數的大篇章骨架與時間線卡點。

## 下一步

1. 依 `docs/CHECKLIST_NOVEL_REVIEW_FIXES.md` 的 active 區完成尚未閉環的卷章回歸。
2. 依 `docs/AUTHOR_REQUIREMENTS_AUDIT_MATRIX.md` 維持作者裁示、唯一來源與正文落點一致。
3. 每次正文修訂同步 development／published，新增設定同步回填 `docs/`。

## Agent 自動化工作流

本專案已在 `.claude/agents/`（repo 根目錄）建立七個 Claude Code 專家 agent：`jie-creative`、`jie-canon`、`jie-continuity`、`jie-character`、`jie-power-system`、`jie-chapter-editor`、`jie-writer`。完整呼叫順序與總控原則見 `CLAUDE.md`。
