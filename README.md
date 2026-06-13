# 学習記録アプリ

## 概要

学習内容と時間を記録し、可視化するためのアプリケーションです

## 機能

- 学習内容、学習時間を記録することができる
- 記録した学習内容、学習時間を一覧表示できる

## 使用技術

- React（TypeScript）
- FastAPI（Python）
- PostgreSQL（Database）
- Vite

## セットアップ

### 1. リポジトリをクローン

```bash
git clone https://github.com/Seripro/study-record-app4.git
cd study-record-app4
```

### 2. 依存関係のインストール

```bash
cd frontend
npm install
```

### 3. テーブル設計

このアプリでは `study-record` テーブルを使用します

| カラム名 | 説明     |
| -------- | -------- |
| id       | 主キー   |
| title    | 学習内容 |
| time     | 学習時間 |

## 起動方法

```bash
cd frontend
npm run dev
```

```bash
cd backend
uvicorn main:app --reload
```
