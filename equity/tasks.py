from __future__ import absolute_import

from celery import shared_task
from equity.models import UserSecuritySelectionModel
from django.conf import settings
from equity.models import Security
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

import requests
from celery.task.schedules import crontab
# import the logging library
import logging

# Get an instance of a logger
logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@task(name="Get_Market_Prices")
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="1", minute="0", day_of_week="*")),
               ignore_result=True)
# @periodic_task(run_every=timedelta(day=1))
def getMarketPrices():
    securitiesToPrice = Security.objects.all()
    count = Security.objects.all().count()

    logger.info('Total Securities in Rebalancer Sec Master' + count)


    # call out to XigNite
    # URL = settings.QUOTE_URL
    # r = requests.get(URL+"symbol")


@shared_task(name='Execute_Rebalance')
def executeRebalance(SSMID):
    RebalanceModel = UserSecuritySelectionModel.objects.filter(SSM_id=SSMID)

    # Get all the targetWeights
