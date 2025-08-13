from datetime import datetime, timezone

def get_date():
    now = datetime.now(timezone.utc)
    formatted_time = now.strftime("%d-%m-%Y %H:%M:%S %Z")

    return formatted_time