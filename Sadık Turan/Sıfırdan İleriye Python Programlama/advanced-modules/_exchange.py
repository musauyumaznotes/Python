import json
import requests

api_url = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=0cd42efba3f56622f5df422121726459&format=1?base=USD")

bozulanDoviz = input("Bozulan Döviz :")
alinanDoviz = input("Alınan Döviz : ")
miktar = int(input(f"ne kadar {bozulanDoviz} bozdurmak istiyorsunuz"))


