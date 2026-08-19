# Customer Churn Prediction - Frontend

A React Web App built to interface with the Churn Prediction FastAPI backend. It allows users to enter customer banking metrics (age, account balance, active membership status, country, salary, etc.) and instantly view the predicted churn risk and probability score.

---

## 📌 Project Features
- **Interactive Form**: Pre-filled default values for quick 1-click testing.
- **Real-Time Predictions**: Communicates directly with the FastAPI model server.
- **Dynamic Visuals**: Visual risk badge (Low / High Risk) and probability bar.
- **Modular Codebase**: Component-based layout (`Header`, `CustomerForm`, `PredictionResult`, `services/api.js`).
- **Environment Config**: Dynamic backend base URL configured via `.env`.

---

## 🛠️ Tech Stack
- **Library**: React 18
- **Bundler**: Webpack 5 + Babel
- **Styling**: Custom CSS (Dark Slate & Indigo Theme)

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Environment
Check `.env` file (or copy from `.env.example`):
```env
API_BASE_URL=http://localhost:8000
```

### 3. Start Development Server
```bash
npm start
```
App runs at `http://localhost:3000`.

### 4. Build for Production
```bash
npm run build
```
Production assets are generated in `dist/`.

---

## 📂 Project Structure
```text
src/
├── components/
│   ├── Header.jsx           # Top title banner
│   ├── CustomerForm.jsx     # Form input fields & controls
│   └── PredictionResult.jsx # Churn probability & risk card
├── services/
│   └── api.js               # API fetch call module
├── constants/
│   └── defaults.js          # Initial sample form values
├── App.jsx                  # Main component
├── main.jsx                 # React root entry
└── index.css                # App styles
```
