import streamlit as st
import math

st.set_page_config(page_title="計算機 - 含稅試算", layout="centered")
st.title("🧮 商用計算機（含稅試算）")

st.markdown("### ✍️ 請輸入多筆計算式（每行一筆，例如 `1000 + 250 * 2`）")
user_input = st.text_area("輸入計算內容：", height=200)

# -------- 計算處理 --------
if user_input:
    lines = user_input.strip().split("\n")
    results = []
    total_sum = 0
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names.update({"abs": abs, "round": round})

    for idx, expr in enumerate(lines):
        try:
            result = eval(expr, {"__builtins__": {}}, allowed_names)
            if isinstance(result, (int, float)):
                val = round(result, 2)
                results.append((expr, val))
                total_sum += val
            else:
                results.append((expr, "錯誤：非數字結果"))
        except Exception as e:
            results.append((expr, f"錯誤：{e}"))

    st.divider()
    st.subheader("📋 各筆結果：")
    for expr, value in results:
        st.write(f"`{expr}` → **{value}**")

    st.divider()
    st.subheader("💰 總計結果（含稅試算）")
    tax_excluded = round(total_sum * 0.95, 2)
    tax_value = round(total_sum * 0.05, 2)

    st.metric("總金額（含稅）", f"NT$ {total_sum:,.2f}")
    st.metric("稅前金額（95%）", f"NT$ {tax_excluded:,.2f}")
    st.metric("進項稅（5%）", f"NT$ {tax_value:,.2f}")
else:
    st.info("請在上方輸入一行一筆的計算式。\n例如：\n1000 + 500\n200 * 2。 按Ctrl + Enter就可執行")

st.caption("版本：1.1 | 支援多筆計算、自動加總、含稅與稅前試算")
