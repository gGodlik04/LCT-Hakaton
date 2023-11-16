from .algoritm import TaskDistributor
from environs import Env
import pandas as pd
from sqlalchemy import create_engine
from celery import shared_task


@shared_task()
def send_tasks():
    env = Env()
    env.read_env()

    connection_string = create_engine(
        env('DB_ENGINE'))

    df_users = pd.read_sql('SELECT * FROM accounts_user', connection_string)
    df_users = df_users[df_users["role"] == 2]

    df_points = pd.read_sql('SELECT * FROM "AgentPoint"', connection_string)
    df_task = pd.read_sql('SELECT * FROM "Task"', connection_string)
    df_task_type = pd.read_sql('SELECT * FROM "TaskType"', connection_string)

    df_points['uuid'] = df_points['uuid'].astype(str)
    df_task['agent_point_id'] = df_task['agent_point_id'].astype(str)
    points_task = pd.merge(df_points, df_task,
                           left_on='uuid', right_on='agent_point_id', how='outer', suffixes=('_x', ''))

    task_distributor = TaskDistributor(points_task, df_users, df_task, df_task_type,
                                       env('API_YANDEX_KEY'),
                                       env('API_OPENROUTE_KEY'))
    task_distributor.run_distribution(connection_string)

    connection_string.dispose()
    return



