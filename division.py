def division(nombre1, nombre2):
    try:
        # Effectuer la division
        resultat = nombre1 / nombre2
        return resultat
    except ZeroDivisionError:
        print("Erreur : Division par zéro n'est pas autorisée.")
        return None

# Exemple d'utilisation de la fonction
nombre1 = 10
nombre2 = 2
resultat = division(nombre1, nombre2)
if resultat is not None:
    print("Le résultat de la division est :", resultat)
