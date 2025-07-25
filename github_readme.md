# SRT Translator (DE → EN)

Ein benutzerfreundliches Python-Tool zur automatischen Übersetzung von SRT-Untertiteldateien von Deutsch nach Englisch mit grafischer Benutzeroberfläche.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## 🎯 Features

- 🖱️ **Grafische Benutzeroberfläche** - Einfache Bedienung ohne Kommandozeile
- ⏱️ **Exakte Zeitstempel-Beibehaltung** - Alle Timings bleiben unverändert
- 📝 **HTML-Tag-Unterstützung** - Formatierungen wie `<b>`, `<i>` bleiben erhalten
- 📊 **Fortschrittsanzeige** - Live-Feedback während der Übersetzung
- 🔄 **Mehrzeilige Untertitel** - Korrekte Verarbeitung von mehrzeiligen Texten
- 💾 **Flexible Speicherorte** - Wähle deinen Zielordner frei aus

## 📸 Screenshot

<img width="600" alt="SRT Translator GUI" src="https://user-images.githubusercontent.com/placeholder/srt-translator-gui.png">

## 🚀 Installation

### Voraussetzungen

- Python 3.6 oder höher
- pip (Python Package Manager)

### Schritt 1: Repository klonen

```bash
git clone https://github.com/deinusername/srt-translator.git
cd srt-translator
```

### Schritt 2: Abhängigkeiten installieren

**Windows:**
```bash
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
pip3 install -r requirements.txt
```

### Alternative: Manuelle Installation

```bash
pip install googletrans==4.0.0-rc1
```

## 📖 Verwendung

### GUI-Modus (Empfohlen)

1. Starte das Programm:
   ```bash
   python srt_translator.py
   ```
   oder auf macOS/Linux:
   ```bash
   python3 srt_translator.py
   ```

2. **Datei auswählen**: Klicke auf "Datei wählen" und wähle deine deutsche SRT-Datei

3. **Zielordner wählen**: Klicke auf "Ordner wählen" und wähle den Speicherort für die Übersetzung

4. **Übersetzen**: Klicke auf "Übersetzen starten" und warte bis der Vorgang abgeschlossen ist

### Kommandozeilen-Modus

```bash
# Automatischer Ausgabename (_EN.srt)
python srt_translator.py input_DE.srt

# Mit spezifischem Ausgabenamen
python srt_translator.py input_DE.srt output_EN.srt
```

## 📋 Beispiel

**Input (Deutsch):**
```srt
1
00:00:01,000 --> 00:00:04,000
<b>Hallo und herzlich willkommen</b>

2
00:00:04,500 --> 00:00:07,000
Dies ist ein Beispiel-Untertitel
```

**Output (Englisch):**
```srt
1
00:00:01,000 --> 00:00:04,000
<b>Hello and welcome</b>

2
00:00:04,500 --> 00:00:07,000
This is an example subtitle
```

## 🛠️ Technische Details

- **Übersetzungs-API**: Google Translate (kostenlos, keine API-Keys erforderlich)
- **GUI-Framework**: Tkinter (im Python-Standard enthalten)
- **Encoding-Support**: UTF-8, UTF-8-BOM, Latin-1
- **Rate Limiting**: Automatische Verzögerung zwischen Anfragen

## 🐛 Bekannte Einschränkungen

- Google Translate API hat ein tägliches Limit für kostenlose Übersetzungen
- Sehr lange SRT-Dateien können einige Minuten zur Übersetzung benötigen
- Die Übersetzungsqualität hängt von Google Translate ab

## 🔧 Fehlerbehebung

### ImportError: No module named 'googletrans'
```bash
pip install --upgrade googletrans==4.0.0-rc1
```

### tkinter nicht gefunden (Linux)
```bash
sudo apt-get install python3-tk
```

### Encoding-Probleme
Das Tool versucht automatisch verschiedene Encodings. Falls Probleme auftreten, konvertiere die SRT-Datei zuerst zu UTF-8.

## 📝 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe [LICENSE](LICENSE) Datei für Details.

## 🤝 Beitragen

Pull Requests sind willkommen! Für größere Änderungen bitte erst ein Issue erstellen.

1. Fork das Projekt
2. Erstelle deinen Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Committe deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

## 💡 Zukünftige Features

- [ ] Unterstützung für weitere Sprachen
- [ ] Batch-Verarbeitung mehrerer Dateien
- [ ] DeepL API Integration für bessere Übersetzungsqualität
- [ ] Vorschau-Funktion für Übersetzungen
- [ ] Export in weitere Untertitelformate

## 👤 Autor

**Dein Name**

- GitHub: [@deinusername](https://github.com/deinusername)

## 🙏 Danksagung

- [googletrans](https://github.com/ssut/py-googletrans) für die Übersetzungs-API
- Alle Mitwirkenden an diesem Projekt

---

⭐️ Wenn dir dieses Projekt gefällt, gib ihm einen Stern auf GitHub!