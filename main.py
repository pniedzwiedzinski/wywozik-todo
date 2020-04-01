import uuid
import json
import datetime
import requests

import config # config.py file

def add_task(token: str, types: list):
    r = requests.post(
        "https://api.todoist.com/rest/v1/tasks",
        data=json.dumps({
            "content": f"Wynieść śmieci ({', '.join(types)})",
            "due_string": "Today evening",
            "due_lang": "en",
         "priority": 4
     }),
    headers={
        "Content-Type": "application/json",
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": f"Bearer {token}"
    })
    print(r.text)

def get_schedule(city: str, street: str, number: str, housing_type: str) -> dict:
    r = requests.get(f"https://wywozik.pl/widget/goap/schedules?a={city}%7C{street}%7C{number}%7C{housing_type}")
    return r.json()

def generate_calendar(schedule: dict) -> dict:
    """
    This function converts API response into a calendar-like dictionary where date is a key
    and list of trash in given day is a value.
    """
    calendar = {}
    trash_types = schedule[list(schedule.keys())[0]]

    for trash_type, wywoziki in trash_types.items():
        for date in wywoziki['dates']:
            if date in calendar:
                calendar[date].append(trash_type)
            else:
                calendar[date] = [trash_type]
    return calendar

def get_wywozik_for_tomorrow(city: str, street: str, number: str, housing_type: str) -> list:
    """
    Returns list of trash types that will colected tomorrow.
    """
    tomorrow_date = datetime.datetime.now() + datetime.timedelta(days=1)
    tomorrow_formatted_date = tomorrow_date.strftime('%Y-%-m-%-d')
    schedule = get_schedule(city, street, number, housing_type)
    calendar = generate_calendar(schedule)
    try:
        return calendar[tomorrow_formatted_date]
    except KeyError:
        return []

def main():
    options = (config.CITY, config.STREET, config.NUMBER, config.HOUSING)
    types = get_wywozik_for_tomorrow(*options)
    print(types)
    if types:
        add_task(config.TOKEN, types)
    else:
        print("Nothing to do!")

if __name__ == "__main__":
    main()
