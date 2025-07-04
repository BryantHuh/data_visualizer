import tkinter as tk
from Contract.observer import Observer
from Controller.data_controller import DataController
from View.data_tree_view import DataTreeView
from View.visualization_view import VisualizationView
from View.plugin_list_view import PluginListView

class MainWindow(tk.Tk, Observer):
    def __init__(self, controller: DataController):
        super().__init__()
        self.title('Data Visualizer')
        self.geometry('800x600')

        button_frame = tk.Frame(self)
        button_frame.pack(side='top', fill='x')

        btn_json = tk.Button(button_frame, text='Open JSON', command=lambda: controller.onOpen('json'))
        btn_json.pack(side='left', padx=5, pady=5)

        btn_yaml = tk.Button(button_frame, text='Open YAML', command=lambda: controller.onOpen('yaml'))
        btn_yaml.pack(side='left', padx=5, pady=5)

        self.controller = controller

        # Deaktiviert die Menüleiste, um macOS NSInternalInconsistencyException zu umgehen
        # menubar = tk.Menu(self)
        # filemenu = tk.Menu(menubar, tearoff=0)
        # filemenu.add_command(label='Open JSON', command=lambda: controller.onOpen('json'))
        # filemenu.add_command(label='Open YAML', command=lambda: controller.onOpen('yaml'))
        # menubar.add_cascade(label='File', menu=filemenu)
        # self.config(menu=menubar)

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
