def broad_firewall(
        packet: dict, filter_rules: list, default_policy: str
) -> str:
    pass


if __name__ == '__main__':
    assert (
               broad_firewall({'source_ip': '235.96.66.37', 'dest_ip': '109.79.108.150', 'source_port': 44772,
                               'dest_port': 61952, 'protocol': 'TCP'},
                              [
                                  {'action': 'Allowlist', 'attribute': 'source_port',
                                   'values': [33291, 45070, 77, 65371, 53918]},
                                  {'action': 'Allowlist', 'attribute': 'source_ip',
                                   'values': ['223.244.162.35', '248.133.0.91']}],
                              'Blocked')
           ) == 'Blocked'

    assert (
               broad_firewall({'source_ip': '47.214.17.89', 'dest_ip': '123.167.142.80', 'source_port': 4516,
                               'dest_port': 5842, 'protocol': 'TCP'},
                              [
                                  {'action': 'Blocklist', 'attribute': 'dest_port', 'values': [40990, 14460]},
                                  {'action': 'Blocklist', 'attribute': 'source_port',
                                   'values': [15086, 27748, 785, 24011]}],
                              'Allowed')
           ) == 'Allowed'
