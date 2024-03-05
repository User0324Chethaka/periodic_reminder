from datetime import datetime, timedelta
from plyer import notification
import json
import sys
import os


def start_msg() -> None:
    notification.notify(
        title = 'Periodic Reminder',
        message = 'Program started',
        timeout = 10
    )


def run_periodic_notification(work_time_: float, rest_time_: float) -> None: 

    start_msg()
    last_run: datetime = datetime.now()

    i: int = 0
    while True:
        work_time = timedelta(minutes=work_time_) # Work time as datetime
        rest_time = timedelta(minutes=rest_time_) # Rest tiem as datetime

        next_run: datetime = last_run + work_time if i % 2 == 0 else last_run +rest_time

        if datetime.now() >= next_run and i % 2 ==0: 
            i += 1
            last_run = datetime.now() # update last time notification was shown
            notification.notify(
                title = 'Periodic Reminder 5 Minure Break',
                message = 'Take a break now', 
                timeout = 10
            )

        elif datetime.now() >= next_run and i % 2 == 1:
            i += 1
            last_run = datetime.now()
            notification.notify(
                title = 'Periodic Reminder Start Work Now', 
                message = 'Break over: start work',
                timeout = 10
            )


def valid_input(input) -> bool: 
    ''' chekc whether given user input is valid'''
    
    if any(e == '' or not e.isdigit() for e in input):
        # raise an error notification
        notification.notify(
            title = "Periodic Reminder WARNING !!!",
            message = 'No invalid input provided\nEXITING PROGRAM\nRerun to activate',
            timeout = 20
        )
        sys.exit()
    else: 
        # valid input 
        return True


def read_input(rel_path: str) -> tuple[str, str]:
    ''' read user input from a json file and return them'''

    script_dir_path: str = os.path.dirname(os.path.abspath(__file__))
    input_file_path: str = os.path.join(script_dir_path, rel_path)

    with open(input_file_path, "r") as jf:
        f = json.load(jf)

    return f.get("work_time"), f.get("rest_time")


def main() -> None:
    user_input_data: tuple = read_input(r"./user_input.json") 

    if valid_input(user_input_data): 
        work_time_min: float = float(user_input_data[0])
        rest_time_min: float = float(user_input_data[1])

    run_periodic_notification(work_time_min, rest_time_min)


if __name__ == '__main__':
    main()
