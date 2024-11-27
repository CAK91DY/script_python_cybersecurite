import argparse
from module.log_reader import LogsReader
def main():
    # Gestion des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Script d'analyse de logs")
    parser.add_argument("repertoire", help="Chemin vers le répertoire contenant les fichiers de logs", type=str)
    args = parser.parse_args()
    
    # créer une instance de LogReader avec le chemin du repertoire
    lecture = LogsReader(args.repertoire)
    fichiers_logs = lecture.trouver_fichiers_logs()

    if fichiers_logs:
        for fichiers_log in fichiers_logs:
            print(f"\nLecture du fichier : {fichiers_log}")
            lecture.lire_logs(fichiers_log)

        lecture.affichier_lignes_lues()

    else:
        print("Aucun fichier de logs trouver dans le repertoire")
if __name__ == "__main__":
    main()
