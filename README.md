### 📄 `README.md`

```markdown
# 📦 Delivery Label Generator – Flask Web App

This project is a minimal yet functional delivery label generator built using Python and Flask. It allows users to log in, enter sender/receiver details, and generate a downloadable PDF delivery label with a unique delivery ID and barcode.

---

## 🚀 Features

- ✅ Hardcoded login screen (`test` / `test123`)
- ✅ Sender and Receiver input form
- ✅ Automatically generated delivery ID
- ✅ PDF delivery label generation with:
  - Sender & receiver information
  - Unique tracking ID
  - Barcode image
- ✅ Downloadable PDF
- ✅ Clean folder structure and modular utility functions

---

## 📂 Folder Structure

```

DeliveryLabelApp/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   └── label.html
├── static/
│   └── logo.png
├── utils/
│   ├── pdf\_generator.py
│   └── barcode\_generator.py
├── session/
│   └── **init**.py
├── output/
│   └── (Generated PDFs will appear here)

````

---

## 🔐 Login Credentials

- **Username:** `test`
- **Password:** `test123`

---

## ⚙️ Setup Instructions

### 1. Clone or extract the folder
```bash
cd DeliveryLabelApp
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📄 PDF & Barcode Output

After confirming a form submission:

* A barcode will be generated as `output/<delivery_id>.png`
* A PDF delivery label will be saved in the `output/` folder
* A download button will be shown in the browser

---

## 🧰 Technologies Used

* **Flask** – Web framework
* **ReportLab** – For generating PDFs
* **python-barcode** – For generating barcode images
* **Pillow** – Image rendering library

---

## 📌 Notes

* All data is temporary (in-memory only); no database is used.
* The app is for demo/testing purposes.
