from celery import Celery

app = Celery(
    "tasks",
    broker="amqps://ngoclinh8123:Ngoclinh08012003@b-af1001fb-b5ff-43fd-80b3-a4afffd06f8f.mq.ap-southeast-2.amazonaws.com:5671",
)


@app.task
def say():
    return "hello celery"
