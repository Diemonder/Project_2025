# -*- coding: utf-8 -*-
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Словарь с играми по жанрам
games_by_genre = {
    "rpg": ["The Witcher 3", "Skyrim", "Dark Souls", "Fallout: New Vegas", "Divinity: Original Sin 2"],
    "action": ["DOOM Eternal", "Grand Theft Auto V", "Red Dead Redemption 2", "Cyberpunk 2077", "Far Cry 6"],
    "strategy": ["Civilization VI", "XCOM 2", "Stellaris", "Total War: Warhammer 3", "Age of Empires IV"],
    "adventure": ["The Legend of Zelda: Breath of the Wild", "God of War", "Uncharted 4", "Horizon Zero Dawn", "Tomb Raider"],
    "indie": ["Hades", "Stardew Valley", "Celeste", "Hollow Knight", "Undertale"],
    "horror": ["Resident Evil Village", "Silent Hill 2", "Amnesia: The Dark Descent", "Outlast", "Alien: Isolation"],
}

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Привет! Я бот, который рекомендует игры по жанрам.\n"
        "Доступные жанры: rpg, action, strategy, adventure, indie, horror.\n"
        "Напиши название жанра, и я предложу игру!"
    )

async def recommend_game(update: Update, context: CallbackContext) -> None:
    genre = update.message.text.lower()
    if genre in games_by_genre:
        game = random.choice(games_by_genre[genre])
        await update.message.reply_text(f"Попробуй игру: {game}!")
    else:
        await update.message.reply_text(
            "Извини, я не знаю такого жанра.\n"
            "Попробуй один из этих: rpg, action, strategy, adventure, indie, horror."
        )

def main() -> None:
    application = Application.builder().token("8039913421:AAGJmrmEST8dAY4n3Y5Tv0LP1le-UcrsdHU").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recommend_game))

    application.run_polling()

if __name__ == '__main__':
    main()