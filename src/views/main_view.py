
from ..controllers.packing import PackingController
from ..models.packing import PackingModel

from ..utils.move_items import retrieve_items_from_inventory

from .packing import PackingView

from ..controllers.basket import BasketController

from .basket import ShoppingBasketView

from ..models.basket import BasketModel

from ..controllers.checkout import ChangeCalculatorController

from ..models.checkout import ChangeCalculatorModel

from .checkout import ChangeCalculatorView

from ..models.inventory import InventoryModel

from ..controllers.inventory import InventoryController
from .inventory import InventoryView

from tkinter import PhotoImage
import ttkbootstrap as ttk


class MainView():
    def __init__(self, root):
        self.root = root
        # dictionary of colors:
        self.color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
        # loading Navbar icon image:
        self.navIcon = PhotoImage(file="src/views/assets/menu.png")
        self.closeIcon = PhotoImage(file="src/views/assets/close.png")
        # setting switch state:
        self.btnState = False
        # define content window 
        self.container = ttk.Frame(root, style='light.TFrame')
        self.container.pack(fill="both", expand=True)

        self.p1 = InventoryView(self.container)
        self.p1_model = InventoryModel()
        self.p1_controller = InventoryController(self.p1_model, self.p1)
        self.p1.set_on_add(on_add=lambda x, y, z, a, b, c, d: self.p1_controller.add_item(x, y, z, a, b, c, d))
        self.p1.set_on_view(on_view=self.p1_controller.view_items)
        self.p1.set_on_delete(on_delete=self.p1_controller.delete_item)
        self.p1.place(in_=self.container, x=0, y=50, relwidth=1, relheight=1)
        

        self.p2 = ChangeCalculatorView(self.container)
        self.p2_model = ChangeCalculatorModel()
        self.p2_controller = ChangeCalculatorController(self.p2_model, self.p2)
        self.p2.set_calculate_change(calculate_change=self.p2_controller.calculate_change)
        self.p2.set_clear_fields(clear_fields=self.p2_controller.clear_fields)
        self.p2.place(in_=self.container, x=0, y=100, relwidth=1, relheight=1)

        self.p3 = ShoppingBasketView(self.container)
        self.p3_model = BasketModel()
        self.p3_controller = BasketController(self.p3_model, self.p3)
        self.p3.place(in_=self.container, x=0, y=100, relwidth=1, relheight=1)



        self.p4 = PackingView(self.container)
        self.p4_model = PackingModel()
        self.p4_controller = PackingController(self.p4_model, self.p4)
        self.p4.place(in_=self.container, x=0, y=100, relwidth=1, relheight=1)
        self.p4.set_on_view(on_view=self.p4_controller.show_items)
        self.p4.set_on_add(on_add=self.p4_controller.add_box)
        self.p4.set_calculate_boxes_needed(calculate_boxes_needed=self.p4_controller.calculate_boxes_needed)
        self.p4.envoke_retrieval(self.share_items)

        self.p1.show()
        # Navbar button:
        self.navbarBtn = ttk.Button(self.container, image=self.navIcon, style='light.TButton', command=self.switch)
        self.navbarBtn.place(x=0, y=0)

        # setting Navbar frame:
        self.navRoot = ttk.Frame(self.container, style='info.TFrame', height=self.root.winfo_screenheight(), width=300)
        self.navRoot.place(x=-300, y=0)
        ttk.Label(self.navRoot, style='info.TLabel').place(x=0, y=0)

        self.views = {
            "Inventory": self.p1,
            "Basket": self.p3,
            "Checkout": self.p2,
            "Packing": self.p4,
        }
        

        # Set up navbar option buttons
        self.y = 80
        for option, view in self.views.items():
            btn = ttk.Button(self.navRoot, text=option, style='info.TButton', command=lambda v=view: self.show_view(v))
            btn.place(x=25, y=self.y)
            self.y += 40


        # Navbar Close Button:
        self.closeBtn = ttk.Button(self.navRoot, image=self.closeIcon, style='info.TButton', command=self.switch)
        self.closeBtn.place(x=250, y=10)

        
    def switch(self):
        def slide_nav(delta_x):
            current_x = self.navRoot.winfo_x()
            new_x = current_x + delta_x

            if (self.btnState and new_x <= -300+delta_x) or (not self.btnState and new_x >= 0+delta_x):
                self.btnState = not self.btnState
                return  # Stop the animation

            self.navRoot.place(x=new_x, y=0)
            self.root.after(10, slide_nav, delta_x)  # Continue the animation

        if self.btnState:
            slide_nav(-10)  # Slide to left
        else:
            slide_nav(30)   # Slide to right
    
    def show_view(self, view):
        """Hide all views and show the selected one."""
        for v in self.views.values():
            v.place_forget()
        
        view.place(in_=self.container, x=0, y=50, relwidth=1, relheight=1)
        self.switch()

    def share_items(self):
        retrieve_items_from_inventory(self.p1_model, self.p4_model)