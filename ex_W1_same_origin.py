def same_origin(url1: str, url2: str) -> bool:
    proto_1, _, hostname_with_port_1, _ = url1.split("/")
    proto_2, _, hostname_with_port_2, _ = url2.split("/")

    if proto_1.lower() == proto_2.lower():
        # trivial case
        if hostname_with_port_1 == hostname_with_port_2:
            return True
        # same hostname, but one has a port
        if ":" in hostname_with_port_1:
            hostname_1, port_1 = hostname_with_port_1.split(":")
            port_1 = int(port_1)
        else:
            port_1 = 443 if proto_1.lower() == 'https:' else 80
            hostname_1 = hostname_with_port_1

        if ":" in hostname_with_port_2:
            hostname_2, port_2 = hostname_with_port_2.split(":")
            port_2 = int(port_2)
        else:
            port_2 = 443 if proto_2.lower() == 'https:' else 80
            hostname_2 = hostname_with_port_2

        return hostname_1 == hostname_2 and port_1 == port_2
    # if protocols mismatch, return False
    return False