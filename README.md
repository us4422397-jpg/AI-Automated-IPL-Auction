# AI Automated IPL Auction Platform

An advanced, AI-powered decision intelligence platform built for the IPL Mega Auction. This system leverages state-of-the-art machine learning, real-time analytics, and an immersive dashboard to provide teams with a competitive edge during the auction.

---

## 📋 Prerequisites

Ensure you have the following installed on your system before proceeding:
- **Python 3.10+**
- **Node.js 18+** & npm
- **Docker Desktop** (Make sure it is running)
- **Supabase Account** (For managed PostgreSQL & Auth)

---

## 🚀 Getting Started

Follow these steps precisely to set up, train, and run the entire platform.

### Step 1: Environment Setup

1. **Clone/Navigate to the Project**:
   Ensure you are in the root directory: `AI Automated IPL Auction`.

2. **Configure Environment Variables**:
   Copy the example environment file and configure it with your credentials:
   ```bash
   cp .env.example .env
   ```
   *Note: Open `.env` and fill in your `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `SUPABASE_JWT_SECRET`, and `DB_URL` (Supabase connection string).*

3. **Install Backend Dependencies**:
   ```bash
   cd backend
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

4. **Install Frontend Dependencies**:
   ```bash
   cd ../frontend
   npm install
   ```

---

### Step 2: Database Initialization

We use **Alembic** to manage database schemas in our Supabase PostgreSQL instance.

1. Ensure your `.env` contains the correct `DB_URL`.
2. Apply the database migrations:
   ```bash
   cd backend
   alembic upgrade head
   ```
3. *(Optional)* Seed the database with initial user roles:
   ```bash
   python scripts/seed_auth.py
   ```

---

### Step 3: Data Ingestion & Cleaning Pipeline

Before training the ML models, the platform must scrape, ingest, and clean historical IPL data, player stats, and injury records.

1. **Run the Ingestion Pipeline**:
   ```bash
   cd backend
   python scripts/seed_db.py
   ```
   **What this does**:
   - Executes `kaggle_parser.py`, `scraper_iplt20.py`, and `scraper_cricinfo.py`.
   - Normalizes player names across datasets.
   - Cleans missing values, handles outliers in salaries, and structures the data into the `data/raw/` directory.
   - Pushes the cleaned data into the Supabase database.

---

### Step 4: ML Model Training & Evaluation

The intelligence of this platform comes from 11 specialized AI modules (Negotiation, Injury Risk, Chemistry, etc.).

1. **Train the Models**:
   ```bash
   cd backend
   python scripts/train_models.py
   ```
   **What this does**:
   - Loads the cleaned data from `data/raw/`.
   - Runs the hyperparameter tuning and training loops for XGBoost, LightGBM, and CatBoost models.
   - Evaluates the models using RMSE, MAE, and R² scores.
   - Serializes the trained models (`.pkl` or `.json` files) into the `data/models/` directory for the backend API to serve.

---

### Step 5: Running the Backend (FastAPI)

To run the backend server natively for development:

1. Activate your virtual environment:
   ```bash
   cd backend
   venv\Scripts\activate  # Windows
   ```
2. Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
3. **Verify**: Open `http://localhost:8000/docs` in your browser to see the interactive API documentation (Swagger UI).

---

### Step 6: Running the Frontend (React + Vite)

To start the beautiful glassmorphism dashboard:

1. Open a **new terminal window**.
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```
4. **Verify**: Open `http://localhost:5173` in your browser to view the Dashboard.

---

### Step 7: Running via Docker Compose (Production/Unified Mode)

Instead of running the frontend and backend separately in your terminal, the entire architecture is designed to be easily spun up using Docker. This creates a unified environment where Nginx routes traffic securely between your React frontend and FastAPI backend, while also providing a Redis instance for real-time WebSocket communication and caching.

#### 1. Preparation
Ensure that **Docker** and **Docker Compose** are installed and running on your system (e.g., Docker Desktop). Verify that your `.env` file at the root of the project is fully populated with your Supabase credentials, as Docker will read these environment variables to pass them to the backend container.

#### 2. Build the Images
To construct the optimized Docker images for both the frontend (Node.js/Nginx) and backend (Python/Uvicorn), open a terminal in the root directory and run:
```bash
docker-compose build --no-cache
```
*Note: The `--no-cache` flag ensures that any recent code or requirement changes are freshly built. This step may take a few minutes as it pulls base images and installs all dependencies.*

#### 3. Start the Containers
Once the build is successful, bring up the entire stack in detached mode (so it runs in the background):
```bash
docker-compose up -d
```
**What this does**:
- Starts the **redis** container on port 6379.
- Starts the **backend** FastAPI container on port 8000.
- Starts the **frontend** React application (served via Nginx) on port 80.
- Starts the **nginx** reverse proxy (if configured separately) to handle unified routing.

#### 4. Access the Application
- **Frontend Dashboard**: Open your browser and navigate to `http://localhost` (or `http://127.0.0.1`).
- **Backend API Docs**: The Swagger UI for the backend is available at `http://localhost/api/v1/docs` (if routed through Nginx) or `http://localhost:8000/docs`.

#### 5. View Logs and Monitor
If you need to debug or watch the real-time AI negotiation WebSocket traffic, you can view the live logs of all containers by running:
```bash
docker-compose logs -f
```
*(Press `Ctrl + C` to exit the log view)*

#### 6. Stop and Teardown
To gracefully stop the application and remove the containers, run:
```bash
docker-compose down
```
If you also want to clear any persistent Docker volumes (e.g., if we added a local Postgres volume later), you can use `docker-compose down -v`.

---

## 📁 Project Structure

```text
AI Automated IPL Auction/
├── .env                  # Global environment variables
├── docker-compose.yml    # Docker orchestration
├── backend/
│   ├── app/              # FastAPI application core
│   │   ├── api/          # RESTful and WebSocket API endpoints
│   │   ├── ml/           # 11 Core ML Modules & XAI (SHAP)
│   │   ├── models/       # SQLAlchemy Database models
│   │   └── auth/         # RBAC & Supabase JWT Auth
│   ├── data/             # Raw data, ingested data, and trained model binaries
│   ├── scripts/          # Ingestion pipelines and training scripts
│   └── tests/            # Pytest test suite
└── frontend/
    ├── src/
    │   ├── components/   # Reusable UI components & Dashboard Layout
    │   ├── pages/        # Views (Dashboard, Auction Room, Team Builder)
    │   ├── store/        # Zustand state management
    │   └── hooks/        # Custom React hooks (e.g., WebSockets)
    └── tailwind.config.js# Tailwind CSS Theme & Styling
```
