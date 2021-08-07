import time
from plyer import notification # we should install from out source using pip install

if __name__ == '__main__':
    while True:
        notification.notify(
            title=" guide : માર્ગદર્શન",
            message="a person who advises or shows the way to others.",
            #app_icon="path to your .ico file",
            timeout=10
        )
        time.sleep(20)
        notification.notify(
            title=" unique : અનન્ય",
            message="not like anything else; being the only one of its type.",
            # app_icon="path to your .ico file",
            timeout=5
        )
        time.sleep(30)