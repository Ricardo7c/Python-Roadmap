import tkinter
from tkinter import ttk

def update_label(volume):
    """Atualiza o texto do Label com o valor do volume."""
    label.config(text=f"Volume: {int(float(volume))}%")

# Janela principal
janela = tkinter.Tk()
janela.title("Controle de Volume")
janela.geometry("300x150")

# Label para exibir o volume
label = ttk.Label(janela, text="Volume: 50%", font=("Arial", 14))
label.pack(pady=20)

# Scale para controle do volume
volume_scale = ttk.Scale(
    janela, from_=0, to=100, orient="horizontal", command=update_label
)
volume_scale.set(50)  # Valor inicial
volume_scale.pack(fill="x", padx=20)

# Loop principal
janela.mainloop()
