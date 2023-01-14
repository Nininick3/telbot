import config as cf
from aiogram import Bot, Dispatcher, executor, types
kromer_list = [1,2,3,4,5,6,7,8,9]
token = cf.token
tgbot = Bot(token)
dp = Dispatcher(tgbot)

HELP_MES = """
<b>/help</b> - <em>Я (не) помогу тебе</em>
<b>/start</b> - <em>Запусти меня (ты чёрт)</em>
<b>/work</b> - <em>Лол пчел ты......</em>
<b>/buy</b><em> Покупай [KROMER]</em>

"""

@dp.message_handler(commands = ['start'])
async def send_welcom(message: types.Message):
    return await message.reply("Зачем ты меня запустил? Мне же теперь работать надо будет!!! ЗА ЭТО ТЫ ДОЛЖЕН КУПИТЬ ВСЕ [KROMER]!!!")


@dp.message_handler(commands = ['work'])
async def Work(message: types.Message):
    return await message.reply("Нет я не буду работать!!! Сам работай! А меня оставь в покое!!!")


@dp.message_handler(commands = ['help'])
async def send_welcom(message: types.Message):
    return await tgbot.send_message(message.chat.id,HELP_MES,"HTML")
'''
@dp.message_handler(commands = ['buy'])
async def buy(message: types.Message):
    args = message.get_args()
    if len(kromer_list) == 0:
        return await tgbot.send_message(message.chat.id, "Брах чел...... Сорян но [KROMER] не осталось. Сейчас напечатую ещё. Вернись позже.")
    if not args:
        return await tgbot.send_message(message.chat.id, f"Сейчас я могу продать тебе только {len(kromer_list)}! ПОКУПАЙ ВСЁ!! БЫСТРО!!!!!")
    else:
        if 
        for i range(args):
            kromer_list.pop()
        return await tgbot.send_message(message.chat.id, "Спасибо за покупку! А теперь уходи!!!")
'''



if __name__=='__main__':
    executor.start_polling(dp, skip_updates = True)