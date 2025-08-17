import requests
import json

# URL da API
API_URL = "https://sua-api.manus.space/api/manus/"

# Função para testar a API
def test_api():
    try:
        # Fazendo uma requisição GET à API
        response = requests.get(API_URL)
        
        # Verificando o status da resposta
        if response.status_code == 200:
            print("Conexão bem-sucedida!")
            print("Resposta da API:")
            print(json.dumps(response.json(), indent=4))  # Exibindo a resposta da API de forma legível
        else:
            print(f"Falha na requisição. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao conectar com a API: {e}")

# Chamando a função para testar a API
if __name__ == "__main__":
    test_api()
