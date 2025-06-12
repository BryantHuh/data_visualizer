import tkinter as tk
from tkinter import ttk
from typing import Dict
from View.observer import Observer
from Controller.data_controller import DataController

class PluginListView(ttk.Frame, Observer):
    def __init__(self, master, controller: DataController):
        super().__init__(master)
        self.controller = controller
        self.vars: Dict[str, tk.BooleanVar] = {}
        for pid in controller.registry.getMetadata():
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(self, text=pid, variable=var,
                                   command=lambda p=pid: controller.onPluginToggle(p))
            chk.pack(anchor='w')
            self.vars[pid] = var

    def update(self):
        pass
