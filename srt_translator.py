#!/usr/bin/env python3
"""
SRT Translator - Übersetzt SRT-Dateien von Deutsch nach Englisch
Mit grafischer Dateiauswahl für Input und Output
Behält dabei die exakten Zeitstempel und Formatierung bei
"""

import re
import sys
from pathlib import Path
from googletrans import Translator
import time
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading

class SRTTranslatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SRT Translator - Deutsch → Englisch")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Variablen
        self.input_file = None
        self.output_folder = None
        self.translator = SRTTranslator()
        
        self.setup_ui()
        
    def setup_ui(self):
        """Erstellt die Benutzeroberfläche"""
        # Hauptframe
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Titel
        title_label = ttk.Label(main_frame, text="SRT Übersetzer (DE → EN)", 
                               font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Input Datei Auswahl
        ttk.Label(main_frame, text="1. SRT-Datei auswählen:", 
                 font=('Helvetica', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=(10, 5))
        
        self.input_label = ttk.Label(main_frame, text="Keine Datei ausgewählt", 
                                    foreground="gray")
        self.input_label.grid(row=2, column=0, sticky=tk.W, padx=(20, 0))
        
        ttk.Button(main_frame, text="Datei wählen", 
                  command=self.select_input_file).grid(row=2, column=1, padx=10)
        
        # Output Ordner Auswahl
        ttk.Label(main_frame, text="2. Zielordner auswählen:", 
                 font=('Helvetica', 10, 'bold')).grid(row=3, column=0, sticky=tk.W, pady=(20, 5))
        
        self.output_label = ttk.Label(main_frame, text="Kein Ordner ausgewählt", 
                                     foreground="gray")
        self.output_label.grid(row=4, column=0, sticky=tk.W, padx=(20, 0))
        
        ttk.Button(main_frame, text="Ordner wählen", 
                  command=self.select_output_folder).grid(row=4, column=1, padx=10)
        
        # Fortschrittsbalken
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, length=400, 
                                           variable=self.progress_var)
        self.progress_bar.grid(row=5, column=0, columnspan=2, pady=(30, 10))
        
        # Status Label
        self.status_label = ttk.Label(main_frame, text="Bereit", foreground="gray")
        self.status_label.grid(row=6, column=0, columnspan=2)
        
        # Übersetzen Button
        self.translate_button = ttk.Button(main_frame, text="Übersetzen starten", 
                                          command=self.start_translation, 
                                          state=tk.DISABLED)
        self.translate_button.grid(row=7, column=0, columnspan=2, pady=(20, 0))
        
        # Style
        style = ttk.Style()
        style.configure('TButton', padding=10)
        
    def select_input_file(self):
        """Öffnet Dialog zur Dateiauswahl"""
        filename = filedialog.askopenfilename(
            title="SRT-Datei auswählen",
            filetypes=[("SRT Dateien", "*.srt"), ("Alle Dateien", "*.*")]
        )
        
        if filename:
            self.input_file = Path(filename)
            self.input_label.config(text=self.input_file.name, foreground="black")
            self.check_ready()
    
    def select_output_folder(self):
        """Öffnet Dialog zur Ordnerauswahl"""
        folder = filedialog.askdirectory(title="Zielordner auswählen")
        
        if folder:
            self.output_folder = Path(folder)
            self.output_label.config(text=str(self.output_folder), foreground="black")
            self.check_ready()
    
    def check_ready(self):
        """Prüft ob alle Eingaben vorhanden sind"""
        if self.input_file and self.output_folder:
            self.translate_button.config(state=tk.NORMAL)
        else:
            self.translate_button.config(state=tk.DISABLED)
    
    def start_translation(self):
        """Startet die Übersetzung in einem separaten Thread"""
        self.translate_button.config(state=tk.DISABLED)
        self.progress_var.set(0)
        
        # Starte Übersetzung in separatem Thread
        thread = threading.Thread(target=self.translate_file)
        thread.start()
    
    def translate_file(self):
        """Führt die Übersetzung durch"""
        try:
            # Erstelle Ausgabedateiname
            output_file = self.output_folder / f"{self.input_file.stem}_EN{self.input_file.suffix}"
            
            # Callback für Fortschritt
            def progress_callback(current, total):
                progress = (current / total) * 100
                self.progress_var.set(progress)
                self.status_label.config(text=f"Übersetze Untertitel {current}/{total}...")
            
            # Übersetze
            self.translator.translate_srt_file(
                str(self.input_file), 
                str(output_file),
                progress_callback
            )
            
            # Erfolgsmeldung
            self.root.after(0, lambda: self.translation_complete(output_file))
            
        except Exception as e:
            self.root.after(0, lambda: self.translation_error(str(e)))
    
    def translation_complete(self, output_file):
        """Zeigt Erfolgsmeldung"""
        self.progress_var.set(100)
        self.status_label.config(text="Übersetzung abgeschlossen!", foreground="green")
        self.translate_button.config(state=tk.NORMAL)
        
        messagebox.showinfo(
            "Erfolgreich",
            f"Übersetzung wurde gespeichert in:\n{output_file}"
        )
    
    def translation_error(self, error):
        """Zeigt Fehlermeldung"""
        self.status_label.config(text="Fehler bei der Übersetzung", foreground="red")
        self.translate_button.config(state=tk.NORMAL)
        
        messagebox.showerror("Fehler", f"Fehler bei der Übersetzung:\n{error}")
    
    def run(self):
        """Startet die GUI"""
        self.root.mainloop()


class SRTTranslator:
    def __init__(self):
        self.translator = Translator()
        self.subtitle_pattern = re.compile(
            r'(\d+)\n'  # Subtitle number
            r'(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n'  # Timestamps
            r'((?:.*\n)*?)(?:\n|$)',  # Text content (including multiple lines)
            re.MULTILINE
        )
    
    def translate_text(self, text, src='de', dest='en'):
        """Übersetzt Text von Deutsch nach Englisch"""
        try:
            # Entferne HTML-Tags für die Übersetzung
            clean_text = re.sub(r'<[^>]+>', '', text)
            
            # Übersetze den Text
            translation = self.translator.translate(clean_text, src=src, dest=dest)
            
            # Füge HTML-Tags wieder ein (vereinfachte Version)
            # Behält <b> Tags bei, wenn sie im Original vorhanden waren
            if '<b>' in text and '</b>' in text:
                return f'<b>{translation.text}</b>'
            
            return translation.text
        except Exception as e:
            print(f"Übersetzungsfehler: {e}")
            return text  # Gib Original zurück bei Fehler
    
    def parse_srt(self, content):
        """Parst SRT-Inhalt und gibt eine Liste von Untertiteln zurück"""
        subtitles = []
        matches = self.subtitle_pattern.findall(content)
        
        for match in matches:
            subtitle = {
                'number': int(match[0]),
                'start': match[1],
                'end': match[2],
                'text': match[3].strip()
            }
            subtitles.append(subtitle)
        
        return subtitles
    
    def translate_subtitle(self, subtitle):
        """Übersetzt einen einzelnen Untertitel"""
        translated_subtitle = subtitle.copy()
        
        # Übersetze den Text
        if subtitle['text']:
            # Warte kurz zwischen Übersetzungen (API-Limit)
            time.sleep(0.1)
            translated_subtitle['text'] = self.translate_text(subtitle['text'])
        
        return translated_subtitle
    
    def format_subtitle(self, subtitle):
        """Formatiert einen Untertitel zurück ins SRT-Format"""
        return f"{subtitle['number']}\n{subtitle['start']} --> {subtitle['end']}\n{subtitle['text']}\n"
    
    def translate_srt_file(self, input_file, output_file, progress_callback=None):
        """Übersetzt eine komplette SRT-Datei"""
        # Lese die Eingabedatei
        try:
            with open(input_file, 'r', encoding='utf-8-sig') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Versuche es mit Latin-1 Encoding
            with open(input_file, 'r', encoding='latin-1') as f:
                content = f.read()
        
        # Parse die Untertitel
        subtitles = self.parse_srt(content)
        total_subtitles = len(subtitles)
        
        # Übersetze jeden Untertitel
        translated_subtitles = []
        for i, subtitle in enumerate(subtitles, 1):
            if progress_callback:
                progress_callback(i, total_subtitles)
            
            translated = self.translate_subtitle(subtitle)
            translated_subtitles.append(translated)
        
        # Schreibe die übersetzte SRT-Datei
        with open(output_file, 'w', encoding='utf-8') as f:
            for subtitle in translated_subtitles:
                f.write(self.format_subtitle(subtitle))
                f.write('\n')
        
        return output_file


def main():
    """Hauptfunktion"""
    # Prüfe ob GUI oder Command Line
    if len(sys.argv) > 1:
        # Command Line Modus
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        
        # Prüfe ob Eingabedatei existiert
        if not Path(input_file).exists():
            print(f"Fehler: Datei '{input_file}' nicht gefunden!")
            sys.exit(1)
        
        # Erstelle Translator und übersetze
        translator = SRTTranslator()
        
        try:
            if output_file is None:
                input_path = Path(input_file)
                output_file = input_path.parent / f"{input_path.stem}_EN{input_path.suffix}"
            
            translator.translate_srt_file(input_file, output_file)
            print(f"Übersetzung gespeichert in: {output_file}")
        except Exception as e:
            print(f"\nFehler: {e}")
            sys.exit(1)
    else:
        # GUI Modus
        app = SRTTranslatorGUI()
        app.run()


if __name__ == "__main__":
    main()