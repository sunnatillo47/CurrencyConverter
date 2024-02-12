from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import datetime
from config import course

rtr = Router()

@rtr.message(CommandStart())
async def rtr_start(message: Message):
	await message.answer(text="Assalomu alykum")

# @rtr.message()
# async def course_dollar(message: Message):
# 	text = message.text
# 	if text.startswith('💲') or text.endswith('💲'):
# 		num = ''
# 		for n in text:
# 			if n.isdigit():
# 				num += n
# 		await message.answer(str(float(course[0]['Rate']) * float(num)))
# 	elif text.startswith('USD') or text.endswith('USD'):
# 		date_txt = ''
# 		for n in text:
# 			if n.isdigit() or n =='.':
# 				date_txt += n
# 		joriy_sana = datetime.now().date().strftime("%d.%m.%Y")
# 		if date_txt == joriy_sana:
# 			await message.answer(f"Siz kiritgan sanadagi kurs: {str((course[0]['Rate']))}")


@rtr.message(Command('hafta'))
async def week(message: Message):
	today = datetime.date.today()
	for i in range(1, 8):
		date = today - datetime.timedelta(days=i)
		for valuta in course:
			if valuta['Ccy'] == 'USD' and valuta['Date'] == '12.02.2024':
				kurs = str(valuta['Rate'])
				diff = float(valuta['Diff'])
				break
		await message.answer(f"AQSh dollari ({date.strftime('%d.%m.%Y')}) kuni: {kurs} so'm")








	# s = "Joriy haftadagi 7 kunlik valyuta kurslari:\n"
	# for kurs in course:

	# 	if kurs['Ccy'] in ['USD', 'EUR', 'RUB']:
	# 		s += f"{kurs['Ccy']}: "
	# 		today = datetime.date.today()

	# 		for i in range(7):

	# 			date = today - datetime.timedelta(days=i)
	# 			kurs_value = next((x['Date'] for x in kurs['Rate'] if x == date.strftime('%Y-%m-%d')), None)
	# 			s += f"{kurs_value} UZS, " if kurs_value is None else "N/A, "
	# 		s += "\n"
	# await message.answer(text=s)