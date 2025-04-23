# vk_internship_qa

Этот репозиторий содержит автоматизированные тесты для API Mattermost, покрывающие аутентификацию, управление каналами, пользователями и сообщениями.

## Структура проекта

- `mattermost-api-tests/`
    - `config.py` - конфигурация
    - `test_auth.py` - тесты аутентификации
    - `test_channels.py` - тесты создания канала
    - `test_messages.py` - тесты отправки сообщения
    - `test_users.py` - тесты управления пользователями
- `.gitignore`
- `documentation.md` - документация к тестам
- `report.html` - отчет о пройденных тестах (требует скачивания)
- `requirements.txt` - зависимости


## Использованные технологии
фреймфорк для тестирования **Pytest**

библиотека для HTTP-запросов **Requests**

язык программирования **Python**


## Для запуска тестов

### Предварительные требования (requirements.txt)
- python
- pytest
- requests
- Git

### Шаги
1. Клонируйте репозиторий
```bash
git clone https://github.com/ssonyii/vk_internship_qa.git
```
2. Установите зависимости

предварительно перейдите в папку с файлом requirements.txt
```bash
cd /путь/к/вашему/проекту
```
```bash
pip install -r requirements.txt
```
3. Запустите тесты
``` bash
python -m pytest mattermost_api_tests -v
```