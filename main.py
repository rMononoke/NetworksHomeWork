from colorama import Fore, Style, init
from config import APP_NAME, APP_VERSION, DEFAULT_IP
from utils import validate_ip, get_ip_info, format_result

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
