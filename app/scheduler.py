from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from typing import List

scheduler = BackgroundScheduler()

def job_function(job_name):
    print(f"Executing job: {job_name} at {datetime.now()}")

def schedule_job(job_name: str, weekdays: List[str]):
    cron_weekdays = ','.join(weekdays)  
    scheduler.add_job(job_function, 'cron', day_of_week=cron_weekdays, args=[job_name], id=job_name)

scheduler.start()