import sys
import base64

from flag import FLAG
from hashlib import sha256

def to_int(x):
    return int(x.encode("hex"), 16)

def h(x):
    return to_int(
        sha256(str(x)).digest()
    )

def hmac(x):
    val = to_int(x)
    key = to_int(FLAG)
    tmp = key ^ val
    return h(tmp + val)

def _write(msg):
    sys.stdout.write(str(msg) + "\n")
    sys.stdout.flush()

def _read():
    data = sys.stdin.readline().strip()
    return data

_write("hm4c v1.0 server starting...")

while True:

    _write("Options:")
    _write("1. Request hmac")
    _write("2. Quit")

    try:
        choice = int(_read())
    except:
        break

    if choice == 1:
        _write("Enter data:")
        try:
            data = base64.b64decode(_read())
            _write(hmac(data))
        except Exception as e:
            _write("Not valid Base64.")
    elif choice == 2:
        _write("KBye.")
        break
    else:
        _write("Invalid choice.")
        break

_write("Quitting...")
sys.exit()