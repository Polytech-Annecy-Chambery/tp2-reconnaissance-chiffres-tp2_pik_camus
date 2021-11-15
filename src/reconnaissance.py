from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    image = image.binarisation(S)
    image = image.localisation()
    similitude = 0
    
    for x in range (len(liste_modeles)):
        im = image.resize(liste_modeles[x].H, liste_modeles[x].W) 
        if im.similitude(liste_modeles[x])> similitude:
            similitude = im.similitude(liste_modeles[x])
            indiceimage = x
            
    return indiceimage

