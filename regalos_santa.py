# -*- coding: utf-8 -*-

def palindromo (id:int)->bool:
    return str(id) == str(id)[::-1]

def par_impar (id:int)->bool:
    return id % 2 == 0

def clasificar_regalo (id:int)->str:
    decision_palindromo = palindromo(id)
    decision_par = par_impar(id)

    mensaje_retorno = ""

    if decision_palindromo and decision_par:
        mensaje_retorno = "boy"
    elif decision_palindromo and not decision_par:
        mensaje_retorno = "girl"

    elif decision_palindromo == False and decision_par == False:
        mensaje_retorno = "woman"
    else:
        mensaje_retorno = "man"
    
    return mensaje_retorno
