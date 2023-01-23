# -*- coding: utf-8 -*-

def sumar_estadisticas(pokemon:dict)->int:
    """
    Suma las estadisticas de todos los pokemon y retorna la sumatoria

    Parameters
    ----------
    pokemon : dict
        Las estadisticas del pokemon.

    Returns
    -------
    int
        La sumatoria de las estadisticas del pokemon.

    """
    
    suma_stats = 0
    for stats in pokemon:
        if stats != 'nombre':
            suma_stats += pokemon[stats]

    return suma_stats


def construir_equipo_pokemon(cantidad:int, lista_pkmn:list)->list:
    """
    Determina si se puede crear un equipo pokemon solo con pokemons pseudolegendarios
    Si se puede retorna una lista con todos los nombre, si no retorna None

    Parameters
    ----------
    cantidad : int
        Cantidad de pokemons que habrá en la batalla.
    lista_pkmn : list
        Lista con los pokemon disponibles.

    Returns
    -------
    list
        Lista con el nombre de los pokemon que son pseudolegendarios.

    """
    nombres_pokemon = []

    for pokemon in range(0, len(lista_pkmn)):
        stats = sumar_estadisticas(lista_pkmn[pokemon])
        if stats >= 600:
            nombres_pokemon.append(lista_pkmn[pokemon]['nombre'])
    
    if len(nombres_pokemon) < cantidad:
        nombres_pokemon = None

    return nombres_pokemon

pokemons = lista_pkmn = [{'nombre': 'Rayquaza', 'vida': 120, 'ataque': 120, 'defensa': 120, 'ataque_especial': 120, 'defensa_especial': 120, 'velocidad': 120}, {'nombre': 'Arceus', 'vida': 120, 'ataque': 120, 'defensa': 120, 'ataque_especial': 120, 'defensa_especial': 120, 'velocidad': 120}, {'nombre': 'Solgaleo', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 200, 'defensa_especial': 100, 'velocidad': 100}, {'nombre': 'Charizard-X', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 50, 'defensa_especial': 50, 'velocidad': 100}, {'nombre': 'Greninja', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 100, 'defensa_especial': 100, 'velocidad': 100}, {'nombre': 'Swellow', 'vida': 60, 'ataque': 80, 'defensa': 50, 'ataque_especial': 70, 'defensa_especial': 60, 'velocidad': 150}, {'nombre': 'Pikachu', 'vida': 20, 'ataque': 20, 'defensa': 20, 'ataque_especial': 20, 'defensa_especial': 20, 'velocidad': 20}]

print(construir_equipo_pokemon(4, pokemons))