from tkinter import *
from tkinter import messagebox
from experta import *

# Definisi Sistem Pakar
class FoodIntoleranceDiagnosis(KnowledgeEngine):
    @Rule(Fact(sakit_perut=True) & Fact(kembung=True) & Fact(diare=True))
    def intoleransi_laktosa(self):
        self.declare(Fact(diagnosis="Intoleransi Laktosa"))

    @Rule(Fact(sakit_kepala=True) & Fact(cemas=True) & Fact(detak_kencang=True))
    def intoleransi_kafein(self):
        self.declare(Fact(diagnosis="Intoleransi Kafein"))

    @Rule(Fact(ruam_kulit=True) & Fact(mual_muntah=True) & Fact(sakit_perut=True))
    def intoleransi_gluten(self):
        self.declare(Fact(diagnosis="Intoleransi Gluten"))

    @Rule(Fact(kentut_berlebih=True) & Fact(sakit_perut=True))
    def intoleransi_fruktosa(self):
        self.declare(Fact(diagnosis="Intoleransi Fruktosa"))

    @Rule(Fact(sulit_tidur=True) & Fact(cemas=True))
    def intoleransi_histamin(self):
        self.declare(Fact(diagnosis="Intoleransi Histamin"))

    @Rule(Fact(diagnosis=None))  
    def tidak_intoleransi(self):
        self.declare(Fact(diagnosis="Tidak ada intoleransi terhadap jenis makanan apapun."))

# Fungsi untuk Menjalankan Diagnosis
def run_diagnosis():
    gejala = {
        "sakit_perut": var_sakit_perut.get(),
        "kembung": var_kembung.get(),
        "diare": var_diare.get(),
        "sakit_kepala": var_sakit_kepala.get(),
        "sakit_sendi": var_sakit_sendi.get(),
        "ruam_kulit": var_ruam_kulit.get(),
        "cemas": var_cemas.get(),
        "detak_kencang": var_detak_kencang.get(),
        "kentut_berlebih": var_kentut_berlebih.get(),
        "mual_muntah": var_mual_muntah.get(),
        "sulit_tidur": var_sulit_tidur.get(),
    }

    engine = FoodIntoleranceDiagnosis()
    engine.reset()

    for key, value in gejala.items():
        engine.declare(Fact(**{key: value}))

    engine.run()

    diagnosis = None
    for fact in engine.facts.values():
        if "diagnosis" in fact:
            diagnosis = fact["diagnosis"]
            break

    if diagnosis:
        messagebox.showinfo("Hasil Diagnosis", diagnosis)
        show_recommendation_page(diagnosis)
    else:
        messagebox.showinfo("Hasil Diagnosis", "Tidak ada diagnosis yang cocok.")

# Fungsi untuk Menampilkan Halaman Saran Makanan
def show_recommendation_page(diagnosis):
    diagnosis_frame.pack_forget()
    recommendation_frame.pack(fill="both", expand=True)
    
    Label(
    recommendation_frame, 
    text="Hasil Diagnosis", 
    font=("Arial", 17, "bold"), 
    bg="#085DB4", 
    fg="white", 
    pady=20, 
    width=50, 
    anchor="center").pack()
    
    Label(recommendation_frame, text=f"Diagnosis: {diagnosis}", font=("Arial", 14), pady=10, bg="#FFFFFF").pack()

    # Menampilkan saran makanan berdasarkan diagnosis
    if diagnosis == "Intoleransi Laktosa":
        saran = "Makanan yang disarankan: Susu bebas laktosa, kedelai, almond."
    elif diagnosis == "Intoleransi Kafein":
        saran = "Makanan yang disarankan: Teh herbal, air putih, jus buah."
    elif diagnosis == "Intoleransi Gluten":
        saran = "Makanan yang disarankan: Beras, kentang, sayuran, buah."
    elif diagnosis == "Intoleransi Fruktosa":
        saran = "Makanan yang disarankan: Daging tanpa lemak, telur, nasi putih."
    elif diagnosis == "Intoleransi Histamin":
        saran = "Makanan yang disarankan: Daging segar, sayuran hijau, beras."
    else:
        saran = "Tidak ada intoleransi yang ditemukan, Anda dapat makan makanan normal."

    Label(recommendation_frame, text=saran, font=("Arial", 14), wraplength=500, justify="left", padx=20, bg="#FFFFFF").pack(pady=10)

    Button(recommendation_frame, text="Kembali", command=show_welcome_page, font=("Arial", 14), bg="#dc3545", fg="white").pack(pady=20)

# Halaman Pengenalan
def show_diagnosis_page():
    welcome_frame.pack_forget()
    diagnosis_frame.pack(fill="both", expand=True)

# Halaman Awal
def show_welcome_page():
    recommendation_frame.pack_forget()
    diagnosis_frame.pack_forget()
    welcome_frame.pack(fill="both", expand=True)
    reset_checkbox()

# Fungsi untuk Mereset Checkbox
def reset_checkbox():
    for var in [var_sakit_perut, var_kembung, var_diare, var_sakit_kepala, var_sakit_sendi, var_ruam_kulit, var_cemas, var_detak_kencang, var_kentut_berlebih, var_mual_muntah, var_sulit_tidur]:
        var.set(False)


def center_window(root, width=619, height=700):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
# Antarmuka Pengguna
root = Tk()
root.title("Diagnosis Intoleransi Makanan")
root.configure(bg="#FFFFFF") 
center_window(root)

# Frame Halaman Pengenalan

welcome_frame = Frame(root, bg="#FFFFFF") 
welcome_frame.pack(fill="both", expand=True)

Label(
    welcome_frame, 
    text="Diagnosis Intoleransi Makanan", 
    font=("Arial", 24, "bold"), 
    bg="#085DB4", 
    fg="white", 
    pady=20, 
    width=50, 
    anchor="center"  
).pack()
Label(
    welcome_frame,
    text=(  
        "Selamat datang di aplikasi diagnosis intoleransi makanan.\n"
        "Berikut adalah beberapa jenis intoleransi yang dapat kami periksa:\n\n"
        "1. Intoleransi Laktosa\n"
        "2. Intoleransi Kafein\n"
        "3. Intoleransi Gluten\n"
        "4. Intoleransi Fruktosa\n"
        "5. Intoleransi Histamin\n\n"
        "Klik tombol di bawah ini untuk memulai diagnosis."
    ),
    font=("Arial", 14),
    bg="#FFFFFF", 
    fg="black",
    justify="left",
    padx=30,
    pady=30,
).pack()

Button(welcome_frame, text="Periksa Sekarang", command=show_diagnosis_page, font=("Arial", 14), bg="#085DB4", fg="white", padx=10, pady=5).pack(pady=20)

# Frame Halaman Diagnosis
diagnosis_frame = Frame(root, bg="#FFFFFF")  

Label(
    diagnosis_frame, 
    text="Gejala- Gejala yang Dialami:",
    font=("Arial", 17, "bold"), 
    bg="#085DB4", 
    fg="white", 
    pady=20, 
    width=50, 
    anchor="center"  
).pack()

# Variabel untuk checkbox
var_sakit_perut = BooleanVar()
var_kembung = BooleanVar()
var_diare = BooleanVar()
var_sakit_kepala = BooleanVar()
var_sakit_sendi = BooleanVar()
var_ruam_kulit = BooleanVar()
var_cemas = BooleanVar()
var_detak_kencang = BooleanVar()
var_kentut_berlebih = BooleanVar()
var_mual_muntah = BooleanVar()
var_sulit_tidur = BooleanVar()

checkboxes = [
    ("Sakit perut", var_sakit_perut),
    ("Kembung", var_kembung),
    ("Diare", var_diare),
    ("Sakit kepala", var_sakit_kepala),
    ("Sakit sendi", var_sakit_sendi),
    ("Ruam kulit", var_ruam_kulit),
    ("Cemas", var_cemas),
    ("Detak kencang", var_detak_kencang),
    ("Kentut berlebih", var_kentut_berlebih),
    ("Mual muntah", var_mual_muntah),
    ("Sulit tidur", var_sulit_tidur),
]

# Membuat checkbox
for text, var in checkboxes:
    Checkbutton(diagnosis_frame, text=text, variable=var, font=("Arial", 14), bg="#FFFFFF", fg="black").pack(anchor="w", padx=40, pady=2)

# Menambah tombol Diagnosa di kanan dan tombol Kembali di kiri
button_frame = Frame(diagnosis_frame, bg="#FFFFFF")
button_frame.pack(fill="x", pady=20)

Button(button_frame, text="Diagnosa", command=run_diagnosis, font=("Arial", 12), bg="#085DB4", fg="white", padx=10, pady=5).pack(side=LEFT, padx=20)
Button(button_frame, text="Kembali", command=show_welcome_page, font=("Arial", 12), bg="#dc3545", fg="white", padx=10, pady=5).pack(side=RIGHT, padx=20)


# Frame Halaman Rekomendasi Makanan
recommendation_frame = Frame(root, bg="#FFFFFF") 

# Tampilkan Halaman Pengenalan
show_welcome_page()

# Menambahkan label background biru di bagian bawah setiap halaman
def add_footer(frame):
    Label(frame, text="Sistem Pakar Diagnosis Intoleransi Makanan", font=("Arial", 10, "bold"), bg="#085DB4", fg="white", pady=10).pack(side=BOTTOM, fill=X)

# Tambahkan footer pada setiap frame
add_footer(welcome_frame)
add_footer(diagnosis_frame)
add_footer(recommendation_frame)


root.mainloop()