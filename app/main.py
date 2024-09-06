from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from . import models, crud
from .scheduler import schedule_job

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/jobs", response_model=models.Job)
def create_job(job: models.Job):
    job_data = crud.create_job(job)
    schedule_job(job.name, job.weekdays)
    return job_data

@app.get("/jobs", response_model=list[models.Job])
def read_jobs():
    return crud.get_jobs()

@app.get("/jobs/{job_id}", response_model=models.Job)
def read_job(job_id: str):
    job = crud.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job