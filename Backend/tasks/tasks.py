from .algoritm import TaskDistributor
from environs import Env


def send_tasks():
    env = Env()
    env.read_env()
    task_distributor = TaskDistributor('tasks/agent_points.csv',
                                       'tasks/employers.csv',
                                       yandex_api_key=env('API_YANDEX_KEY'),
                                       openroute_api_key=env('API_OPENROUTE_KEY'))
    task_distributor.run_distribution()
    print(env.str('API_OPENROUTE_KEY'))




