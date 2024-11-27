import os 

class LogsReader:
    def __init__(self, repertoire):
        self.repertoire = repertoire
        self.lignes_lues = []

    def trouver_fichiers_logs(self, extension='.log'):
        fichiers_logs = []

        try:
            for fichier in os.listdir(self.repertoire):
                if fichier.endswith(extension):
                    fichiers_logs.append(os.path.join(self.repertoire, fichier))
            return fichiers_logs
        
        except FileNotFoundError:
            print(f"Erreur : le dossier {self.repertoire} n'a été trouvé")
            return []
    

    def lire_logs(self, fichier_log):

        try:
            with open(fichier_log, 'r') as f:
                self.lignes_lues = f.readlines()
            print(f"Le fichier {fichier_log} a été lu avec succès")
        except FileNotFoundError:
            print(f"Erreur : le fichier {fichier_log} n'a été trouvé")
            return self.lignes_lues
        
    def affichier_lignes_lues(self):
        if self.lignes_lues:
            print(f"Nombre total de lignes lues : {len(self.lignes_lues)}")
            print("première lignes du fichier")

            for ligne in self.lignes_lues[:5]:
                print(ligne.strip())
        else:
            print("Aucune ligne n'a été lue")
