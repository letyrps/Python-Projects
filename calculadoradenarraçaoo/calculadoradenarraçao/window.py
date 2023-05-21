import tkinter as tk
from tkinter import messagebox, INSERT
from PIL import ImageTk, Image
from main import calculate

BG_COLOR = '#34495E'

window = tk.Tk()
window.title("Calculadora de narração")
window.minsize(width=500, height=450)


canvas = tk.Canvas(width=500, height=450, background=BG_COLOR)
canvas.config(background=BG_COLOR)
title = tk.Label(text='Calculadora de Narração', font=('Arial', 24, 'bold'), background=BG_COLOR, fg='#ECF0F1')
canvas.create_window(250, 50, window=title)
file_name_entry = tk.Entry(bg="white", width=50, borderwidth=2)
explanation_label = tk.Label(text='Calcula o tempo em segundos de cada roteiro e renomeia o arquivo com o tempo correto', font=('Arial', 10, 'normal'), background=BG_COLOR, fg='#ECF0F1')
canvas.create_window(250, 90, width=500, window=explanation_label)

def temp_text(e):
   file_name_entry.delete(0, "end")
file_name_entry.insert(0, "Cole o nome do arquivo aqui:")
file_name_entry.bind("<FocusIn>", temp_text)
canvas.create_window(250, 120, window=file_name_entry)
canvas.pack()


def action():
   name = file_name_entry.get()
   file_name_entry.delete(0, "end")
   new_name = calculate(name)
   messagebox = tk.messagebox.showinfo(title='Sucesso!', message=f'Arquivo renomeado com sucesso!')
   label_answer = tk.Label(text=f'O arquivo {name} foi alterado para:', width=65, font=('Arial', 12, 'normal'))
   canvas.create_window(250, 200, window=label_answer)
   text_box = tk.Text(height=2, width=75, font=('Arial', 10, 'normal'))
   text_box.focus()
   text_box.insert(INSERT, f"{new_name}")
   canvas.create_window(250, 230, window=text_box)
   text_box_importante = tk.Text(height=2, width=75, font=('Arial', 10, 'bold'))
   text_box_importante.focus()
   timeinsec = new_name.split('_')
   timeinsec = str(timeinsec[6])
   timeinsec = timeinsec[0:2]
   print(timeinsec)
   text_box_importante.insert(INSERT, f"IMPORTANTE: Tempo de duração estimado {timeinsec}, o roteiro pode ter até {int(int(timeinsec)*2.5)} palavras narradas para o tempo contratado")
   canvas.create_window(250, 270, window=text_box_importante)


img = (Image.open("click-me-button-flat.png"))
resized_image = img.resize((70, 20), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)
button_calculate = tk.Button(image=new_image, command=action, background=BG_COLOR, fg=BG_COLOR)
canvas.create_window(250, 160, window=button_calculate)

rules_label = tk.Label(width=50,
                       text='Para funcionar é necessário colocar o texto do roteiro\n entre * com espaços, como no exemplo abaixo:\n*\nEsse é um exemplo de roteiro, todo o conteúdo a ser narrado,\n deverá estar aqui, dentro.\nPasso 1: colocar os **\n Passo 2: clicar no botão\nPasso 3: copiar o conteudo do campo importante\n e colar no documento\nPasso 4: Sucesso!\n*')
canvas.create_window(250, 300, window=rules_label)

window.mainloop()
