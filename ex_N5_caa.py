def check_inside(dns_response: dict, current_domain: str, caa_type: str, ca: str) -> bool | None:
    if caa_type in dns_response[current_domain]:
        return ca in dns_response[current_domain][caa_type]
    return None


def certificate_issuance_allowed(domain: str, ca: str, dns_responses: dict) -> bool:
    labels_parts = domain.split(".")
    if labels_parts[0] == "*":
        # wildcard, check for both issue and issuewild
        labels_parts.pop(0)
        caa_types = ["issuewild", "issue"]
    else:
        caa_types = ["issue"]
    while len(labels_parts) > 1:
        current_domain = ".".join(labels_parts)
        if current_domain in dns_responses:
            for caa_type in caa_types:
                check_value = check_inside(dns_responses, current_domain, caa_type, ca)
                if check_value is not None:
                    return check_value
        else:
            labels_parts.pop(0)
    return True


if __name__ == '__main__':
    dns_responses = {'sub.cysec1.de':
                         {'issue': ['letsencrypt', 'dfn'],
                          'issuewild': ['letsencrypt']
                          },
                     'sub2.cysec1.de': {
                         'issuewild': ['letsencrypt'],
                         'issue': [';']
                     },
                     'cysec1.de': {
                         'issue': [';']
                     }
                     }
    assert certificate_issuance_allowed("*.sub.cysec1.de", "dfn", dns_responses) is False
    assert certificate_issuance_allowed("sub2.cysec1.de", "letsencrypt", dns_responses) is False
