import requests
import json
import os

# URL da API
API_URL = "https://sua-api.manus.space/api/manus/"

# Função para buscar as melhores moradias em Santo Antônio de Jesus, BA
def buscar_moradias():
    try:
        # Parâmetros de consulta (ajustar conforme a API)
        params = {
            "cidade": "Santo Antônio de Jesus",
            "estado": "BA",
            "categoria": "moradias",
            "data": "hoje"
        }

        # Realizando a requisição GET para a API
        response = requests.get(API_URL, params=params)
        
        # Verificando o status da resposta
        if response.status_code == 200:
            print("Consulta bem-sucedida!")

            # Garantir que o diretório de trabalho está correto
            output_path = '/tmp/moradias_santo_antonio.txt'  # Usando um diretório temporário que o GitHub Actions pode acessar

            # Salvando as informações em um arquivo .txt
            with open(output_path, 'w') as file:
                moradias = response.json()  # Supondo que a resposta seja em formato JSON
                
                # Verificando se há resultados
                if moradias:
                    file.write("Melhores Moradias em Santo Antônio de Jesus - BA (Hoje):\n\n")
                    for moradia in moradias:
                        file.write(f"Nome: {moradia.get('nome', 'N/A')}\n")
                        file.write(f"Endereço: {moradia.get('endereco', 'N/A')}\n")
                        file.write(f"Preço: {moradia.get('preco', 'N/A')}\n\n")
                else:
                    file.write("Nenhuma moradia encontrada para hoje.\n")
                    
            print(f"Informações salvas no arquivo: {output_path}")
            # Fazendo upload do arquivo gerado (opcional, caso queira que o arquivo esteja disponível no final do workflow)
            os.rename(output_path, 'moradias_santo_antonio.txt')  # Mover para o diretório do repositório

        else:
            print(f"Falha na requisição. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao conectar com a API: {e}")

# Chamando a função para buscar as moradias
if __name__ == "__main__":
    buscar_moradias()
