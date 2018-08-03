from lib.config import config
from lib import datehandler
import shutil


def _buildHeader(dates, calweek, year):
    """
    Simple copy of Lars function with few edits

    :param dates: Dates as list of date objects
    :param calweek: Calender week as int/string
    :param year: Year as int/str
    :return: Every line of the header as list
    """

    lheader = ['\n', '\\newpage\n', '\n', '\\subsection{KW ' + str(calweek) + ' '
               + str(year) + ': '
               + dates[0].strftime("%d.%m.%Y") + ' - '
               + dates[-1].strftime("%d.%m.%Y")+ '}\n', '\\begin{tabular}{|L{2cm}|L{10cm}|L{5cm}|}\n', '\\hline\n',
               '\\textbf{Datum} & \\textbf{Taetigkeit Betrieb '
               '/ Lerninhalt Schule [Zeit in h]} & '
               '\\textbf{Schulung / Meeting / Termin} \\\\\n']

    return lheader


def buildWeek(file_name, dates, calweek, year):
    """
    Simple copy of Lars function with few edits
    This function will be called from the menu

    :param file_name: Name of the .tex file
    :param dates: Dates as list of date objects
    :param calweek: Calender week as int/string
    :param year: Year as int/str
    :return:
    """

    data = _buildHeader(dates, calweek, year)

    for entry in dates:
        data.append('\\hline\n')
        data.append(entry.strftime("%A") + ', ' + entry.strftime("%d.%m.%Y") + '\n')
        data.append('&\n')
        # put stuff for day-templates here
        with open('./templates/' + entry.strftime("%A") + '.txt', 'r') as template:
            content = template.readlines()
            for line in content:
                data.append(line)

        data.append('\\\\\n')

    # rest of day can be appended after the loop:
    data.append('\\hline\n')
    data.append('\\end{tabular}\n')
    data.append('\\vfill\n')
    data.append('\\unterschriften {' + config.get("name") + " " + config.get("last_name") + '}{Auszubildender}{'
                + config.get("instructor_title") + " " + config.get("instructor_name") + " " + config.get("instructor_last_name")
                + '}{Ausbilder}\n')
    data.append('\\end{document}\n')

    # Write the data we have to the file
    _writeToFile(file_name, data)


def _writeToFile(file_name, data):
    # Backup the file if something goes wrong
    _backupFile(file_name)

    # Remove last '\end{document}' and write our data to the file
    with open(file_name, "r+") as f:
        lines = f.readlines()
        lines.remove("\end{document}\n")
        lines.extend(data)
        f.seek(0)
        f.writelines(lines)
        f.truncate()


def _backupFile(file_name):
    shutil.copy(file_name, file_name + ".backup")
