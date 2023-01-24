from telebot import types

admin = types.InlineKeyboardMarkup(row_width=2)
admin.add(
    types.InlineKeyboardButton('Рассылка', callback_data='admin_msg'),
    types.InlineKeyboardButton('Сообщение пользователю', callback_data='admin_msg_user'),
    types.InlineKeyboardButton('Статистика', callback_data='statistics'),
    types.InlineKeyboardButton('Выгрузка БД', callback_data='subd'),
    types.InlineKeyboardButton('Логи', callback_data='logging')
)

menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
deliv_q = types.InlineKeyboardButton('Вопрос по заказу', callback_data='deliv_q')
table_menu = types.InlineKeyboardButton('Вопрос по окрашиванию', callback_data='table')
safe_menu = types.InlineKeyboardButton('Безопасность', callback_data='safe_menu')
contacts_menu = types.InlineKeyboardButton('Контакты', callback_data='instructions')
partner_menu = types.InlineKeyboardButton('Сотрудничество', callback_data='partner')
menu.add(deliv_q)
menu.add(table_menu)
# menu.add(safe_menu)
menu.add(contacts_menu, safe_menu)
menu.add(partner_menu)


make_order = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
search_ord = types.InlineKeyboardButton('Как отследить заказ', callback_data='search_ord')
transfer_ord = types.InlineKeyboardButton('Условия доставки', callback_data='transfer_ord')
web_ord = types.InlineKeyboardButton('Сайт', callback_data='web_ord')
help_ord = types.InlineKeyboardButton('Нужна консультация по продукту', callback_data='help_ord')
back = types.InlineKeyboardButton('Назад', callback_data='back')
make_order.add(search_ord, transfer_ord)
make_order.add(help_ord)
make_order.add(back, web_ord)


info_deliv = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
info_deliv.add(
types.InlineKeyboardButton('Доставка в РФ'),
types.InlineKeyboardButton('Международная доставка'),
types.InlineKeyboardButton('Назад')
)


instructions = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
instructions.add(
types.InlineKeyboardButton('Инструкция', callback_data='instr'),
types.InlineKeyboardButton('Мастерклассы', callback_data='masterclass'),
types.InlineKeyboardButton('Назад', callback_data='back')
)

call_drop = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
call_drop.add(
types.InlineKeyboardButton('Сотрудничество'),
types.InlineKeyboardButton('Все контакты'),
types.InlineKeyboardButton('Назад', callback_data='back'),
types.InlineKeyboardButton('Сайт')
)

partner_d = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
partner_d.add(
types.InlineKeyboardButton('Условия сотрудничества'),
types.InlineKeyboardButton('Связаться с менеджером'),
types.InlineKeyboardButton('Назад', callback_data='back')
)


buy_choice = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
buy_choice.add(
types.InlineKeyboardButton('Онлайн'),
types.InlineKeyboardButton('Офлайн'),
types.InlineKeyboardButton('Назад')
)


buy_d = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
buy_d.add(
types.InlineKeyboardButton('Сайт'),
types.InlineKeyboardButton('Озон'),
types.InlineKeyboardButton('Вайлдберриз'),
types.InlineKeyboardButton('Яндекс Маркет'),
types.InlineKeyboardButton('Назад', callback_data='back')
)


deliv_quesch = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
make_ord_q = types.InlineKeyboardButton('Хочу сделать заказ')
payd_ord_q = types.InlineKeyboardButton('Оплатил заказ, а на почте отображается «не оплачен»')
where_ord_q = types.InlineKeyboardButton('Где мой заказ?')
give_ord_q = types.InlineKeyboardButton('Вы получили мой заказ? Когда он будет отправлен?')
fast_ord_q = types.InlineKeyboardButton('Заказ нужен срочно')
problem_ord_q = types.InlineKeyboardButton('Проблема с заказом')
samov_ord_q = types.InlineKeyboardButton('Самовывоз')
prob_site_ord_q = types.InlineKeyboardButton('Проблема на сайте, проблема с заказом')
back = types.InlineKeyboardButton('Назад', callback_data='back')
deliv_quesch.add(make_ord_q, where_ord_q)
deliv_quesch.add(payd_ord_q)
deliv_quesch.add(fast_ord_q, problem_ord_q, samov_ord_q)
deliv_quesch.add(give_ord_q)
deliv_quesch.add(prob_site_ord_q)
deliv_quesch.add(back)

deliv_quesch_make = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
deliv_quesch_make.add(
types.InlineKeyboardButton('Как отследить заказ'),
types.InlineKeyboardButton('Посмотреть условия доставки'),
types.InlineKeyboardButton('Нужна консультация по продукту и ассортименту'),
types.InlineKeyboardButton('Назад', callback_data='back'),
)

color_q = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
table_color = types.InlineKeyboardButton('Таблица распада красителей')
instr_color = types.InlineKeyboardButton('Инструкции и мастер-классы')
how_color = types.InlineKeyboardButton('Как окрашивать?')
how2_color = types.InlineKeyboardButton('Как ухаживать за окрашенной вещью?')
mix_color = types.InlineKeyboardButton('Можно смешивать цвета?')
textil_color = types.InlineKeyboardButton('Какой текстиль можно окрашивать?')
activator_color = types.InlineKeyboardButton('Что такое активатор и зачем он нужен?')
back = types.InlineKeyboardButton('Назад', callback_data='back')
color_q.add(table_color)
color_q.add(instr_color)
color_q.add(how_color, mix_color)
color_q.add(how2_color)
color_q.add(textil_color)
color_q.add(activator_color)
color_q.add(back)


contacts = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
contacts.add(
types.InlineKeyboardButton('Связаться с DROP'),
types.InlineKeyboardButton('Где купить'),
types.InlineKeyboardButton('Назад'),
)


buy_offline_choice = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
buy_offline_choice.add(
types.InlineKeyboardButton('РФ'),
types.InlineKeyboardButton('Другие страны'),
types.InlineKeyboardButton('Назад'),
)


buy_offline_city = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
buy_offline_city.add(
types.InlineKeyboardButton('Москва'),
types.InlineKeyboardButton('Санкт-Петербург'),
types.InlineKeyboardButton('Нижний Новгород'),
types.InlineKeyboardButton('Московская область'),
types.InlineKeyboardButton('Другие города'),
types.InlineKeyboardButton('Назад'),
)


instr = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
instr.add(
types.InlineKeyboardButton('Окрашивание тай-дай'),
types.InlineKeyboardButton('Однотонное окрашивание'),
types.InlineKeyboardButton('Назад'),
)


instr_mono_color = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
instr_mono_color.add(
types.InlineKeyboardButton('Красителями для тай-дай'),
types.InlineKeyboardButton('Прямыми красителями'),
types.InlineKeyboardButton('Назад'),
)

masterclass_main = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
masterclass_main.add(
types.InlineKeyboardButton('Общая информация о техниках'),
types.InlineKeyboardButton('Техники окрашивания'),
types.InlineKeyboardButton('Назад'),
)

masterclass_technics = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
master_liq = types.InlineKeyboardButton('Окрашивание жидкими красителями')
master_diving = types.InlineKeyboardButton('Погружная техника')
master_ice = types.InlineKeyboardButton('Ледяная техника')
master_zheoda = types.InlineKeyboardButton('Жеода')
master_grad = types.InlineKeyboardButton('Градиент')
master_shib = types.InlineKeyboardButton('Шибори')
master_foam = types.InlineKeyboardButton('Окрашивание пеной')
master_boiled = types.InlineKeyboardButton('Окрашивание кипятком')
back = types.InlineKeyboardButton('Назад')
masterclass_technics.add(master_zheoda, master_grad)
masterclass_technics.add(master_liq)
masterclass_technics.add(master_ice, master_shib)
masterclass_technics.add(master_diving)
masterclass_technics.add(master_foam)
masterclass_technics.add(master_boiled)
masterclass_technics.add(back)