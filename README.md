# Управление кафе

В этом файле README.md содержится вся необходимая информация о проекте **Управление кафе**. Здесь вы найдете инструкции по установке, настройке и использованию приложения, а также полезные советы для быстрого старта.

---

## Содержание

1. [Описание проекта](#описание-проекта)
2. [Основные функции](#основные-функции)
3. [Установка и запуск](#установка-и-запуск)
4. [Настройка путей](#настройка-путей)
5. [Использование приложения](#использование-приложения)
6. [Стили и дизайн](#стили-и-дизайн)

---

## Описание проекта

**Управление кафе** — это веб-приложение, разработанное на Django, которое помогает управлять заказами в кафе. Оно позволяет добавлять новые заказы, обновлять их статусы, просматривать активные заказы и генерировать отчеты о выручке.

> Этот проект идеально подходит для небольших кафе или ресторанов, которые хотят автоматизировать процесс управления заказами.

---

## Основные функции

- **Создание заказа**:
  - Добавление нескольких блюд с ценами.
  - Указание номера столика.
- **Просмотр заказов**:
  - Отображение всех активных заказов.
  - Фильтрация заказов по ID, номеру столика или названию блюд.
- **Обновление статуса заказа**:
  - Возможные статусы: "В ожидании", "Готово", "Оплачено".
- **Удаление заказа**:
  - Подтверждение перед удалением.
- **Отчет о выручке**:
  - Просмотр общей выручки.
  - Список оплаченных заказов с детализацией.

---

## Установка и запуск
## Установка зависимостей
Убедитесь, что у вас установлен **Python** и **pip**. Затем установите зависимости

```bash
pip install django
```

### 1. Клонирование репозитория
Для начала склонируйте репозиторий на ваш компьютер:

```bash
git clone https://github.com/example/cafe-orders.git
cd cafe-orders
```

## 2. Применение миграций
Примените миграции для создания базы данных:

```bash
python cafe_orders.py migrate
```

## 3. Запуск сервера
Запустите локальный сервер:

```bash
python cafe_orders.py runserver
```

## 4. Доступ к приложению
Откройте браузер и перейдите по адресу:
```
http://127.0.0.1:8000/
```

## Настройка путей
### 1. Путь к базе данных SQLite
В файле `cafe_orders.py`:

```python
'NAME': r'C:\Users\Костя\PycharmProjects\PythonProject12\cafe_orders\db.sqlite3',
```

Замените этот путь на абсолютный путь, где будет расположена база данных SQLite.
Убедитесь, что путь указан в формате "сырой строки" (с префиксом r), чтобы избежать проблем с экранированием символов.

### 2. Путь к статическим файлам
В файле `cafe_orders.py`:

```python
r'C:\Users\Костя\PycharmProjects\PythonProject12\cafe_orders\static',
```

Замените этот путь на абсолютный путь к папке со статическими файлами в вашей системе.

 # Использование приложения    

## Создание заказа
1. Перейдите на страницу "Добавить заказ".
2. Введите номер столика.
3. Добавьте блюда с ценами (можно добавить несколько).
4. Нажмите **"Сохранить заказ"**.

## Просмотр заказов
- На главной странице отображаются все активные заказы.
- Используйте форму поиска для фильтрации заказов.

## Обновление статуса
- На странице списка заказов выберите новый статус из выпадающего списка.
- Изменения сохраняются автоматически.

## Удаление заказа
- Нажмите значок корзины 🗑️ рядом с заказом.
- Подтвердите удаление.

## Отчет о выручке
- Перейдите на страницу "Финансы".
- Здесь отображается общая выручка и список оплаченных заказов с детализацией.

---

 # Стили и дизайн

## Основные элементы дизайна

Приложение использует современные CSS-стили для улучшения пользовательского интерфейса. Основные элементы дизайна включают:

- **Анимации**: Плавное появление карточек заказов.
- **Адаптивность**: Интерфейс адаптирован для мобильных устройств.
- **Эмоджи индикаторы**: Разные эмоджи для статусов заказов:
  - **В ожидании**: ⏳.
  - **Готово**: ✅.
  - **Оплачено**: 💵.
