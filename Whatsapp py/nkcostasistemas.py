from selenium import webdriver
import pyautogui
import time
from io import BytesIO
import win32clipboard
from PIL import Image
import pyperclip as pc
import threading
import os


def send_image_to_clipboard(clip_type, filepath):
    image = Image.open(filepath)

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


def send_image(caminho):
    with open(caminho, 'r') as f:
        numeros_txt = f.readlines()
        numeros_txt = [x.rstrip('\n') for x in numeros_txt]
    lista = []
    for x in numeros_txt:
        item = x
        for y in ['\n', '\t', '/', '.', '-', '(', ')', ' ']:
            item = item.replace(y, "")
        lista.append(item)
    for x in range(len(lista)):
        driver = webdriver.Chrome()
        driver.get('https://api.whatsapp.com/send?phone=55' + lista[x])
        x += 1
        time.sleep(3)
        pyautogui.click(579, 249)
        time.sleep(2)
        pyautogui.click(644, 1012)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)


def send_text_and_image(caminho, imagem):
    with open(caminho, 'r') as f:
        numeros_txt = f.readlines()
        numeros_txt = [x.rstrip('\n') for x in numeros_txt]
    lista = []
    for x in numeros_txt:
        item = x
        for y in ['\n', '\t', '/', '.', '-', '(', ')', ' ']:
            item = item.replace(y, "")
        lista.append(item)
    for x in range(len(lista)):
        driver = webdriver.Chrome()
        driver.get('https://api.whatsapp.com/send?phone=55' + lista[x])
        x += 1
        time.sleep(3)
        pyautogui.click(579, 249)
        time.sleep(2)
        pyautogui.click(644, 1012)
        pc.copy(text)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        send_image_to_clipboard(win32clipboard.CF_DIB, imagem)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)


while True:
    menu = float(input('MENU\n'
                       '1- Enviar imagem\n'
                       '2- Enviar texto com imagem\n'
                       '3- Enviar tudo\n'
                       '0- Finalizar programa\n'))
    if menu == 0:
        print('Finalizando...')
        time.sleep(3)
        break
    if menu == 3:
        submenu = float(input('MENU\n'
                              '1- Enviar imagem\n'
                              '2- Enviar texto com imagem\n'
                              '0- Finalizar programa\n'))
        if submenu == 0:
            print('Finalizando...')
            time.sleep(3)
            break
        if submenu == 1:
            send_image_to_clipboard(win32clipboard.CF_DIB, 'vence_5dias.jpg')
            send_image('vence_5dias.txt')
            send_image_to_clipboard(win32clipboard.CF_DIB, 'Vence_hoje.jpg')
            send_image('vence_hoje.txt')
            send_image_to_clipboard(win32clipboard.CF_DIB, 'Vencido_dias.jpg')
            send_image('vencido_dias.txt')
            break
        while True:
            if submenu == 2:
                text = input('Qual texto você deseja enviar ?\n')
                confirmacao = input('Confirma este texto? S/N\n')
                if confirmacao in 'Ss':
                    send_text_and_image('Vence_5dias.txt', 'vence_5dias.jpg')
                    send_text_and_image('vence_hoje.txt', 'vence_hoje.jpg')
                    send_text_and_image('vencido_dias.txt', 'vencido_dias.jpg')
                break
    elif menu == 1 or menu == 2:
        while True:
            submenu = float(input('MENU\n'
                                  '1- Vai_vencer\n'
                                  '2- Vence_hoje\n'
                                  '3- Vencido_dias\n'
                                  '0- Voltar ao menu anterior\n'))

            if menu == 1 and submenu == 1:
                send_image_to_clipboard(win32clipboard.CF_DIB, 'vence_5dias.jpg')
                send_image('Vence_5dias.txt')
            if menu == 1 and submenu == 2:
                send_image_to_clipboard(win32clipboard.CF_DIB, 'Vence_hoje.jpg')
                send_image('vence_hoje.txt')
            if menu == 1 and submenu == 3:
                send_image_to_clipboard(win32clipboard.CF_DIB, 'vencido_dias.jpg')
                send_image('vencido_dias.txt')
            if menu == 2 and submenu == 1:
                text = input('Qual texto você deseja enviar ?\n')
                confirmacao = input('Confirma este texto? S/N\n')
                if confirmacao in 'Ss':
                    send_text_and_image('Vence_5dias.txt', 'vence_5dias.jpg')
            if menu == 2 and submenu == 2:
                text = input('Qual texto você deseja enviar ?\n')
                confirmacao = input('Confirma este texto? S/N\n')
                if confirmacao in 'Ss':
                    send_text_and_image('vence_hoje.txt', 'vence_hoje.jpg')
            if menu == 2 and submenu == 3:
                text = input('Qual texto você deseja enviar ?\n')
                confirmacao = input('Confirma este texto? S/N\n')
                if confirmacao in 'Ss':
                    send_text_and_image('vencido_dias.txt', 'vencido_dias.jpg')
            if submenu == 0:
                break

    else:
        print('Opção inválida.')
        time.sleep(2)
