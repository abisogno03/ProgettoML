import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib

# Carica modello e scaler
model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_fraud():
    try:
        amount = float(entry_amount.get())
        time = float(entry_time.get())
        features = np.array([[time, amount]])
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]

        if prediction == 1:
            messagebox.showwarning("Risultato", "Transazione FRAUDOLENTA!")
        else:
            messagebox.showinfo("Risultato", "Transazione LEGITTIMA")
    except Exception as e:
        messagebox.showerror("Errore", f"Qualcosa è andato storto:\n{e}")

root = tk.Tk()
root.title("Fraud Detection - Demo")
root.geometry("400x250")

label_title = tk.Label(root, text="Fraud Detection App", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

label_time = tk.Label(root, text="Tempo (Time):")
label_time.pack()
entry_time = tk.Entry(root)
entry_time.pack()

label_amount = tk.Label(root, text="Importo (Amount):")
label_amount.pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

btn_predict = tk.Button(root, text="Verifica Transazione", command=predict_fraud, bg="blue", fg="white")
btn_predict.pack(pady=20)

root.mainloop()
