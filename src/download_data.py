"""
download_data.py
=================
Tải toàn bộ raw data từ Google Drive về data/raw/
Chạy một lần trước khi bắt đầu pipeline:
    python download_data.py
"""

import os
import urllib.request

# ── CẤU HÌNH — điền File ID từ Google Drive ───────────────────────────────────
# Cách lấy File ID:
#   1. Chuột phải file trên Drive → "Get link"
#   2. Link dạng: https://drive.google.com/file/d/FILE_ID/view
#   3. Copy phần FILE_ID dán vào bên dưới

FILES = {
    "ton_kho_hang_thang.csv":      "1ang5hL_Fnd_FWV3jhD0ecCNQw-OfTDjF",
    "phieu_nhap_kho.csv":          "1NAsmW_HOdMBfpMyLwJf-gUz6wlLY3LgS",
    "khach_hang_2023_2024.csv":    "1TkV7I-Es1i7O2n78KEcTlzrkHiQVmmwf",
    "khach_hang_2020_2022.csv":    "144sPkogIzoyrpuHYeB895n9Jz9RcmXnm",
    "don_hang_2020_2024.csv":      "1jHAybKrBVytmH6aBMpvleUFyN_HNxJo6",
    "danh_sach_nha_cung_cap.csv":  "1ZJHHhYKDdUDAsukWZbZAAh7oRCshwDpu",
    "danh_sach_cua_hang.csv":      "1TvGTpOuD5WfjM9nV_dybx4B4sYGeQ9ev",
    "danh_muc_san_pham.csv":       "1NYaGJFonpzMBHYJ-v-HMHfBcxV94_y3C",
    "chuong_trinh_khuyen_mai.csv": "1jaA1GuZN3ypXKJTUyW0EyQ1r46ESR7bU",
    "chi_tiet_don_hang.csv":       "1z4BXdOhhju_UdskvNyZZ5q6Zekwq0Oo9",
}

# ── Download ───────────────────────────────────────────────────────────────────
def download_file(file_id, dest_path):
    """Download file công khai từ Google Drive."""
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    print(f"  Downloading {os.path.basename(dest_path)}...", end=" ")
    try:
        urllib.request.urlretrieve(url, dest_path)
        size_kb = os.path.getsize(dest_path) / 1024
        print(f"OK ({size_kb:.0f} KB)")
    except Exception as e:
        print(f"FAILED — {e}")


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
    os.makedirs(out_dir, exist_ok=True)

    print("=" * 50)
    print("FMCG Raw Data Downloader")
    print("=" * 50)

    not_configured = [f for f, fid in FILES.items() if fid == "PASTE_FILE_ID_HERE"]
    if not_configured:
        print("\n⚠  Chưa điền File ID cho các file sau:")
        for f in not_configured:
            print(f"   - {f}")
        print("\nHướng dẫn:")
        print("  1. Vào Google Drive, chuột phải từng file → Get link")
        print("  2. Copy File ID từ link (phần giữa /d/ và /view)")
        print("  3. Điền vào dict FILES trong file này")
        return

    for filename, file_id in FILES.items():
        dest = os.path.join(out_dir, filename)
        if os.path.exists(dest):
            print(f"  {filename} — đã có, bỏ qua")
            continue
        download_file(file_id, dest)

    print("\nXong! Kiểm tra thư mục data/raw/")


if __name__ == "__main__":
    main()
