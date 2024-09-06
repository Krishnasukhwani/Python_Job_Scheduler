# Python_Job_Scheduler

This is a job scheduling microservice built with FastAPI and MongoDB. It allows users to create, retrieve, and schedule jobs with various configurations.

## Features

- Create new jobs with customizable attributes.
- Schedule jobs to run on specific weekdays.
- Store job details in MongoDB.
- Scalable architecture for handling high loads.

## Requirements

- Python 3.9 or higher
- MongoDB (local or hosted on MongoDB Atlas)
- Docker (optional, for containerization)

## Setup Instructions
 
Step 1: Clone the Repository

```bash
git clone https://github.com/Krishnasukhwani/Python_Job_Scheduler.git
cd Python_Job_Scheduler

```
Step 2: Create a Virtual Environment
Create a virtual environment to manage dependencies:
```bash
python -m venv venv
```
Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

Step 3: Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```


Step 4: Configure MongoDB
Local MongoDB: If you are using a local MongoDB instance, ensure it is running.
MongoDB Atlas: If you prefer a cloud solution, create a MongoDB Atlas account and set up a cluster. Obtain the connection string and replace it in app/database.py.

MONGO_DETAILS = "mongodb+srv://<username>:<password>@cluster.mongodb.net/mydatabase?retryWrites=true&w=majority"

Step 5: Run the Application
Run the FastAPI application using Uvicorn:
bash
uvicorn app.main:app --reload


### You can now access the API documentation at http://127.0.0.1:8000/docs.
 This will open swagger document to test the Apis


Step 6: Example API Requests
Create a Job
To create a job, send a POST request to /jobs with the following JSON body:
json
{
    "name": "Send Weekly Report",
    "next_run": "2024-09-09T10:00:00",
    "weekdays": ["mon", "tue", "wed"],
    "job_type": "email",
    "job_details": "Send a weekly report to the marketing team",
    "parameters": {
        "recipient": "user@example.com"
    }
}

Get All Jobs
To retrieve all jobs, send a GET request to /jobs.

Get a Specific Job
To retrieve a specific job by ID, send a GET request to /jobs/{job_id}.


Step 7: Dockerization (Optional)
If you want to run the application in a Docker container, you can build and run it using the following commands:
Build the Docker Image:
bash
docker build -t Python_Job_Scheduler .

Run the Docker Container:
bash
docker run -d -p 8000:8000 Python_Job_Scheduler