#GUITranslator.py
from tkinter import *
#จากไลบรารี ชื่อ tkinter, * คือให้ดึงความสามารถหลักมาทั้งหมด
from tkinter import ttk
#ttk is theme of tk
from googletrans import Translator
translator = Translator()

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x500')
GUI.title('โปรแกรมแปลภาษา')
#-----Config-----
FONT = ('Angsana New',15)

#-----Label------
L = ttk.Label(GUI, text = 'กรุณากรอกคำศัพท์ที่ต้องการแปล', font = FONT)
L.pack()
# ----Entry-----
v_vocab  = StringVar() #กล่องเก็บข้อความ

E1 = ttk.Entry(GUI, textvariable = v_vocab, font = FONT, width = 40)
E1.pack(pady=20)


# ----Button----
def Translate():
    vocab = v_vocab.get() #.get คือ ให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest = 'th')
    print(vocab + ' : ' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text)

B1 = Button(GUI, text = 'Translate', command = Translate) #สร้างปุ่มขึ้นมา
B1.pack(ipadx=20, ipady = 10) #show ปุ่มขึ้นมาวางจากบนลงล่าง


#-----Label------
L = ttk.Label(GUI, text = 'คำแปล', font = FONT)
L.pack()

#-----Result------
v_result = StringVar() #กล่องสำหรับเก็บคำแปล

R = ttk.Label(GUI, textvariable = v_result, font = FONT, foreground = 'green')
R.pack() 

GUI.mainloop() # ทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด
