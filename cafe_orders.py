import sys
from django.conf import settings
from django.urls import path, include
from django.apps import apps
from django.core.management import execute_from_command_line

# Настройки Django
settings.configure(
    DEBUG=True,
    SECRET_KEY='secret_key_for_mvp',
    ROOT_URLCONF=__name__,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': r'C:\Users\Костя\PycharmProjects\PythonProject12\cafe_orders\db.sqlite3',  # Файл базы данных SQLite
        }
    },
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'orders.apps.OrdersConfig',  # Добавляем наше приложение
    ],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],  # Шаблоны будут искаться в папках приложений
            'APP_DIRS': True,
        },
    ],
    STATIC_URL='/static/',  # Настройка статических файлов
    STATICFILES_DIRS=[
        r'C:\Users\Костя\PycharmProjects\PythonProject12\cafe_orders\static',  # Путь к статическим файлам
    ],
)

# Инициализация приложений
apps.populate(settings.INSTALLED_APPS)

# Маршруты
urlpatterns = [
    path('', include('orders.urls')),  # Включаем маршруты из приложения orders
]

# Запуск приложения
if __name__ == '__main__':
    from django.core.management import call_command
    call_command('makemigrations', 'orders')  # Создаем миграции для приложения orders
    call_command('migrate')  # Применяем миграции
    execute_from_command_line(sys.argv)