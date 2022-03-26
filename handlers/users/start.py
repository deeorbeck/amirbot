from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import menu
from loader import dp
from states.cv import cv


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await cv.zero.set()
    TEXT = """
    Ассалому алайкум, СИЗНИ ҚАДРЛАЙДИГАН ЖАМОАДА ИШЛАШНИ ҲОҲЛAЙСИЗМИ?  
        
Унда сиз учун ажойиб имконият!

"AMIR SHOES" Корхонаси жамоаси сизни ишга таклиф қилади! 

☝️ Онлине тарзда анкетангизни тўлдиринг ва бизни сафимиздан жой олинг. 

✅БИЗ АЙНАН СИЗНИ ТАНЛАЙМИЗ, АГАР СИЗ: 
• 20-40 ёшдаги;
• Хушмомилали;
• Жамоа билан ишлаш маҳорати;
• Ҳалол ва шижоатли 
• Маъсулиятли;


📌СИЗ НИМАЛАРГА ЭГА БЎЛАСИЗ? 
• Бир мақсад асосида еғилган жамоа;
• Ойлик маошдан ташқари БОНУС олиш;
• Замонавий офис ва ишхона;
• Ўз вақтидаги ойлик маош;
• Расмий ишга қабул қилиш;
• БЕПУЛ ўқув платформа;
• Шахсий ривожланиш;

Бизга мурожаат қилинг ва жамоамизга қўшилинг!"""
    await message.answer(TEXT, parse_mode="html", reply_markup=menu.markup_menu)
