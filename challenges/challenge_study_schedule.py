def study_schedule(permanence_period, target_time):
    if type(target_time) != int and not target_time:
        return None
    number_of_students = 0
    for period in permanence_period:
        if period[0] and period[1] and type(period[0]) == int\
                and type(period[1]) == int:
            if period[0] <= target_time <= period[1]:
                number_of_students += 1
        else:
            return None
    return number_of_students
