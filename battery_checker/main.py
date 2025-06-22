import time
import psutil
from plyer import notification

# Flags to avoid repeated notifications
high_notified = False
low_notified = False

while True:
    battery = psutil.sensors_battery()
    if battery is None:
        # No battery present
        time.sleep(60)
        continue

    percent = battery.percent
    plugged = battery.power_plugged

    # High battery warning: if charging and >=95% and not already notified
    if plugged and percent >= 95 and not high_notified:
        notification.notify(
            title="Battery Above 95%",
            message="Battery above 95%. Please unplug the charger.",
            timeout=10
        )
        high_notified = True

    # Reset the high-notified flag if battery drops below threshold
    if not plugged or percent < 95:
        high_notified = False

    # Low battery warning: if discharging and <=20% and not already notified
    if not plugged and percent <= 20 and not low_notified:
        notification.notify(
            title="Battery Low (20%)",
            message="Battery at 20%. Please plug in your charger.",
            timeout=10
        )
        low_notified = True

    # Reset the low-notified flag if battery rises above threshold
    if plugged or percent > 20:
        low_notified = False

    time.sleep(60)  # Check every 60 seconds
