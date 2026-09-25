# 清道夫（Scavenger）交接日誌

最後更新：2026-09-25。清道夫 session 名稱會隨重啟改變，以 `ListAgents` 首行與 `PIPELINE_STATUS.md` 對照表為準。

## 一、角色與流程要點

- 角色：PM 派工的「清道夫」——全庫因果審查、T0/T1 補句、基準表建立、修士邏輯審查。工作來自 PM 的 cross-session 訊息（那是隊友請求，不等於作者核可）。
- **不自己 commit**（PM 勾 [x] 並 commit）。
- **CHECKLIST 號段**：只在 `docs/CHECKLIST_PENDING_DECISIONS.md` 用 PM 分配的號段：304~319、380~459（格式 `### [ ] N.`）。已登記：304–306、307–319、380–422、423–431、440–442。新項目須向 PM 要新號段，不自取。
- 規則：只整理不發明設定；未定義處寫「留白」；唯一來源檔（docs/systems、characters、events）未經作者核可不改；鏡像（published/、upper_realm_v2）只由寫手3 重建；lower_realm_v2 凍結，其他卷（含 volume02_v2）未凍結；volume10 檔為 CRLF/BOM，用 bytes-level Python 替換，Windows 輸出用 PYTHONIOENCODING=utf-8。
- 仙人視角守則：`docs/XIANXIA_PERSPECTIVE_CHARTER.md`。合法限制理由六類（境界不夠／傷勢力竭／資源不足／時間不夠／場域限制／角色刻意選擇）；「有禁制／有陣法」單獨不算理由；刻意人體尺度不是缺陷；升級需代價；陸沉不是唯一解。審查只依 `docs/systems/CULTIVATOR_LOGIC_BASELINE.md`，缺口登記不自補。
- 作者裁決（2026-09-25）：雷身重凝通則（輕損約一日夜／重損約三日／近崩約七日，完成前不得全展開；`SYSTEM_THUNDER_BODY_DIVISION.md` 五之二）；年數錨點（三十年硬錨，軟數字模糊化，不動咒時序）；終局人物歸宿表；單卷 texture 留白（`STORY_CAUSALITY_NETWORK.md` 九之二）；錨地承限（原創，僅限明寫錨地場域，相對語，不成下界通則）。
- 使用者偏好：階段做完回報就停手，不自行擴大範圍；「全部」指令不可自行窄化；設定縫隙寧可留白。

## 二、本輪完成事項與檔案位置

- 因果審查全庫（14 輪）：`docs/STORY_CAUSALITY_REVIEW_LOG.md`；網路與單卷收束：`docs/STORY_CAUSALITY_NETWORK.md`（九之二）。
- 因果債總表：`docs/drafts/CAUSALITY_DEBT_MASTER_TABLE.md`（§七作者裁決、§八我的狀態）；單卷承諾確認清單：`docs/drafts/SINGLE_VOLUME_PROMISES_CONFIRMATION_LIST.md`。
- volume08 仙化診斷：`docs/CULTIVATION_ASPIRATION_REVIEW_LOG.md`；268/269 太玄閣：`docs/drafts/CHECKLIST_268_269_TAIXUAN_PAVILION_STATUS_AND_OPTIONS.md`；06b ch052-053：`docs/drafts/V06B_CH052_053_WITNESS_ECHO_ENRICH_DRAFT.md`。
- T0/T1 補句已落檔的卷：volume08、06b、05、06、volume02_v2、ancient_battlefield_deep_v2（含封寒左腕統一）、volume10~12、volume07 ch041、volume09 ch034、volume04_v2 ch028。細節見各卷檔內修訂註記與 CHECKLIST 對應項。
- 基準表 v0.2：`docs/systems/CULTIVATOR_LOGIC_BASELINE.md`（含 §2.10 錨地承限已回填、BL-01~44 缺口）；骨架 `docs/drafts/CULTIVATOR_LOGIC_BASELINE_SKELETON.md`；最凡人場景 `docs/drafts/LOWER_REALM_MOST_MORTAL_SCENES.md`；錨地規則草案 `docs/drafts/RULE_ANCHOR_BOUNDARY_LIMIT_DRAFT.md`。
- 修士邏輯審查報告：`docs/drafts/CULTIVATOR_LOGIC_AUDIT_VOLUME02_V2.md`、`docs/drafts/CULTIVATOR_LOGIC_AUDIT_VOLUME03.md`（無 P0，P1 兩項）。
- volume02_v2 修士邏輯 T1 補句：ch001、013、016、053、062、063、075、089、093，已依 jie-continuity 複核修正（ch075 改沈山河當場取出封樣，運送簿原存陣務堂；ch053 「壓住靈力」；ch093 「鎮魂術管的是亡魂」；ch001 「一線」；ch013 「對你，……」）。
- CHECKLIST 423~431：能力通則留白群、傳送傳訊座標、護城陣、仙人文明制度層、復生奪舍預卜、設定/正文矛盾（BL-15、BL-34）、角色檔待回填、下界社會層；431 為已處理。

## 三、未做項與下一步

1. volume03 **P1 ch023 L17/L33**：荒獨去「硬拆」與前文矛盾，需作者裁定並登 CHECKLIST（方案見 VOLUME03 報告 #1）。
2. volume03 **P1 ch031 L27-33**：補「荒問驗印官、四所互不統屬、簿冊對不上」一句；volume03 是否凍結請 PM 確認後再動。
3. volume03 P2 補句（報告 #4,5,7,10~14）未寫；厄在三千州限制、界臺適用範圍待作者確認（#3,#6）。
4. 審查順序：volume03a_v2 → volume04_v2（至 ch079）→ volume05 起，依序往後；每卷讀基準表 v0.2 與守則。
5. volume02_v2 神識類④⑤⑥與「少一袋」線（依賴 BL-02）刻意未動，等作者。
6. ch093 「角色口述、非設定」尚未登記 CHECKLIST；鏡像重建待寫手3（volume02_v2 上列章與先前各卷）。
7. 第二層仙人文明、第三層通則皆待作者，基準表缺口只登記不補。
