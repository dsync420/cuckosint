import requests
import folium
import webbrowser
import os
import colorama
from colorama import Fore, init
init()


R = Fore.RED
B = Fore.BLUE 
W = Fore.WHITE
G = Fore.GREEN

def c():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def Menu():
    c()
    # 'Menu'
    print(rf'''{B}
  ___ _   _  ___ _  __
 / __| | | |/ __| |/ /
| (__| |_| | (__| ' <     {W}Made by {G}Marta {W}& {G}C0nixx{B}
 \___|\___/ \___|_|\_\    {R}v1.0.2

{W}
[{B}1{W}] - DNI Lookup          [{B}2{W}] - IP Lookup
[{B}3{W}] - DNI/IP Lookup       [{B}4{W}] - Discord Tools
[{B}5{W}] - Chat                [{B}E{W}] - Exit


    ''')

    x = input(f'{W}user{G}@{W}cuck{B}${W} ')
    if x == '1':
        DNIT()
    elif x == '2':
        IPT()
    elif x == '3':
        DNIIP()
    elif x == '4':
        DiscordTools()
    elif x == '5':
        Chat()
    elif x.strip().lower() in ['e', 'exit']:
        c()
        exit
    else:
        print(f'{R}Invalid Option. {W}Please select {G}1 {W}or {G}2.')
        gback = input('Press any key to go back.')
        Menu()




# SOOOON
# ########################################################################

# OSINT

def DNIIP():
    print()

def DiscordTools():
    print()

def Chat():
    print()



# ########################################################################


def DNIT():
    dni = input('DNI: ')
    api = f"https://clientes.credicuotas.com.ar/v1/onboarding/resolvecustomers/{dni}"
    
    try:
        req = requests.get(api)
        data = req.json()

        if isinstance(data, list) and len(data) > 0:
            cliente = data[0]
            print("\nInformación del cliente:")
            print(f"  NAME            : {cliente.get('nombrecompleto')}")
            print(f"  DNI             : {cliente.get('dni')}")
            print(f"  CUIT            : {cliente.get('cuit')}")
            print(f"  BIRTHDATE       : {cliente.get('fechanacimiento')}")
            print(f"  SEX             : {cliente.get('sexo')}")
            print(f"  DNI             : {cliente.get('dni_calculado')}")
        else:
            print("Invalid DNI.")

        ABC = input('\nGo back to menu?: Y/N: ')
        if ABC.strip().lower() in ['y', 'yes']:
            Menu()
        else:
            c()
            exit()

    except Exception as e:
        print(e)


def IPT():
    ip4 = input('IPv4: ')
    api = 'https://ipinfo.io/' + ip4 + '/json'
    
    try:
        req = requests.get(api)
        data = req.json()
        
        print("\nIP Information:")
        print(f"  IP           : {data.get('ip', 'N/A')}")
        print(f"  Hostname     : {data.get('hostname', 'N/A')}")
        print(f"  City         : {data.get('city', 'N/A')}")
        print(f"  Region       : {data.get('region', 'N/A')}")
        print(f"  Country      : {data.get('country', 'N/A')}")
        print(f"  Postal       : {data.get('postal', 'N/A')}")
        print(f"  Org          : {data.get('org', 'N/A')}")
        print(f"  Hour         : {data.get('timezone', 'N/A')}")
        
        loc = data.get('loc')
        if loc:
            lat, lon = map(float, loc.split(','))
            print(f"  Latitud      : {lat}")
            print(f"  Longitud     : {lon}")

            os.makedirs("maps", exist_ok=True)

            mapa = folium.Map(location=[lat, lon], zoom_start=13)
            folium.Marker([lat, lon], tooltip=f"IP: {ip4}").add_to(mapa)
            filepath = f'maps/{ip4}.html'
            mapa.save(filepath)
            print(f'Map saved at: {filepath}')
        else:
            print("Can not obtain geographical information.")

    except Exception as e:
        print("\n", e)

    ABC = input('\nGo back to menu?: Y/N: ')
    if ABC.strip().lower() in ['y', 'yes']:
        Menu()
    else:
        c()
        exit()



Menu()