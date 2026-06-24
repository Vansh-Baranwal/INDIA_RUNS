python src/offline/feature_engineering.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python src/offline/embeddings.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python src/offline/indexer.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python src/online/rank.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
