import os
import sys
import subprocess


def ruta_recurso(rel_path):
    ruta_pdf = ruta_recurso(os.path.join("documentosCarpeta", "ManualdeusuarioRAG.pdf"))

    if sys.platform.startswith('win'):
        os.startfile(ruta_pdf)
    elif sys.platform.startswith('darwin'):
        subprocess.call(['open', ruta_pdf])
    else:
        subprocess.call(['xdg-open', ruta_pdf])
        
def abrir_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta donde está documentos.py
    ruta_pdf = os.path.join(base_dir, "documentosCarpeta", "ManualdeusuarioRAG.pdf")

    if sys.platform.startswith('win'):  # Windows
        os.startfile(ruta_pdf)
    elif sys.platform.startswith('darwin'):  # macOS
        subprocess.call(['open', ruta_pdf])
    else:  # Linux (y otros Unix)
        subprocess.call(['xdg-open', ruta_pdf])


def abrir_readme():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta donde está documentos.py
    ruta_pdf = os.path.join(base_dir, "documentosCarpeta", "creditos.pdf")

    if sys.platform.startswith('win'):  # Windows
        os.startfile(ruta_pdf)
    elif sys.platform.startswith('darwin'):  # macOS
        subprocess.call(['open', ruta_pdf])
    else:  # Linux (y otros Unix)
        subprocess.call(['xdg-open', ruta_pdf])
