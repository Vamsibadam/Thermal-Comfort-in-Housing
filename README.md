### # Thermal Comfort Analysis Dashboard

This Streamlit app visualizes and analyzes thermal comfort in different building types based on climate, ventilation strategies, and user feedback.

---

### ## 🚀 Features

* Interactive dashboard with filtering by building type, cooling strategy, and country.
* Visualizations: scatter plots, bar charts, histograms.
* Practical recommendations for building materials and ventilation.
* Built with **Python**, **Pandas**, **Plotly**, and **Streamlit**.

---

### ## 📁 Project Structure

```
.
├── ashrae_db2.01.csv           # Dataset (Large file handled via Git LFS)
├── app.py                      # Main Streamlit app
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitattributes              # Git LFS tracking (auto-created)
```

---

### ## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

### ## 📦 Requirements

Make sure to install dependencies listed in `requirements.txt`, e.g.:

```txt
streamlit
pandas
plotly
```

---

### ## 📊 Dataset

* File: `ashrae_db2.01.csv`
* Size: \~50MB
* Tracked with [Git Large File Storage (LFS)](https://git-lfs.github.com/)

---

### ## 📌 Notes

* If the dataset fails to load due to GitHub limits, download manually from: \[Add Google Drive or alternative link]
* Streamlit requires internet access to load Plotly graphs.

---

### ## 👤 Author

* **Vamsi Badam**

---

