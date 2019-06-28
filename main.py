from get_data import GetData
from gui import Gui
from time import sleep


crypto = GetData("https://coinmarketcap.com/all/views/all/", 'data/')
crypto.save_file()
crypto.find_line()
crypto.data_to_list()
print(crypto.final_list)

gui = Gui(100, 6)
gui.create_window(800, 600)
gui.create_grid(crypto.final_list)

Gui.root.mainloop()
