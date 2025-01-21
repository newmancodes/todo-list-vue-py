from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI()

class Patient(BaseModel):
    id: int
    name: str
    birth_date: date
    email: Optional[str] = None

patients_db: List[Patient] = []

@app.get("/patients/", response_model=List[Patient])
def list_patients() -> List[Patient]:
    return patients_db

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="localhost", port=8000, reload=True)