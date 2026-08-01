[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$previousTexInputs = $env:TEXINPUTS

Push-Location -LiteralPath $PSScriptRoot
try {
    $env:TEXINPUTS = ".;..;$previousTexInputs"

    & pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
    if ($LASTEXITCODE -ne 0) {
        throw "First pdflatex pass failed with exit code $LASTEXITCODE."
    }

    & bibtex main
    if ($LASTEXITCODE -ne 0) {
        throw "BibTeX failed with exit code $LASTEXITCODE."
    }

    & pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
    if ($LASTEXITCODE -ne 0) {
        throw "Second pdflatex pass failed with exit code $LASTEXITCODE."
    }

    & pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
    if ($LASTEXITCODE -ne 0) {
        throw "Final pdflatex pass failed with exit code $LASTEXITCODE."
    }
}
finally {
    $env:TEXINPUTS = $previousTexInputs
    Pop-Location
}
