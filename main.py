from plyer import notification
from datetime import datetime, timedelta


def main():
    print('started')
    end_point = datetime.now()
    while True:
        now = datetime.now()
        work_time = timedelta(minutes=20)
        rest_time = timedelta(minutes=5)
        if work_time <= now - end_point:
            print('work break now')
            end_point += work_time
            notification.notify(
                title = '5 minure break',
                message = 'Take a break now', 
                timeout = 10
            )
        elif rest_time <= now - end_point:
            print('break finishes now')
            end_point += rest_time
            notification.notify(
                title = 'Start work now', 
                message = 'Break over: start work',
                timeout = 10
            )


if __name__ == '__main__':
    main()