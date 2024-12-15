from datetime import datetime

actual_time = datetime.now()
timestamp = actual_time.timestamp()
timestamp_formatted = f"{timestamp:,.4f}"
scientific_notation = f"{timestamp:.2e}"
date = actual_time.strftime("%b %d %Y")


print(f"Seconds since January 1, 1970: {timestamp_formatted} or {scientific_notation} in scientific notation")
print(date)