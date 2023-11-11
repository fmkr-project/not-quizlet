function CustomTree {
    param (
        [string]$basePath,
        [int]$depth = 0,
        [bool]$isRoot = $true
    )
    $items = Get-ChildItem -Path $basePath -Directory
    foreach ($item in $items) {
        $indent = '    ' * $depth  # Adjust indentation as needed
        $prefix = if ($isRoot) { "" } else { "|-- " }

        "$indent$prefix$($item.Name)"

        if ($item.Name -ne "node_modules" -and $item.Name -notmatch "__pycache__") {
            CustomTree -basePath $item.FullName -depth ($depth + 1) -isRoot $false
        } elseif ($item.Name -eq "node_modules") {
            "$indent|   `--> ..."
        }
    }

    if (-not $isRoot) {
        $files = Get-ChildItem -Path $basePath -File | Where-Object { $_.Name -notmatch "\.txt$|\.md$|LICENSE" }
        foreach ($file in $files) {
            $indent = '    ' * $depth
            "$indent|-- $($file.Name)"
        }
    }
}

$rootPath = Resolve-Path "..\.."
CustomTree -basePath $rootPath | Out-File -FilePath "..\documentation\project_structure.txt" -Encoding UTF8