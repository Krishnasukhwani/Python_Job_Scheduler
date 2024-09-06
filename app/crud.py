from bson import ObjectId
from .database import jobs_collection
from .models import Job

def create_job(job: Job):
    job_dict = job.model_dump()
    result = jobs_collection.insert_one(job_dict)
    job_dict['id'] = str(result.inserted_id)
    return job_dict

def get_jobs():
    jobs = []
    for job in jobs_collection.find():
        job['id'] = str(job['_id'])
        jobs.append(job)
    return jobs

def get_job(job_id: str):
    job = jobs_collection.find_one({"_id": ObjectId(job_id)})
    if job:
        job['id'] = str(job['_id'])
    return job