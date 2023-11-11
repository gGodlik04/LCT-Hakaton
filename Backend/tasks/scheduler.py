from .tasks import send_tasks


def start_scheduler(scheduler):

    scheduler.add_job(send_tasks, 'cron', hour='08',
                      minute='00', day_of_week='mon-fri',
                      timezone='Europe/Moscow',)

