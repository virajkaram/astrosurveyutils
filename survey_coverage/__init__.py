from survey_coverage.surveys import known_surveys


def get_known_surveys():
    return known_surveys.keys()


def get_survey_by_name(name):
    if name in known_surveys.keys():
        return known_surveys[name]
    else:
        raise ValueError(f"Survey {name} is not a known survey.")