import subprocess

def is_server_up(ip_address):
    ping_response = subprocess.run(['ping', '-c', '3', ip_address], stdout=subprocess.DEVNULL)
    if ping_response.returncode == 0:
        return True
    else:
        return False

# >>> is_server_up('8.8.8.8')
# True
# >>> is_server_up('192.168.1.1')
# True
# >>> is_server_up('example.com')
# False