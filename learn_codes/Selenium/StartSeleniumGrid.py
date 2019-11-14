import time
import subprocess
import os
from multiprocessing import Process as p

class Proc():

    processes = []

    @classmethod
    def f(cls, args):
        hub = subprocess.Popen([args])
        cls.processes.append(hub)
        print(args, '->', hub)

    @classmethod
    def stop_process(cls):
        for i in cls.processes:
            os.killpg(os.getpid(i.pid))


if __name__ == '__main__':
    os.chdir("E:\\grid")
#   os.system('dir')
#   hub = subprocess.Popen(['java', '-jar', 'selenium-server-standalone.jar', '-role', 'hub'])

    process_one_hub = p(target=Proc.f, args=('hub.bat',))
    process_one_hub.start()  ##  netstat -ano

    ############
    time.sleep(5)

    process_two_server = p(target=Proc.f, args=('node1.bat',))
    process_two_server.start()

    Proc.stop_process()
