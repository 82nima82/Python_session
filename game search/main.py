import telebot
from telebot import types
import requests
from deep_translator import GoogleTranslator
import re

TELEGRAM_BOT_TOKEN = "12345"
RAWG_API_KEY = "12345"
YOUTUBE_API_KEY = "12345"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
user_state = {}
user_keywords = {}
user_genre = {}

# ژانرهای پیشنهادی
GENRES = ["Action", "Adventure", "RPG", "Strategy", "Simulation", "Shooter", "Puzzle", "Sports"]


def translate_if_needed(text):
    if re.search(r'[\u0600-\u06FF]', text):
        return GoogleTranslator(source='auto', target='en').translate(text)
    else:
        return text


def get_games_from_keywords_and_genre(keywords, genre, max_games=3):
    query = translate_if_needed(keywords)
    url = f"https://api.rawg.io/api/games?key={RAWG_API_KEY}&search={query}&page_size={max_games}"
    response = requests.get(url).json()
    games = []

    for game in response.get("results", []):
        # اگر ژانر انتخاب شده هم در ژانرهای بازی بود
        game_genres = [g['name'] for g in game.get('genres', [])]
        if genre in game_genres:
            games.append({
                "id": game["id"],
                "name": game["name"],
                "rating": game["rating"],
                "released": game["released"],
                "image": game["background_image"],
            })
        # اگر ژانر None باشد (انتخاب نشود) همه اضافه شوند
        elif not genre:
            games.append({
                "id": game["id"],
                "name": game["name"],
                "rating": game["rating"],
                "released": game["released"],
                "image": game["background_image"],
            })
    return games


def get_system_requirements(game_id):
    url = f"https://api.rawg.io/api/games/{game_id}?key={RAWG_API_KEY}"
    response = requests.get(url).json()

    for platform in response.get("platforms", []):
        if platform["platform"]["name"].lower() in ["pc", "pc (windows)", "windows"]:
            req = platform.get("requirements", {})
            minimum = req.get("minimum", "❌ اطلاعات موجود نیست")
            recommended = req.get("recommended", "❌ اطلاعات موجود نیست")
            return minimum, recommended
    return None, None


def get_youtube_trailer(game_name):
    search_query = game_name + " trailer"
    url = (
        f"https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&q={search_query}&key={YOUTUBE_API_KEY}&maxResults=1&type=video"
    )
    response = requests.get(url).json()

    if "items" in response and len(response["items"]) > 0:
        video_id = response["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"
    return None


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "سلام 👋\nحداکثر ۳ کلمه درباره بازی مورد نظرت بگو (فارسی یا انگلیسی) تا بازی‌های مرتبط معرفی کنم 🎮"
    )
    user_state[message.chat.id] = "waiting_for_keywords"


@bot.message_handler(func=lambda m: True)
def main_chat(message):
    chat_id = message.chat.id

    if chat_id in user_state:
        state = user_state[chat_id]

        if state == "waiting_for_continue":
            bot.send_message(chat_id, "لطفاً از دکمه‌های زیر استفاده کن 👇")
            return

        elif state == "waiting_for_keywords":
            # ذخیره کلمات کاربر
            user_keywords[chat_id] = message.text
            # ارسال دکمه‌های ژانر
            markup = types.InlineKeyboardMarkup(row_width=2)
            buttons = [types.InlineKeyboardButton(g, callback_data=f"genre_{g}") for g in GENRES]
            markup.add(*buttons)
            bot.send_message(chat_id, "یک ژانر برای بازی انتخاب کن:", reply_markup=markup)
            user_state[chat_id] = "waiting_for_genre"
            return


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.message.chat.id

    # مرحله انتخاب ژانر
    if call.data.startswith("genre_"):
        selected_genre = call.data.replace("genre_", "")
        user_genre[chat_id] = selected_genre
        keywords = user_keywords.get(chat_id, "")
        bot.send_message(chat_id, f"ژانر انتخاب شد: {selected_genre}\n⏳ در حال جستجو بازی‌ها...")

        games = get_games_from_keywords_and_genre(keywords, selected_genre, max_games=3)
        if not games:
            bot.send_message(chat_id, "❌ بازی مرتبط پیدا نشد. دوباره تلاش کن.")
            user_state[chat_id] = "waiting_for_keywords"
            return

        for game in games:
            minimum, recommended = get_system_requirements(game["id"])
            trailer = get_youtube_trailer(game["name"])

            caption = (
                f"🎮 **{game['name']}**\n"
                f"⭐ امتیاز: {game['rating']}\n"
                f"📅 تاریخ انتشار: {game['released']}\n"
            )

            if game["image"]:
                bot.send_photo(chat_id, game["image"], caption=caption, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, caption, parse_mode="Markdown")

            if trailer:
                bot.send_message(chat_id, f"🎬 تریلر:\n{trailer}")

            bot.send_message(
                chat_id,
                "💻 **سیستم مورد نیاز (PC)**:\n\n"
                f"🔻 *Minimum:* \n{minimum}\n\n"
                f"🔹 *Recommended:* \n{recommended}",
                parse_mode="Markdown"
            )

        # دکمه بله / نه بعد از معرفی
        markup2 = types.InlineKeyboardMarkup()
        yes_button = types.InlineKeyboardButton("بله 🎮", callback_data="yes")
        no_button = types.InlineKeyboardButton("نه ❌", callback_data="no")
        markup2.add(yes_button, no_button)
        bot.send_message(chat_id, "میخوای یه بازی دیگه هم معرفی کنم؟", reply_markup=markup2)
        user_state[chat_id] = "waiting_for_continue"
        return

    # مرحله بله/نه
    if call.data == "yes":
        bot.send_message(chat_id, "حداکثر ۳ کلمه درباره بازی مورد نظرت بگو (فارسی یا انگلیسی) 🎮")
        user_state[chat_id] = "waiting_for_keywords"
        if chat_id in user_keywords:
            del user_keywords[chat_id]
        if chat_id in user_genre:
            del user_genre[chat_id]

    elif call.data == "no":
        bot.send_message(chat_id, "باشه 👌 هر وقت بازی جدید خواستی فقط پیام بده.")
        if chat_id in user_state:
            del user_state[chat_id]
        if chat_id in user_keywords:
            del user_keywords[chat_id]
        if chat_id in user_genre:
            del user_genre[chat_id]


bot.infinity_polling()