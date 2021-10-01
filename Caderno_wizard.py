from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

driver = webdriver.Chrome()
try:
    driver.get('http://192.168.15.1/cgi-bin/sophia_index.cgi')
    driver.maximize_window()
except:
    driver = webdriver.Firefox()
    driver.maximize_window()
# Teste 373 - Acesso ao wizard

driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
time.sleep(2)
config = driver.find_element_by_xpath('//*[@id="MLG_Menu_Settings"]').click()
time.sleep(2)
wifi2 = driver.find_element_by_xpath('//*[@id="MLG_Menu_Wireless"]').click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
time.sleep(2)
usuario = driver.find_element_by_xpath('//*[@id="Loginuser"]').send_keys('admin')
time.sleep(2)
senha = driver.find_element_by_xpath('//*[@id="LoginPassword"]').send_keys('69a62b15')
time.sleep(2)
entrar = driver.find_element_by_xpath('//*[@id="acceptLogin"]').click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
status = driver.find_element_by_xpath('//*[@id="wizardMLG"]').click()

#Teste 374 botão logout
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
sair = driver.find_element_by_xpath('//*[@id="header-gateway"]/div[1]/p/a[3]').click()
#Teste 375 - (campo gpon(link))

time.sleep(10)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
link = driver.find_element_by_xpath('//*[@id="status"]/tbody/tr[1]/td[1]/div[1]').text
print(link)
#Teste -376 - user em branco

time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
configuracao = driver.find_element_by_xpath('//*[@id="MLG_Menu_Settings"]').click()
time.sleep(2)
internet = driver.find_element_by_xpath('//*[@id="MLG_Menu_Internet"]').click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
time.sleep(2)
usuario1 = driver.find_element_by_xpath('//*[@id="Loginuser"]').send_keys('admin')
time.sleep(2)
senha1 = driver.find_element_by_xpath('//*[@id="LoginPassword"]').send_keys('69a62b15')
time.sleep(2)
entrar1 = driver.find_element_by_xpath('//*[@id="acceptLogin"]').click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
time.sleep(2)
usuario_ppoe = driver.find_element_by_xpath('//*[@id="RN_UserName"]').clear()
time.sleep(2)
salvar = driver.find_element_by_xpath('//*[@id="PPPOE_Account_Save"]').click()
time.sleep(10)
for i in range(0,5):
    try:
        click_alert = driver.switch_to.alert
        click_alert.accept()
        continue
    except TimeoutException:
        print()
    except NoAlertPresentException:
        print()
#Teste 377/378 - conta invalida

usuario_ppoe = driver.find_element_by_xpath('//*[@id="RN_UserName"]').send_keys('higor@higor')
time.sleep(2)
senha_ppoe = driver.find_element_by_xpath('//*[@id="RN_Password"]').clear()
time.sleep(2)
senha_ppoe1 = driver.find_element_by_xpath('//*[@id="RN_Password"]').send_keys('higor')
time.sleep(2)
salvar = driver.find_element_by_xpath('//*[@id="conteudo-gateway"]/table/tfoot/tr/td/a[2]').click()
time.sleep(30)
iframe = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/iframe')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td/a').click()
time.sleep(20)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
logout = driver.find_element_by_xpath('//*[@id="header-gateway"]/div[1]/p/a[3]').click()
time.sleep(3)
#TESTE 379 - HTTPS BLOQUEADO

try:
    driver.get('https://192.168.15.1/cgi-bin/sophia_index.cgi')
except Exception as erro:
    print()
time.sleep(10)

#TESTE 380 - INFOS SEM LOGIN
try:
    driver.get('http://192.168.15.1/cgi-bin/sophia_index.cgi')
except Exception as erro:
    print()
#Teste 381/382 - Possível edição com login e Idioma padrão

time.sleep(3)
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
time.sleep(2)
gerenciamento = driver.find_element_by_xpath('//*[@id="MLG_Menu_Management"]').click()
time.sleep(2)
idioma = driver.find_element_by_xpath('//*[@id="MLG_Menu_Language"]').click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
time.sleep(2)
usuario = driver.find_element_by_xpath('//*[@id="Loginuser"]').send_keys('admin')
time.sleep(2)
senha = driver.find_element_by_xpath('//*[@id="LoginPassword"]').send_keys('69a62b15')
time.sleep(2)
entrar = driver.find_element_by_xpath('//*[@id="acceptLogin"]').click()

#Teste 384 - ping

time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
geren = driver.find_element_by_xpath('//*[@id="MLG_Menu_Management"]').click()
time.sleep(2)
ferramentas= driver.find_element_by_xpath('//*[@id="MLG_Menu_Utilities"]').click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
destino = driver.find_element_by_xpath('//*[@id="diagAddr"]').send_keys('8.8.8.8')
time.sleep(2)
tentativas = driver.find_element_by_xpath('//*[@id="diagPingNum"]').send_keys('4')
time.sleep(2)
executar = driver.find_element_by_xpath('//*[@id="tab-01"]/table/tbody[1]/tr[4]/td/a[2]').click()
time.sleep(20)
#Teste 386 - status wifi 2.4 e 5g
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
status = driver.find_element_by_xpath('//*[@id="accordion"]/li[1]/a').click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
wifi2_4 = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[5]/td[1]/div').text
wifi2_4 = wifi2_4.replace('\n', ' ')
print(wifi2_4)
time.sleep(3)
wifi5g = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[7]/td[1]/div').text
wifi5g = wifi5g.replace('\n', ' ')
print(wifi5g)
time.sleep(3)
status_ppp = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[3]/td[1]/div').text
status_ppp - status_ppp.replace('\n', ' ')
print(status_ppp)
time.sleep(3)
telefone = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[15]/td[1]/div[2]').text
telefone = telefone.replace('\n', ' ')
print(telefone)
time.sleep(3)
hpna = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[11]/td[1]/div[4]').text
hpna = hpna.replace('\n', ' ')
print(hpna)
#Teste 392 - DNS
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[1]'))
confi = driver.find_element_by_xpath('//*[@id="setmenu"]').click()
time.sleep(3)
rede = driver.find_element_by_xpath('//*[@id="accordion"]/li[2]/ul/li[2]').click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frameset/frameset/frame[2]'))
habilitar = driver.find_element_by_xpath('//*[@id="input_dns"]').click()
time.sleep(5)
desabilitar = driver.find_element_by_xpath('//*[@id="input_dns"]').click()




