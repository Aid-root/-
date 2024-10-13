import requests


# главная функция с основным кодом программы
def main():
    file_name = input('Файл с ссылками(адрес относительный):\t')
    url = input('URL для поиска:\t')  # здесь записываете url сайта, на котором будете искать директории
    extension = input('Адреса оканчиваются на("/" или ""):\t')

    links = []

    # загружаем все ссылки из файла
    with open('common-files.txt', 'rt') as f:
        links = f.readlines()

    # если ссылок нет, то мы завершаем работу программы
    if len(links) == 0:
        print('Нет ссылок для проверки')
        return

    for link in links:
        # убираем знак переноса строки в конце каждой ссылки
        link = link.replace('\n', '')
        full_link = ''.join((url, link, extension))  # формируем полную ссылку, по которой будут отправлять запросы

        response = requests.get(
            full_link)  # получаем ответ от запроса, скорость запроса будет зависеть от скорости вашего интернет-соединения, тут всё как в браузере

        if response.status_code != 404:  # если вернувшийся ответ не содержит код 404, то значит, такая ссылка существует, и мы можем по ней попасть
            print(f'{full_link} - существует')
            successful_links = open('file.txt', 'a')    #   Создаем файл "file.txt" в которм будем сохранять найденные ссылки
            successful_links.write(full_link + '\n')    #   записываем найденные ссылки в "fail.txt"
            successful_links.close()    #   закрываем файл


if __name__ == "__main__":
    main()
