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
<b>/buy</b><em> Покупай любую валюту</em>

"""

def print_dict (val):
    tmp = ""
    for i in val:
        tmp += f'{i} : {val[i]} \n'
    return tmp

@dp.message_handler(commands = ['start'])
async def send_welcom(message: types.Message):
    return await message.reply("Зачем ты меня запустил? Мне же теперь работать надо будет!!! ЗА ЭТО ТЫ ДОЛЖЕН КУПИТЬ ВСЕ [KROMER]!!!")

@dp.message_handler(commands = ['work'])
async def Work(message: types.Message):
    return await message.reply("Работай человек!! Работай!!! Сам!!!")

@dp.message_handler(commands = ['help'])
async def send_help(message: types.Message):
    return await tgbot.send_message(message.chat.id,HELP_MES,"HTML")

@dp.message_handler(commands = ['buy'])
async def buy(message: types.Message):
    print_dict(val_dict)
    args = message.get_args()

    if not args:
        return await tgbot.send_message(message.chat.id, f"Сейчас я могу продать тебе только \n{print_dict(val_dict)}! ПОКУПАЙ ВСЁ!! БЫСТРО!!!!! НЕ ЗАСТАВЛЯЙ МЕНЯ ПОВТОРЯТЬ!!! Пиши в формате: /buy число (число валюты которой ты хочешь купить)! "
                                                         f"")
    else:
        if len(val_list) == 0:
            return await tgbot.send_message(message.chat.id,
                                            "Брах чел...... Сорян но валюты не осталось. Сейчас напечатую ещё. Вернись позже.")
        if args.isdigit():
            args = int(args)
            if args  > len(val_list):
                return await tgbot.send_message(message.chat.id, f"ВОУ! ВОУ! ВОУ! Чел...... А ты хорош! Но к сожалению я могу продать тебе только {len(val_list)}! Прости!")
            elif args == len(val_list):
                for i in range(args):
                    print(i)
                    val_list.pop()
                await tgbot.send_message(message.chat.id, "Молодец! Хороший человек!!! Так уж и быть продам я продам тебе твою валюту! Заслужил!")
                return await tgbot.send_message(message.chat.id, "ВСЁ!!! УРА!!! Я СВОБОДЕН!!! Я ПРОДАЛ ВАЛЮТУ!!!! А ТЫ МОЖЕШЬ ИДТИ ОТСУДА!!!!")
            elif args < len(val_list):
                return await tgbot.send_message(message.chat.id, "ТЫ ЧТО НЕ ПОНЯЛ!!!!!!! Я ЖЕ СКАЗАЛ ЧТОБЫ ТЫ ПОКУПАЛ ВСЁ!!!!!!! ИЛИ К ТЕБЕ ГРУППУ УСТРАНЕНИЯ ОТПРАВИТЬ????!!!!?!?!!?!? А ЧЁРТ!!!!!")



if __name__=='__main__':
    executor.start_polling(dp, skip_updates = True)