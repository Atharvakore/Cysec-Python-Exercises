import struct


def unpack_ip(ip: str) -> int:
    return sum([int(octet) << (3 - i) * 8 for i, octet in enumerate(ip.split("."))])


def calculate_tcp_checksum(segment: bytes, ip_sender, ip_receiver) -> int:
    # Pseudo Header: Sender IP, Recv. IP, 0, Proto (6), TCP Length
    ip_sender = struct.pack("!I", unpack_ip(ip_sender))
    ip_receiver = struct.pack("!I", unpack_ip(ip_receiver))
    pseudo_header = ip_sender + ip_receiver + b"\x00" + b"\x06" + struct.pack("!H", len(segment))
    checksum = 0

    # skip original checksum
    to_checksum = pseudo_header + segment[:16] + segment[18:]
    for offset in range(0, len(to_checksum), 2):
        checksum = (checksum + (to_checksum[offset] << 8) + to_checksum[offset + 1])
    # add the carry bits
    checksum += (checksum >> 16)
    checksum = ~checksum & 0xffff
    return checksum

def main() -> None:
    segment = b'\xe3}\x01\xbb\xd9:\xde\xfb\xef\xf8 \xb9\x80\x10\x08\x00\x00\x00\x00\x00\x01\x01\x08\n\xff:bx\xf2\xee\xc7U'
    ip_sender = "192.168.2.151"
    ip_receiver = "18.165.227.57"

    assert calculate_tcp_checksum(segment, ip_sender, ip_receiver) == 0xeb85


if __name__ == '__main__':
    main()
