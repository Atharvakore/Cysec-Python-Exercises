import hashlib
import struct
import base64
def compute_ds(dnskey: str, owner: str) -> str:
    f = int(dnskey.split(' ', maxsplit=3)[0])
    p = int(dnskey.split(' ', maxsplit=3)[1])
    a = int(dnskey.split(' ', maxsplit=3)[2])
    k = base64.b64decode(dnskey.split(' ', maxsplit=3)[3])
    enc = encode_owner_name(owner)
    pack = struct.pack("!HBB", f, p, a)
    return hashlib.sha256(enc + pack + k).hexdigest()


def encode_owner_name(owner: str) -> bytes:
    res = b''
    for l in owner.split('.'):
        res += len(l).to_bytes(1, 'big') + l.encode()
    return res + b'\x00'

if __name__ == '__main__':
    # let's assume that DE has the correct DS set ;-)
    print(encode_owner_name("cysec1.de") == b'\x06cysec1\x02de\x00')
    print(compute_ds("257 3 8 AwEAAbWUSd/QN9Ae543xzdiacY6qbjwtZ21QfmdgxRdm4Z7bjjHWy249 "
                      "uqxCyjjjoS4LDoRDKmj7ElffMKvTWKE1qFKu0p8TUy4wyhX0M+m5FUjv "
                      "Q3CiZMi+qY7GSHA5B+Zd73cidmnTeb3e8lso6jEsXg05/VZ2AyAqWF6F "
                      "exEIFxIqiwwLk4UP0BwZ17Ur3q1qx9VSbPMyHgQ9d6nHUN1EEJsTDA2v "
                      "0vKumsUyp74ZanRZ/bB/6IzpaaZyr5BLF5pSCNdbRNjVmkwYD0993vm7 "
                      "9LueyOeibsoHRc16jhALrIJou1PFjdq7YQsYN0KtqRiJtaAfPprDBREp eamPuW/MnW0=",
                      "de"))


    assert compute_ds("257 3 8 AwEAAbWUSd/QN9Ae543xzdiacY6qbjwtZ21QfmdgxRdm4Z7bjjHWy249 "
                      "uqxCyjjjoS4LDoRDKmj7ElffMKvTWKE1qFKu0p8TUy4wyhX0M+m5FUjv "
                      "Q3CiZMi+qY7GSHA5B+Zd73cidmnTeb3e8lso6jEsXg05/VZ2AyAqWF6F "
                      "exEIFxIqiwwLk4UP0BwZ17Ur3q1qx9VSbPMyHgQ9d6nHUN1EEJsTDA2v "
                      "0vKumsUyp74ZanRZ/bB/6IzpaaZyr5BLF5pSCNdbRNjVmkwYD0993vm7 "
                      "9LueyOeibsoHRc16jhALrIJou1PFjdq7YQsYN0KtqRiJtaAfPprDBREp eamPuW/MnW0=",
                      "de") == "F341357809A5954311CCB82ADE114C6C1D724A75C0395137AA3978035425E78D".lower()
