# Juni — asystent systemowy

Desktopowy asystent sterowany głosem. Pierwsza funkcja: nasłuch mikrofonu
i zamiana mowy na tekst (Speech-to-Text), na bazie którego docelowo
podejmowane będą akcje w systemie.

## Struktura projektu

```
juni/
├── main_juni.py          # punkt wejścia (uruchamia aplikację)
├── requirements.txt
├── README.md
└── py_juni/               # pakiet z logiką asystenta
    ├── __init__.py
    ├── juni.py             # główna klasa Juni (pętla, obsługa komend)
    ├── listener.py         # nasłuch mikrofonu / STT
    ├── config.py           # konfiguracja (język, progi czasowe itd.)
    └── logger.py           # wspólne logowanie
```

## Instalacja

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Uwaga (Windows): PyAudio czasem wymaga osobnego wheela, jeśli `pip install`
się nie powiedzie — pobierz odpowiedni plik `.whl` dla swojej wersji Pythona
i zainstaluj go ręcznie: `pip install PyAudio-X.X.X-cpXX-cpXX-win_amd64.whl`.

## Uruchomienie

```bash
python main_juni.py
```

Asystent skalibruje poziom szumu otoczenia, a następnie zacznie nasłuchiwać.
Powiedz "koniec", "stop" lub "wyłącz się", aby zakończyć działanie.

## Co dalej (planowany rozwój)

- Router intencji w `Juni._handle_command` (rozpoznawanie konkretnych poleceń).
- Wake word (np. "Juni, ...") zamiast trybu ciągłego nasłuchu.
- Synteza mowy (TTS) jako odpowiedź asystenta — np. nowy moduł `speaker.py`.
- Moduł akcji systemowych (otwieranie aplikacji, sterowanie głośnością itd.).
- Konfiguracja w pliku `.env` / `.yaml` zamiast stałych w `config.py`.