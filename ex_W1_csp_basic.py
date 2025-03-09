def parse_csp(csp_str: str) -> dict[str, set[str]]:
    csp = dict()
    for part in csp_str.split(";"):
        directive, *rest = part.split(" ")
        if not directive or directive in csp:
            continue
        csp[directive] = set(rest)
    return csp


if __name__ == '__main__':
    expected = {'img-src': {
        "'strict-dynamic'", "'unsafe-inline'"}, 'child-src': {
        "'sha384-b9fc4c6cbac88c738abbbd87c0d1bb7bfe3948c8f0a0dec4ddbbbcf5b6cc47c9'", "'strict-dynamic'",
        'http://vfxvnueymlwmrplaw.net'}, 'default-src': {"'unsafe-inline'",
                                                         'https://clvlpokvrjamkauuolmgjtldorpbvd.net',
                                                         'https://tobvyhidplsbcwtidn.org'}}
    parsed_result = parse_csp("img-src 'unsafe-inline' 'strict-dynamic' 'strict-dynamic';img-src "
                              "'nonce-6a5B713406317e82264eb247fa9766d4' 'self' "
                              "'nonce-EFdBdC46bba8CB3Dc6BA86C2D84D0058';child-src "
                              "'sha384-b9fc4c6cbac88c738abbbd87c0d1bb7bfe3948c8f0a0dec4ddbbbcf5b6cc47c9' "
                              "http://vfxvnueymlwmrplaw.net 'strict-dynamic';default-src "
                              "https://clvlpokvrjamkauuolmgjtldorpbvd.net https://tobvyhidplsbcwtidn.org "
                              "'unsafe-inline';child-src 'self' 'unsafe-inline' 'unsafe-eval';")
    assert parsed_result == expected
