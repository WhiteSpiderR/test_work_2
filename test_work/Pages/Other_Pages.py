class OtherPages:
    """
    class with constants and method for other page
    """

    TEXT_ON_ONLY_AUTO_PAGE = '//h1[contains(text(), "Автомобили, запчасти и")]'
    TEXT_ON_ONLY_REALESTATE_PAGE = '//h1[contains(text(), "Недвижимость в")]'
    TEXT_ON_ONLY_JOB_PAGE = '//h1[contains(text(), "Работа в")]'
    TEXT_ON_ONLY_SERVICE_PAGE = '//h1[contains(text(), "Услуги в")]'

    CANONICAL_ELEM = '//link[@rel="canonical"]'