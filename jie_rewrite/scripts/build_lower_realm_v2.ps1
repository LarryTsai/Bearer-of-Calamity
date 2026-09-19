param()

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $projectRoot 'novel/lower_realm_v2'
$outputRoot = Join-Path $projectRoot 'novel/published/lower_realm_v2'
$utf8 = [System.Text.UTF8Encoding]::new($false)
$digits = @('零', '一', '二', '三', '四', '五', '六', '七', '八', '九')

function Convert-ChapterNumber([int]$number) {
    if ($number -lt 10) { return $digits[$number] }
    if ($number -eq 10) { return '十' }
    if ($number -lt 20) { return '十' + $digits[$number - 10] }
    if ($number -eq 20) { return '二十' }
    return '二十' + $digits[$number - 20]
}

$volumes = @(
    @{ Name = 'volume01'; Groups = @('prologue', 'arc01_body_foundation', 'arc02_enter_mountain'); Expected = 18 },
    @{ Name = 'volume02'; Groups = @('arc03_void_spirit_realm', 'arc04_taixuan_forging', 'arc05_hundred_broken_mountain'); Expected = 26 },
    @{ Name = 'volume03'; Groups = @('arc06_false_commission', 'bridge_north_sea', 'arc07_lower_realm_storm'); Expected = 21 }
)

$plan = [System.Collections.Generic.List[object]]::new()
foreach ($volume in $volumes) {
    $number = 0
    foreach ($group in $volume.Groups) {
        $groupPath = Join-Path $sourceRoot $group
        $files = @(Get-ChildItem -LiteralPath $groupPath -Filter 'chapter*.md' -File | Sort-Object Name)
        foreach ($file in $files) {
            $number++
            $raw = [System.IO.File]::ReadAllText($file.FullName)
            $raw = $raw.Replace("`r`r`n", "`n").Replace("`r`n", "`n")
            $firstBreak = $raw.IndexOf("`n")
            if ($firstBreak -lt 0) { throw "Missing chapter body: $($file.FullName)" }
            $heading = $raw.Substring(0, $firstBreak)
            if ($heading -notmatch '^# 第[一二三四五六七八九十]+章\s+(.+)$') {
                throw "Unexpected chapter heading: $($file.FullName): $heading"
            }
            $title = $Matches[1]
            $newHeading = '# 第' + (Convert-ChapterNumber $number) + '章 ' + $title
            $content = $newHeading + $raw.Substring($firstBreak)
            $destinationName = 'chapter{0:D3}.md' -f $number
            $plan.Add([pscustomobject]@{
                Volume = $volume.Name
                Number = $number
                Title = $title
                Source = $file.FullName
                Destination = Join-Path (Join-Path $outputRoot $volume.Name) $destinationName
                Content = $content
                Group = $group
            })
        }
    }
    if ($number -ne $volume.Expected) {
        throw "$($volume.Name) contains $number chapters; expected $($volume.Expected)."
    }
}

if ($plan.Count -ne 65) { throw "Expected 65 chapters, got $($plan.Count)." }

foreach ($entry in $plan) {
    $directory = Split-Path -Parent $entry.Destination
    [System.IO.Directory]::CreateDirectory($directory) | Out-Null
    [System.IO.File]::WriteAllText($entry.Destination, $entry.Content, $utf8)
}

$manifest = [System.Collections.Generic.List[string]]::new()
$manifest.Add('# 下界新版閱讀版逐章來源表')
$manifest.Add('')
$manifest.Add('此表由 `scripts/build_lower_realm_v2.ps1` 依已審開發稿產生。新版三卷與舊 `published/volume01` 並存；此處的來源是新版開發稿，不表示與舊版章號一對一。')
$manifest.Add('')
$manifest.Add('| 新版卷章 | 標題 | 開發稿來源 |')
$manifest.Add('| --- | --- | --- |')
foreach ($entry in $plan) {
    $sourceRelative = 'novel/lower_realm_v2/' + $entry.Group + '/' + (Split-Path -Leaf $entry.Source)
    $publishedRelative = $entry.Volume + '/' + (Split-Path -Leaf $entry.Destination)
    $manifest.Add('| [' + $entry.Volume + ' 第' + $entry.Number + '章](' + $publishedRelative + ') | ' + $entry.Title + ' | `' + $sourceRelative + '` |')
}
[System.IO.Directory]::CreateDirectory($outputRoot) | Out-Null
[System.IO.File]::WriteAllText((Join-Path $outputRoot 'SOURCE_MANIFEST.md'), ($manifest -join "`n") + "`n", $utf8)
Write-Output "Built $($plan.Count) chapters across $($volumes.Count) volumes."
