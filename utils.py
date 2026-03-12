import ipaddress


def validate_ip(ip_text):
    try:
        return ipaddress.ip_address(ip_text)
    except ValueError:
        return None



