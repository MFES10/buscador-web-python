import tkinter as tk
import webbrowser
from os import path

directorio_actual = path.dirname(path.abspath(__file__))

# Creación de la ventana
root = tk.Tk()
root.title('Buscador Web')
root.iconbitmap(f'{directorio_actual}\icon.ico')
root.resizable(False, False)

# Lista de sitios web
sitios_web = {
    'GG': 'https://www.google.com',
    'FB': 'https://www.facebook.com',
    'TW': 'https://www.twitter.com',
    'IG': 'https://www.instagram.com',
    'SC': 'https://www.snapchat.com',
    'LI': 'https://www.linkedin.com',
    'PT': 'https://www.pinterest.com',
    'TT': 'https://www.tiktok.com',
    'YT': 'https://www.youtube.com',
    'WA': 'https://web.whatsapp.com',
    'TG': 'https://web.telegram.org',
    'SF': 'https://open.spotify.com',
    'RD': 'https://www.reddit.com',
    'TM': 'https://www.tumblr.com',
    'WC': 'https://www.wechat.com',
    'SK': 'https://www.skype.com',
    'DC': 'https://www.discord.com',
    'TC': 'https://www.twitch.tv',
    'SL': 'https://www.slack.com',
    'VM': 'https://www.vimeo.com',
    'MD': 'https://www.medium.com',
    'QR': 'https://www.quora.com'
}

# Abrir búsqueda con el navegador
def openNav(url):
    webbrowser.open(url)

    '''
    # Use el siguiente código si necesita usar otro navegador diferente al por defecto de su sistema operativo
    # El ejemplo proporciona la ruta del navegador Firefox Developer Edition, cambie la ruta por la del navegador que desea usar
    
    navegador_path = (
        "C:/Program Files/Firefox Developer Edition/firefox.exe %s"
    )
    webbrowser.get(navegador_path).open(url)
    '''


# Limpiar la entrada de búsquedas
def borrar():
    sitio.set('')


# Realizar búsqueda
def buscar():
    busqueda = str(sitio.get())

    if busqueda.upper() in sitios_web:
        openNav(sitios_web[busqueda.upper()])
    else:
        openNav(f'https://www.google.com/search?q={busqueda}')
    
    ent_entrada.delete(0, tk.END)


def buscar_enter(event):
    if event.keysym == 'Return':
        buscar()
        ent_entrada.delete(0, tk.END)


sitio = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.grid(row=0, column=0, columnspan=2)

ent_entrada = tk.Entry(frame, border=1, textvariable=sitio, width=30)
ent_entrada.grid(row=0, column=0, padx=10)
ent_entrada.bind('<KeyRelease>', buscar_enter)
ent_entrada.focus_set()

btn_buscar = tk.Button(frame, text="Buscar", command=buscar, bg="#32cd32", fg="black", relief="groove")
btn_buscar.grid(row=0, column=1, padx=5)

btn_borrar = tk.Button(frame, text="Borrar", command=borrar, bg="#cd0000", fg="white", relief="groove")
btn_borrar.grid(row=0, column=2, padx=5)

lbl_watermark = tk.Label(root, text="Desarrollado por MFES")
lbl_watermark.grid(row=1, column=0, pady=5)

lbl_version = tk.Label(root, text="Versión v1.0.0")
lbl_version.grid(row=1, column=1, pady=5)


root.mainloop()
