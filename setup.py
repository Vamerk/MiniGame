from cx_Freeze import setup, Executable
import sys

# Список дополнительных файлов, которые нужно включить в сборку
include_files = [
    ('./data/AirH.png', 'data/AirH.png'),
    ('./data/cross.png', 'data/cross.png'),
    ('./data/game-controller.png', 'data/game-controller.png'),
    ('./data/nought.png', 'data/nought.png'),
    ('./data/SB.png', 'data/SB.png'),
    ('./data/sb_back.png', 'data/sb_back.png'),
    ('./data/start_screen.png', 'data/start_screen.png'),
    ('./data/TicTac.png', 'data/TicTac.png'),
    ('./sounds/bell.mp3', 'sounds/bell.mp3'),
    ('./sounds/click.mp3', 'sounds/click.mp3'),
    ('./sounds/goal.mp3', 'sounds/goal.mp3'),
    ('./sounds/hit.mp3', 'sounds/hit.mp3'),
    ('./sounds/restart.mp3', 'sounds/restart.mp3'),
    ('./sounds/SB_explosion.mp3', 'sounds/SB_explosion.mp3'),
    ('./sounds/SB_miss.mp3', 'sounds/SB_miss.mp3'),
    ('./sounds/snatch.mp3', 'sounds/snatch.mp3'),
    ('./sounds/start.mp3', 'sounds/start.mp3'),
    ('./sounds/win.mp3', 'sounds/win.mp3'),
    ('AirHockey.py', '.'),
    ('Board.py', '.'),
    ('constants.py', '.'),
    ('load_image.py', '.'),
    ('load_sound.py', '.'),
    ('TicTacToe.py', '.'),
    ('SeaBattle.py', '.'),
    ('SB_player1.txt', '.'),
    ('SB_player2.txt', '.'),
    ('style.json', '.')
]

# Определите базу (только для Windows)
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Используйте "Console" для консольных приложений

# Список используемых пакетов
packages = [
    "os",
    "pygame",
    "pygame_gui",
    "itertools",
]

# Создайте объект Executable
executables = [Executable("main.py", base=base)]

# Определите параметры настройки
setup(
    name="MiniGames",
    version="1.0",
    description="MiniGames Project",
    options={
        "build_exe": {
            "packages": packages,
            "include_files": include_files,
        }
    },
    executables=executables,
)