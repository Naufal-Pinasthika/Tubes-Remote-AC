import tkinter as tk
from tkinter import messagebox

# Status AC
is_on = False
temperature = 24
mode_options = ["Cool", "Fan", "Dry"]
fan_speed_options = ["Low", "Medium", "High"]
current_mode = mode_options[0]
current_fan_speed = fan_speed_options[0]

# Fungsi untuk setiap tombol
def toggle_power():
    global is_on
    is_on = not is_on
    status = "On" if is_on else "Off"
    print(f"AC is now {status}")
    messagebox.showinfo("Power", f"AC is now {status}")

def increase_temp():
    global temperature
    if is_on:
        temperature += 1
        print(f"Temperature increased to {temperature}°C")
    else:
        print("AC is off. Turn it on first.")

def decrease_temp():
    global temperature
    if is_on:
        temperature -= 1
        print(f"Temperature decreased to {temperature}°C")
    else:
        print("AC is off. Turn it on first.")

def change_mode():
    global current_mode
    if is_on:
        current_mode_index = mode_options.index(current_mode)
        current_mode = mode_options[(current_mode_index + 1) % len(mode_options)]
        print(f"Mode changed to {current_mode}")
    else:
        print("AC is off. Turn it on first.")

def change_fan_speed():
    global current_fan_speed
    if is_on:
        current_fan_speed_index = fan_speed_options.index(current_fan_speed)
        current_fan_speed = fan_speed_options[(current_fan_speed_index + 1) % len(fan_speed_options)]
        print(f"Fan speed changed to {current_fan_speed}")
    else:
        print("AC is off. Turn it on first.")

# Fungsi untuk menampilkan status AC di terminal
def display_status():
    power_status = "On" if is_on else "Off"
    print("\n=== Status AC ===")
    print(f"Power: {power_status}")
    print(f"Temperature: {temperature}°C")
    print(f"Mode: {current_mode}")
    print(f"Fan Speed: {current_fan_speed}")
    print("=================")

# Set up GUI dengan Tkinter
root = tk.Tk()
root.title("Remote AC Simulation")

# Label untuk miniatur gambar remote
remote_label = tk.Label(root, text="Remote AC", font=("Helvetica", 16, "bold"))
remote_label.pack(pady=10)

# Tambahkan tombol-tombol ke GUI
btn_power = tk.Button(root, text="Power On/Off", width=30, command=toggle_power)
btn_power.pack(pady=5)

btn_temp_up = tk.Button(root, text="Temperature +", width=30, command=increase_temp)
btn_temp_up.pack(pady=5)

btn_temp_down = tk.Button(root, text="Temperature -", width=30, command=decrease_temp)
btn_temp_down.pack(pady=5)

btn_mode = tk.Button(root, text="Mode (Cool/Fan/Dry)", width=30, command=change_mode)
btn_mode.pack(pady=5)

btn_fan_speed = tk.Button(root, text="Fan Speed (Low/Medium/High)", width=30, command=change_fan_speed)
btn_fan_speed.pack(pady=5)

btn_status = tk.Button(root, text="Show AC Status", width=30, command=display_status)
btn_status.pack(pady=5)

# Jalankan main loop
root.mainloop()
