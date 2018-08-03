#!/usr/bin/env python3
# If you import the function without
import subprocess
from lib import datehandler, filehandler
import argparse
import locale
import sys


# Arguement parser for the .tex file name
# Default value is Berichtsheft.tex
# Edit this value by passing the name with -f name
parser = argparse.ArgumentParser(description="Fügt einfach ganze Wochen, etc. an deinem Berichtsheft")
parser.add_argument("-f", type=str, dest="file_name", default="Berichtsheft.tex",
                    help="Der Name deines Berichtsheftes")
args = parser.parse_args()


# dev branch test
def main():
    # Set locale to get the name of the weekday in german
    # If the set fails, the weekdays will be displayed in english!
    try:
        locale.setlocale(locale.LC_TIME, "de_DE.utf8")
    except locale.Error as e:
        print("Die locale(sprache) 'de_DE.utf8' ist nicht installiert",
              "Bitte installieren sie diese um die Wochentage auf Deutsch zu haben",
              "Um zu sehen welche locales installiert sind geben sie in der Shell ein: 'locale -a'",
              sep="\n")
        sys.exit()

    doSomeEyeCandy()
    menu()


def doSomeEyeCandy():
    """
    EyeCandy

    :return:
    """
    subprocess.call("clear")

    print("###################################################################",
          "####              Leerseiten in Berichtsheft V 3.0              ###",
          "###################################################################",
          "### Die Arbeit ist etwas Unnatürliches.                         ###",
          "### Die Faulheit allein ist göttlich.                           ###",
          "###                                             Anatole France  ###",
          "###################################################################",
          "######### Nicht vergessen die config.py Datei anzupassen! #########",
          sep="\n",
          end="\n\n\n")


def menu():
    """
    Main menu of the Creator

    :return:
    """
    selection = -1

    while selection:
        print("1) Leerseite für eine Kalenderwoche erstellen",
              "2) Leerseite für Schulungen erstellen",
              "0) Beenden",
              sep="\n",
              end="\n\n")

        try:
            selection = int(input("$ "))
        except ValueError as e:
            pass

        subprocess.call("clear")

        if selection == 1:
            input_date = ""
            valid_date = False

            while not valid_date:
                input_date = input("Datum des ersten Tages der gewünschten Woche eingeben (T.M.JJJJ): ")
                sure = input("Ist das eingegebene Datum wirklich korrekt? (y/n): ").lower()
                if sure == "n":
                    subprocess.call("clear")
                    valid_date = False
                else:
                    valid_date = datehandler.dateValid(input_date)
                    subprocess.call("clear")

            weekdays = 0
            while weekdays < 1 or weekdays > 7:
                weekdays = int(input("Wie viele Wochentage sollen hinzugefügt werden?: "))
                subprocess.call("clear")

            year = input_date.split(".")[2]
            calweek = datehandler.getCalWeek(input_date)
            dates = datehandler.makeDateList(input_date, weekdays)

            filehandler.buildWeek(args.file_name, dates, calweek, year)

            input("Die Woche wurde erfolgreich erstellt! (Drücke beliebige Taste)")

        elif selection == 2:
            input("Noch nicht verfügbar (Drücke beliebige Taste)")
        elif selection:
            try:
                # ;-)
                subprocess.call("sl")
            except Exception as e:
                pass

        subprocess.call("clear")


if __name__ == '__main__':
    main()
