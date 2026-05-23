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
don_hang = pd.read_csv(f"{RAW}/don_hang_2020_2024.csv", encoding="utf-8-sig")
profile(don_hang, "don_hang_2020_2024.csv")

# File 2: Chi tiết đơn hàng
# TODO: load file chi_tiet_don_hang.csv rồi gọi profile()

# File 3: Danh mục sản phẩm
# TODO: load file danh_muc_san_pham.csv rồi gọi profile()

# File 4 & 5: Khách hàng (2 file riêng)
# TODO: load cả 2 file khách hàng, so sánh tên cột giữa 2 file
# Gợi ý: print(df_a.columns.tolist()) và print(df_b.columns.tolist())

# File 6: Phiếu nhập kho
# TODO

# File 7: Cửa hàng
# TODO

# File 8: Tồn kho tháng
# TODO

# File 9: Chương trình khuyến mãi
# TODO

# File 10: Nhà cung cấp
# TODO


# ══════════════════════════════════════════════════════════════════════════════
# FINDINGS — Bạn tự điền sau khi chạy xong
# ══════════════════════════════════════════════════════════════════════════════
"""
FILE: don_hang_2020_2024.csv
  - Số dòng / cột    :
  - Null đáng chú ý  :
  - Duplicate        :
  - Vấn đề phát hiện :

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
