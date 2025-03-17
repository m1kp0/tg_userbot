# в боте есть ошибки, не юзайте

# импорт
from telethon import *
import datetime
import time
import os

# переменные
zametks = []

# апи
api_id = 1234567
api_hash = "аррр"

# бот
m1kp = TelegramClient(
    "session_1",
    api_id=api_id, 
    api_hash=api_hash
)

# функции
# удаление сообщения
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".-"))
async def delete_msg(event):
    msg = await event.get_reply_message()
    if event and msg:
        await msg.delete()
        await event.delete()
    elif event:
        time.sleep(0.5)
        await event.edit("нет сообщения для удаления!")
        time.sleep(2)
        await event.delete()

# пр
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".пр"))
async def pr(event):
    text = event.text.split()
    if event and text[1] == "1":
        await event.edit("П")
        time.sleep(0.1)
        await event.edit("Пр")
        time.sleep(0.1)
        await event.edit("При")
        time.sleep(0.1)
        await event.edit("Прив")
        time.sleep(0.1)
        await event.edit("Приве")
        time.sleep(0.1)
        await event.edit("Привет")
        time.sleep(0.1)
        await event.edit("Привет!")
    elif event and text[1] == "2":
        for i in range(1, 100):
            time.sleep(0.1)
            await event.edit("р---------------")
            time.sleep(0.1)
            await event.edit("-пр-------------")
            time.sleep(0.1)
            await event.edit("--пр------------")
            time.sleep(0.1)
            await event.edit("---пр-----------")
            time.sleep(0.1)
            await event.edit("----пр----------")
            time.sleep(0.1)
            await event.edit("-----пр---------")
            time.sleep(0.1)
            await event.edit("------пр--------")
            time.sleep(0.1)
            await event.edit("-------пр-------")
            time.sleep(0.1)
            await event.edit("--------пр------")
            time.sleep(0.1)
            await event.edit("---------пр-----")
            time.sleep(0.1)
            await event.edit("----------пр----")
            time.sleep(0.1)
            await event.edit("-----------пр---")
            time.sleep(0.1)
            await event.edit("------------пр--")
            time.sleep(0.1)
            await event.edit("-------------пр-")
            time.sleep(0.1)
            await event.edit("--------------пр")
            time.sleep(0.1)
            await event.edit("-----------------п")
    elif event and text[1] == "3":
        await event.edit("Ч")
        await event.edit("ЧУ")
        await event.edit("ЧУВ")
        await event.edit("ЧУВА")
        await event.edit("ЧУВАА")
        await event.edit("ЧУВААА")
        await event.edit("ЧУВАААА")
        await event.edit("ЧУВААААА")
        await event.edit("ЧУВАААААА")
        await event.edit("ЧУВАААААААК З")
        await event.edit("ЧУВАААААААК ЗД")
        await event.edit("ЧУВАААААААК ЗДА")
        await event.edit("ЧУВАААААААК ЗДАР")
        await event.edit("ЧУВАААААААК ЗДАРО")
        await event.edit("ЧУВАААААААК ЗДАРОВ")
        await event.edit("ЧУВАААААААК ЗДАРОВА")

# подожди
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".жди"))
async def sec(event):
    if event:
        await event.edit("подожди 5 сек пж")
        time.sleep(3)
        await event.edit("я чуть занят просто")

# во
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".во"))
async def like(event):
    if event:
        await event.edit("👍")

# не во
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".нево"))
async def dislike(event):
    if event:
        await event.edit("👎")

# скрипты
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".скрипт"))
async def script(event):
    text = event.text.split()
    if event and text[1]:
        if text[1] == "лб":
            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/DMO/refs/heads/main/ladder_breaker.lua'))()") # ладдер бреакер дмо
        elif text[1] == "лбв6":
            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/DMO/refs/heads/main/ladder_breaker_v6_beta.lua'))()") # ладдер бреакер 6
        elif text[1] == "чатбайпасс":
            await event.edit("loadstring(game:HttpGet'https://raw.githubusercontent.com/m1kp0/universal_scripts/refs/heads/main/chat_bypass.lua')()") # чат байпасс
        elif text[1] == "иур":
            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/alajayid/infiniteyield-reborn-reborn/master/source'))()") # инфините уиелд реборн
        elif text[1] == "патх": 
            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/universal_scripts/refs/heads/main/ONLY-PC_pathing'))()") # pathing
        elif text[1] == "лбб":
            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/lucky_block_battleground/refs/heads/main/lbb.lua'))()") # лаки блоки
        elif text[1] == "беар":
            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/auto_farm/refs/heads/main/bear_alpha.lua'))()") # беар альфа автофарм
        elif text[1] == "фриадмин":
            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/free_admin/refs/heads/main/free_admin_script.lua'))()") # фри админ скрипт
        elif text[1] == "тох":
            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/tower_of_hell/refs/heads/main/toh.lua'))()") # тавер оф хелл

# спам
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".спам"))
async def spam(event):
    text = event.text.split()
    if event and text[1] and text[2]:
        await event.edit("спам...")
        for i in range(int(text[2])):
            await m1kp.send_message(event.chat_id, text[1])
            time.sleep(0.1)
        
        await event.delete()


# заметки функции
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".сейв"))
async def zametka_save(event):
    text = event.text.split()
    reply = await event.get_reply_message()
    if event and reply:
        zametks.append(reply.text)
        await event.edit(f"добавлено в сохранённые")
    elif event and text[1]:
        zametks.append(text[1])
        await event.edit(f"добавлено в сохранённые: {text[1]}")

@m1kp.on(events.NewMessage(outgoing=True, pattern=r".удалить_сейв"))
async def zametka_delete(event):
    text = event.text.split()
    reply = event.get_reply_message()
    if event and text[1]:
        zametks.remove(text[1])
        await event.edit(f"удалено из сохранённых: {text[1]}")
    elif event and reply:
        zametks.remove(reply.text)
        await event.edit("удалено из сохранённых")

@m1kp.on(events.NewMessage(outgoing=True, pattern=r".очистить_сейвы"))
async def clear_zametks(event):
    text = event.text.split()
    if event:
        zametks.clear()
        await event.edit("удалены все сохранённые сообщения")

@m1kp.on(events.NewMessage(outgoing=True, pattern=r".сейвы"))
async def see_zametks(event):
    if event:
        for i in zametks:
            await m1kp.send_message(event.chat_id, i)
            event.delete()

@m1kp.on(events.NewMessage(outgoing=True, pattern=r".см"))
async def zametka_save(event):
    reply = await event.get_reply_message()
    if event and reply:
        await m1kp.send_message("me", reply)
        await event.edit("сообщение переслано себе")
    else:
        await event.edit("сообщение не найдено")
        time.sleep(3)
        await event.delete()

# время сейчас
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".время"))
async def zametka_save(event):
    if event:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        await event.edit(f"время сейчас: {time_now}")

# команды
@m1kp.on(events.NewMessage(outgoing=True, pattern=r".команды"))
async def zametka_save(event):
    if event:
        await event.edit(".- - удаление сообщения\n.пр (1, 2, 3) - привет\n.жди - просит собеседника подождать\n.во - лайк\n.нево - дизлайк\n.скрипт (лб, лбв6, чатбайпасс, иур, патх, лбб, фриадмин, тох) - даёт скрипт\n.сейв - сохраняет сообщение\n.удалить_сейв - удалить сейв\n.очистить_сейвы - очистить сейвы\n.сейвы - показывает все сохранённые сообщения\n.время - точное время сейчас\n.см - переслать сообщение самому себе\n.команды - все команды")

# старт
m1kp.start()
m1kp.run_until_disconnected()
