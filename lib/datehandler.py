import datetime
import calendar


def makeDateList(input_date, weekdays):
    """
    Takes the user input date and produces a list with up to 7 date objects from Monday-Sunday

    :param input_date: Date as string
    :return: List of date objects
    """
    input_date = input_date.split(".")
    dates = []
    day = int(input_date[0])
    month = int(input_date[1])
    year = int(input_date[2])
    update_month = True

    days_in_month = calendar.monthrange(year, month)[1]
    for i in range(day, day+weekdays):
        if i > days_in_month:
            i = i - days_in_month
            if update_month:
                month = month + 1
                update_month = False
        date_object = datetime.date(year, month, i)
        dates.append(date_object)
    return dates


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


