# 《劫》正文改寫產線狀態板（2026-09-25 重整）

狀態：PM維護。舊版（369行歷史敘事）已歸檔於 `docs/archive/PIPELINE_STATUS_until_20260925.md`。**目前：作者指示「全面暫停」（2026-09-25），各人停在階段完成點，無人在跑。**

## 一、現況摘要
- 主線故事已寫完（序篇～第十九篇＋戰後沉封域）。**唯一完稿缺口＝古界N-2**（`novel/volume04_v2/` ch080~086已寫，N2-7〈窗〉、N2-8未落筆）。
- N-2依據：作者2026-09-24/25裁決方案6（出口早就存在、難處在誰願意用它）；章綱`docs/outlines/ANCIENT_REALM_N2_CHAPTER_OUTLINE_DRAFT.md`、骨架`ANCIENT_REALM_N2_PLAN6_SKELETON.md`、CHECKLIST 231/320。ch080~084已審修（083/084為標竿）；ch085〈沒有門〉、ch086〈告別〉初稿，五審已跑未修（`docs/drafts/N2_CH085_086_REVIEW_SUMMARY.md`）。
- 已完成：volume02_v2/03/03a_v2/05/06/06b/07/08/09仙俠質感；causality全庫審查（`docs/drafts/CAUSALITY_DEBT_MASTER_TABLE.md`）與T0/T1補句；蒼梧代詞「牠→他」全書；終局人物歸宿表（`docs/outlines/OUTLINE_FINALE_CHARACTER_DESTINATIONS.md`）；洛生衣觀生錨點；published/upper_realm_v2鏡像全庫一致（稽核腳本）。
- 進行中被暫停：修士邏輯審查（基準表`docs/systems/CULTIVATOR_LOGIC_BASELINE.md` v0.2；agent `.claude/agents/jie-cultivator-logic.md`）已審 下界arc01~04、volume02_v2、volume03；共同守則`docs/XIANXIA_PERSPECTIVE_CHARTER.md`。volume10~12質感改寫未開始（volume10審查報告已產出）。

## 二、待作者裁定（依重要度）
1. 空中救殿/救宗大型場面六題：`docs/drafts/BIG_SCENE_AIR_RESCUE_FLOWC_ROUND1.md`（位置已定後續卷/番外）。
2. volume03 P1：ch023荒獨去硬拆矛盾（三方向見`CULTIVATOR_LOGIC_AUDIT_VOLUME03.md`#1）；ch031補「四所互不統屬」一句；劫厄在三千州行蹤。
3. 465天譴射程、467黑旗來源、468周回女兒走位、370（203題對話）、345（已定「蒼梧」）、347鑑月/分身「牠」、閣老傷在胸口回填角色檔、442黑水城撞名、440人名撞字、CHARACTER_LU_CHEN L128慢半拍。
4. 下界arc03~04 B/D類一句補丁（已授權有限解凍：僅補一句專屬理由＋機械修正）；P1：arc04 ch009、arc03 ch007 L79。
5. 340 volume05前提：已採方案A止血；B/C待N-2完稿後裁。
6. 單卷承諾確認清單：`docs/drafts/SINGLE_VOLUME_PROMISES_CONFIRMATION_LIST.md`；原作待核項（御空/儲物/傳訊、461/462暫定口徑）等作者讀原作。

## 三、恢復時的建議順序
1. 寫手1：修ch085~086（依彙整檔）→N2-7〈窗〉（高潮：蒼梧自己決定不把窗口做更穩更久）→N2-8；再登記待登記項、補README。
2. 寫手3：重建N-2鏡像（volume04_v2無鏡像則免）；volume10~12質感。
3. 寫手2/清道夫：修士邏輯審查往後（arc05起、03a_v2、04_v2至ch079、05起）＋已核可補句。
4. 全書完成後：`docs/FINAL_REVIEW_PIPELINE_MANUAL.md` 的最終審查pipeline。

## 四、協作規則（持續有效）
- 每次對話開始先ListAgents確認身分，讀本檔＋自己的`PIPELINE_WRITERn_LOG.md`。
- **git commit/push只由PM統一做**；寫手回報附「檔案清單＋一行摘要」。
- CHECKLIST號段：清道夫304~319/380~459、寫手1 320~339、寫手2 340~359、寫手3 360~379/460~479。
- published/與upper_realm_v2鏡像只由寫手3重建（用`scripts/build_upper_realm_reading_v2.py`＋稽核腳本）。
- 作者指示原則：「階段完成就停手」；創作/設定重大決定（角色道、悲劇本質、新能力）交作者，連續性/對表由PM裁決。

## 五、角色↔session
ListAgents查當下事實，不記名字。角色：PM、寫手1、寫手2、寫手3、清道夫、顧問（創作面諮詢、與作者多輪討論）。
