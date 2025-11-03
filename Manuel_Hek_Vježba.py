
def izracunaj_prosjek(lista_brojeva):
    
    if len(lista_brojeva) == 0:
        return 0


    suma = 0
    for broj in lista_brojeva:
        suma += broj

    return suma / len(lista_brojeva) 

lista_mjerenja = []


print(" ALAT ZA PROSJEK MJERENJA JE POKRENUT! ")


while True:
    print("\n--- Alat za Prosjek Mjerenja ---")
    print(f"Trenutno u memoriji: {len(lista_mjerenja)} mjerenja")
    print("\n1. Unesi novo mjerenje (V)")
    print("2. Izračunaj prosjek i obriši mjerenja")
    print("3. Pregledaj sva spremljena mjerenja")
    print("0. Izlaz")
    print("---")

   
    try:
        opcija = int(input("Odaberi opciju (0-3): "))
    except ValueError:
        print("GREŠKA: Unesite brojčanu vrijednost (0-3).")
        continue

   
    if opcija == 1:
        
        try:
            vrijednost = float(input("Unesite vrijednost mjerenja u voltima (V): "))
            lista_mjerenja.append(vrijednost)
            print(f"Mjerenje {vrijednost} V uspješno dodano. ")
        except ValueError:
            print("GREŠKA: Unesite točnu brojčanu vrijednost.")


    elif opcija == 2:
        if len(lista_mjerenja)== 0:
            print("Nema spremljenih mjerenja za izračun prosjeka. ")
            continue
        prosjek = izracunaj_prosjek(lista_mjerenja)
        print(f"\n Prosjek od {len(lista_mjerenja)} mjerenja iznosi: {prosjek:.2f} V")
        lista_mjerenja.clear()
        print("Sva mjerenja su obrisana. Spremno za novu listu")


    elif opcija == 3:
        print("f\n Spremljena mjerenja: {lista_mjerenja}")


    elif opcija == 0:
        
        print("\n Izlazak iz programa.")
        break

    else:
        print("Nepostojeća opcija, odaberite broj između 0 i 3.")

