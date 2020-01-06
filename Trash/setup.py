import os, shutil, sys, time

try:
    print("Trying import cx_Freeze")
    time.sleep(2)
    import cx_Freeze
except:
    print("Failed!")
    print("You don't have cx_Freeze. Do you wan't install? (Y|n)", end=" ")
    if (input().upper() == "Y"):
        os.system("pip install cx_Freeze")
        import cx_Freeze
    else:
        sys.exit()

exe = [cx_Freeze.Executable("main.py", base = "Win32GUI")] # <-- HERE
build_exe_options = {'build_exe': '3.14 Doors'}

cx_Freeze.setup(
    name = "3.14 Click",
    version = "1.0",
    options = {"build_exe": build_exe_options},
    executables = exe
)

shutil.move("Images", "3.14 Doors\\Images")
shutil.move("Levels", "3.14 Doors\\Levels")
shutil.move("Saves", "3.14 Doors\\Saves")
shutil.move("Classes", "3.14 Doors\\Classes")
shutil.move("Languages", "3.14 Doors\\Languages")
shutil.move("Sounds", "3.14 Doors\\Sounds")
os.remove("main.py")
os.remove("setup.py")