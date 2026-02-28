# 📊 Sales Dashboard (Streamlit)

โปรเจกต์นี้เป็น **Interactive Sales Dashboard**  
พัฒนาด้วยภาษา **Python** โดยใช้ **Streamlit** และ **Plotly**  
เพื่อแสดงข้อมูลยอดขายในรูปแบบกราฟที่เข้าใจง่าย และสามารถโต้ตอบได้

โปรเจกต์นี้จัดทำขึ้นเพื่อฝึกการสร้าง Dashboard, การจัดโครงสร้างโค้ด และการใช้งาน Git ตามหลัก Commit Early & Commit Often

---

## 🎯 วัตถุประสงค์ของโปรเจกต์

- สร้าง Dashboard อย่างง่ายด้วย Streamlit
- แสดงผลข้อมูลด้วยกราฟอย่างน้อย 3 ประเภท
- มี Interactive ระหว่างผู้ใช้กับกราฟ
- ฝึกการใช้งาน Git และการจัดการ commit
- เขียน README เพื่ออธิบายโค้ดและวิธีการรันโปรแกรม

---

## ✨ Features

- เลือก Metric ที่ต้องการดูได้ (sales, profit, customers)
- แสดงกราฟ 3 รูปแบบ
  - Line Chart : แนวโน้มรายเดือน
  - Bar Chart : เปรียบเทียบรายเดือน
  - Pie Chart : สัดส่วนข้อมูล
- Layout แบบ Dashboard (3 columns)
- แสดงข้อมูลดิบ (Raw Data)
- รองรับกรณีข้อมูลว่าง (Empty State Handling)

---

## 🗂️ โครงสร้างโปรเจกต์

```text
dashboard_demo/
│
├── app.py          # ไฟล์หลักสำหรับรัน Streamlit Dashboard
├── data.csv        # ไฟล์ข้อมูลยอดขาย
├── README.md       # เอกสารอธิบายโปรเจกต์
└── requirements.txt (ถ้ามี)

---

🧠 อธิบายโค้ด (app.py)
1. Import Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

streamlit ใช้สร้างหน้าเว็บ dashboard

pandas ใช้จัดการข้อมูลจากไฟล์ CSV

plotly.express ใช้สร้างกราฟแบบ interactive

2. ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

ตั้งชื่อหน้าเว็บ

ใช้ layout แบบกว้าง เหมาะกับ dashboard

3. ส่วนหัวของ Dashboard
st.title("📊 Sales Dashboard")
st.write("Interactive dashboard for sales performance analysis")
st.markdown("---")

แสดงชื่อและคำอธิบาย

ใช้เส้นคั่นเพื่อแบ่ง section

4. โหลดข้อมูลจาก CSV
df = pd.read_csv("data.csv")
ตรวจสอบกรณีข้อมูลว่าง
if df.empty:
    st.warning("No data available")
    st.stop()

ถ้าไฟล์ CSV ไม่มีข้อมูล ระบบจะแสดงข้อความเตือนและหยุดการทำงาน

5. ส่วนควบคุม (Select Metric)
metric_options = ["sales", "profit", "customers"]
selected_metric = st.selectbox(
    "Choose a metric to visualize",
    metric_options,
    index=0
)

ผู้ใช้สามารถเลือก metric ที่ต้องการดูได้ และกราฟจะเปลี่ยนตามทันที

6. การสร้างกราฟ
Line Chart (แนวโน้ม)
px.line(
    df,
    x="month",
    y=selected_metric,
    title=f"Monthly {selected_metric.capitalize()} Trend",
    markers=True
)
Bar Chart (เปรียบเทียบ)
px.bar(
    df,
    x="month",
    y=selected_metric,
    title=f"Monthly {selected_metric.capitalize()} Comparison"
)
Pie Chart (สัดส่วน)
px.pie(
    df,
    values=selected_metric,
    names="month",
    title=f"{selected_metric.capitalize()} Distribution by Month"
)
7. การจัด Layout ของกราฟ
col1, col2, col3 = st.columns(3)

แสดงกราฟทั้ง 3 แบบในแถวเดียว เพื่อให้ดูเหมือน Dashboard จริง

8. แสดงข้อมูลดิบ (Raw Data)
st.dataframe(df)

ใช้แสดงข้อมูลจากไฟล์ CSV เพื่อความโปร่งใสและตรวจสอบข้อมูลได้ง่าย

▶️ วิธีรันโปรเจกต์
1. ตรวจสอบเวอร์ชัน Python
python --version

แนะนำ Python 3.9 หรือใหม่กว่า

2. สร้าง Virtual Environment (แนะนำ)
python -m venv venv
venv\Scripts\activate
3. ติดตั้ง Library ที่จำเป็น
pip install streamlit pandas plotly
4. รัน Dashboard
streamlit run app.py

เมื่อรันสำเร็จ จะเปิดเว็บอัตโนมัติ
