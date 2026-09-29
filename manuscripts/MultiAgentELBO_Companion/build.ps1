# Build the companion against a fresh build of the technical documents.
#
# The companion imports the labels of main.tex and both supplements through
# xr-hyper, so it needs their .aux files. Following the theory folder's SPEC,
# nothing is built inside either folder: sources are copied to a scratch
# directory, the three technical documents are built there first, then the
# companion, and only companion.pdf is copied back.
#
#   .\build.ps1               full build (technical documents, then companion)
#   .\build.ps1 -SkipTheory   reuse the technical .aux files of the last build
param([switch]$SkipTheory)
$ErrorActionPreference = 'Stop'

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$theory  = Join-Path (Split-Path -Parent $here) 'MultiAgentELBO_Theory'
$scratch = Join-Path $env:TEMP 'multiagentelbo-companion-build'
$tbuild  = Join-Path $scratch 'theory'
$cbuild  = Join-Path $scratch 'companion'

function Invoke-Latexmk([string]$dir, [string]$file) {
    Push-Location $dir
    try {
        # latexmk reports progress on stderr, which Windows PowerShell would turn into errors.
        cmd /c "latexmk -pdf -interaction=nonstopmode -halt-on-error $file > $file.build.txt 2>&1"
        if ($LASTEXITCODE -ne 0) { throw "latexmk failed on $file; see $dir\$file.build.txt" }
    } finally { Pop-Location }
}

if (-not $SkipTheory -or -not (Test-Path (Join-Path $tbuild 'main.aux'))) {
    if (Test-Path $tbuild) { Remove-Item -Recurse -Force $tbuild }
    New-Item -ItemType Directory -Force $tbuild | Out-Null
    Copy-Item (Join-Path $theory '*.tex'), (Join-Path $theory '*.bib'), (Join-Path $theory '*.sty') $tbuild
    foreach ($doc in 'main.tex', 'supplement_gaussian.tex', 'supplement_base.tex') { Invoke-Latexmk $tbuild $doc }
}

if (Test-Path $cbuild) { Remove-Item -Recurse -Force $cbuild }
New-Item -ItemType Directory -Force $cbuild | Out-Null
Copy-Item (Join-Path $here '*.tex') $cbuild
Copy-Item (Join-Path $theory 'references.bib'), (Join-Path $theory 'scientific_report.sty') $cbuild
Copy-Item (Join-Path $tbuild 'main.aux'), (Join-Path $tbuild 'supplement_gaussian.aux'), (Join-Path $tbuild 'supplement_base.aux') $cbuild
Invoke-Latexmk $cbuild 'companion.tex'

$log = Get-Content (Join-Path $cbuild 'companion.log') -Raw
$problems = [regex]::Matches($log, "(Reference|Citation) [^\r\n]* undefined|multiply defined") | ForEach-Object { $_.Value } | Sort-Object -Unique
Copy-Item (Join-Path $cbuild 'companion.pdf') $here -Force
if ($problems) {
    Write-Output 'Undefined or duplicate references (a renamed or removed technical label shows up here):'
    $problems | ForEach-Object { Write-Output "  $_" }
    exit 1
}
Write-Output ([regex]::Match($log, 'Output written on [^\r\n]*').Value)
