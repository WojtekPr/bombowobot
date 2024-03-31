# Lista słów
slowa = [
    'wers', 'konkurs', 'pampers', 'morski', 'mars',
    'łaszt', 'baszt', 'kaszt', 'koszt', 'laszt', 'maszt', 'meszt', 'reszt', 'ruszt', 'sztab',
    'łażeń', 'aliaż', 'angaż', 'ażeby', 'ażuru', 'ażury', 'bagaż', 'baraż', 'bażyn', 'dokaż',
    'łonny', 'hanna', 'hanny', 'annat', 'cenna', 'cenne', 'cenni', 'cenny', 'denny', 'denną',
    'budda', 'buddy', 'buddę', 'łobuz', 'erebu', 'kubuś', 'ślubu', 'album', 'arbuz', 'babul'
]

# Lista użytych słów
uzyte_slowa = []

# Pętla do wpisywania sylab i wyświetlania słów
while True:
    sylaba_uzytkownika = input("Wpisz sylabę (lub wpisz 'q' aby zakończyć): ").strip()
    if sylaba_uzytkownika.lower() == 'q':
        print("Koniec programu.")
        break
    
    znalezione_slowo = None
    for slowo in slowa:
        if sylaba_uzytkownika in slowo:
            znalezione_slowo = slowo
            break
    
    if znalezione_slowo:
        print("Znalezione słowo zawierające sylabę '{}': {}".format(sylaba_uzytkownika, znalezione_slowo))
        slowa.remove(znalezione_slowo)
        uzyte_slowa.append(znalezione_slowo)
    else:
        print("Nie znaleziono żadnego słowa zawierającego sylabę '{}'.",format(sylaba_uzytkownika))

print("Użyte słowa:", uzyte_slowa)
