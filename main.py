from plyer import notification
from datetime import datetime, timedelta


def main():
    end_point = datetime.now()
    while True:
        now = datetime.now()
        work_time = timedelta(minutes=20)
        rest_time = timedelta(minutes=5)
        if work_time == timedelta(now - end_point):
            end_point += work_time
            notification.notify(
                title = '5 minure break',
                message = 'Take a break now', 
                timeout = 5
            )
        elif rest_time == timedelta(now - end_point):
            end_point += rest_time
            notification.notify(
                title = 'Start work now', 
                message = 'Break over: start work',
                timeout = 5
            )


if __name__ == '__main__':
    main()