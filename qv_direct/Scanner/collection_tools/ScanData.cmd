if '%~1'=='' (
    python ScanData.py --all
) ELSE (
    python ScanData.py --project=%1
)
