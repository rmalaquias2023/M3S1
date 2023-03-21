import requests

class FipeIterator:

    def __init__(self, id:str):
        # Desenvolvendo nossa URL com o ID passado
        url = "https://parallelum.com.br/fipe/api/v1/carros/marcas/{}/modelos"
        url = url.format(id)

         # Obtendo informações da API através do método GET
        response = requests.get(url, headers=headers)

        # Salvando a resposta da API
        carros = response.json()
        
        # Obtendo valores para o Dict `modelos`
        self.modelos = carros['modelos']
        
        # Instanciando nosso estado atual e final
        self.current = 0
        self.end = len(self.modelos)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.modelos[self.current]
        self.current += 1
        return result
 

# Instanciando a URL e o User-Agent
url_marcas = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
headers = {
    "User-Agent": "MyApp/1.0"
}

# Obtendo informações da API através do método GET
response = requests.get(url_marcas, headers=headers)

# Salvando a resposta da API
marcas = response.json()

for marca in marcas:
    print("Marca:", marca["nome"], "Codigo:", marca["codigo"])


id = input('Qual o codigo da marca que você deseja listar?')
iterator = FipeIterator(id) 

for modelo in iterator:
    print(modelo)




