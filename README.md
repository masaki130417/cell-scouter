# CellScouter (セルスカウター)

現在地や指定した場所から近い基地局をリストアップするWebアプリ。

## 開発運用ルール

### 1. ブランチ作成ルール
新しい機能開発や修正を行う際は、必ず `main` からブランチを切り、以下の命名規則に従います。

**命名規則:** `feature/機能名-YYYYMMDD`
- 例：現在地取得機能（2026年3月15日着手）の場合
  `feature/get-location-20260315`

### 2. 開発フロー
1. ブランチ作成: `git checkout -b feature/機能名-YYYYMMDD`
2. 開発・コミット: `git add .` -> `git commit -m "メッセージ"`
3. GitHubへ送信: `git push origin feature/機能名-YYYYMMDD`
4. マージ: GitHub上でのPull Request、またはローカルでの `git merge`