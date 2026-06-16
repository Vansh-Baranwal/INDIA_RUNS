$ErrorActionPreference = "Stop"

Write-Host "--- Running parse_candidates.py ---"
python offline/parse_candidates.py
if ($LASTEXITCODE -ne 0) { throw "parse_candidates failed" }

Write-Host "--- Running feature_engineering.py ---"
python offline/feature_engineering.py
if ($LASTEXITCODE -ne 0) { throw "feature_engineering failed" }

Write-Host "--- Running embeddings.py ---"
python offline/embeddings.py
if ($LASTEXITCODE -ne 0) { throw "embeddings failed" }

Write-Host "--- Running build_faiss.py ---"
python offline/build_faiss.py
if ($LASTEXITCODE -ne 0) { throw "build_faiss failed" }

Write-Host "--- Running rank.py ---"
Set-Location -LiteralPath "online"
python rank.py
if ($LASTEXITCODE -ne 0) { throw "rank failed" }

Write-Host "Pipeline execution complete!"
