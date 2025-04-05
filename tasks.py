from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672')

@app.task
def add(x, y):
    return x + y

def print_hello_func(name):
    print(f"Hello {name}")
    return f"Hello {name}"

@app.task
def print_hello(name):
    return print_hello_func(name)

def create_hello_file(filename, text):
    with open(f"{filename}.txt", "w") as f_h:
        res = f_h.write(text)
        print(f"File {filename} successfully created")
        return res

@app.task
def create_new_file(filename, text):
    print(f"New file {filename} created")
    return create_hello_file(filename, text)
