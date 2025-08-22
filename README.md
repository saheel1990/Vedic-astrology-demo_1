# Vedic Astrology Blueprint — Deploy Package (Demo)
## Contents
- backend/: FastAPI demo API (simple sun-sign stub)
- frontend/: Static single-page app (calls backend at http://localhost:8000)
- Dockerfile included for backend

## Quick start (local)
1. Start backend:
   ```
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
2. Open frontend/index.html in a browser (or serve it with a static server).
3. Replace GA4 MEASUREMENT_ID in frontend/index.html with your actual ID.

## Notes
- This package is a **demo scaffold**. Replace astrology stubs with real sidereal/ephemeris calculations for production.
- SQLite/Postgres integration, authentication, and analytics event wiring are intentionally left minimal to keep the demo portable.
