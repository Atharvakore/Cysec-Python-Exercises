def bailiwick_check(list_of_answers: list[dict]) -> set:
    non_authoritative_ips = set()

    # Iterate through each response in the list
    for response in list_of_answers:
        domain = response['query']['name']  # Extract the queried domain

        # Create a dictionary of glue records: nameserver -> IP
        glue_dict = {glue['name']: glue['response'] for glue in response['glue']}

        # Iterate through the answers to check for NS records
        for answer in response['answers']:
            if answer['RR'] == 'NS':
                nameserver = answer['response']  # Extract the nameserver

                # Bailiwick check: nameserver should not end with the queried domain
                if not nameserver.endswith(domain):  # If not authoritative
                    # Now check if this nameserver has a corresponding glue record (IP address)
                    if nameserver in glue_dict:
                        non_authoritative_ips.add(glue_dict[nameserver])  # Add the IP address

    return non_authoritative_ips



def get_non_authoritative_nameservers(response):
    res = set()
    g = {glue['name']: glue['response'] for glue in response['glue']}
    for a in response['answers']:
        if a['RR'] == 'NS':
            ns = a['response']
            if ns in g:
                res.add(g[ns])
    return res


def main():
    l = [{'nameserver': '56.77.143.128', 'query': {'RR': 'NS', 'name': 'gmkqcqoxahz.de'},
          'answers': [{'RR': 'NS', 'name': 'gmkqcqoxahz.de', 'response': 'nofba.gmkqcqoxahz.de'},
                      {'RR': 'NS', 'name': 'gmkqcqoxahz.de', 'response': 'zsagg.xvlqzlqqgtuwspf.de'}],
          'glue': [{'RR': 'A', 'name': 'nofba.gmkqcqoxahz.de', 'response': '225.30.1.150'},
                   {'RR': 'A', 'name': 'zsagg.xvlqzlqqgtuwspf.de', 'response': '138.119.32.145'}]},
         {'nameserver': '172.232.133.5', 'query': {'RR': 'NS', 'name': 'awrkokvuwyxqjcckyjyygtd.de'}, 'answers': [
             {'RR': 'NS', 'name': 'awrkokvuwyxqjcckyjyygtd.de', 'response': 'fqzft.awrkokvuwyxqjcckyjyygtd.de'},
             {'RR': 'NS', 'name': 'awrkokvuwyxqjcckyjyygtd.de', 'response': 'nseyz.wrkokvuwyxqjcckyjyygtd.de'}],
          'glue': [{'RR': 'A', 'name': 'fqzft.awrkokvuwyxqjcckyjyygtd.de', 'response': '45.100.216.139'},
                   {'RR': 'A', 'name': 'nseyz.wrkokvuwyxqjcckyjyygtd.de', 'response': '182.221.94.210'}]},
         {'nameserver': '97.29.197.117', 'query': {'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de'},
          'answers': [{'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de', 'response': 'dblov.ktqylzjthcixpusnjafh.de'},
                      {'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de',
                       'response': 'cimvg.wlouyxspozetylhcpxzpscvbvjmiq.de'}],
          'glue': [{'RR': 'A', 'name': 'dblov.ktqylzjthcixpusnjafh.de', 'response': '173.41.201.30'},
                   {'RR': 'A', 'name': 'cimvg.wlouyxspozetylhcpxzpscvbvjmiq.de', 'response': '135.104.96.17'}]},
         {'nameserver': '66.203.2.91', 'query': {'RR': 'NS', 'name': 'de'},
          'answers': [{'RR': 'NS', 'response': 'nofba.gmkqcqoxahz.de'},
                      {'RR': 'NS', 'response': 'zsagg.xvlqzlqqgtuwspf.de'}],
          'glue': [{'RR': 'A', 'name': 'nofba.gmkqcqoxahz.de', 'response': '250.17.65.213'},
                   {'RR': 'A', 'name': 'zsagg.xvlqzlqqgtuwspf.de', 'response': '84.14.106.59'}]},
         {'nameserver': '235.31.227.87', 'query': {'RR': 'NS', 'name': 'de'},
          'answers': [{'RR': 'NS', 'response': 'fqzft.awrkokvuwyxqjcckyjyygtd.de'},
                      {'RR': 'NS', 'response': 'xxmjf.jpndfnijfozjbsnm.de'}],
          'glue': [{'RR': 'A', 'name': 'fqzft.awrkokvuwyxqjcckyjyygtd.de', 'response': '7.116.157.19'},
                   {'RR': 'A', 'name': 'xxmjf.jpndfnijfozjbsnm.de', 'response': '135.230.4.90'}]},
         {'nameserver': '22.111.99.94', 'query': {'RR': 'NS', 'name': 'de'},
          'answers': [{'RR': 'NS', 'response': 'dblov.ktqylzjthcixpusnjafh.de'},
                      {'RR': 'NS', 'response': 'cimvg.wlouyxspozetylhcpxzpscvbvjmiq.de'}],
          'glue': [{'RR': 'A', 'name': 'dblov.ktqylzjthcixpusnjafh.de', 'response': '106.249.52.115'},
                   {'RR': 'A', 'name': 'cimvg.wlouyxspozetylhcpxzpscvbvjmiq.de', 'response': '48.121.107.154'}]},
         {'nameserver': '111.109.235.190', 'query': {'RR': 'NS', 'name': 'gmkqcqoxahz.de'},
          'answers': [{'RR': 'NS', 'name': 'gmkqcqoxahz.de', 'response': 'nofba.gmkqcqoxahz.de'},
                      {'RR': 'NS', 'name': 'gmkqcqoxahz.de', 'response': 'dkocx.mkqcqoxahz.de'}],
          'glue': [{'RR': 'A', 'name': 'nofba.gmkqcqoxahz.de', 'response': '90.88.92.215'},
                   {'RR': 'A', 'name': 'dkocx.mkqcqoxahz.de', 'response': '29.217.205.31'}]},
         {'nameserver': '239.161.158.155', 'query': {'RR': 'NS', 'name': 'awrkokvuwyxqjcckyjyygtd.de'}, 'answers': [
             {'RR': 'NS', 'name': 'awrkokvuwyxqjcckyjyygtd.de', 'response': 'fqzft.awrkokvuwyxqjcckyjyygtd.de'},
             {'RR': 'NS', 'name': 'awrkokvuwyxqjcckyjyygtd.de', 'response': 'ysqwc.vawrkokvuwyxqjcckyjyygtd.de'}],
          'glue': [{'RR': 'A', 'name': 'fqzft.awrkokvuwyxqjcckyjyygtd.de', 'response': '201.241.13.234'},
                   {'RR': 'A', 'name': 'ysqwc.vawrkokvuwyxqjcckyjyygtd.de', 'response': '48.13.129.178'}]},
         {'nameserver': '208.123.88.81', 'query': {'RR': 'NS', 'name': 'pgycrrxbjl.de'},
          'answers': [{'RR': 'NS', 'name': 'pgycrrxbjl.de', 'response': 'ljlbf.pgycrrxbjl.de'},
                      {'RR': 'NS', 'name': 'pgycrrxbjl.de', 'response': 'bbfgt.gycrrxbjl.de'}],
          'glue': [{'RR': 'A', 'name': 'ljlbf.pgycrrxbjl.de', 'response': '168.207.87.255'},
                   {'RR': 'A', 'name': 'bbfgt.gycrrxbjl.de', 'response': '90.113.129.247'}]},
         {'nameserver': '176.102.126.167', 'query': {'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de'},
          'answers': [{'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de', 'response': 'dblov.ktqylzjthcixpusnjafh.de'},
                      {'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de', 'response': 'djosx.oktqylzjthcixpusnjafh.de'}],
          'glue': [{'RR': 'A', 'name': 'dblov.ktqylzjthcixpusnjafh.de', 'response': '206.193.101.128'},
                   {'RR': 'A', 'name': 'djosx.oktqylzjthcixpusnjafh.de', 'response': '79.143.204.185'}]},
         {'nameserver': '193.134.57.176', 'query': {'RR': 'NS', 'name': 'pgycrrxbjl.de'},
          'answers': [{'RR': 'NS', 'name': 'pgycrrxbjl.de', 'response': 'ljlbf.pgycrrxbjl.de'},
                      {'RR': 'NS', 'name': 'pgycrrxbjl.de', 'response': 'pkpci.ngsaqdehpsw.de'}],
          'glue': [{'RR': 'A', 'name': 'ljlbf.pgycrrxbjl.de', 'response': '217.113.93.31'},
                   {'RR': 'A', 'name': 'pkpci.ngsaqdehpsw.de', 'response': '21.93.214.34'}]},
         {'nameserver': '183.121.52.156', 'query': {'RR': 'NS', 'name': 'pgycrrxbjl.de'},
          'answers': [{'RR': 'NS', 'name': 'pgycrrxbjl.de', 'response': 'ljlbf.pgycrrxbjl.de'},
                      {'RR': 'NS', 'name': 'pgycrrxbjl.de', 'response': 'uxbng.lpgycrrxbjl.de'}],
          'glue': [{'RR': 'A', 'name': 'ljlbf.pgycrrxbjl.de', 'response': '14.85.8.168'},
                   {'RR': 'A', 'name': 'uxbng.lpgycrrxbjl.de', 'response': '156.245.78.14'}]},
         {'nameserver': '151.8.214.248', 'query': {'RR': 'NS', 'name': 'awrkokvuwyxqjcckyjyygtd.de'}, 'answers': [
             {'RR': 'NS', 'name': 'awrkokvuwyxqjcckyjyygtd.de', 'response': 'fqzft.awrkokvuwyxqjcckyjyygtd.de'},
             {'RR': 'NS', 'name': 'awrkokvuwyxqjcckyjyygtd.de', 'response': 'xxmjf.jpndfnijfozjbsnm.de'}],
          'glue': [{'RR': 'A', 'name': 'fqzft.awrkokvuwyxqjcckyjyygtd.de', 'response': '248.168.158.167'},
                   {'RR': 'A', 'name': 'xxmjf.jpndfnijfozjbsnm.de', 'response': '187.71.54.108'}]},
         {'nameserver': '28.20.104.197', 'query': {'RR': 'NS', 'name': 'de'},
          'answers': [{'RR': 'NS', 'response': 'ljlbf.pgycrrxbjl.de'},
                      {'RR': 'NS', 'response': 'pkpci.ngsaqdehpsw.de'}],
          'glue': [{'RR': 'A', 'name': 'ljlbf.pgycrrxbjl.de', 'response': '57.249.184.97'},
                   {'RR': 'A', 'name': 'pkpci.ngsaqdehpsw.de', 'response': '130.226.192.216'}]},
         {'nameserver': '27.205.125.58', 'query': {'RR': 'NS', 'name': 'gmkqcqoxahz.de'},
          'answers': [{'RR': 'NS', 'name': 'gmkqcqoxahz.de', 'response': 'nofba.gmkqcqoxahz.de'},
                      {'RR': 'NS', 'name': 'gmkqcqoxahz.de', 'response': 'mwzqe.lgmkqcqoxahz.de'}],
          'glue': [{'RR': 'A', 'name': 'nofba.gmkqcqoxahz.de', 'response': '105.220.227.197'},
                   {'RR': 'A', 'name': 'mwzqe.lgmkqcqoxahz.de', 'response': '11.194.2.127'}]},
         {'nameserver': '122.245.37.50', 'query': {'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de'},
          'answers': [{'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de', 'response': 'dblov.ktqylzjthcixpusnjafh.de'},
                      {'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de', 'response': 'skkas.tqylzjthcixpusnjafh.de'}],
          'glue': [{'RR': 'A', 'name': 'dblov.ktqylzjthcixpusnjafh.de', 'response': '175.127.225.126'},
                   {'RR': 'A', 'name': 'skkas.tqylzjthcixpusnjafh.de', 'response': '11.84.127.227'}]}]
    d = {
        'nameserver': '122.245.37.50',
        'query': {'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de'},
        'answers': [
            {'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de', 'response': 'dblov.ktqylzjthcixpusnjafh.de'},
            {'RR': 'NS', 'name': 'ktqylzjthcixpusnjafh.de', 'response': 'skkas.tqylzjthcixpusnjafh.de'}
        ],
        'glue': [
            {'RR': 'A', 'name': 'dblov.ktqylzjthcixpusnjafh.de', 'response': '175.127.225.126'},
            {'RR': 'A', 'name': 'skkas.tqylzjthcixpusnjafh.de', 'response': '11.84.127.227'}
        ]
    }
    print(bailiwick_check(l)-{'40.136.187.203', '127.244.122.172', '121.193.244.82', '188.4.226.65', '222.150.34.78', '29.50.78.195', '238.207.199.233', '59.169.134.190', '165.25.135.37', '239.142.95.26', '160.18.46.241', '17.228.180.96'})


if __name__ == "__main__":
    main()
