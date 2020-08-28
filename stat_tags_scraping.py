# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:41:29 2020

@author: Damien AUBAIL
"""

def tag_stat(url):
    
    """Cette fonction se connecte à une page web donnée par l’utilisateur, 
    elle analyse le site et calcule en pourcentages 
    l’utilisation des tags dans cette page"""
    
    from requests import get as connecte
    from pandas import DataFrame as Tableau
    from bs4 import BeautifulSoup as bs
    
    global glossaire, tableau, site
    
    try:
        connection = connecte("https://" + str(url))
    except IOError:
        print("Merci de bien vérifier le site fournit")
    else:
        site = bs(connection.content, 'lxml')
        glossaire = {'Tag_Name': [tag.name for tag in site.find_all(True)], 
               'Attribut': [tag.attrs for tag in site.find_all(True)]}
        tableau =  Tableau(glossaire)
        Tags = dict(round(tableau.Tag_Name.value_counts(normalize=True)*100,2))
        print()
        print('TAGS')
        print('--------------------')
        return print(Tags)

