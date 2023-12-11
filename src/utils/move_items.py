
# this helper function will move items from inventory to packing model 
# this function will be envoked when show_items is called in packing controller
def retrieve_items_from_inventory(inventorymodel, packingmodel):
    # get the items from the inventory model
    items = inventorymodel.get_items()
    # set the items in the packing model
    packingmodel.set_inventory_items(items)