import pypdfium2 as pdfium
from PIL import Image
import pytesseract
import easyocr
import cv2
import os
import warnings
# filter warnings
warnings.filterwarnings('ignore')


# Load a document
pdf = pdfium.PdfDocument("example.pdf")
# Loop over pages and render
for i in range(len(pdf)):
    page = pdf[i]
    image = page.render(scale=4).to_pil()
    image.save(f"output/output{i}.jpg")


#convert image to text method 1
file = "output/output0.jpg"
img = cv2.imread(file)
reader = easyocr.Reader(['ar'],gpu=True)
res = reader.readtext(img)
text = ""
for i in range(len(res)):
        text+=res[i][1]
        text+=" "
#print(text)
with open("output/text1.txt", "w", encoding="utf-8") as file:
    file.write(text)

#convert image to text method 2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'
def extract_arabic_text(image_path, output_file):
    # Open the image
    img = Image.open(image_path)
    # Configure Tesseract for Arabic OCR
    custom_config = r'--oem 3 --psm 6 -l ara'
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img, config=custom_config)
    # Save the extracted text to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)
# Example usage
image_path = 'output/output0.jpg'
output_file_path = 'output/text2.txt'
extract_arabic_text(image_path, output_file_path)


##################################
#using chatgpt to predict the Q&A#
##################################

from dotenv import load_dotenv
import os
import openai

# Load environment variables from the .env file
print("set your chatgpt token in .env file")
load_dotenv()
gpt = os.environ.get('chatgpt_token')

if gpt == "":
    print("Please set your OpenAI API Key in the .env file...")
else:
    print("API Key loaded successfully.")

# File paths
file1_path = "output/text1.txt"
file2_path = "output/text2.txt"
qa_output_path = "output/Q&A.txt"

with open(file1_path, 'r', encoding="utf-8") as file:
    content1 = file.read()

with open(file2_path, 'r', encoding="utf-8") as file:
    content2 = file.read()

# Initialize OpenAI API key
if gpt != "":
    openai.api_key = gpt

    all_messages = []

    message = f"I have this text:\n{content1}\n"
    all_messages.append({'role': 'user', 'content': message})

    message = f"And also, I have this text:\n{content2}\n"
    all_messages.append({'role': 'user', 'content': message})

    user_input = 'انطلاقًا من النصين استخرج 5 أسئلة، تتضمن هذه الأسئلة بعض الأسئلة ذات إجابة مباشرة، و اسئلة ذات إجوبة متعددة واسئلة صحيح او خطأ، وارفق بكل سؤال الجواب الصحيح'
    all_messages.append({'role': 'user', 'content': user_input})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=all_messages,
        temperature=0
    )

    reply = response['choices'][0]['message']['content']
    all_messages.append({"role": "assistant", "content": reply})

    #print(reply)
    # Save Q&A to a file
    with open(qa_output_path, 'a', encoding='utf-8') as qa_file:
        qa_file.write(f"Question: {user_input}\nAnswer: {reply}\n\n")

    print(f"Q&A saved to {qa_output_path}")