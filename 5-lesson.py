# Создание бота
# Урок 8  Задание 5  Искуственный интелект

print("Привет! Я бот созданный человеком\n")
print("Я хочу выбрать тебе подарок!\n")
print("Ты должен выбрать какой тебе нравится чтобы я тебе подарил\n")
komputers = ['MAC OS', 'Компьютер с Kali Linux', 'Компьютер с Windows 11']
print(komputers)
print("Если хочешь Apple введи 'Mac Os', 'Windows', 'linux'\n")

while True:
    try:
        shell = input()
        if shell == 'mac os':
            print("Хорошо! Забирай")
            break

        elif shell == 'macos':
            print("Хорошо! Забирай")
            break

        elif shell == 'MAC OS':
            print("Хорошо! Забирай ")
            break

        elif shell == 'MACOS':
            print("Хорошо! Забирай")
            break

        elif shell == 'Linux':
            print("Хорошо! Забирай")
            break

        elif shell == 'linux':
            print("Хорошо! Забирай")
            break

        elif shell == 'LINUX':
            print("Хорошо! Забирай")
            break

        elif shell == 'windows':
            print("Хорошо! Забирай")
            break

        elif shell == 'WINDOWS':
            print("Хорошо! Забирай")
            break

        elif shell == 'Windows':
            print("Хорошо! Забирай")
            break

        else:
            print("У меня к сожалению нету таких подарков :(")
    except:
        print("У меня к сожалению нету таких подарков :(")
