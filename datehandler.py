import datetime


def getWeekday(daynumber):
    """
    Get weekday by its number

    :param daynumber: Number of the day of the week
    :return: The day corresponding the the number as string, undefined if unknown number
    """
    ger_weekdays = {
        0: 'Montag',
        1: 'Dienstag',
        2: 'Mittwoch',
        3: 'Donnerstag',
        4: 'Freitag'
    }

    weekday = ger_weekdays.get(daynumber, "Undefined")

    return weekday


def makeDateList(input_date):
    """
    Tales the user input date and produces a list with 5 date objects from Monday-Friday

    :param input_date: Date as string
    :return: List of date objects
    """
    input_date = input_date.split(".")
    dates = []
    for i in range(int(input_date[0]), int(input_date[0])+5):
        date_object = datetime.date(int(input_date[2]), int((input_date[1])), i)
        dates.append(date_object)
    return dates


def datesToGermanDates(dates):
    """
    Converts date objects to german date strings

    :param dates: List of dates objects
    :return: List of german dates as string
    """
    ger_date = []
    for i in dates:
        ger_date.append(i.strftime("%d.%m.%Y"))
    return ger_date


def getCalWeek(input_date):
    """
    Converts user date input to the corresponding calender date

    :param input_date: Date as string
    :return: Calender week as int
    """
    input_date = input_date.split(".")
    return datetime.date(int(input_date[2]), int((input_date[1])), int((input_date[0]))).isocalendar()[1]


def dateValid(input_date):
    """
    Checks if input date is valid

    :param input_date: Date as string
    :return: True if the date is valid and False if otherwise
    """
    input_date = input_date.split(".")
    try:
        datetime.date(int(input_date[2]), int((input_date[1])), int((input_date[0])))
    except IndexError as e:
        return False
    except ValueError as e:
        return False
    return True


