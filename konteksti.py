import requests
import streamlit
from datetime import datetime

def hae_aikalaislehdet(paivamaara_str):
    """
    Hakee Kansalliskirjaston Digi-rajapinnasta sanomalehdet
    annetulle päivämäärälle.
    """
    
    # 1. Muutetaan päivämäärä API:n vaatimaan muotoon (DD.MM.YYYY -> YYYY-MM-DD)
    try:
        pvm_obj = datetime.strptime(paivamaara_str, "%d.%m.%Y")
        api_date = pvm_obj.strftime("%Y-%m-%d")
        print(f"\n--- Haetaan lehtiä päivälle {paivamaara_str} ---\n")
    except ValueError:
        print("Virhe: Anna päivämäärä muodossa pp.kk.vvvv (esim. 21.11.1908)")
        return

    # 2. Määritellään Kansalliskirjaston hakuosoite ja parametrit
    # Dokumentaatio: https://digi.kansalliskirjasto.fi/opendata
    url = "https://digi.kansalliskirjasto.fi/api/search"
    
    params = {
        "startDate": api_date,
        "endDate": api_date,
        "formats": "NEWSPAPER", # Haetaan vain sanomalehtiä
        "language": "fi",       # Rajataan suomenkielisiin (vapaaehtoinen)
        "limit": 5,             # Haetaan aluksi vain 5 tulosta
        "orderBy": "RELEVANCE"
    }

    try:
        # 3. Tehdään haku (HTTP GET)
        response = requests.get(url, params=params)
        response.raise_for_status() # Tarkistaa onko yhteysvirheitä
        
        data = response.json()
        tulokset = data.get("rows", [])

        if not tulokset:
            print("Ei löytynyt lehtiä tälle päivälle. Kokeile toista päivää (esim. arkipäivää).")
            return

        # 4. Tulostetaan löydökset
        print(f"Löytyi {len(tulokset)} lehteä (näytetään ensimmäiset):\n")
        
        for lehti in tulokset:
            nimi = lehti.get("bindingTitle", "Tuntematon lehti")
            julkaisu_pvm = lehti.get("date", "Ei pvm")
            
            # Rakennetaan suora linkki digitoituun sivuun
            binding_id = lehti.get("bindingId")
            linkki = f"https://digi.kansalliskirjasto.fi/sanomalehti/binding/{binding_id}?page=1"
            
            print(f"📰 LEHTI: {nimi}")
            print(f"📅 JULKAISTU: {julkaisu_pvm}")
            print(f"🔗 LUE TÄSTÄ: {linkki}")
            print("-" * 40)

    except requests.exceptions.RequestException as e:
        print(f"Yhteysvirhe rajapintaan: {e}")

# --- PÄÄOHJELMA ---
if __name__ == "__main__":
    # Kysytään käyttäjältä pvm
    syote = input("Anna päivämäärä (pp.kk.vvvv), esim. 21.11.1908: ")

    hae_aikalaislehdet(syote)
