import customtkinter as ctk
from tkinter import messagebox

class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Sistem Perpustakaan")
        self.geometry("360x420")
        self.resizable(False, False)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(
            self.frame,
            text="LOGIN SISTEM",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15))

        self.entry_username = ctk.CTkEntry(
            self.frame, placeholder_text="Username"
        )
        self.entry_username.pack(pady=10, padx=20, fill="x")

        self.entry_password = ctk.CTkEntry(
            self.frame, placeholder_text="Password", show="*"
        )
        self.entry_password.pack(pady=10, padx=20, fill="x")

        self.btn_login = ctk.CTkButton(
            self.frame, text="Masuk", fg_color="blue"
        )
        self.btn_login.pack(pady=(15, 10), padx=20, fill="x")

        ctk.CTkLabel(
            self.frame,
            text="Belum punya akun?"
        ).pack(pady=(5, 0))

        self.btn_register = ctk.CTkButton(
            self.frame,
            text="Daftar Akun",
            fg_color="green",
            command=self.tampil_register
        )
        self.btn_register.pack(pady=(8, 15), padx=20, fill="x")

    def tampil_register(self):
        self.register_window = ctk.CTkToplevel(self)
        self.register_window.title("Registrasi Akun")
        self.register_window.geometry("360x400")
        self.register_window.resizable(False, False)

        frame_register = ctk.CTkFrame(self.register_window)
        frame_register.pack(
            pady=20, padx=20, fill="both", expand=True
        )

        ctk.CTkLabel(
            frame_register,
            text="REGISTRASI AKUN",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15))

        self.reg_username = ctk.CTkEntry(
            frame_register, placeholder_text="Username"
        )
        self.reg_username.pack(pady=10, padx=20, fill="x")

        self.reg_password = ctk.CTkEntry(
            frame_register, placeholder_text="Password", show="*"
        )
        self.reg_password.pack(pady=10, padx=20, fill="x")

        self.reg_role = ctk.CTkOptionMenu(
            frame_register,
            values=["anggota", "admin"]
        )
        self.reg_role.pack(pady=10, padx=20, fill="x")

        self.btn_simpan_register = ctk.CTkButton(
            frame_register,
            text="Daftar",
            fg_color="green",
            command=self.register_user
        )
        self.btn_simpan_register.pack(
            pady=(20, 10), padx=20, fill="x"
        )

    def register_user(self):
        username = self.reg_username.get().strip()
        password = self.reg_password.get()
        role = self.reg_role.get()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan password harus diisi!"
            )
            return

        # Nantinya hubungkan ke UserModel.register_user()
        messagebox.showinfo(
            "Informasi",
            f"Data registrasi siap diproses untuk username: {username}"
        )


if __name__ == "__main__":
    app = LoginView()
    app.mainloop()