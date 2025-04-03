from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Order
import dbm
import json
# def decode_unicode(data):
#     """Декодирует Unicode-последовательности в читаемый текст."""
#     if isinstance(data, str):
#         return data.encode('latin1').decode('utf-8')
#     if isinstance(data, list):
#         return [decode_unicode(item) for item in data]
#     elif isinstance(data, dict):
#         return {key: decode_unicode(value) for key, value in data.items()}
#     elif isinstance(data, str):
#         # Сначала декодируем из байтовой строки (если нужно)
#         try:
#             data = data.encode('latin1').decode('utf-8')
#         except UnicodeError:
#             pass
#         # Затем обрабатываем Unicode-последовательности
#         try:
#             return data.encode('utf-8').decode('unicode_escape')
#         except Exception:
#             return data
#     else:
#         return data
# def get_old_db():
#     return dbm.open('orders_db', 'r')  # Открываем старую базу данных только для чтения


# Представления
# orders/views.py
def order_list(request):
    search_query = request.GET.get('search', '').strip().lower()
    orders = Order.objects.all()

    if search_query:
        filtered_orders = [
            order for order in orders
            if (search_query in str(order.id).lower() or
                search_query in str(order.table_number).lower() or
                any(search_query in item['name'].lower() for item in order.items))
        ]
        orders = filtered_orders

    return render(request, 'order_list.html', {
        'orders': orders,
        'search_query': search_query
    })


# В файле views.py

def migrate_data(request):
    """Мигрирует данные из dbm в SQLite через Django ORM."""
    with get_old_db() as old_db:
        for key in old_db.keys():
            # Считываем байты и декодируем в строку
            raw_data = old_db[key].decode('utf-8')  # Указываем кодировку
            # Парсим JSON безопасным способом
            order_data = json.loads(raw_data)

            # Декодируем Unicode-последовательности в названиях блюд
            items = []
            for item in order_data['items']:
                # Пример: "\\u041f\\u0438\\u0446\\u0430" → "Пицца"
                decoded_name = item['name'].encode('utf-8').decode('unicode_escape')
                items.append({
                    'name': decoded_name,
                    'price': item['price']
                })

            # Сохраняем заказ с нормальными символами
            Order.objects.create(
                table_number=order_data['table_number'],
                items=items,
                status=order_data.get('status', 'В ожидании'),
            )
    return HttpResponse("Данные успешно перенесены из dbm в SQLite!")
def revenue_report(request):
    """Отображает общий объем выручки за заказы со статусом 'Оплачено'."""
    paid_orders = Order.objects.filter(status="Оплачено")
    total_revenue = sum(order.total_price for order in paid_orders)

    return render(request, 'revenue_report.html', {
        'total_revenue': total_revenue,
        'paid_orders': paid_orders
    })


# orders/views.py
def order_create(request):
    """Добавляет новый заказ."""
    if request.method == 'POST':
        table_number = int(request.POST.get('table_number', 0))
        items = []
        dish_count = int(request.POST.get('dish_count', 0))
        for i in range(1, dish_count + 1):
            dish_name = request.POST.get(f'dish_name_{i}', '')
            dish_price = float(request.POST.get(f'dish_price_{i}', 0))
            if dish_name and dish_price > 0:
                items.append({'name': dish_name, 'price': dish_price})
        Order.objects.create(
            table_number=table_number,
            items=items,
            status="В ожидании",
        )
        return redirect('/')
    else:
        return render(request, 'create_order.html')


def update_status(request, order_id):
    """Обновляет статус заказа."""
    if request.method == 'POST':
        new_status = request.POST.get('status', 'В ожидании')
        order = Order.objects.get(id=order_id)
        order.status = new_status
        order.save()
    return HttpResponseRedirect('/')


def order_delete(request, order_id):
    """Удаляет заказ."""
    Order.objects.filter(id=order_id).delete()
    return HttpResponseRedirect('/')

def order_create(request):
    """Добавляет новый заказ."""
    if request.method == 'POST':
        # Получаем данные из формы
        table_number = int(request.POST.get('table_number', 0))
        items = []
        dish_count = int(request.POST.get('dish_count', 0))

        for i in range(1, dish_count + 1):
            dish_name = request.POST.get(f'dish_name_{i}', '')
            dish_price = float(request.POST.get(f'dish_price_{i}', 0))
            if dish_name and dish_price > 0:
                items.append({'name': dish_name, 'price': dish_price})

        # Создаем заказ
        Order.objects.create(
            table_number=table_number,
            items=items,
            status="В ожидании",
        )
        return redirect('/')  # Перенаправляем на главную страницу
    else:
        # Отображаем форму для создания заказа
        return render(request, 'create_order.html')