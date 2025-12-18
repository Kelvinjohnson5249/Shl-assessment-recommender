## How to Run the Application Locally

### Backend API (FastAPI)

1. Clone the repository
2. Create a Python virtual environment (Python 3.10 recommended)
3. Install dependencies:
   pip install -r requirements.txt
4. Start the backend API:
   uvicorn main:app --host 0.0.0.0 --port 8000

Endpoints:
- Health Check: http://localhost:8000/health
- Recommendation API: http://localhost:8000/recommend

### Frontend (Streamlit UI)

If you want to run the optional Streamlit frontend:

1. Open a new terminal
2. Activate the same virtual environment
3. Run:
   streamlit run app.py

The Streamlit UI interacts with the FastAPI backend to submit queries and display recommended assessments.
