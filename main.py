import requests
import json

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
            
            # Salvando as informações em um arquivo .txt
            with open('moradias_santo_antonio.txt', 'w') as file:
                moradias = response.json()  # Supondo que a resposta seja em formato JSON
                
                # Verificando se há resultados
                if moradias:
                    file.write("Melhores Moradias em Santo Antônio de Jesus - BA (Hoje):\n\n")
                    for moradia in moradias:
                        file.write(f"Nome: {moradia['nome']}\n")
                        file.write(f"Endereço: {moradia['endereco']}\n")
                        file.write(f"Preço: {moradia['preco']}\n\n")
                else:
                    file.write("Nenhuma moradia encontrada para hoje.\n")
                    
            print("Informações salvas no arquivo moradias_santo_antonio.txt.")
        else:
            print(f"Falha na requisição. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao conectar com a API: {e}")

# Chamando a função para buscar as moradias
if __name__ == "__main__":
    buscar_moradias()
