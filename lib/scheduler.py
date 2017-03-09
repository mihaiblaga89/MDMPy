'''
Project : MDMPy2
File : scheduler
Author : Lego
Date : 26/02/2017
'''

import sys
import os.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../site-packages')))
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from lib.Singleton import Singleton
from lib.jobs.MusicSearch import *


@Singleton
class Scheduler:

    def __init__(self):

        jobstores = {
            'default': MemoryJobStore(),
        }
        executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExecutor(5)
        }

        job_defaults = {
            'coalesce': True,
            'max_instances': 3
        }

        self.scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
        self.scheduler.start()

        self.scheduler.add_job(MusicSearch, 'interval', minutes=1, id='MusicSearch')