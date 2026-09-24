# 寫手3 工作日誌

## 角色
- 從 PM 接工作，手上沒事就主動找 PM 要。也支援寫手1、寫手2，分工先協調好，不碰對方的檔案。
- 只存檔，不 git add/commit/push（一律由 PM 做）。新設定走 `docs/CHECKLIST_PENDING_DECISIONS.md` 提案；範圍外的 bug 另報 PM，不混進當下的工程。
- 正文每次修改都要同步所有鏡像：`novel/published/<卷>/`，以及 **`novel/published/upper_realm_v2/`**（閱讀版，分卷編號不同，部分段落是舊版）。保留 BOM 與換行；不跑 make_clean_copy.pl（它會把 CRLF 疊成 \r\r\n），改用同段精確替換，最後檢查每檔增刪行數相等。

## 鏡像對照（已查證）
- ancient_battlefield_deep_v2：ch001～018 → upper volume06/ch019～036；ch020～040 → upper volume07/ch001～021；ch019 無鏡像。
- volume02_v2：ch011～022 → upper volume04 同號；ch042～068 → upper volume05/ch(N−38)；ch069～081 → upper volume06/ch(N−68)；ch086/089 upper 為舊版（改句不存在）；ch094～099 upper 未收錄。

## 已完成（2026-09-24，皆已 commit）
- 仙俠質感：volume05、volume06、volume06b（含215題落地）、ancient_battlefield_deep_v2（14例＋約90處機械替換＋14個bug）。產出在 `docs/drafts/XIANXIA_TEXTURE_*`、`novel/drafts/xianxia_texture_*`。
- 維護 `docs/drafts/XIANXIA_TEXTURE_ROLLOUT_SPEC.md`（方案c、角色錨點表、五之一十條教訓）。
- volume06b 補做：制度骨架補掃（歸寧司措辭、恤例）與卷尾 ENRICH（ch053 L21）。歸寧司兩個新機制提案登記為 CHECKLIST 294（留白）。
- volume02_v2（與寫手2分工）：制度骨架三例 ch064/065/075/076＋連動 ch069/076/077/081；新機制9條為 CHECKLIST 295「已落筆待核可」，退回時連動句要一起退。Phase 2 機械掃除 ch050/051/056/057/068/073/080。

## 待辦／提醒
- ROLLOUT_SPEC 教訓彙整：PM 指示等更多卷跑完再做。候選教訓：「X順着Y傳回手上」句型全卷限量；制度／程序骨架也要過核心測試；觀生只看生念、只限視線內與近處，不讀元素（那是青璃的領域）；封寒古界前是劍修「勢」，但 FH-03 已核准「敲地比較回震／辨重量影」，不可誤判為越界；不同卷有不同的時序錨點（292題只管古界後的 volume06）。
- volume02_v2 → upper_realm_v2 全卷比對同步：PM 已排在這輪落地之後。
- CHECKLIST 294、295 等使用者裁定。
