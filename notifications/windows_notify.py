from win10toast import ToastNotifier
from time import sleep
toaster = ToastNotifier()
while True:
    toaster.show_toast("일미치과의원예약","고속버스예매")
    sleep(60*3)