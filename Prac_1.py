import telepot
token = '1254737734:AAEdf-P0_E8CUg29xA4N9p8c7n92WOabIJo'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id.format(msg["text"]))

TelegramBot.message_loop(handle)
