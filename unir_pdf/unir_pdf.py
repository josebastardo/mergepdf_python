# cogigo para unir archivos.pdf en direrents directorios
# Debe llenar la lista de directorios 

from PyPDF2 import PdfFileMerger
import os

paths=[
'/home/bastardo/Escritorio/Python3_POO-master/unir_pdf/',
 '/home/bastardo/Escritorio/Python3_POO-master/unir_pdf/uno/'

 ##listado de directorios
]

for i in range(len(paths)):
    try:
        lista_pdfs = os.listdir(paths[i])
    except FileNotFoundError:
      print(f" Depure la lista, el directorio -- {paths[i]} -- esta vacio ")
    else:
        archivo_salida =  f'salida_{i}.pdf'
        print(archivo_salida)

        file= PdfFileMerger()

        for pdf in lista_pdfs:
            if (pdf).endswith(".pdf"):
                file.append(open(f'{paths[i]}{pdf}', 'rb'))

        with open(f'{paths[i]}{archivo_salida}', 'wb') as salida:
            file.write(salida)

