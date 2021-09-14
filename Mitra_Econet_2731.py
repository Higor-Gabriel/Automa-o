from selenium import webdriver
import json
from socket import socket
import socket
import time
import re
import paramiko
from paramiko.ssh_exception import AuthenticationException, BadHostKeyException, SSHException

#LEITURA WIZARD INICIAL#

driver = webdriver.Chrome()

def acesso():


    try:
        driver.get('http://192.168.15.1/cgi-bin/sophia_index.cgi')
        driver.maximize_window()
    except:
        driver.maximize_window()
        time.sleep(5)
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
    time.sleep(2)
    config = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[2]/a/span').click()
    time.sleep(2)
    wifi2 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[2]/ul/li[3]').click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
    time.sleep(3)
    login = driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div/table/tbody/tr[2]/td[2]/input').send_keys('admin')
    time.sleep(3)
    password = driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div/table/tbody/tr[5]/td[2]/input').send_keys('69a62b15')
    time.sleep(2)
    entrar = driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div/table/tbody/tr[6]/td/input[2]').click()
    time.sleep(2)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
    time.sleep(2)
    status = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[1]/a').click()
    time.sleep(10)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="basefrm"]'))
    time.sleep(2)
    link = driver.find_element_by_xpath('//*[@id="status"]/tbody/tr[1]/td[1]/div[1]').text
    link = link.replace('\n', ' ')
    potenciaRX = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[1]/td[1]/div[2]').text
    potenciaRX = potenciaRX.replace('\n', ' ')
    potenciaTX = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[1]/td[1]/div[3]').text
    potenciaTX = potenciaTX.replace('\n', ' ')
    internet = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[3]/td[1]/div').text
    internet = internet.replace('\n', ' ')
    botaoInternet = driver.find_element_by_xpath('//*[@id="status"]/tbody/tr[3]/td[2]/a').click()
    time.sleep(2)
    ipv4Local = driver.find_element_by_xpath('//*[@id="internet_v4_table"]/ul/li[1]').text
    ipv4Publico = driver.find_element_by_xpath('//*[@id="internet_v4_table"]/ul/li[2]').text
    Gateway = driver.find_element_by_xpath('//*[@id="internet_v4_table"]/ul/li[3]').text
    dns_Primario = driver.find_element_by_xpath('//*[@id="internet_v4_table"]/ul/li[4]').text
    dns_Secundario = driver.find_element_by_xpath('//*[@id="internet_v4_table"]/ul/li[5]').text
    wifi2_4 = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[5]/td[1]/div').text
    botaoIpv6 = driver.find_element_by_xpath("/html/body/div/div[1]/table/tbody/tr[4]/td[2]/div[1]/ul/li[2]/a").click()
    time.sleep(2)
    prefixo = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[4]/td[2]/div[3]/div[2]/ul/li[1]').text
    ipv6_local = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[4]/td[2]/div[3]/div[2]/ul/li[2]').text
    ipv6_wan = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[4]/td[2]/div[3]/div[2]/ul/li[3]').text
    gateway_ipv6 = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[4]/td[2]/div[3]/div[2]/ul/li[4]').text
    dns_Primario_ipv6 = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[4]/td[2]/div[3]/div[2]/ul/li[5]').text
    dns_Secundario_ipv6 = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[4]/td[2]/div[3]/div[2]/ul/li[6]').text
    wifi2_4 = wifi2_4.replace('\n', ' ')
    wifi5g = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[7]/td[1]/div').text
    wifi5g = wifi5g.replace('\n', ' ')
    lan1 = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[11]/td[1]/div[1]').text
    lan1 = lan1.replace('\n', ' ')
    lan2 = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[11]/td[1]/div[2]').text
    lan2 = lan2.replace('\n', ' ')
    lan3 = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[11]/td[1]/div[3]').text
    lan3 = lan3.replace('\n', ' ')
    hpna = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[11]/td[1]/div[4]').text
    hpna = hpna.replace('\n', ' ')
    tv = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[13]/td[1]/div').text
    tv = tv.replace('\n', ' ')
    rede = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[15]/td[1]/div[1]').text
    rede = rede.replace('\n', ' ')
    telefone = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[15]/td[1]/div[2]').text
    telefone = telefone.replace('\n', ' ')


    status_wizard_json = {
        "info": {
            "Gpon": {
                (link, potenciaRX, potenciaTX)
            },
            "Internet": {
                internet
            },
            "iPv4": {
                "Endereço de Ipv4 local": ipv4Local,
                "Endereço de IPv4 público": ipv4Publico,
                "Gateway Padrao": Gateway,
                "DNS Primário": dns_Primario,
                "DNS Secundário": dns_Secundario

            },
            "IPv6": {
                "Prefixo Delegado": prefixo,
                "Endereço de IPv6 Link-Local - LAN": ipv6_local,
                "Endereço de IPv6 Global - WAN": ipv6_wan,
                "Gateway Padrao": gateway_ipv6,
                "DNS Primário": dns_Primario_ipv6,
                "DNS Secundário": dns_Secundario_ipv6

            },
            "WI-FI 2.4GHZ": {
                wifi2_4
            },
            "WI-FI 5GHZ": {
                wifi5g,
            },
            "Rede Local": {
                (lan1,
                 lan2,
                 lan3,
                 hpna)
            },
            "TV": {
                tv
            },
            "Telefone": {
                (rede,
                 telefone)
            }
        },

        "Result": "OK",
        "Exception": "OK"
    }

    print(status_wizard_json)
    print('=' * 150)



#TROCA USUÁRIO E SENHA WI-FI 2.4#

def wifi1():


    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
    time.sleep(3)
    ssid = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/form/table/tbody/tr[3]/td[2]/input').clear()
    ssid.send_keys('Aut_Mitra')
    time.sleep(3)
    senha = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/form/table/tbody/tr[4]/td[2]/input[1]').clear()
    senha.send_keys('1234567890ab')
    time.sleep(3)
    salvar = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/form/table/tbody/tr[7]/td/a[2]/span').click()

#TROCA USUÁRIO E SENHA WI-FI 5G#


def wifi2():


    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
    time.sleep(2)
    config1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[2]/a/span').click()
    time.sleep(2)
    wifi5 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[2]/ul/li[4]/a').click()
    time.sleep(2)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
    time.sleep(2)
    ssid5 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/form/table/tbody/tr[3]/td[2]/input').clear()
    time.sleep(3)
    ssid5 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/form/table/tbody/tr[3]/td[2]/input').send_keys('aut_mitra5')
    time.sleep(3)
    senha5 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/form/table/tbody/tr[4]/td[2]/input').clear()
    time.sleep(2)
    senha5 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/form/table/tbody/tr[4]/td[2]/input').send_keys('12345678ab')
    time.sleep(2)
    salvar1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/form/table/tbody/tr[7]/td/a[2]').click()
    time.sleep(5)

#CONEXÃO COM O SSH#


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
    'Result': {}

}

saida = comando_ssh.splitlines()

for chave in saida:
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
    regex9 = '(1[0-6]\d{1}\d{3})'
    aux9 = re.search(regex9, chave)
    regex10 = '1[0-9]{5}'
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

print('=' *150)

#SCAN DE PORTAS#

def scan_portas():


     alvo = '192.168.15.1'

     for porta in range(1, 65535):

        client = socket.socket()
        client.settimeout(0.05)
        if client.connect_ex((alvo, porta)) == 0:
            print('Porta Aberta ==>', porta)


def main():
    window_inicial = acesso(), wifi2(),scan_portas()
    print(window_inicial)


if __name__ == '__main__':
    main()