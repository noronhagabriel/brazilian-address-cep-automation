import csv
import requests
import time

def buscar_cep(rua, cidade, estado):
    viacep_url = f"https://viacep.com.br/ws/{estado}/{cidade}/{rua}/json/"
    try:
        response = requests.get(viacep_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return data[0]["cep"]
            else:
                print(f"Nenhum resultado para {rua}, {cidade}-{estado}")
        else:
            print(f"Erro HTTP {response.status_code} para {rua}, {cidade}-{estado}")
    except Exception as e:
        print(f"Erro buscando {rua}, {cidade}-{estado}: {e}")
    return ""


def preencher_ceps(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        leitor = csv.DictReader(infile)
        campos = leitor.fieldnames
        escritor = csv.DictWriter(outfile, fieldnames=campos)
        escritor.writeheader()

        for linha in leitor:
            if not linha['cep']:
                linha['cep'] = buscar_cep(linha['rua'], linha['cidade'], linha['estado'])
                print(f"{linha['rua']} → {linha['cep']}")
                time.sleep(1)
            escritor.writerow(linha)

# Executar
preencher_ceps('enderecos.csv', 'enderecos_com_cep.csv')
