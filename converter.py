import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

def get_exchange_rate(base_currency, target_current):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency.upper()}"
    response = requests.get(url)
    print('Status code: ', response.status_code)

    data = response.json()

    if response.status_code != 200 or data.get('result') != 'success':
        raise Exception('Erro ao buscar taxa de cambio!')
    
    rate = data['conversion_rates'].get(target_current.upper())
    if rate is None:
        raise Exception(f'Moeda invalida: {target_current}')
    
    return rate
