# FMCG Retail Analytics Pipeline

Dự án phân tích dữ liệu bán lẻ FMCG end-to-end: từ raw CSV các phòng ban → cleaning → Star Schema → SQL analysis → Dashboard.

## Bài toán kinh doanh
Chuỗi bán lẻ FMCG với 28 cửa hàng, 5 năm dữ liệu (2020–2024), ~500K giao dịch.  
Ba bài toán chính cần giải quyết:
1. **Doanh thu & hiệu quả kinh doanh** — kênh nào tốt, sản phẩm nào sinh lời, KM có hiệu quả không?
2. **Hành vi khách hàng** — RFM segmentation, churn risk, cohort retention
3. **Tồn kho & dự báo** — stockout ở đâu, turnover ratio, dự báo nhu cầu tháng tới

## Nguồn dữ liệu (raw)
| File | Phòng ban | Mô tả |
|---|---|---|
| `don_hang_2020_2024.csv` | Kinh doanh | Đơn hàng header |
| `chi_tiet_don_hang.csv` | Kinh doanh | Line items |
| `danh_muc_san_pham.csv` | MIS | Master sản phẩm |
| `khach_hang_2020_2022.csv` | Marketing | KH nửa đầu |
| `khach_hang_2023_2024.csv` | Marketing | KH nửa sau |
| `phieu_nhap_kho.csv` | Kế toán | Nhập kho |
| `danh_sach_cua_hang.csv` | Nhân sự | Master cửa hàng |
| `ton_kho_hang_thang.csv` | Kho | Snapshot tồn kho |
| `chuong_trinh_khuyen_mai.csv` | Kinh doanh | Chương trình KM |
| `danh_sach_nha_cung_cap.csv` | Mua hàng | Master NCC |

## Cấu trúc project
```
fmcg_project/
├── data/
│   ├── raw/          ← CSV gốc từ các phòng ban (không sửa)
│   ├── cleaned/      ← Sau khi clean & transform
│   └── output/       ← Kết quả analysis (RFM, monthly_revenue...)
├── notebooks/        ← Jupyter notebook khám phá & EDA
├── src/              ← Python scripts (pipeline chính)
│   ├── day1_explore.py
│   ├── day2_clean_orders.py
│   ├── day3_clean_master.py
│   ├── day4_clean_inventory.py
│   ├── day5_build_schema.py
│   ├── day7_rfm_churn.py
│   └── day8_inventory_analysis.py
├── sql/              ← SQL queries phân tích
│   └── analysis_queries.sql
├── dashboard/        ← Link & screenshot Looker Studio
└── tests/            ← Test scripts kiểm tra data quality
```

## Lộ trình thực hiện
| Ngày | Việc làm |
|---|---|
| 1 | Explore & profile toàn bộ 10 file raw |
| 2 | Clean đơn hàng + chi tiết |
| 3 | Clean master data (SP, KH, cửa hàng) |
| 4 | Clean tồn kho + nhập kho + NCC |
| 5 | Thiết kế Star Schema, build dim/fact |
| 6 | SQL: Doanh thu & hiệu quả |
| 7 | Python: RFM + Churn |
| 8 | SQL+Python: Tồn kho & dự báo |
| 9 | Dashboard Looker Studio |
| 10 | GitHub README + luyện phỏng vấn |

## Tech stack
- **Python**: pandas, numpy (cleaning & feature engineering)
- **SQL**: SQLite local → Google BigQuery
- **Visualization**: Google Looker Studio
- **Version control**: Git / GitHub

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/fmcg-retail-analytics.git
cd fmcg-retail-analytics
pip install -r requirements.txt
python src/day1_explore.py
```
