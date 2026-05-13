# Automated Sales Agent - System Design Document

## Project Overview
Hệ thống có nhiệm vụ thu thập dữ liệu sản phẩm từ website đối thủ, phân tích so sánh giá, và tự động sinh ra bài PR cho sản phẩm của bên mình dựa trên dữ liệu so sánh đó. Mục tiêu kinh doanh là tự động hóa quy trình phân tích đối thủ và marketing sản phẩm, với một hệ thống có tính mở rộng cao và tự động hóa hoàn toàn bằng Python.

## Tech Stack Cốt Lõi
- **Web Scraping:** Playwright (để render được JavaScript) hoặc Crawl4AI (chuyên dùng cho LLM).
- **Database:** SQLite (hoặc PostgreSQL) và SQLAlchemy (ORM).
- **AI/LLM:** OpenAI API hoặc Gemini API (sử dụng Structured Outputs để bóc tách thông tin và Prompt Chaining để viết content).

## Architecture Diagram
```text
Target URL 
   │
   ▼
Scraper 
   │
   ▼
LLM Extractor (lấy tên, giá, tính năng) 
   │
   ▼
Database 
   │
   ▼
Comparison Engine 
   │
   ▼
LLM Content Generator
```

## Phases of Development

### Phase 1: Web Crawling & DOM Parsing
- Mục tiêu: Vượt qua anti-bot và lấy HTML/Markdown.

### Phase 2: Data Extraction & Structuring
- Mục tiêu: Dùng LLM để biến text thô thành JSON chứa Giá, Thông số.

### Phase 3: Analytics & Content Generation
- Mục tiêu: So sánh giá và tạo bài PR tự động.

### Phase 4: Orchestration & Automation
- Mục tiêu: Lên lịch chạy định kỳ và báo cáo.

## Current Status
Đang ở Phase 1.
