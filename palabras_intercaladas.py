# -*- coding: utf-8 -*-

def intercalar_cadenas(cad1:str, cad2: str)->str:
    
    """
    crear una frase a partir de dos string, los cuales tendras palabras 
    intercaladas
    
    Parameters
    ----------
    cad1 : str
        Un string con palabras separadas por espacios
    cad1 : str
        Un string con palabras separadas por espacios

    Returns
    -------
    str
        Un string con la frase resultante de unir una palabra intercalada de 
        cada string hasta el final de los mismo

    """
    
    resultado = ""
    
    palabras_1 = cad1.split()
    palabras_2 = cad2.split()
    
    for i in range(0, len(palabras_1)):
        resultado += (palabras_1[i] + " " + palabras_2[i] + " ")

    return resultado



c_1 = "La casa esta cerca río"
c_2 = "linda no muy del grande"

print(intercalar_cadenas(c_1, c_2))

