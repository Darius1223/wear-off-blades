import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["PyQt5"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="WearOfBlades",
    version="0.1",
    description="WearOfBlades GUI application",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            script="app.py",
            base=base,
            icon="images/Icon1.ico",
            target_name="WearOfBlades",
            shortcut_name="WearOfBlades",
            shortcut_dir="WearOfBlades",
            copyright="Copyright (C) 2022 WearOfBlades",
        )
    ],
)
