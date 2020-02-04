# QA-Python
Курс "Python QA Engineer"

Тестирование API:
1) test_api_dog.py 
    - Тестирование: https://dog.ceo/api 
    - Запуск тестов: pytest test_api_dog.py --url=dog
    
2) test_api_brewerydb.py 
    - Тестирование: https://api.openbrewerydb.org
    - Запуск тестов: pytest test_api_brewerydb.py --url=brewery
    
3) test_api_placeholder.py 
    - Тестирование: https://jsonplaceholder.typicode.com
    - Запуск тестов: pytest test_api_placeholder.py --url=placeholder -s
    
2) test_api_ya.py 
    - Тестирование: https://jsonplaceholder.typicode.com
    - Запуск тестов: pytest test_api_ya.py --url=ya.ru --status_code==404 -s
