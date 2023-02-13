import datetime


def log(message):
    time = datetime.datetime.now().strftime('%D %H:%M:%S')

    with open('log.txt', 'a') as file:
        file.write(f"{time} - {message}\n")
