# import random
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor

# # Your bot token from BotFather
# TOKEN = "YOUR_BOT_TOKEN_HERE"

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)

# # Example content
# memes = [
#     ("https://example.com/meme1.jpg", "😂 LOL! Sponsored: Buy cool gadgets here: https://affiliatelink.com"),
#     ("https://example.com/meme2.jpg", "🔥 Trending! Check out this: https://affiliatelink.com"),
# ]

# jokes = [
#     "Why don’t skeletons fight each other? They don’t have the guts! 😂",
#     "I told my wife she was drawing her eyebrows too high. She looked surprised! 😆",
# ]

# quotes = [
#     "“Success is not final, failure is not fatal: it is the courage to continue that counts.” – Winston Churchill",
#     "“The only way to do great work is to love what you do.” – Steve Jobs",
# ]

# # Start command
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.reply("👋 Welcome to ViralBytesBot! Type /meme, /joke, or /quote for daily fun! 😊")

# # Meme command
# @dp.message_handler(commands=['meme'])
# async def send_meme(message: types.Message):
#     meme_url, caption = random.choice(memes)
#     await bot.send_photo(message.chat.id, meme_url, caption=caption)

# # Joke command
# @dp.message_handler(commands=['joke'])
# async def send_joke(message: types.Message):
#     joke_text = random.choice(jokes) + "\n\n🔥 Sponsored: Get more fun here: https://affiliatelink.com"
#     await message.reply(joke_text)

# # Quote command
# @dp.message_handler(commands=['quote'])
# async def send_quote(message: types.Message):
#     quote_text = random.choice(quotes) + "\n\n💡 Sponsored: Read more inspiring books: https://affiliatelink.com"
#     await message.reply(quote_text)

# # Run the bot
# if __name__ == "__main__":
#     executor.start_polling(dp)
