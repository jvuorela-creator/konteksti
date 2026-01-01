import datetime

class ElamanRaamit:
    def __init__(self):
        # Yksinkertaistettu "tietokanta" Suomen historian aikakausista
        self.aikakaudet = [
            (1809, 1916, "Autonomian aika (Venäjän vallan alla)", "Suomi oli suuriruhtinaskunta. Elämä oli pääosin maatalousvaltaista, ja sääty-yhteiskunta oli voimissaan."),
            (1917, 1918, "Itsenäistyminen ja sisällissota", "Suomi itsenäistyi, mutta ajautui veriseen sisällissotaan. Yhteiskunta oli syvästi jakautunut."),
            (1919, 1938, "Nuori tasavalta ja eheytyminen", "Suomi rakensi tasavaltaista hallintoa. 1930-luvun pula-aika koetteli, mutta elintaso alkoi nousta."),
            (1939, 1945, "Sotavuodet (Talvi- ja jatkosota)", "Koko kansakunta oli valjastettu maanpuolustukseen. Säännöstely, evakot ja rintamaelämä koskettivat jokaista."),
            (1946, 1955, "Jälleenrakennus ja sotakorvaukset", "Ankara työnteon aika. Rintamamiestalot nousivat ja teollisuus kasvoi sotakorvausten vauhdittamana."),
            (1956, 1969, "Rakennemuutos ja maaltamuutto", "Suomi alkoi kaupungistua vauhdilla. Hyvinvointivaltion perusteita luotiin."),
            (1970, 1990, "Hyvinvointivaltion nousu", "Elintaso nousi kohisten. Peruskoulu, terveyskeskukset ja lähiöt tulivat osaksi arkea."),
            (1991, 1999, "Lama ja EU-aika", "Syvä taloudellinen lama, jota seurasi nousu ja liittyminen Euroopan Unioniin."),
            (2000, 2025, "Digitaalinen aika", "Tietoyhteiskunta ja globalisaatio.")
        ]
        
        # Suomen valtionpäämiehet
        self.johtajat = {
            1881: "Keisari Aleksanteri III",
            1894: "Keisari Nikolai II",
            1917: "Itsenäistymisvaihe (Svinhufvud senaatin pj)",
            1919: "Presidentti K.J. Ståhlberg",
            1925: "Presidentti L.K. Relander",
            1931: "Presidentti P.E. Svinhufvud",
            1937: "Presidentti Kyösti Kallio",
            1940: "Presidentti Risto Ryti",
            1944: "Presidentti C.G.E. Mannerheim",
            1946: "Presidentti J.K. Paasikivi",
            1956: "Presidentti Urho Kekkonen",
            1982: "Presidentti Mauno Koivisto",
            1994: "Presidentti Martti Ahtisaari",
            2000: "Presidentti Tarja Halonen",
            2012: "Presidentti Sauli Niinistö",
            2024: "Presidentti Alexander Stubb"
        }

    def hae_johtaja(self, vuosi):
        # Etsii kuka oli vallassa kyseisenä vuonna
        viimeisin_johtaja = "Tuntematon"
        for aloitusvuosi, nimi in sorted(self.johtajat.items()):
            if vuosi >= aloitusvuosi:
                viimeisin_johtaja = nimi
            else:
                break
        return viimeisin_johtaja

    def hae_konteksti(self, vuosi):
        for start, end, nimi, kuvaus in self.aikakaudet:
            if start <= vuosi <= end:
                return f"{nimi}. {kuvaus}"
        return "Määrittelemätön historiallinen aika."

    def luo_raportti(self, syntyma, kuolema):
        ika = kuolema - syntyma
        
        print(f"\n{'='*60}")
        print(f"HISTORIALLINEN KONTEKSTI: {syntyma}–{kuolema}")
        print(f"Henkilö eli {ika}-vuotiaaksi.")
        print(f"{'='*60}\n")

        # 1. SYNTYMÄHETKI
        print(f"--- SYNTYMÄVUOSI {syntyma} ---")
        print(f"Hallitsija: {self.hae_johtaja(syntyma)}")
        print(f"Aikakausi: {self.hae_konteksti(syntyma)}")
        print("")

        # 2. LAPSUUS JA NUORUUS (Ikä 0-20)
        nuoruus_loppuu = syntyma + 20
        if nuoruus_loppuu > kuolema: nuoruus_loppuu = kuolema
        
        print(f"--- NUORUUS ({syntyma}-{nuoruus_loppuu}) ---")
        # Tarkistetaan, osuiko suuria tapahtumia nuoruuteen
        tapahtumat = []
        if syntyma <= 1917 <= nuoruus_loppuu:
            tapahtumat.append(f"Henkilö oli {1917-syntyma}-vuotias Suomen itsenäistyessä.")
        if syntyma <= 1939 <= nuoruus_loppuu:
             tapahtumat.append(f"Henkilö oli {1939-syntyma}-vuotias Talvisodan syttyessä.")
        
        if tapahtumat:
            for t in tapahtumat:
                print(f"* {t}")
        else:
            print(f"Henkilö varttui aikana: {self.hae_konteksti(syntyma + 10)}")
        print("")

        # 3. AIKUISUUS
        if ika > 20:
            keski_ika = syntyma + 40
            if keski_ika > kuolema: keski_ika = kuolema
            print(f"--- AIKUISUUS JA TYÖIKÄ (n. {nuoruus_loppuu}-{keski_ika}) ---")
            print(f"Yhteiskunnallinen tilanne: {self.hae_konteksti(keski_ika)}")
            print(f"Valtionpäämies 40-vuotispäivänä: {self.hae_johtaja(syntyma+40) if syntyma+40 <= kuolema else 'Ei ehtinyt täyttää'}")
            print("")

        # 4. KUOLINVUOSI
        print(f"--- KUOLINVUOSI {kuolema} ---")
        print(f"Henkilö kuoli {ika}-vuotiaana.")
        print(f"Hallitsija: {self.hae_johtaja(kuolema)}")
        print(f"Suomi kuolinhetkellä: {self.hae_konteksti(kuolema)}")
        print(f"{'='*60}\n")

# --- KÄYTTÖLIITTYMÄ (Simulaatio) ---

def main():
    print("ELÄMÄN RAAMIT - Sukututkijan apuri")
    print("Syötä henkilön tiedot:")
    
    try:
        s_vuosi = int(input("Syntymävuosi: "))
        k_vuosi = int(input("Kuolinvuosi: "))
        
        app = ElamanRaamit()
        app.luo_raportti(s_vuosi, k_vuosi)
        
    except ValueError:
        print("Virhe: Syötä vuosiluvut numeroina.")

if __name__ == "__main__":
    main()
