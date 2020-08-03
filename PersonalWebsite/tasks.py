from celery.decorators import task

from dynamic_scraper.utils.task_utils import TaskUtils
from mysite.models import Basicinfo, VisaInformation

@task()
def run_spiders():
    t = TaskUtils()
    t.run_spiders(Basicinfo, 'scraper_runtime', 'article_spider')

@task()
def run_checkers():
    t = TaskUtils()
    t.run_checkers(VisaInformation, 'checker_runtime', 'article_checker')