# 《劫》

[開始閱讀](novel/published/README.md) · [正文工作區](novel/README.md) · [故事大綱](docs/MACRO_OUTLINE.md) · [逐章對照](docs/STORY_STRUCTURE.md)

正文依「時期 → 篇章／插段 → 章節」排列。每層資料夾使用三位數順序前綴，例如 `001_下界成根/000_命落大荒/001_雷比雨先到.md`；各層獨立從001編號，序篇用000。每篇章號亦從001起算；戰後收束在大劫決裂子目錄另從001起算。資料夾前綴是現行排序號，舊中文篇號僅供歷史對照。

現有新版867章。古界尚未完成N-2末段與N-3；第二十篇〈萬古獨行〉是可選容器，目前沒有正文。目錄與章數不代表故事已全部定稿。

`novel/` 是帶開發註記的唯一正文來源；`novel/published/` 是同一新版的乾淨閱讀鏡像。修改來源後執行：

```powershell
python scripts/build_story.py
python scripts/build_story.py --check
```

`docs/STORY_STRUCTURE.json` 管理時期、篇名、順序與章目錄；`docs/MACRO_OUTLINE.md` 管理故事內容與篇界，兩者須一起更新。新章先登記manifest，再生成目錄和閱讀版。舊施工章號對照保留在manifest與逐章表，不再用舊volume編號判斷閱讀順序。

開發共同前提：[作者硬需求](docs/AUTHOR_CORE_REQUIREMENTS.md)、[仙人視角與境界差異](docs/XIANXIA_PERSPECTIVE_CHARTER.md)。每階段完成、驗證後由PM commit並push。產線進度見[狀態板](docs/PIPELINE_STATUS.md)。
