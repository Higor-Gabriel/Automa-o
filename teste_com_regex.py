import json
from socket import socket
import time
import re
import paramiko
from paramiko.ssh_exception import AuthenticationException, BadHostKeyException, SSHException


def connectSSH(ip, username, password):
    global channel
    result = {
        'connection': '',
        'status': '',
        'exception': ''
    }

    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=username, password=password, timeout=5, allow_agent=False,
                    look_for_keys=False, banner_timeout=30)

        channel = ssh.invoke_shell()
        result['connection'] = channel
        result['status'] = 'OK'
        result['exception'] = ''

    except AuthenticationException as error:
        result = {'connection': 'channel_NOK', 'status': 'NOK', 'exception': 'VERIFIQUE SENHA INSERIDA'}

    except socket.timeout as error:
        result = {'connection': 'channel_NOK', 'status': 'NOK', 'exception': 'VERIFIQUE CABO DESCONETADO'}

    except SSHException as error:
        result = {'connection': 'channel_NOK', 'status': 'NOK', 'exception': error}

    except BadHostKeyException as error:
        result = {'connection': 'channel_NOK', 'status': 'NOK', 'exception': 'VERIFIQUE HOST SERVER KEY'}

    except Exception as error:
        result = {'connection': 'channel_NOK', 'status': 'NOK', 'exception': error}

    finally:
        try:
            if result['status'] == 'NOK':
                channel.transport.close()
                channel.close()
            return result
        except:
            return result
            pass


###Método para enviar e recebre comandos enviados ao HGU
def send_and_get_command(channel, cmd, sleep=2):
    try:

        bufsize = 65000
        if not cmd.endswith("\n"):
            cmd += "\n"
        channel.send(cmd)
        # results = get_command_results(channel)
        time.sleep(sleep)
        results = channel.recv(bufsize)
        results = results.decode('unicode_escape')

    except Exception as error:
        results = 'NOK'

    return results


login_ssh = connectSSH('192.168.15.1', 'support', '69a62b15')

comando_ssh = send_and_get_command(login_ssh['connection'], 'ifconfig')

saida_json = {
    "Interface": {},
    "Link Encap": {},
    "MAC": {},
    "Bcast": {},
    "Mask": {},
    "inet addr": {},
    "Ip Wan": {},
    "IPV6": {},
    "MTU": {},
    "RX packets": {},
    "TX packets": {},
    'Result': {},
    'Exception': {}
}

saida = comando_ssh.splitlines()

for chave in saida:
    print(chave)
    regex = '^[b-s]{2}[0-1]{1}'
    aux = re.search(regex, chave)
    regex2 = '[A-E]{1}[a-z]{7}'
    aux2 = re.search(regex2, chave)
    regex3 = '(([1-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2})'
    aux3 = re.search(regex3, chave)
    regex4 = '(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,7}:([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'
    aux4 = re.search(regex4, chave)
    regex5 = '[0-9]{3}\.?[0-9]{3}\.?[2{1}5]{3}\.?[0]'
    aux5 = re.search(regex5, chave)
    regex6 = '(1[2-9]{2})\.[1-9]{3}\.([1-5]{2}\.1)'
    aux6 = re.search(regex6, chave)
    regex7 = '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    aux7 = re.search(regex7, chave)
    regex8 = '[2]+[0+]{3}'
    aux8 = re.search(regex8, chave)
    regex9 = '(1[5]\d{1}\d{3})'
    aux9 = re.search(regex9, chave)
    regex10 = '(1[0-9]{5})'
    aux10 = re.search(regex10, chave)
    regex11 = '(1[2-9]{2})\.[1-9]{3}\.([1-5]{2}\.[2-5]{3})'
    aux11 = re.search(regex11, chave)
    aux12 = 'OK'

    if aux:
        saida_json["Interface"] = aux.group()
    elif aux2:
        saida_json["Link Encap"] = aux2.group()
        if aux3:
            saida_json["MAC"] = aux3.group()
    elif aux4:
        saida_json["IPV6"] = aux4.group()
    elif aux5:
        saida_json["Mask"] = aux5.group()
        if aux6:
            saida_json["inet addr"] = aux6.group()
    elif aux7:
        saida_json["Ip Wan"] = aux7.group()
    elif aux8:
        saida_json["MTU"] = aux8.group()
    elif aux9:
        saida_json["RX packets"] = aux9.group()
    elif aux10:
        saida_json["TX packets"] = aux10.group()
    if aux11:
        saida_json["Bcast"] = aux11.group()
    elif aux12:
        saida_json["Result"] = aux12

print(saida_json)
