# Shellshock (CVE-2014-6271) - Уязвимость в OpenSSL, позволяющая читать память сервера и клиента, включая ключи шифрования
import socket
import argparse

def check_vulnerability(args, host):
    # Эмуляция проверки на наличие уязвимости Shellshock
    print(f"[*] Проверка уязвимости Shellshock (CVE-2014-6271) на {host[0]}...")

    # Эмуляция: предположим, что уязвимость обнаружена
    vulnerability_detected = True 

    if vulnerability_detected:
        print(f"[+] Уязвимость Shellshock (CVE-2014-6271) обнаружена на {host[0]}!")
    else:
        print(f"[-] Уязвимость Shellshock (CVE-2014-6271) не обнаружена на {host[0]}.")

    return vulnerability_detected

def testRevShell(args, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Проверка, занят ли порт
    try:
        s.connect((args.LHOST, int(args.LPORT)))
        s.close()
        print(f"\n[-] Не удалось создать Reverse shell: порт {args.LPORT} занят")
        exit()
    except:
        s.close()
        print(f"\n[+] Reverse shell от {host[0]} подключен к [{args.LHOST}:{args.LPORT}].")
        print(f"\n[+] Payload отправлен успешно!")

def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description='Эмуляция реверс-шелла и проверка уязвимости Shellshock (CVE-2014-6271)')
    parser.add_argument('--LHOST', type=str, default='127.0.0.1', help='IP-адрес атакующего')
    parser.add_argument('--LPORT', type=str, default='4444', help='Порт атакующего')
    parser.add_argument('--RHOST', type=str, default='127.0.0.1', help='IP-адрес жертвы')
    args = parser.parse_args()

    # Пример хоста жертвы
    host = (args.RHOST, 80)

    # Проверка на наличие уязвимости
    if check_vulnerability(args, host):
        # Если уязвимость обнаружена, эмулируем отправку реверс-шелла
        testRevShell(args, host)

if __name__ == '__main__':
    main()
