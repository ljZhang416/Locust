from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/song/hot?playlistId=2")

    @task(1)
    def about(self):
        self.client.get("/dailySelectionSongs")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000

class MyTaskSet(TaskSet):
    min_wait = 5000
    max_wait = 15000
