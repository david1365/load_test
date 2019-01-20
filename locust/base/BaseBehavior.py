from locust import HttpLocust, TaskSet, task
import locust.stats

class BaseBehavior(TaskSet):

  def on_start(self):
   """ on_start is called when a Locust start before any task is scheduled """
   self.login()

  def on_stop(self):
   """ on_stop is called when the TaskSet is stopping """
   self.logout()

   # def on_request_success(self):
   #      """
   #      Event handler that get triggered on every successful request
   #      """
   #      pass

   def login(self):
    pass
    # self.client.post("/login", {
    #  "username": "test_user",
    #  "password": ""
    # })

   def logout(self):
        pass