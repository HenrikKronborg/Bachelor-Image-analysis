#!/urs/bin/python
import threading
import time

counter = 0

def lokke():
    print("5delay")
    time.sleep(5)
    print("Fortsetter")

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            if counter < 5:
                counter++
            else:
                counter = 0
            
            print(counter)
            time.sleep(self.interval)

example = ThreadingExample()
time.sleep(10)
print('Checkpoint')
time.sleep(2)
print('Bye')
