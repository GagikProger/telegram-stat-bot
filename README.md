<h3>Бот предназначен для сбора статистики с чатов</h3>
<h4>На данный момент функционала не так много, но в будущем планируются обновления</h4> 
<h2>Добавление бота в чат</h2>
Для добавления бота необходимо администратору перейти стартануть бота и добавить его в свой чат. Далее следует написать /add_bot <какое-то_название>

<h2>Какие функции доступны</h2>

```
/mail - главный админ отправляет во все чаты сообщения
/add_bot - админ чата добавляет бота
@<bot_username> - инлайн список из всех каналов базы
```

<h2>Какие данные собираются</h2>
<ul>
<li>Количество активных пользователей</li>
<li>Количество сообщений</li>
<li>Самый активный пользователь</li>
</ul>
<h2>Установка бота</h2>
<h3>Сначала скачаем данные</h3>

```bash
git clone https://github.com/GagikProger/telegram-stat-bot
cd telegram-stat-bot
```

<h3>Далее создаем файл config.py</h3>

```bash
nano config.py
```

<h3>Записываем в файл данные по следующему образцу</h3>

```python
BOT_TOKEN = ''
DB_LOGIN = ''
DB_PASSWORD = ''
DB_HOST = ''
DB_PORT = ''
DB_NAME = ''
ADMINS = [000000000]
```

В ADMINS можно ставить id главных админов (он может сделать рассылку для всех групп)

<h3>Запуск бота</h3>

```bash
python bot.py
```
