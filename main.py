from colorama import Fore, Style, init
from config import APP_NAME, APP_VERSION, DEFAULT_IP 
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


def format_result(ip_obj, info):
    return (
        f"IP address: {ip_obj}\n"
        f"Version: IPv{info['version']}\n"
        f"Private: {info['is_private']}\n"
        f"Global: {info['is_global']}\n"
        f"Loopback: {info['is_loopback']}"
    )

init(autoreset=True)


def main():
    print(Fore.CYAN + f"{APP_NAME} v{APP_VERSION}")
    user_input = input(f"Enter IP address (default: {DEFAULT_IP}): ").strip()

    if not user_input:
        user_input = DEFAULT_IP

    ip_obj = validate_ip(user_input)

    if ip_obj is None:
        print(Fore.RED + "Invalid IP address!")
        return

    info = get_ip_info(ip_obj)
    result = format_result(ip_obj, info)

    print(Fore.GREEN + "\nResult:")
    print(Style.BRIGHT + result)


if __name__ == "__main__":
    main()