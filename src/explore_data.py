"""
Ngày 1 — Explore & Profile Raw Data
=====================================
Mục tiêu: hiểu toàn bộ 10 file raw TRƯỚC khi clean bất cứ thứ gì.
Với mỗi file, trả lời được 5 câu hỏi:
  1. Bao nhiêu dòng, bao nhiêu cột?
  2. Cột nào null? Null bao nhiêu %?
  3. Có duplicate không?
  4. Cột số có giá trị bất thường không?
  5. Cột ngày đang ở format gì?

Hướng dẫn:
  - Tự viết phần "TODO" bên dưới
  - Chạy: python src/day1_explore.py
  - Ghi lại kết quả vào phần FINDINGS cuối file
"""

import pandas as pd
import os

RAW = "data/raw"

# ── Helper: in thông tin cơ bản của 1 dataframe ───────────────────────────────
def profile(df, name):
    print(f"\n{'='*60}")
    print(f"FILE: {name}")
    print(f"{'='*60}")

    # TODO: In ra shape (số dòng x số cột)
    # Gợi ý: df.shape
    print(df.shape)

    # TODO: In ra danh sách cột và kiểu dữ liệu
    # Gợi ý: df.info()
    print(df.info())

    # TODO: Tính % null của từng cột, chỉ in ra cột có null > 0
    # Gợi ý: df.isnull().sum() / len(df) * 100
    null_pct = df.isnull().sum() / len(df) * 100
    print(null_pct[null_pct > 0])

    # TODO: Đếm số dòng duplicate
    # Gợi ý: df.duplicated().sum()
    print(df.duplicated().sum())

    # TODO: Với các cột số, in df.describe() để xem min/max/mean
    # Gợi ý: df.describe()
    print(df.describe())

    print("→ GHI CHÚ CỦA TÔI:")
    print("   (bạn tự viết vào đây sau khi đọc kết quả)")


# ── Load và profile từng file ──────────────────────────────────────────────────

# File 1: Đơn hàng
chi_tiet_don_hang = pd.read_csv(f"{RAW}/chi_tiet_don_hang.csv", encoding="utf-8-sig")
profile(chi_tiet_don_hang, "chi_tiet_don_hang.csv")

# # File 2: Chi tiết đơn hàng
don_hang = pd.read_csv(f"{RAW}/don_hang_2020_2024.csv", encoding="utf-8-sig")
profile(don_hang, "don_hang_2020_2024.csv")

# # File 3: Danh mục sản phẩm
dm_sanpham = pd.read_csv(f"{RAW}/danh_muc_san_pham.csv", encoding="utf-8-sig")
profile(dm_sanpham, "danh_muc_san_pham.csv")

# File 4 & 5: Khách hàng (2 file riêng)
kh_2020_2022 = pd.read_csv(f"{RAW}/khach_hang_2020_2022.csv", encoding="utf-8-sig")
profile(kh_2020_2022, "khach_hang_2020_2022.csv")

kh_2023_2024 = pd.read_csv(f"{RAW}/khach_hang_2023_2024.csv", encoding="utf-8-sig")
profile(kh_2023_2024, "khach_hang_2023_2024.csv")

# File 6: Phiếu nhập kho
phieu_nhap_kho = pd.read_csv(f"{RAW}/phieu_nhap_kho.csv", encoding="utf-8-sig")
profile(phieu_nhap_kho, "phieu_nhap_kho.csv")

# File 7: Cửa hàng
danh_sach_cua_hang = pd.read_csv(f"{RAW}/danh_sach_cua_hang.csv", encoding="utf-8-sig")
profile(danh_sach_cua_hang, "danh_sach_cua_hang.csv")

# File 8: Tồn kho tháng
ton_kho_hang_thang = pd.read_csv(f"{RAW}/ton_kho_hang_thang.csv", encoding="utf-8-sig")
profile(ton_kho_hang_thang, "ton_kho_hang_thang.csv")

# File 9: Chương trình khuyến mãi
chuong_trinh_khuyen_mai = pd.read_csv(f"{RAW}/chuong_trinh_khuyen_mai.csv", encoding="utf-8-sig")
profile(chuong_trinh_khuyen_mai, "chuong_trinh_khuyen_mai.csv")

# File 10: Nhà cung cấp
danh_sach_nha_cung_cap = pd.read_csv(f"{RAW}/danh_sach_nha_cung_cap.csv", encoding="utf-8-sig")
profile(danh_sach_nha_cung_cap, "danh_sach_nha_cung_cap.csv")


# ══════════════════════════════════════════════════════════════════════════════
# FINDINGS — Bạn tự điền sau khi chạy xong
# ══════════════════════════════════════════════════════════════════════════════
"""
FILE: don_hang_2020_2024.csv
  - Số dòng / cột    : (122400, 10)
  - Null đáng chú ý  : Ma_khach_hang ->  88376 non-null
  - Duplicate        : Mã đơn hàng -> 2400
  - Vấn đề phát hiện : 3 vấn đề
    + Mã khách hàng null 27,8% do là khách hàng lẻ/khách vãng lai, không lưu thông tin khách hàng.
    + Mã khách hàng trùng tên là do nhân viên nhập đơn 2 lần giống y hệt nhau với tỷ lệ 2%
    + 75th percentile là 0, điều này nói lên rất ít giảm giá, khi giảm giá thì sẽ giảm giá lớn

FILE: chi_tiet_don_hang.csv
  - Số dòng / cột    :
  - Null đáng chú ý  :
  - Duplicate        :
  - Vấn đề phát hiện :

FILE: danh_muc_san_pham.csv
  - ...

[Tiếp tục cho các file còn lại]

NHẬN XÉT CHUNG:
  - File nguy hiểm nhất  :
  - Join key tin được    :
  - Ưu tiên clean trước  :
"""
