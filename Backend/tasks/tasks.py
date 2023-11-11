from .algoritm import TaskDistributor
from environs import Env
import pandas as pd
from sqlalchemy import create_engine


def send_tasks():
    env = Env()
    env.read_env()

    connection_string = create_engine(
        'postgresql://fzpvuodf:ZJhLvoXnBVUJRGxCkDNpMvWmddimNytV@cornelius.db.elephantsql.com/fzpvuodf')

    query_for_users = 'SELECT * FROM accounts_user'
    query_for_points = 'SELECT * FROM "AgentPoint"'
    query_for_task = 'SELECT * FROM "Task"'
    query_for_task_type = 'SELECT * FROM "TaskType"'

    df_users = pd.read_sql(query_for_users, connection_string)
    df_users = df_users[df_users["role"] == 2]

    df_points = pd.read_sql(query_for_points, connection_string)
    df_task = pd.read_sql(query_for_task, connection_string)
    df_task_type = pd.read_sql(query_for_task_type, connection_string)

    df_points['uuid'] = df_points['uuid'].astype(str)
    df_task['agent_point_id'] = df_task['agent_point_id'].astype(str)
    points_task = pd.merge(df_points, df_task,
                           left_on='uuid', right_on='agent_point_id', how='outer', suffixes=('_x', ''))

    task_distributor = TaskDistributor(points_task, df_users, df_task, df_task_type,
                                       'your_yandex_api',
                                       'your_openroute_api')

    task_distributor.run_distribution()
    connection_string.dispose()

    return



