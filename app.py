import streamlit as st
import pandas as pd
import random
from bidi.algorithm import get_display
from arabic_reshaper import reshape

def persian(text):
    return get_display(reshape(str(text)))

st.set_page_config(page_title="مدیریت پورتفو", layout="centered")
st.title(persian("📊 اپلیکیشن بررسی حد ضرر"))

st.subheader(persian("ورود اطلاعات سهم"))
نماد = st.text_input(persian("نماد"))
تعداد = st.number_input(persian("تعداد"), min_value=1)
قیمت_خرید = st.number_input(persian("قیمت خرید"), min_value=1)
حد_ضرر = st.number_input(persian("حد ضرر"), min_value=1)

if st.button(persian("افزودن و بررسی")):
    قیمت_فعلی = random.randint(int(حد_ضرر * 0.8), int(قیمت_خرید * 1.2))
    هشدار = قیمت_فعلی < حد_ضرر

    وضعیت = persian("⛔ هشدار: حد ضرر فعال شده") if هشدار else persian("✅ وضعیت ایمن")

    df = pd.DataFrame([{
        persian("نماد"): persian(نماد),
        persian("تعداد"): تعداد,
        persian("قیمت خرید"): f"{قیمت_خرید:,}",
        persian("حد ضرر"): f"{حد_ضرر:,}",
        persian("قیمت فعلی"): f"{قیمت_فعلی:,}",
        persian("وضعیت"): وضعیت
    }])

    st.table(df)
    st.warning(وضعیت) if هشدار else st.success(وضعیت)
