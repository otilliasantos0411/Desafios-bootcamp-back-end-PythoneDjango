import time 

def sync_task(task_id):
    print(f"començando a tarefa {task_id}")
    time.sleep(2)
    print(f"Terminando a tarefa {task_id}")

star_time = time.time()

sync_task(1)
sync_task(2)
sync_task(3)


print(f"tempo decorrido:{time.time() - star_time:.2f}s")