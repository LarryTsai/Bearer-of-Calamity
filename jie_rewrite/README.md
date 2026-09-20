# 《劫》重新撰寫工作區

本目錄是《劫》的全新寫作工作區。

**直接讀故事：**[v2 正文閱讀總目錄（卷一至九，逐章連結）](novel/published/README.md)。依序閱讀；卷內章號每卷重新起算。

## 當前狀態

- v2 正式閱讀線目前至卷九，共 251 章；古界 Act1–4 另在 `novel/volume04_v2/` 開發中，尚未編入閱讀卷。舊版延伸至 Volume12，不能與 v2 連讀。
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

## Codex 小說工作指令

以下指令可直接貼到 Codex 使用。路徑為本機個人 skill 路徑；若搬到其他電腦，需改成該電腦的 Codex skills 目錄。

### 只審查，不修改正文

```text
[$review-serialized-novel](C:\Users\larry_tsai\.codex\skills\review-serialized-novel\SKILL.md) Volume03，只列出需要合併、擴寫、重建或刻意保留的章節，暫時不要修改
```

此流程會檢查章長分布、中位數、連續短章、場景完整性、情節因果、人物、視角、對話、戰鬥、設定與 development／published 同步狀態。字數只作警示，不會因低於固定數字便直接判定不合格。

### 擴寫過短章節並 closed loop

```text
[$develop-and-expand-novel-chapters](C:\Users\larry_tsai\.codex\skills\develop-and-expand-novel-chapters\SKILL.md) closed loop 重新開發 Volume03，讓每個重要事件成為完整故事，不以湊字數為目標
```

此流程會先閱讀整個目標故事段及相鄰章節，再把問題章分類為：

- 合併：章節只是把同一場戲機械切開。
- 擴寫：原有因果成立，但缺少阻力、選擇、戰術、情緒或餘波。
- 重建：內容只是大綱、戰報或設定說明，尚未成為小說場景。
- 保留短章：短小本身能形成衝擊、轉折或節奏效果。

完成後會再執行 review，檢查前後章承接、後續影響、設定回填及 development／published 一致性；未通過便繼續修正。

### 指定卷章與故事重點

```text
[$develop-and-expand-novel-chapters](C:\Users\larry_tsai\.codex\skills\develop-and-expand-novel-chapters\SKILL.md) 擴寫 Volume03 ch015～ch024，重點補足魔女、劫與生的事件、選擇和關係累積，完成 published 同步與 closed-loop review
```

可以在指令中指定：

- 卷別或章節範圍；
- 主要人物；
- 戰鬥、機緣、禁制、異雷或感情線；
- 是否允許合章、改章名或新增章節；
- 只提出方案，或直接修改到 closed loop 完成。

### 修改章節名稱

```text
[$revise-novel-chapter-titles](C:\Users\larry_tsai\.codex\skills\revise-novel-chapter-titles\SKILL.md) Volume03，依完整故事內容 review 並修改章名，同步 development、published 與索引
```

### 完成後 commit and push

```text
[$commit-and-push-story](C:\Users\larry_tsai\.codex\skills\commit-and-push-story\SKILL.md)
```

此指令應在正文、published、設定、索引及 closed-loop review 全部完成後另外執行。審查或擴寫 skill 不會自行 commit 或 push。

### 建議的完整順序

```text
1. review-serialized-novel：找出真正問題
2. develop-and-expand-novel-chapters：合併、擴寫或重建
3. review-serialized-novel：重新閱讀並關閉問題
4. revise-novel-chapter-titles：需要時統一章名
5. commit-and-push-story：確認完成後提交與推送
```
