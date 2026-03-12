import ipaddress


def validate_ip(ip_text):
    try:
        return ipaddress.ip_address(ip_text)
    except ValueError:
        return None


def get_ip_info(ip_obj):
    return {
        "version": ip_obj.version,
        "is_private": ip_obj.is_private,
        "is_global": ip_obj.is_global,
        "is_loopback": ip_obj.is_loopback,
    }



