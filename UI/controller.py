import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # gestisce l'evento del pulsante "Mostra"
    def handler_mostra_strumenti(self, e):
        print("Ricerca strumenti")
        result = self._model.get_strumenti()
        # evito duplicati
        self._view.list_view_strumenti.controls.clear()
        for strumento in result:
            self._view.list_view_strumenti.controls.append(ft.Text(f"{strumento}"))

        #aggiorno la pagina
        self._view.page.update()

    # gestisce l'evento del pulsante "Cerca"
    def handler_cerca_strumenti(self, e):
        print("Cerca strumenti")
        tipo_strumento_cercato = self._view.controllo_strumento.value

        # controllo che lo strumento cercato esista
        if not tipo_strumento_cercato:
            self._view.show_alert("Inserire uno strumento valido!")

        result = self._model.cerca_strumenti_per_tipo(tipo_strumento_cercato)

        # evito duplicato
        self._view.list_view_cerca_strumenti.controls.clear()
        for strumento in result:
            self._view.list_view_cerca_strumenti.controls.append(ft.Text(f"{strumento}"))

        # aggiorno la pagina
        self._view.page.update()

