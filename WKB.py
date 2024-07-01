from shapely import wkb

# Funkcja do konwersji WKB do WKT
def convert_wkb_to_wkt(wkb_hex_str):
    try:
        # Konwersja ciągu szesnastkowego (hex) WKB do bajtów
        wkb_bytes = bytes.fromhex(wkb_hex_str)

        # Konwersja bajtów do obiektu Shapely
        geom = wkb.loads(wkb_bytes)

        # Konwersja obiektu Shapely do WKT
        wkt_str = geom.wkt

        return wkt_str

    except Exception as e:
        print(f"Błąd konwersji WKB do WKT: {str(e)}")
        return None

# Pobranie ciągu szesnastkowego WKB od użytkownika
wkb_hex_str = input("Podaj ciąg szesnastkowy WKB: ").strip()

# Wywołanie funkcji i wyświetlenie wyniku
if wkb_hex_str:
    wkt_str = convert_wkb_to_wkt(wkb_hex_str)
    if wkt_str:
        print(f"WKT Geometry: {wkt_str}")
else:
    print("Nie podano ciągu szesnastkowego WKB.")
