# 🌍 AI Global Insight Dashboard

<div dir="rtl">

# لوحة رؤى الذكاء الاصطناعي العالمية

</div>

An interactive dashboard that visualizes AI usage statistics across different countries with a modern dark theme, featuring interactive maps, charts, and data tables.

<div dir="rtl">

لوحة تحكم تفاعلية تعرض إحصائيات استخدام الذكاء الاصطناعي حول العالم مع سمة داكنة عصرية، وتشمل خرائط ورسوم بيانية وجداول بيانات تفاعلية.

</div>

## 🌟 Features | المميزات

- **Dark Theme UI** with modern, eye-catching visualizations
- **Interactive World Map** showing AI usage intensity by country
- **Top Countries** visualization with rainbow-colored bar charts
- **Users Distribution** pie chart by continent
- **Usage Analysis** with box plots showing distribution by continent
- **Responsive Design** that works on different screen sizes
- **Interactive Data Table** with filtering capabilities

<div dir="rtl">

- **واجهة مستخدم داكنة** مع تصورات بصرية جذابة
- **خريطة عالمية تفاعلية** تُظهر كثافة استخدام الذكاء الاصطناعي حسب الدولة
- **تصور للدول الأكثر استخداماً** مع ألوان قوس قزح
- **مخطط دائري** لتوزيع المستخدمين حسب القارة
- **تحليل الاستخدام** مع مخططات الصندوق والعُصَيّات
- **تصميم متجاوب** يعمل على مختلف أحجام الشاشات
- **جدول بيانات تفاعلي** مع إمكانية التصفية

</div>

## 🚀 Getting Started | البدء

### Prerequisites | المتطلبات الأساسية

- Python 3.8 or higher
- pip (Python package manager)

### Installation | التثبيت

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-global-insight-dashboard.git
   cd ai-global-insight-dashboard
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application | تشغيل التطبيق

```bash
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`

## 📊 Data | البيانات

The dashboard uses a CSV file (`ai_data.csv`) containing the following columns:
- `Country`: Name of the country
- `Continent`: Continent where the country is located
- `AI_Usage_Perc`: Percentage of AI usage in the country
- `Users_Millions`: Number of AI users in millions
- `BenefitsIndex`: Index measuring AI benefits (1-10)
- `Latitude`: Geographic latitude
- `Longitude`: Geographic longitude

## 🛠️ Dependencies | التبعيات

- streamlit
- pandas
- matplotlib
- seaborn
- plotly

## 📝 License | الترخيص

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing | المساهمة

Contributions are welcome! Please feel free to submit a Pull Request.

## 📂 Project Structure | هيكل المشروع

```
ai-global-insight-dashboard/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── ai_data.csv         # Data file
└── README.md          # This file
```

## 📊 Data Sources | مصادر البيانات

The dashboard uses sample data for demonstration purposes. In a production environment, you would connect to a real data source or API.

## 🛠️ Customization | التخصيص

### Adding More Data

To add more countries or update the existing data, modify the `load_data()` function in `app.py`.

### Changing the Theme

You can customize the theme by modifying the CSS in the `st.markdown()` call at the beginning of `app.py`.

## 📝 Acknowledgments | الشكر

- Built with [Streamlit](https://streamlit.io/)
- Icons by [Twemoji](https://twemoji.twitter.com/)
- Map visualization by [PyDeck](https://deckgl.readthedocs.io/en/latest/)

## 📧 Contact | الاتصال

For any questions or suggestions, please open an issue or contact the project maintainers.

---

<div dir="rtl" style="text-align: center; margin-top: 2rem; color: #666;">
    <p>تم تطوير هذا المشروع باستخدام Streamlit و Python</p>
    <p>© 2023 AI Global Insight Dashboard - جميع الحقوق محفوظة</p>
</div>
