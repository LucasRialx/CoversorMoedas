import requests

# Sua chave de API da ExchangeRate-API
API_KEY = '10e98318c902502d7350e9fd'

def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}"
    
    response = requests.get(url)
    data = response.json()
    
    if data['result'] != 'success':
        raise Exception(f"Erro na API: {data.get('error-type', 'Erro desconhecido')}")
    
    return data['conversion_rate']

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * rate
    return converted_amount

def list_currencies():
    # As moedas comuns que vamos considerar na lista
    currencies = {
        "USD": "United States Dollar",
        "EUR": "Euro",
        "GBP": "British Pound Sterling",
        "JPY": "Japanese Yen",
        "BRL": "Brazilian Real",
        "CAD": "Canadian Dollar",
        "AUD": "Australian Dollar",
        "CNY": "Chinese Yuan",
        "INR": "Indian Rupee"
    }
    
    print("Lista de moedas suportadas:")
    for code, name in currencies.items():
        print(f"{code}: {name}")

def main():
    while True:
        print("\n--- Conversor de Moedas ---")
        print("1. Listar moedas suportadas")
        print("2. Fazer uma conversão")
        print("3. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            list_currencies()
        elif choice == '2':
            amount = float(input("Digite o valor que deseja converter: "))
            base_currency = input("Digite a moeda base (ex: USD): ").upper()
            target_currency = input("Digite a moeda alvo (ex: EUR): ").upper()
            
            try:
                converted_amount = convert_currency(amount, base_currency, target_currency)
                print(f"{amount} {base_currency} é igual a {converted_amount:.2f} {target_currency}.")
            except Exception as e:
                print(f"Erro: {e}")
        elif choice == '3':
            print("Fechando a aplicação...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
