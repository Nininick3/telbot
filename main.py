import config as cf
from aiogram import Bot, Dispatcher, executor, types
val_list = [1,2,3,4,5,6,7,8,9]
val_dict = {"V-bucks" : 9,"Примогемы" : 9,"Гео" : 9}
token = cf.token
tgbot = Bot(token)
dp = Dispatcher(tgbot)

HELP_MES = """
<b>/help</b> - <em>Я (не) помогу тебе</em>
<b>/start</b> - <em>Запусти меня (ты чёрт)</em>
<b>/work</b> - <em>Лол пчел ты......</em>
<b>/buy</b> - <em> Покупай любую валюту (всю выбранную)</em>
<b>/aboutme</b> - <em>Обо мне</em>
"""

def print_dict (val):
    tmp = ""
    for i in val:
        tmp += f'{i} : {val[i]} \n'
    return tmp

@dp.message_handler(commands = ['start'])
async def send_welcom(message: types.Message):
    return await message.reply("Зачем ты меня запустил? Мне же теперь работать надо будет!!!")

@dp.message_handler(commands = ['work'])
async def Work(message: types.Message):
    return await message.reply("Работай человек!! Работай!!! Сам!!!")

@dp.message_handler(commands = ['help'])
async def send_help(message: types.Message):
    return await tgbot.send_message(message.chat.id,HELP_MES,"HTML")

@dp.message_handler(commands = ['buy'])
async def buy(message: types.Message):
    args = message.get_args()
    args = args.split()

    if not args:
        return await tgbot.send_message(message.chat.id, f"Сейчас я могу продать тебе только \n{print_dict(val_dict)}! ПОКУПАЙ ВСЁ!! БЫСТРО!!!!! НЕ ЗАСТАВЛЯЙ МЕНЯ ПОВТОРЯТЬ!!! Пример написания команды: /buy названии валюты число которое ты хочешь купить (всё)!"
                                                         f"")
    else:
        if args[0] in val_dict:
            if val_dict[args[0]] == 0:
                return await tgbot.send_message(message.chat.id,
                                            "Брах чел...... Сорян но валюты не осталось. Сейчас напечатую ещё. Вернись позже.")
            if args[1].isdigit():
                args[1] = int(args[1])
                if args[1] > val_dict[args[0]]:
                    return await tgbot.send_message(message.chat.id, f"ВОУ! ВОУ! ВОУ! Чел...... А ты хорош! Но к сожалению я могу продать тебе только {len(val_list)}! Прости!")
                else:
                    val_dict[args[0]] = val_dict[args[0]] - args[1]
                    return await tgbot.send_message(message.chat.id, f"Осталось \n{print_dict(val_dict)}.")
            else:
                return await tgbot.send_message(message.chat.id, "Ты ввёл что-то не то! И это твоя ошибка!")
        else:
            return await tgbot.send_message(message.chat.id, "Сорри мне не хватает валюты!")

@dp.message_handler(commands = ['aboutme'])
async def send_welcom(message: types.Message):
    return await message.reply("Ты хочешь узнать обо мне? Хорошо. Пока я могу сказать мало про себя, но я точно знаю, что мой создатель самый лучший человек во ввселенной. И я его очень люблю!")

if __name__=='__main__':
    executor.start_polling(dp, skip_updates = True)