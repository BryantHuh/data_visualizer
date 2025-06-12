import tkinter as tk
from tkinter import ttk
from typing import Any
from Domain_Model.data import Data
from Domain_Model.node import Node
from Domain_Model.leaf import Leaf
from View.observer import Observer

class DataTreeView(ttk.Frame, Observer):
    def __init__(self, master, model):
        super().__init__(master)
        self.model = model
        # Als Observer anmelden
        self.model.addObserver(self)
        self.tree = ttk.Treeview(self)
        self.tree.pack(fill='both', expand=True)

    def update(self):
        self.tree.delete(*self.tree.get_children())
        def _insert(node: Data, parent=''):
            key = node.key if hasattr(node, 'key') else '<root>'
            uid = self.tree.insert(parent, 'end', text=key)
            if isinstance(node, (Node, Leaf)):
                for child in getattr(node, 'children', []): _insert(child, uid)
        if self.model.currentData:
            _insert(self.model.currentData)