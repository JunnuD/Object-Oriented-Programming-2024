import time

class SimpleAlarmClock:
    def __init__(self):
        self.current_time = time.localtime()
        self.alarm_time = None
        self.alarm_status = False
        self.snooze_time = 5  # Default snooze time in minutes
        self.time_format = '%I:%M %p'  # Default time format in 12-hour clock

    def set_alarm(self, hour, minute):
        # Set the alarm time as a tuple (hour, minute)
        self.alarm_time = (hour, minute)

    def toggle_alarm(self):
        # Toggle the alarm status
        self.alarm_status = not self.alarm_status

    def snooze(self):
        if self.alarm_status and self.alarm_time:
            # Snooze the alarm for the specified time
            snooze_minutes = self.snooze_time
            current_hour, current_minute = self.alarm_time
            new_minute = (current_minute + snooze_minutes) % 60
            new_hour = current_hour + (current_minute + snooze_minutes) // 60
            self.alarm_time = (new_hour, new_minute)

    def set_time_format(self, format):
        if format in ['12-hour', '24-hour']:
            # Set the time format
            self.time_format = '%I:%M %p' if format == '12-hour' else '%H:%M'

    def display_time(self):
        # Display the current time in the specified format
        return time.strftime(self.time_format, self.current_time)

    def display_alarm_status(self):
        # Display the alarm status and time if set
        if self.alarm_status:
            return f"Alarm set for {time.strftime('%H:%M', (0, 0, 0, 0, self.alarm_time[0], self.alarm_time[1], 0, 0, -1, -1))}"
        else:
            return "Alarm is currently off."



# Example Usage:
alarm_clock = SimpleAlarmClock()

# Set the alarm for 21:20 (9:20 PM)
alarm_clock.set_alarm(21, 21)

# Toggle the alarm on
alarm_clock.toggle_alarm()

# Display the alarm status
print(alarm_clock.display_alarm_status())

# Display the current time
print("Current Time:", alarm_clock.display_time())

# Snooze the alarm
alarm_clock.snooze()

# Display the updated alarm status
print(alarm_clock.display_alarm_status())
