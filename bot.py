#!/usr/bin/env python
from telegram.ext import Updater, MessageHandler, CommandHandler, InlineQueryHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode
from parser import Parser

class TelegramBot(object):

	def listener(self, bot, update):
		id = update.message.chat_id
		mensaje = update.message.text
		print("ID: " + str(id) + " MESSAGE: " + mensaje)

	def start(self, bot, update):
		self.listener(bot, update)
		bot.sendMessage(chat_id=update.message.chat_id, text='Bienvenido')

	def book(self, bot, update):
		self.listener(bot, update)
		for msg in self.parser.get_book() :
			bot.sendMessage(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
		bot.sendPhoto(chat_id=update.message.chat_id, photo=self.parser.get_image())

	def link(self, bot, update):
		self.listener(bot, update)
		bot.sendMessage(chat_id=update.message.chat_id,
			text='Download today\'s free book <a href="https://www.packtpub.com/packt/offers/free-learning/">HERE</a>.', parse_mode=ParseMode.HTML, disable_web_page_preview=True)

	def run(self):
		updater = Updater('558256017:AAGEKKqDDV4vRw2O45N8es1UVX6GBdvOr1s')

		self.parser = Parser()

		dispatcher = updater.dispatcher

		listener_handler = MessageHandler(Filters.text, self.listener)
		dispatcher.add_handler(listener_handler)

		dispatcher.add_handler(CommandHandler("start", self.start))
		dispatcher.add_handler(CommandHandler("book", self.book))
		dispatcher.add_handler(CommandHandler("link", self.link))

		updater.start_polling()
		updater.idle()

if __name__ == "__main__":
    telegramBot = TelegramBot()
    telegramBot.run()
