def c_get_hello(full_name: str) -> str:
    return f"Assalomu alaykum, <b>{full_name.title()}</b>\nBu Midjorneydan to'g'ridan-to'g'ri telegramda mavjud bo'lgan bot!\n\n" \
        "🔥Endi siz messenjerdan chiqmasdan matn tavsifiga muvofiq istalgan tasvirni yaratishingiz mumkin!\n\n"\
        "Namunalarni ko'rish uchun bosing👇"


def c_example_get_caption(description: str, indx: int = 0) -> str:
    if indx != 0:
        return f'{indx} - namuna \n\n' \
            f"Tavsif: <b>{description}</b>"
    else:
        return f"\n\nTavsif: <b>{description}</b>\n\n👉@midjourney_imagebot"


c_create_description = 'Marhamat tassavuringizdagi suratni so\'zlar yordamida bayon qilib bering. \n\n🖋<i>Matnni kiriting...</i>'
c_null_base = 'Bizda hali namunalar mavjud emas.'
c_example = 'Namunalar🏞'
c_create = 'Yaratish🤖'
c_contact = '📑Bog\'lanish'
c_about_us = "Biz haqimizda 👁️"
c_error_words = '🛠Botda texnik ishlar olib borilmoqda. Birozdan keyin qayta urinib ko\'ring.\n\n<i>Keltirilgan noqulayliklar uchun uzr so\'raymiz!</i>'
c_block_words = '📌12 soatda 2 marta so\'rov jo\'natishingiz mumkin. \n\nSizni so\'rovingiz limitdan oshdi. 12 soatdan keyin qayta ishlatishingiz mumkin'
c_contact_message = "📥Marhamat murojaatingizni yo'llang:"
c_cancel = '🔙Ortga',
c_create_image = '🖍Rasm chizilmoqda...'
c_send_admin_succsess = '✔Murojjat muaffaqiyatli jo\'natildi, Tez orada javob qaytariladi.'
