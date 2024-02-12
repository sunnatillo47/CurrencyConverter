from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from datetime import datetime, timedelta
from config import course

rtr = Router()

@rtr.message(CommandStart())
async def rtr_start(message: Message):
	await message.answer(text="Assalomu alykum")

@rtr.message()
async def course_dollar(message: Message):
	text = message.text
	if text.startswith('💲') or text.endswith('💲'):
		num = ''
		for n in text:
			if n.isdigit():
				num += n
		await message.answer(str(float(course[0]['Rate']) * float(num)))
	elif text.startswith('USD') or text.endswith('USD'):
		date_txt = ''
		for n in text:
			if n.isdigit() or n =='.':
				date_txt += n
		joriy_sana = datetime.now().date().strftime("%d.%m.%Y")
		if date_txt == joriy_sana:
			await message.answer(f"Siz kiritgan sanadagi kurs: {str((course[0]['Rate']))}")










	