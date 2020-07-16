import threading

counter = 0


def increase():
    global counter
    while True:
        counter += 1
        print(counter)


for x in range(10):
    thread = threading.Thread(target = increase())
    thread.start()

