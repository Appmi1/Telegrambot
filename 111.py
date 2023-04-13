import os
import PyPDF2
import telegram
from telegram.ext import CommandHandler, Updater

# Replace YOUR_API_TOKEN with your actual API token
bot = telegram.Bot(token='6218090132:AAGpEtEsDQUPlyr8r2Og5k5BLAjOJR5x9fs')

# Define the phone numbers and corresponding PDF file pathsb
pdf_paths = {
    '1': '/Users/maksimkurdinovic/PycharmProjects/pythonProject1/1.pdf',
    '12': '/User/maksimkurdinovic/PycharmProjects/pythonProject1/12.pdf',
    '123': '/Users/maksimkurdinovic/PycharmProjects/pythonProject1/123.pdf',
    '1234': '/Users/maksimkurdinovic/PycharmProjects/pythonProject1/1234.pdf',
    '12345': '/Users/maksimkurdinovic/PycharmProjects/pythonProject1/12345.pdf',
}


def start(update, context):
    update.message.reply_text('Please enter your phone number')


def doc(update, context):
    phone_number = update.message.contact.phone_number

    if phone_number is None:
        update.message.reply_text('Please provide a phone number')
        return

    pdf_path = pdf_paths.get(phone_number)

    if pdf_path is None or not os.path.exists(pdf_path):
        update.message.reply_text('Document not found')
        return

    try:
        with open(pdf_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            document = pdf_reader.getPage(0).extractText()
    except Exception as e:
        update.message.reply_text(f'An error occurred while processing the document: {str(e)}')
        return

    update.message.reply_document(document=document, filename=f'{phone_number}.pdf')


# Create an Updater object and attach the command handler
updater= Updater(token='6218090132:AAGpEtEsDQUPlyr8r2Og5k5BLAjOJR5x9fs', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('doc', doc))




# Start polling for updates
updater.start_polling()


