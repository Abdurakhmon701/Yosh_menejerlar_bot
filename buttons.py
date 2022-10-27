from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

# Til uchun knopka
til = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "🇺🇿 O'zbekcha",callback_data="uz"),
			InlineKeyboardButton(text = "🇬🇧 English",callback_data="en")

		],
	],
)
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Menu English
menu_1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "📑About Project",callback_data="project_menu"),
			InlineKeyboardButton(text = "📜Registration",callback_data="registration")

		],
		[
			InlineKeyboardButton(text = "📤Send questions",callback_data="questions"),
		],
	],
)
#=========================================================================================================
# Project menu
project_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Aim of the project',callback_data='aim'),
		InlineKeyboardButton(text = "Project task",callback_data='task')
	],
	[
		InlineKeyboardButton(text = "The order of process",callback_data='process'),
		InlineKeyboardButton(text = "Requirements",callback_data='require')
	],
	[
		InlineKeyboardButton(text = 'Back',callback_data='back'),
	],
	]
	
)
#=========================================================================================================
aim = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Back',callback_data='back_1'),
	],
	]
	
)
#=========================================================================================================
task = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Back',callback_data='back_2'),
	],
	]
	
)
#=========================================================================================================
process = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Back',callback_data='back_3'),
	],
	]
	
)
#=========================================================================================================
require = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Back',callback_data='back_4'),
	],
	]
	
)
#=========================================================================================================
questions = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Back',callback_data='back_5'),
	],
	]
	
)
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Menu Uzbek
menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "📑Loyiha haqida",callback_data="loyiha"),
			InlineKeyboardButton(text = "📜Ro'yxatdan o'tish",callback_data="royxat")

		],
		[
			InlineKeyboardButton(text = "📤Savollar yo'llash",callback_data="savollar0"),
		],
	],
)
#=========================================================================================================
# Loyiha menu
loyiha_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Loyiha maqsadi',callback_data='maqsadi'),
		InlineKeyboardButton(text = "Loyiha vazifasi",callback_data='vazifa')
	],
	[
		InlineKeyboardButton(text = "O'tkazilish tartibi",callback_data='tartibi'),
		InlineKeyboardButton(text = "Talablar",callback_data='talabi')
	],
	[
		InlineKeyboardButton(text = 'Orqaga',callback_data='ortga'),
	],
	]
	
)
#=========================================================================================================
maqsadi = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Orqaga',callback_data='ortga_1'),
	],
	]
	
)
#=========================================================================================================
vazifa = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Orqaga',callback_data='ortga_2'),
	],
	]
	
)
#=========================================================================================================
tartibi = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Orqaga',callback_data='ortga_3'),
	],
	]
	
)
#=========================================================================================================
talabi = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Orqaga',callback_data='ortga_4'),
	],
	]
	
)
#=========================================================================================================
savollar = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = 'Orqaga',callback_data='ortga_5'),
	],
	]
	
)