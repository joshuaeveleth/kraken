from django.db import models
import os, time, hashlib, datetime
from ngt.messaging.queue import MessageBus

class RemoteJob(models.Model):
    date_added = models.DateTimeField('date acquired')
    job_id = models.CharField(max_length=64)
    job_string = models.CharField(max_length=4096)

    def generate_unique_id(self, job_str):
        '''Returns a unique job ID that is the MD5 hash of the local
        hostname, the local time of day, and the job string.'''
        hostname = os.uname()[1]
        t = time.clock()
        m = hashlib.md5()
        m.update(str(hostname))
        m.update(str(t))
        m.update(job_str)
        return m.hexdigest()

    def __init__(self, job_string, callback = None):
        self.job_id = self.generate_unique_id(job_string)
        self.date_added = datetime.datetime.now()
        self.job_string = job_string
        print('[' + str(self.date_added) + '] ' + 'Registering NGT job ' + self.job_id +
              ' : ' + self.job_string)
        MessageBus().basic_publish("JOB " + str(self.job_id) +
                                   " EXECUTE " + str(self.job_string))
        
    def __unicode__(self):
        return "NGT job: " + self.job_id + "    Started at " + self.date_added


