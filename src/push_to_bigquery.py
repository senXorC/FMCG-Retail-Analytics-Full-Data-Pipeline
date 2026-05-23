"""
push_to_bigquery.py
====================
Upload cleaned data lên Google BigQuery.

Setup một lần:
    pip install google-cloud-bigquery pandas-gbq pyarrow

Authentication:
    1. Vào GCP Console → IAM → Service Accounts
    2. Tạo service account, gán role "BigQuery Data Editor"
    3. Download JSON key → lưu vào credentials/gcp_key.json
    4. Đừng bao giờ commit file này lên GitHub (.gitignore đã chặn)

Chạy:
    python push_to_bigquery.py
"""

import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# ── CẤU HÌNH — bạn điền vào ───────────────────────────────────────────────────
GCP_PROJECT    = "YOUR_PROJECT_ID"       # VD: "fmcg-analytics-2024"
BQ_DATASET     = "fmcg_retail"           # Tên dataset trên BigQuery
CREDENTIALS    = "credentials/gcp_key.json"

CLEANED_DIR    = "data/cleaned"
OUTPUT_DIR     = "data/output"

# ── Schema mapping: file → tên bảng trên BQ ───────────────────────────────────
# Dim tables: load FULL mỗi lần (nhỏ, ít thay đổi)
DIM_TABLES = {
    "dim_products.csv":   "dim_products",
    "dim_customers.csv":  "dim_customers",
    "dim_stores.csv":     "dim_stores",
    "dim_suppliers.csv":  "dim_suppliers",
    "dim_promotions.csv": "dim_promotions",
}

# Fact tables: APPEND — chỉ thêm mới, không ghi đè
FACT_TABLES = {
    "fact_orders_clean.csv":      "fact_orders",
    "fact_order_items_clean.csv": "fact_order_items",
    "fact_inventory_clean.csv":   "fact_inventory",
}

# Output tables (RFM, monthly revenue...): FULL replace
OUTPUT_TABLES = {
    "rfm_segments.csv":    "rfm_segments",
    "monthly_revenue.csv": "monthly_revenue",
    "inventory_turnover.csv": "inventory_turnover",
}


# ── Upload function ────────────────────────────────────────────────────────────
def upload_table(client, df, table_id, write_mode):
    """
    write_mode:
        "WRITE_TRUNCATE" → xóa hết rồi ghi lại (dùng cho dim + output)
        "WRITE_APPEND"   → chỉ thêm rows mới (dùng cho fact)
    """
    job_config = bigquery.LoadJobConfig(
        write_disposition=write_mode,
        autodetect=True,         # BQ tự detect schema từ DataFrame
        source_format=bigquery.SourceFormat.CSV,
    )
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Chờ job hoàn thành
    print(f"  ✓ {table_id.split('.')[-1]:<30} {len(df):>8,} rows  [{write_mode}]")


def main():
    # ── Kiểm tra config ────────────────────────────────────────────────────────
    if GCP_PROJECT == "YOUR_PROJECT_ID":
        print("⚠  Chưa điền GCP_PROJECT_ID.")
        print("   Mở file này và điền vào dòng GCP_PROJECT = ...")
        return

    if not os.path.exists(CREDENTIALS):
        print(f"⚠  Không tìm thấy credentials: {CREDENTIALS}")
        print("   Hướng dẫn tạo service account key:")
        print("   GCP Console → IAM → Service Accounts → Create → Download JSON")
        return

    # ── Kết nối BigQuery ───────────────────────────────────────────────────────
    creds  = service_account.Credentials.from_service_account_file(CREDENTIALS)
    client = bigquery.Client(project=GCP_PROJECT, credentials=creds)

    # Tạo dataset nếu chưa có
    dataset_ref = bigquery.Dataset(f"{GCP_PROJECT}.{BQ_DATASET}")
    dataset_ref.location = "US"
    client.create_dataset(dataset_ref, exists_ok=True)
    print(f"\nDataset: {GCP_PROJECT}.{BQ_DATASET}")
    print("=" * 60)

    # ── Upload dim tables (TRUNCATE) ───────────────────────────────────────────
    print("\n[1/3] Dim tables (full replace)...")
    for filename, table_name in DIM_TABLES.items():
        path = os.path.join(CLEANED_DIR, filename)
        if not os.path.exists(path):
            print(f"  ⚠ Không tìm thấy {path} — bỏ qua")
            continue
        df = pd.read_csv(path)
        table_id = f"{GCP_PROJECT}.{BQ_DATASET}.{table_name}"
        upload_table(client, df, table_id, "WRITE_TRUNCATE")

    # ── Upload fact tables (APPEND) ────────────────────────────────────────────
    print("\n[2/3] Fact tables (append only)...")
    for filename, table_name in FACT_TABLES.items():
        path = os.path.join(CLEANED_DIR, filename)
        if not os.path.exists(path):
            print(f"  ⚠ Không tìm thấy {path} — bỏ qua")
            continue
        df = pd.read_csv(path)

        # Incremental: chỉ lấy data từ ngày chưa có trên BQ
        # (Đơn giản hóa: dùng WRITE_APPEND, production thì cần check duplicate)
        table_id = f"{GCP_PROJECT}.{BQ_DATASET}.{table_name}"
        upload_table(client, df, table_id, "WRITE_APPEND")

    # ── Upload output tables (TRUNCATE) ───────────────────────────────────────
    print("\n[3/3] Output/analytics tables (full replace)...")
    for filename, table_name in OUTPUT_TABLES.items():
        path = os.path.join(OUTPUT_DIR, filename)
        if not os.path.exists(path):
            print(f"  ⚠ Không tìm thấy {path} — bỏ qua")
            continue
        df = pd.read_csv(path)
        table_id = f"{GCP_PROJECT}.{BQ_DATASET}.{table_name}"
        upload_table(client, df, table_id, "WRITE_TRUNCATE")

    print("\n✅ Xong! Vào BigQuery Console để kiểm tra:")
    print(f"   https://console.cloud.google.com/bigquery?project={GCP_PROJECT}")


if __name__ == "__main__":
    main()
