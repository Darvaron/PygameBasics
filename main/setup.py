import cx_Freeze

executables = [cx_Freeze.Executable("Main.py")]

cx_Freeze.setup(
    name="Test game",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["car.png","icon.png","crash.wav","music.wav"]}},
    executables=executables
)
