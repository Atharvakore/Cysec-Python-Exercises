def bailiwick_check(list_of_answers: list[dict]) -> set:
    res = set()
    for l in list_of_answers:
        s = is_authoritative_response(l)[1]
        for ss in s:
            res.add(ss)
    return res


def is_authoritative_response(data):
    ns = data['nameserver']
    a = data['answers']
    g = data['glue']
    authoritative = False
    for ans in a:
        if ans['RR'] == 'NS' and ans['response'] == ns:
            authoritative = True
            break
    has_glue = False
    for gg in g:
        if gg['RR'] == 'A' and gg['name'] == ns:
            has_glue = True
            break
    ress = set()
    if not (authoritative and has_glue):
        ress.add(ns)
    return authoritative and has_glue, ress


def main():
    la = bailiwick_check([{'nameserver': '29.21.77.217', 'query': {'RR': 'NS', 'name': 'iibiuepontzm.de'},
                           'answers': [{'RR': 'NS', 'name': 'iibiuepontzm.de', 'response': 'nqzig.iibiuepontzm.de'},
                                       {'RR': 'NS', 'name': 'iibiuepontzm.de', 'response': 'qzqbr.giibiuepontzm.de'}],
                           'glue': [{'RR': 'A', 'name': 'nqzig.iibiuepontzm.de', 'response': '166.129.101.38'},
                                    {'RR': 'A', 'name': 'qzqbr.giibiuepontzm.de', 'response': '159.138.116.223'}]},
                          {'nameserver': '102.42.221.240',
                           'query': {'RR': 'NS', 'name': 'eqqazrbittwkfxxkdpyeyvso.org'},
                           'answers': [{'RR': 'NS', 'name': 'eqqazrbittwkfxxkdpyeyvso.org',
                                        'response': 'kopra.eqqazrbittwkfxxkdpyeyvso.org'},
                                       {'RR': 'NS', 'name': 'eqqazrbittwkfxxkdpyeyvso.org',
                                        'response': 'nkyut.aejarocvnlfesrdnh.org'}], 'glue': [
                              {'RR': 'A', 'name': 'kopra.eqqazrbittwkfxxkdpyeyvso.org', 'response': '45.84.91.159'},
                              {'RR': 'A', 'name': 'nkyut.aejarocvnlfesrdnh.org', 'response': '39.243.218.234'}]},
                          {'nameserver': '194.59.242.32',
                           'query': {'RR': 'NS', 'name': 'brfvczpcakadpaiievwpehgojgx.net'}, 'answers': [
                              {'RR': 'NS', 'name': 'brfvczpcakadpaiievwpehgojgx.net',
                               'response': 'ryosf.brfvczpcakadpaiievwpehgojgx.net'},
                              {'RR': 'NS', 'name': 'brfvczpcakadpaiievwpehgojgx.net',
                               'response': 'ooqri.cdieuyxjpchvvvpmkumvhw.net'}], 'glue': [
                              {'RR': 'A', 'name': 'ryosf.brfvczpcakadpaiievwpehgojgx.net', 'response': '90.20.46.118'},
                              {'RR': 'A', 'name': 'ooqri.cdieuyxjpchvvvpmkumvhw.net', 'response': '121.226.183.14'}]},
                          {'nameserver': '237.99.70.200', 'query': {'RR': 'NS', 'name': 'wlvzriorprxcwtoq.de'},
                           'answers': [
                               {'RR': 'NS', 'name': 'wlvzriorprxcwtoq.de', 'response': 'gcidt.wlvzriorprxcwtoq.de'},
                               {'RR': 'NS', 'name': 'wlvzriorprxcwtoq.de', 'response': 'jspsr.lvzriorprxcwtoq.de'}],
                           'glue': [{'RR': 'A', 'name': 'gcidt.wlvzriorprxcwtoq.de', 'response': '114.119.94.3'},
                                    {'RR': 'A', 'name': 'jspsr.lvzriorprxcwtoq.de', 'response': '174.24.153.130'}]},
                          {'nameserver': '252.42.255.5', 'query': {'RR': 'NS', 'name': 'de'},
                           'answers': [{'RR': 'NS', 'response': 'gcidt.wlvzriorprxcwtoq.de'},
                                       {'RR': 'NS', 'response': 'uevts.iiwppmgwec.de'}],
                           'glue': [{'RR': 'A', 'name': 'gcidt.wlvzriorprxcwtoq.de', 'response': '247.161.10.254'},
                                    {'RR': 'A', 'name': 'uevts.iiwppmgwec.de', 'response': '126.6.157.196'}]},
                          {'nameserver': '204.215.121.227',
                           'query': {'RR': 'NS', 'name': 'brfvczpcakadpaiievwpehgojgx.net'}, 'answers': [
                              {'RR': 'NS', 'name': 'brfvczpcakadpaiievwpehgojgx.net',
                               'response': 'ryosf.brfvczpcakadpaiievwpehgojgx.net'},
                              {'RR': 'NS', 'name': 'brfvczpcakadpaiievwpehgojgx.net',
                               'response': 'bjgng.rfvczpcakadpaiievwpehgojgx.net'}], 'glue': [
                              {'RR': 'A', 'name': 'ryosf.brfvczpcakadpaiievwpehgojgx.net', 'response': '111.144.69.75'},
                              {'RR': 'A', 'name': 'bjgng.rfvczpcakadpaiievwpehgojgx.net',
                               'response': '240.87.60.132'}]},
                          {'nameserver': '160.253.14.123',
                           'query': {'RR': 'NS', 'name': 'eqqazrbittwkfxxkdpyeyvso.org'},
                           'answers': [{'RR': 'NS', 'name': 'eqqazrbittwkfxxkdpyeyvso.org',
                                        'response': 'kopra.eqqazrbittwkfxxkdpyeyvso.org'},
                                       {'RR': 'NS', 'name': 'eqqazrbittwkfxxkdpyeyvso.org',
                                        'response': 'dnivc.qqazrbittwkfxxkdpyeyvso.org'}],
                           'glue': [
                               {'RR': 'A', 'name': 'kopra.eqqazrbittwkfxxkdpyeyvso.org', 'response': '56.228.2.33'},
                               {'RR': 'A', 'name': 'dnivc.qqazrbittwkfxxkdpyeyvso.org',
                                'response': '212.88.35.181'}]},
                          {'nameserver': '254.13.136.190', 'query': {'RR': 'NS', 'name': 'de'},
                           'answers': [{'RR': 'NS', 'response': 'nqzig.iibiuepontzm.de'},
                                       {'RR': 'NS', 'response': 'psjgb.zweqajwuqkbkxkhgilqeeiehqlmap.de'}],
                           'glue': [{'RR': 'A', 'name': 'nqzig.iibiuepontzm.de', 'response': '216.117.165.147'},
                                    {'RR': 'A', 'name': 'psjgb.zweqajwuqkbkxkhgilqeeiehqlmap.de',
                                     'response': '125.136.18.171'}]},
                          {'nameserver': '119.136.239.6', 'query': {'RR': 'NS', 'name': 'iibiuepontzm.de'},
                           'answers': [{'RR': 'NS', 'name': 'iibiuepontzm.de', 'response': 'nqzig.iibiuepontzm.de'},
                                       {'RR': 'NS', 'name': 'iibiuepontzm.de', 'response': 'vqcuz.ibiuepontzm.de'}],
                           'glue': [{'RR': 'A', 'name': 'nqzig.iibiuepontzm.de', 'response': '50.169.39.115'},
                                    {'RR': 'A', 'name': 'vqcuz.ibiuepontzm.de', 'response': '141.92.163.146'}]},
                          {'nameserver': '71.121.244.138', 'query': {'RR': 'NS', 'name': 'wlvzriorprxcwtoq.de'},
                           'answers': [
                               {'RR': 'NS', 'name': 'wlvzriorprxcwtoq.de', 'response': 'gcidt.wlvzriorprxcwtoq.de'},
                               {'RR': 'NS', 'name': 'wlvzriorprxcwtoq.de', 'response': 'uevts.iiwppmgwec.de'}],
                           'glue': [{'RR': 'A', 'name': 'gcidt.wlvzriorprxcwtoq.de', 'response': '20.240.156.4'},
                                    {'RR': 'A', 'name': 'uevts.iiwppmgwec.de', 'response': '193.131.101.130'}]},
                          {'nameserver': '214.255.77.241', 'query': {'RR': 'NS', 'name': 'wlvzriorprxcwtoq.de'},
                           'answers': [
                               {'RR': 'NS', 'name': 'wlvzriorprxcwtoq.de', 'response': 'gcidt.wlvzriorprxcwtoq.de'},
                               {'RR': 'NS', 'name': 'wlvzriorprxcwtoq.de', 'response': 'jlfcy.bwlvzriorprxcwtoq.de'}],
                           'glue': [{'RR': 'A', 'name': 'gcidt.wlvzriorprxcwtoq.de', 'response': '57.120.235.247'},
                                    {'RR': 'A', 'name': 'jlfcy.bwlvzriorprxcwtoq.de', 'response': '70.76.90.42'}]},
                          {'nameserver': '244.102.6.229', 'query': {'RR': 'NS', 'name': 'net'},
                           'answers': [{'RR': 'NS', 'response': 'ryosf.brfvczpcakadpaiievwpehgojgx.net'},
                                       {'RR': 'NS', 'response': 'ooqri.cdieuyxjpchvvvpmkumvhw.net'}], 'glue': [
                              {'RR': 'A', 'name': 'ryosf.brfvczpcakadpaiievwpehgojgx.net',
                               'response': '135.49.124.177'},
                              {'RR': 'A', 'name': 'ooqri.cdieuyxjpchvvvpmkumvhw.net', 'response': '145.178.158.121'}]},
                          {'nameserver': '147.120.64.246', 'query': {'RR': 'NS', 'name': 'org'},
                           'answers': [{'RR': 'NS', 'response': 'kopra.eqqazrbittwkfxxkdpyeyvso.org'},
                                       {'RR': 'NS', 'response': 'nkyut.aejarocvnlfesrdnh.org'}], 'glue': [
                              {'RR': 'A', 'name': 'kopra.eqqazrbittwkfxxkdpyeyvso.org', 'response': '160.160.245.96'},
                              {'RR': 'A', 'name': 'nkyut.aejarocvnlfesrdnh.org', 'response': '210.89.85.17'}]},
                          {'nameserver': '43.250.144.147', 'query': {'RR': 'NS', 'name': 'iibiuepontzm.de'},
                           'answers': [{'RR': 'NS', 'name': 'iibiuepontzm.de', 'response': 'nqzig.iibiuepontzm.de'},
                                       {'RR': 'NS', 'name': 'iibiuepontzm.de',
                                        'response': 'psjgb.zweqajwuqkbkxkhgilqeeiehqlmap.de'}],
                           'glue': [{'RR': 'A', 'name': 'nqzig.iibiuepontzm.de', 'response': '85.66.151.7'},
                                    {'RR': 'A', 'name': 'psjgb.zweqajwuqkbkxkhgilqeeiehqlmap.de',
                                     'response': '16.175.221.230'}]},
                          {'nameserver': '85.142.203.115',
                           'query': {'RR': 'NS', 'name': 'eqqazrbittwkfxxkdpyeyvso.org'},
                           'answers': [{'RR': 'NS', 'name': 'eqqazrbittwkfxxkdpyeyvso.org',
                                        'response': 'kopra.eqqazrbittwkfxxkdpyeyvso.org'},
                                       {'RR': 'NS', 'name': 'eqqazrbittwkfxxkdpyeyvso.org',
                                        'response': 'abnfy.ceqqazrbittwkfxxkdpyeyvso.org'}], 'glue': [
                              {'RR': 'A', 'name': 'kopra.eqqazrbittwkfxxkdpyeyvso.org', 'response': '80.246.65.95'},
                              {'RR': 'A', 'name': 'abnfy.ceqqazrbittwkfxxkdpyeyvso.org', 'response': '92.155.236.13'}]},
                          {'nameserver': '68.218.152.102',
                           'query': {'RR': 'NS', 'name': 'brfvczpcakadpaiievwpehgojgx.net'}, 'answers': [
                              {'RR': 'NS', 'name': 'brfvczpcakadpaiievwpehgojgx.net',
                               'response': 'ryosf.brfvczpcakadpaiievwpehgojgx.net'},
                              {'RR': 'NS', 'name': 'brfvczpcakadpaiievwpehgojgx.net',
                               'response': 'acjxl.ubrfvczpcakadpaiievwpehgojgx.net'}], 'glue': [
                              {'RR': 'A', 'name': 'ryosf.brfvczpcakadpaiievwpehgojgx.net',
                               'response': '246.112.72.190'},
                              {'RR': 'A', 'name': 'acjxl.ubrfvczpcakadpaiievwpehgojgx.net',
                               'response': '8.41.64.247'}]}])
    print(la)
    print(la - {'97.29.197.117', '176.102.126.167', '122.245.37.50', '56.77.143.128', '172.232.133.5', '239.161.158.155', '111.109.235.190', '208.123.88.81', '27.205.125.58', '193.134.57.176', '151.8.214.248', '183.121.52.156'})
    print({'97.29.197.117', '176.102.126.167', '122.245.37.50', '56.77.143.128', '172.232.133.5', '239.161.158.155', '111.109.235.190', '208.123.88.81', '27.205.125.58', '193.134.57.176', '151.8.214.248', '183.121.52.156'} - la)

if __name__ == "__main__":
    main()
