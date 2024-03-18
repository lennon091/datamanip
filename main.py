import os

from domain.archive import Archive

if __name__ == '__main__':
    pass

if __name__ == '__main__':
    file_name = "transparencia.csv"
    arquivo = Archive(file_name)
    if os.path.exists(file_name):
        pass
    else:
        arquivo.create_archive()


