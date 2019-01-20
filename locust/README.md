#Maskan Load Testing Tool

### Developement Environment

- Python 2.7, 3.3, 3.4, 3.5, and 3.6. 
- The PyPA(pip) recommended tool for installing Python packages
- latest version of locustio
- IntelliJ IDEA (don't forget to install crack)
- PyDev (Python plug-in provides smart editing for Python scripts In IntelliJ IDEA) 
- An active internet connection.

### Install Python
- Download the latest version https://www.python.org/downloads/ or \\\10.12.47.19\Navaco\Software\python 
- Install And Add '...\Python27' And '...\Python27\Scripts' On The Windows Path

### Install PIP
- Pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4

### Install locustio
 - The easiest way to install Locust is from PyPI, using pip.
 Locust is available on PyPI and can be installed through pip or easy_install
```
> pip install locustio
```

 - When Locust is installed, a locust command should be available in your shell (if you’re not using virtualenv—which you should—make sure your python script directory is on your path).

To see available options, run:
```
locust --help
```

### Quick start

### Example locustfile.py
Below is a quick little example of a simple locustfile.py:
```
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/login", {"username":"ellen_key", "password":"education"})

    def logout(self):
        self.client.post("/logout", {"username":"ellen_key", "password":"education"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/profile")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
```
The Locust class (as well as HttpLocust since it’s a subclass) also allows one to specify minimum and maximum wait time in milliseconds—per simulated user—between the execution of tasks (min_wait and max_wait) as well as other user behaviours. By default the time is randomly chosen uniformly between min_wait and max_wait, but any user-defined time distributions can be used by setting wait_function to any arbitrary function. For example, for an exponentially distributed wait time with average of 1 second:
```
    import random

    class WebsiteUser(HttpLocust):
        task_set = UserBehaviour wait_function = lambda self: random.expovariate(1)*1000



```
###Start Locust
To run Locust with the above Locust file, if it was named locustfile.py and located in the current working directory, we could run:
```
locust --host=http://example.com
```

If the Locust file is located under a subdirectory and/or named different than locustfile.py, specify it using -f:
```
locust -f locust_files/my_locust_file.py --master --host=http://example.com
```
and then we would start an arbitrary number of slave processes:
```
locust -f locust_files/my_locust_file.py --slave --host=http://example.com
```

If we want to run Locust distributed on multiple machines we would also have to specify the master host when starting the slaves (this is not needed when running Locust distributed on a single machine, since the master host defaults to 127.0.0.1):
```
locust -f locust_files/my_locust_file.py --slave --master-host=192.168.0.100 --host=http://example.com
```

###Open up Locust’s web interface
Once you’ve started Locust using one of the above command lines, you should open up a browser and point it to http://127.0.0.1:8089 (if you are running Locust locally).Then you should be greeted with something like this:
![Screenshot](webui-splash-screenshot.png)
###Note:
- To see all available options type: ```locust --help```
- Locust Documentation: https://docs.locust.io/en/latest/ 


