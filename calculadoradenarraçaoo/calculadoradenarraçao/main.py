# pedir qual arquivo
time_in_sec = 0

# encontrar o arquivo
import os


def calculate(name):
    global time_in_sec
    def find_all(name, path):
        result = []
        for root, dirs, files in os.walk(path):
            if name in files:
                result.append(os.path.join(root, name))
        return result


    path_file = find_all(name, '/Users/vfx/VFX Vídeos Dropbox/TRAMPOS/')
    path_file = str(path_file[0])
    print(path_file)
    # abrir o arquivo e ler o conteúdo

    import docx2txt

    my_text = docx2txt.process(path_file).split()
    print(my_text)
    position_list = [index for (index, item) in enumerate(my_text) if item == "*"]

    # calcular duraçao em segundos

    total_words = int(position_list[1]) - int(position_list[0] + 1)
    time_in_sec = 81 / 2.5
    time_in_sec = int(round(time_in_sec))
    # retornar resultado

    print(f'Esse roteiro tem {time_in_sec} segundos')

    # renomear file
    list_path = path_file.split('_')
    print(list_path)
    version = list_path[7].split('.')
    new_version = int(version[0]) +1
    if new_version <10:
        new_version = f'0{new_version}'

    os.rename(
        path_file,
        f"{list_path[0]}_{list_path[1]}_{list_path[2]}_{list_path[3]}_{list_path[4]}_{list_path[5]}_{time_in_sec}s_{new_version}.docx")

    new_path = f"{list_path[0]}_{list_path[1]}_{list_path[2]}_{list_path[3]}_{list_path[4]}_{list_path[5]}_{time_in_sec}s_{new_version}.docx"
    return new_path