from initialize_database import initialize_database


def build():
    '''
    Funktio, joka alustaa tietokannan.
    '''
    initialize_database()


if __name__ == "__main__":
    build()