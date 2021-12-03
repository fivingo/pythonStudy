# 15.2 명령 자동화

# 15.2.1 Invoke

from invoke import task
@task

def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Local time is", time_str)
