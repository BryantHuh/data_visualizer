import tkinter as tk
from View.observer import Observer
from Controller.data_controller import DataController
from View.data_tree_view import DataTreeView
from View.visualization_view import VisualizationView
from View.plugin_list_view import PluginListView

class MainWindow(tk.Tk, Observer):
    def __init__(self, controller: DataController):
        super().__init__()
        self.title('Data Visualizer')
        self.geometry('800x600')
        self.controller = controller

        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open JSON', command=lambda: controller.onOpen('json'))
        filemenu.add_command(label='Open YAML', command=lambda: controller.onOpen('yaml'))
        menubar.add_cascade(label='File', menu=filemenu)
        self.config(menu=menubar)

        left = tk.Frame(self)
        left.pack(side='left', fill='both', expand=True)
        right = tk.Frame(self)
        right.pack(side='right', fill='y')

        self.treeView = DataTreeView(left, controller.model)
        self.treeView.pack(fill='both', expand=True)
        self.vizView = VisualizationView(left)
        self.vizView.pack(fill='both', expand=True)
        self.plugView = PluginListView(right, controller)
        self.plugView.pack(fill='y')

    def update(self) -> None:
        self.treeView.update()
        self.vizView.update()
        self.plugView.update()
