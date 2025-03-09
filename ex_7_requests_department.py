import re
import requests


def requests_department(nonce: str) -> str:
    s = requests.Session()
    res = s.get("https://python.cysec1.de/challenges/random_departments", params={"nonce": nonce})
    print(res.text)
    j = res.json()
    r = j['raw_data']
    d = j['department']
    m = 0
    for l in r.split('\n'):
        if l.endswith(f"spent by {d}"):
            ll = l.split()
            if ll[1] == "$":
                m += int(ll[0])
    p = s.post("https://python.cysec1.de/challenges/random_departments", data={"nonce": nonce, "computed_sum": m})
    print(p.text)
    h = p.json()
    return h['hmac']

def main():
    nonce = '#XKxo7Rwbo6#'
    hmac_value = requests_department(nonce)
    print(hmac_value)

if __name__ == "__main__":
    main()