import telebot
from telebot import types
import functions as func
import big_data as bd
import keyboard as kb
from config import TOKEN, admin
import logging
import time

bot = telebot.TeleBot(TOKEN)
bot_username = bot.get_me().username

markdown = """
    *bold text*
    _italic text_
    [text](URL)
    """

logging.basicConfig(level=logging.INFO, filename="log.log",
                    format="%(asctime)s %(levelname)s %(message)s", filemode="w", encoding = "UTF-8")

print('Бот запущен')

@bot.message_handler(commands=['start'])
def get_text_message(message):
    user_first_name = message.from_user.first_name
    chat_id = message.chat.id
    username = message.from_user.username
    print('Присоединился ', user_first_name, username, message.from_user.id)
    func.first_join(user_id=chat_id, username=username)
    bot.send_message(message.from_user.id, '👋 Здравствуйте!\nЭто бот Drop.\n\nКакой у вас вопрос?', parse_mode= "Markdown", reply_markup=kb.menu)
    logging.info(f"Новый пользователь {username}, {user_first_name}.")


# Вызов Админ Панели
@bot.message_handler(commands=['admin'])
def start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    print(username, ' использует команду admin')
    logging.info(f"Использует команду admin: {username}, {user_id}.")
    if message.chat.id == admin:
        print(username, 'получил доступ к админке')
        logging.info(f"Получил доступ к админке: {username}, {user_id}.")
        bot.send_message(message.chat.id, ' {}, вы авторизованы!'.format(message.from_user.first_name),
                         reply_markup=kb.admin)


@bot.message_handler(content_types=['text'])
def main(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_name = message.from_user.username
    if message.text == 'Вопрос по окрашиванию':
        msg = bot.send_message(message.chat.id, 'Выберите вопрос', reply_markup=kb.color_q)
        bot.register_next_step_handler(msg, color_q)
    elif message.text == 'Вопрос по заказу':
        msg = bot.send_message(message.chat.id, f"Выберите действие", parse_mode= "Markdown", reply_markup=kb.deliv_quesch)
        bot.register_next_step_handler(msg, deliv_q)
    elif message.text == 'Безопасность':
        bot.send_message(message.chat.id, bd.safe, parse_mode= "Markdown", reply_markup=kb.menu)
    elif message.text == 'Контакты':
        msg = bot.send_message(message.chat.id, f"Выберите ссылку", parse_mode= "Markdown", reply_markup=kb.contacts)
        bot.register_next_step_handler(msg, contacts)
    elif message.text == 'Сотрудничество':
        bot.send_message(message.chat.id, bd.partner, parse_mode= "Markdown", reply_markup=kb.menu)
    elif message.text == 'Назад':
        bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.menu)
    else:
        logging.info(f"Ошибка, некорректное значение при вводе в гл.меню {user_name}, {user_first_name}.")
        bot.send_message(message.chat.id, "Пожалуйста, воспользуйтесь кнопками!", reply_markup=kb.menu)







def make_order(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Как отследить заказ":
        msg = bot.send_message(message.chat.id, text = bd.see_deliv, parse_mode= "Markdown", reply_markup=kb.make_order)
        bot.register_next_step_handler(msg, make_order)
    elif message.text == 'Условия доставки':
        msg = bot.send_message(message.chat.id, f"Выберите формат доставки", parse_mode= "Markdown", reply_markup=kb.info_deliv)
        bot.register_next_step_handler(msg, info_deliv)
    elif message.text == 'Сайт':
        bot.send_message(message.chat.id, f"Информация", parse_mode= "Markdown", reply_markup=kb.make_order)
    elif message.text == 'Нужна консультация по продукту':
        msg = bot.send_message(message.chat.id, text=bd.consult_prod, parse_mode= "Markdown", reply_markup=kb.make_order)
        bot.register_next_step_handler(msg, make_order)
    elif text == 'Назад':
        bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.menu)
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!')
        logging.info(f"Введено некорректное значение при отметке прочитанного (авто) {user_name}, {user_first_name}.")


def info_deliv(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Доставка в РФ":
        msg = bot.send_message(message.chat.id, text = bd.deliv_rf, parse_mode= "Markdown", reply_markup=kb.make_order)
        bot.register_next_step_handler(msg, make_order)
    elif text == 'Международная доставка':
        msg = bot.send_message(message.chat.id, text = bd.deliv_world, parse_mode= "Markdown", reply_markup=kb.make_order)
        bot.register_next_step_handler(msg, make_order)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.make_order)
        bot.register_next_step_handler(msg, make_order)
    else:
        bot.send_message(message.from_user.id, "Пожалуйста, используйте кнопки!", reply_markup=kb.make_order)

def deliv_q(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Хочу сделать заказ":
        msg = bot.send_message(message.chat.id, 'Выберите действие', parse_mode= "Markdown", reply_markup=kb.deliv_quesch_make)
        bot.register_next_step_handler(msg, deliv_quesch_make)
    elif text == 'Оплатил заказ, а на почте отображается «не оплачен»':
        msg = bot.send_message(message.chat.id, text = bd.payd_order, parse_mode= "Markdown", reply_markup=kb.deliv_quesch)
        bot.register_next_step_handler(msg, deliv_q)
    elif text == 'Где мой заказ?':
        msg = bot.send_message(message.chat.id, bd.how_see_del, parse_mode= "Markdown", reply_markup=kb.deliv_quesch)
        bot.register_next_step_handler(msg, deliv_q)
    elif text == 'Вы получили мой заказ? Когда он будет отправлен?':
        msg = bot.send_message(message.chat.id, text = bd.do_y_give_mon, parse_mode= "Markdown", reply_markup=kb.deliv_quesch)
        bot.register_next_step_handler(msg, deliv_q)
    elif text == 'Заказ нужен срочно':
        msg = bot.send_message(message.chat.id, text = bd.fast_deliv, parse_mode= "Markdown", reply_markup=kb.deliv_quesch)
        bot.register_next_step_handler(msg, deliv_q)
    elif text == 'Проблема с заказом':
        msg = bot.send_message(message.chat.id, text = bd.problem_order, parse_mode= "Markdown", reply_markup=kb.deliv_quesch)
        bot.register_next_step_handler(msg, deliv_q)
    elif text == 'Самовывоз':
        msg = bot.send_message(message.chat.id, text = bd.samovyvoz, parse_mode= "Markdown", reply_markup=kb.deliv_quesch)
        bot.register_next_step_handler(msg, deliv_q)
    elif text == 'Проблема на сайте, проблема с заказом':
        msg = bot.send_message(message.chat.id, text = bd.problem, parse_mode= "Markdown", reply_markup=kb.deliv_quesch)
        bot.register_next_step_handler(msg, deliv_q)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.menu)
    else:
        bot.send_message(message.from_user.id, "Пожалуйста, используйте кнопки!", reply_markup=kb.make_order)



def deliv_quesch_make(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Как отследить заказ":
        msg = bot.send_message(message.chat.id, text = bd.how_see_del, parse_mode= "Markdown", reply_markup=kb.deliv_quesch_make)
        bot.register_next_step_handler(msg, deliv_quesch_make)
    elif text == 'Посмотреть условия доставки':
        msg = bot.send_message(message.chat.id, f"Выберите формат доставки", parse_mode= "Markdown", reply_markup=kb.info_deliv)
        bot.register_next_step_handler(msg, info_deliv_quesch)
    elif text == 'Нужна консультация по продукту и ассортименту':
        msg = bot.send_message(message.chat.id, text=bd.consult_prod, parse_mode= "Markdown", reply_markup=kb.deliv_quesch_make)
        bot.register_next_step_handler(msg, deliv_quesch_make)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.deliv_quesch)
        bot.register_next_step_handler(msg, deliv_q)
    else:
        bot.send_message(message.from_user.id, "Пожалуйста, используйте кнопки!", reply_markup=kb.deliv_quesch)

def info_deliv_quesch(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Доставка в РФ":
        msg = bot.send_message(message.chat.id, text = bd.deliv_rf, parse_mode= "Markdown", reply_markup=kb.info_deliv)
        bot.register_next_step_handler(msg, info_deliv_quesch)
    elif text == 'Международная доставка':
        msg = bot.send_message(message.chat.id, text = bd.deliv_world, parse_mode= "Markdown", reply_markup=kb.info_deliv)
        bot.register_next_step_handler(msg, info_deliv_quesch)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.deliv_quesch_make)
        bot.register_next_step_handler(msg, deliv_quesch_make)
    else:
        bot.send_message(message.from_user.id, "Пожалуйста, используйте кнопки!", reply_markup=kb.deliv_quesch_make)


def color_q(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Таблица распада красителей":
        msg = bot.send_message(message.chat.id, text = bd.table_drop, reply_markup=kb.color_q)
        bot.register_next_step_handler(msg, color_q)
    elif text == 'Инструкции и мастер-классы':
        msg = bot.send_message(message.chat.id, 'Выберите что хотите посмотреть', parse_mode= "Markdown", reply_markup=kb.instructions)
        bot.register_next_step_handler(msg, instructions_color_q)
    elif text == 'Как окрашивать?':
        msg = bot.send_message(message.chat.id, bd.how_color, parse_mode= "Markdown", reply_markup=kb.color_q)
        bot.register_next_step_handler(msg, color_q)
    elif text == 'Как ухаживать за окрашенной вещью?':
        msg = bot.send_message(message.chat.id, bd.how2_color, parse_mode= "Markdown", reply_markup=kb.color_q)
        bot.register_next_step_handler(msg, color_q)
    elif text == 'Можно смешивать цвета?':
        msg = bot.send_message(message.chat.id, bd.mix_color, parse_mode= "Markdown", reply_markup=kb.color_q)
        bot.register_next_step_handler(msg, color_q)
    elif text == 'Какой текстиль можно окрашивать?':
        msg = bot.send_message(message.chat.id, bd.textil_color, parse_mode= "Markdown", reply_markup=kb.color_q)
        bot.register_next_step_handler(msg, color_q)
    elif text == 'Что такое активатор и зачем он нужен?':
        msg = bot.send_message(message.chat.id, bd.activator_color, parse_mode= "Markdown", reply_markup=kb.color_q)
        bot.register_next_step_handler(msg, color_q)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.menu)
    else:
        bot.send_message(message.from_user.id, "Пожалуйста, используйте кнопки!", reply_markup=kb.color_q)

def instructions_color_q(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Инструкция":
        msg = bot.send_message(message.chat.id, 'Какая инструкция вас интересует?', parse_mode= "Markdown", reply_markup=kb.instr)
        bot.register_next_step_handler(msg, instr)
    elif message.text == 'Мастерклассы':
        msg = bot.send_message(message.chat.id, "Какой мастеркласс вас интересует?", parse_mode= "Markdown", reply_markup=kb.masterclass_main)
        bot.register_next_step_handler(msg, masterclass_main)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.color_q)
        bot.register_next_step_handler(msg, color_q)
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!')

def instr(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Окрашивание тай-дай":
        msg = bot.send_message(message.chat.id, bd.instr_tai_dai, parse_mode= "Markdown", reply_markup=kb.instr)
        bot.register_next_step_handler(msg, instr)
    elif message.text == 'Однотонное окрашивание':
        msg = bot.send_message(message.chat.id, 'Выберите способ окрашивания', parse_mode= "Markdown", reply_markup=kb.instr_mono_color)
        bot.register_next_step_handler(msg, instr_mono_color)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.instructions)
        bot.register_next_step_handler(msg, instructions_color_q)
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!')

def instr_mono_color(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Красителями для тай-дай":
        msg = bot.send_message(message.chat.id, bd.instr_mono_tai_dai, parse_mode= "Markdown", reply_markup=kb.instr_mono_color)
        bot.register_next_step_handler(msg, instr_mono_color)
    elif message.text == 'Прямыми красителями':
        msg = bot.send_message(message.chat.id, bd.instr_mono_straight, parse_mode= "Markdown", reply_markup=kb.instr_mono_color)
        bot.register_next_step_handler(msg, instr_mono_color)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.instr)
        bot.register_next_step_handler(msg, instr)
    else:
        msg = bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!', reply_markup=kb.instr_mono_color)
        bot.register_next_step_handler(msg, instr_mono_color)

def masterclass_main(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Общая информация о техниках":
        msg = bot.send_message(message.chat.id, bd.master_main, parse_mode= "Markdown", reply_markup=kb.masterclass_main)
        bot.register_next_step_handler(msg, masterclass_main)
    elif message.text == 'Техники окрашивания':
        msg = bot.send_message(message.chat.id, 'Выберите технику', parse_mode= "Markdown", reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.instructions)
        bot.register_next_step_handler(msg, instructions_color_q)
    else:
        msg = bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!', reply_markup=kb.masterclass_main)
        bot.register_next_step_handler(msg, masterclass_main)


def masterclass_technics(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Окрашивание жидкими красителями":
        msg = bot.send_message(message.chat.id, bd.master_liq, reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)
    elif message.text == 'Погружная техника':
        msg = bot.send_message(message.chat.id, bd.master_diving, reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)
    elif message.text == 'Ледяная техника':
        msg = bot.send_message(message.chat.id, bd.master_ice, reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)
    elif message.text == 'Жеода':
        msg = bot.send_message(message.chat.id, bd.master_zheoda, reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)
    elif message.text == 'Градиент':
        msg = bot.send_message(message.chat.id, bd.master_grad, reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)
    elif message.text == 'Шибори':
        msg = bot.send_message(message.chat.id, bd.master_shib, reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)
    elif message.text == 'Окрашивание пеной':
        msg = bot.send_message(message.chat.id, bd.master_foam, reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)
    elif message.text == 'Окрашивание кипятком':
        msg = bot.send_message(message.chat.id, bd.master_boiled, reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.masterclass_main)
        bot.register_next_step_handler(msg, masterclass_main)
    else:
        msg = bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!', reply_markup=kb.masterclass_technics)
        bot.register_next_step_handler(msg, masterclass_technics)


def contacts(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Связаться с DROP":
        msg = bot.send_message(message.chat.id, f"Что вас интересует?", parse_mode= "Markdown", reply_markup=kb.call_drop)
        bot.register_next_step_handler(msg, call_drop)
    elif message.text == 'Где купить':
        msg = bot.send_message(message.chat.id, f"Выберите формат заказа", parse_mode= "Markdown", reply_markup=kb.buy_choice)
        bot.register_next_step_handler(msg, buy_choice)
    elif text == 'Назад':
        bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.menu)
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!')


def call_drop(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Сотрудничество":
        msg = bot.send_message(message.chat.id, bd.contacts_sotr, parse_mode= "Markdown", reply_markup=kb.call_drop)
        bot.register_next_step_handler(msg, call_drop)
    elif message.text == 'Все контакты':
        msg = bot.send_message(message.chat.id, bd.contacts_all, parse_mode= "Markdown", reply_markup=kb.call_drop)
        bot.register_next_step_handler(msg, call_drop)
    elif message.text == 'Сайт':
        msg = bot.send_message(message.chat.id, bd.contacts_site, parse_mode= "Markdown", reply_markup=kb.call_drop)
        bot.register_next_step_handler(msg, call_drop)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.contacts)
        bot.register_next_step_handler(msg, contacts)
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!')

def buy_choice(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if text == "Онлайн":
        msg = bot.send_message(message.chat.id, f"Выберите магазин", parse_mode= "Markdown", reply_markup=kb.buy_d)
        bot.register_next_step_handler(msg, buy)
    elif message.text == 'Офлайн':
        msg = bot.send_message(message.chat.id, f"Выберите локацию", parse_mode= "Markdown", reply_markup=kb.buy_offline_choice)
        bot.register_next_step_handler(msg, buy_offline_choice)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.contacts)
        bot.register_next_step_handler(msg, contacts)
    else:
        msg = bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!')
        bot.register_next_step_handler(msg, buy_choice)


def buy(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if message.text == 'Озон':
        msg = bot.send_message(message.chat.id, bd.buy_ozon, parse_mode= "Markdown", reply_markup=kb.buy_d)
        bot.register_next_step_handler(msg, buy)
    elif message.text == 'Вайлдберриз':
        msg = bot.send_message(message.chat.id, bd.buy_wb, parse_mode= "Markdown", reply_markup=kb.buy_d)
        bot.register_next_step_handler(msg, buy)
    elif message.text == 'Яндекс Маркет':
        msg = bot.send_message(message.chat.id, bd.buy_yand, parse_mode= "Markdown", reply_markup=kb.buy_d)
        bot.register_next_step_handler(msg, buy)
    elif message.text == 'Сайт':
        msg = bot.send_message(message.chat.id, bd.buy_site, parse_mode= "Markdown", reply_markup=kb.buy_d)
        bot.register_next_step_handler(msg, buy)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.buy_choice)
        bot.register_next_step_handler(msg, buy_choice)
    else:
        msg = bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!')
        bot.register_next_step_handler(msg, buy_choice)


def buy_offline_choice(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if message.text == 'РФ':
        msg = bot.send_message(message.chat.id, f"Выберите город", parse_mode= "Markdown", reply_markup=kb.buy_offline_city)
        bot.register_next_step_handler(msg, buy_offline_city)
    elif message.text == 'Другие страны':
        msg = bot.send_message(message.chat.id, bd.buy_off_ot_country, parse_mode= "Markdown", reply_markup=kb.buy_d)
        bot.register_next_step_handler(msg, buy)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.buy_choice)
        bot.register_next_step_handler(msg, buy_choice)
    else:
        msg = bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!')
        bot.register_next_step_handler(msg, buy_offline_choice)


def buy_offline_city(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    text = message.text
    if message.text == 'Москва':
        msg = bot.send_message(message.chat.id, bd.buy_off_moscow, parse_mode= "Markdown", reply_markup=kb.buy_offline_city)
        bot.register_next_step_handler(msg, buy_offline_city)
    elif message.text == 'Санкт-Петербург':
        msg = bot.send_message(message.chat.id, bd.buy_off_spb, parse_mode= "Markdown", reply_markup=kb.buy_offline_city)
        bot.register_next_step_handler(msg, buy_offline_city)
    elif message.text == 'Нижний Новгород':
        msg = bot.send_message(message.chat.id, bd.buy_off_nn, parse_mode= "Markdown", reply_markup=kb.buy_offline_city)
        bot.register_next_step_handler(msg, buy_offline_city)
    elif message.text == 'Московская область':
        msg = bot.send_message(message.chat.id, bd.buy_off_mos_area, parse_mode= "Markdown", reply_markup=kb.buy_offline_city)
        bot.register_next_step_handler(msg, buy_offline_city)
    elif message.text == 'Другие города':
        msg = bot.send_message(message.chat.id, bd.buy_off_other, parse_mode= "Markdown", reply_markup=kb.buy_offline_city)
        bot.register_next_step_handler(msg, buy_offline_city)
    elif text == 'Назад':
        msg = bot.send_message(message.from_user.id, "Выберите кнопку", reply_markup=kb.buy_choice)
        bot.register_next_step_handler(msg, buy_choice)
    else:
        msg = bot.send_message(message.from_user.id, 'Пожалуйста, используйте кнопки!', reply_markup=kb.buy_offline_city)
        bot.register_next_step_handler(msg, buy_offline_city)



#Функции бота (админ)
@bot.callback_query_handler(func=lambda call: True)   
def handler_call(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user_id = call.from_user.id
    if call.data == 'statistics':
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=func.stats(), reply_markup=kb.admin)
    elif call.data == 'admin_msg':
            chat_id = call.message.chat.id
            text = call.message.text
            msg = bot.send_message(chat_id=chat_id, text='Введите текст для рассылки. \n\nДля отмены нажми Назад!', reply_markup=kb.back)
            bot.register_next_step_handler(msg, message1)
    elif call.data == 'logging': 
        bot.send_document(chat_id=chat_id, document=open('log.log', 'rb'))
    elif call.data == 'subd':
        bot.send_document(chat_id=chat_id, document=open('db.db', 'rb'))

def message1(message):
    text = message.text
    if message.text == '🔙 Назад':
            bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=kb.menu)
    else:
        info = func.admin_message(text)
        bot.send_message(message.chat.id, text=' Рассылка начата!')
        for i in range(len(info)):
            try:
                time.sleep(1)
                bot.send_message(info[i][0], str(text))
            except:
                pass
        bot.send_message(message.chat.id, text=' Рассылка завершена!')


# Поддержание работы
bot.polling(none_stop=True)
bot.infinity_polling()