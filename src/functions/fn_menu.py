from os import system


def clear():
    _ = system('clear')


def display_M1():
    clear()
    print(
        '''
    -----------------------------------------------------------------------
    -              FIND THE PERFECT LOCATION FOR YOUR COMPANY             -
    -----------------------------------------------------------------------
    ''')

    print('''
    CHOOSE YOUR FIRST PREFERENCE BY THE NUMBER:
    -----------------------------------------------------------------------
    | 1. Rounded by companies that raises at least 1 million dollar      |
    | 2. Rounded by tech companies                                       |
    | 3. Rounded by new companies (founded before 2005)                  |
    -----------------------------------------------------------------------
    '''
          )


def display_M2():
    clear()
    print('''
    CHOOSE YOUR SECOND PREFERENCE BY THE NUMBER:
    -----------------------------------------------------------------------
    | 1. Rounded by companies that raises at least 1 million dollar      |
    | 2. Rounded by tech companies                                       |
    | 3. Rounded by new companies (founded before 2005)                  |
    -----------------------------------------------------------------------
    '''
          )


def display_Mcity(lst_city):
    clear()
    print(
        '''
    -----------------------------------------------------------------------
    -           I HAVE THREE DIFFERENT CITY FOR YOUR COMPANY              -
    -----------------------------------------------------------------------
    ''')
    print(f'''
    CHOOSE YOUR CITY:
    -----------------------------------------------------------------------
    | 1ST CITY: {lst_city[0]} 
    | 2ND CITY: {lst_city[1]}  
    | 3RD CITY: {lst_city[2]} 
    -----------------------------------------------------------------------
    '''
          )
    print(
        '''
    -----------------------------------------------------------------------
    -           SEARCHING FOR THE BEST PLACE, PLEASE WAIT                 -
    -----------------------------------------------------------------------
    ''')


def display_Mmap(city, lon, lat):
    clear()
    print(
        '''
    -----------------------------------------------------------------------
    -              YEAH! I HAVE A LOCATION FOR YOUR COMPANY               -
    -----------------------------------------------------------------------
    ''')
    print(f'''
    THE BEST LOCATION IS IN:
    -----------------------------------------------------------------------
    | CITY: {city} 
    | LONGITUDE: {lon}  
    | LATITUDE: {lat} 
    -----------------------------------------------------------------------
    '''
          )
    print(
        '''
    -----------------------------------------------------------------------
    -      I'M PRINTING A MAP WITH YOUR COMPANY LOCATION, PLEASE WAIT     -
    -----------------------------------------------------------------------
    ''')
