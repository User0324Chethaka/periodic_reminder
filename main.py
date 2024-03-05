from plyer import notification
from datetime import datetime, timedelta
import json
import sys


def main():
    user_input_file = r"./user_input.json"
    work_time_min = None #  Time to work in int
    rest_time_min = None #  Time to rest in int
    with open(user_input_file, "r") as jf:
        f = json.load(jf)
        work_time_min = f["work_time"]
        rest_time_min = f["rest_time"]

    # No user input notification / warning 
    if work_time_min == '' or rest_time_min == '':
        notification.notify(
            title = 'WARNING !!!',
            message = 'No user input provided ',
            timeout = 20
        )
        sys.exit()

    end_point = datetime.now()
    while True:
        now = datetime.now()
        work_time = timedelta(minutes=work_time_min) # Work time as datetime
        rest_time = timedelta(minutes=rest_time_min) # Rest tiem as datetime
        if work_time <= now - end_point:
            end_point += work_time
            notification.notify(
                title = '5 minure break',
                message = 'Take a break now', 
                timeout = 10
            )
        elif rest_time <= now - end_point:
            end_point += rest_time
            notification.notify(
                title = 'Start work now', 
                message = 'Break over: start work',
                timeout = 10
            )


if __name__ == '__main__':
    main()
