import logging
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from typing import Optional



# Instantiate FastAPI
app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)