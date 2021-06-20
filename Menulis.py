##
## ################################################
## ###### Please Don't Remove Author Name #########
## ############# Thanks ###########################
## ################################################
##
##
__author__ = '''

######################################################
                By                            
######################################################

    Suraj Singh


    surajsinghbisht054@gmail.com
    http://www.bitforestinfo.com/


######################################################
'''

import tkinter


class StationeryFunctions:
    def __init__(self, text):
        self.text = text
        self.create_binding_keys()
        self.binding_functions_config()
        self.join_function_with_main_stream()

    def join_function_with_main_stream(self):
        self.text.storeobj['Copy'] = self.copy
        self.text.storeobj['Cut'] = self.cut
        self.text.storeobj['Paste'] = self.paste
        self.text.storeobj['SelectAll'] = self.select_all
        self.text.storeobj['DeselectAll'] = self.deselect_all
        return

    def binding_functions_config(self):
        self.text.tag_configure("sel", background="skyblue")
        return

    def copy(self, event):
        self.text.event_generate("&lt;&lt;>>")
        return

    def paste(self, event):
        self.text.event_generate("&lt;&lt;Paste>>")
        return

    def cut(self, event):
        self.text.event_generate("&lt;&lt;Cut>>")
        return

    def create_binding_keys(self):
        for key in ["&lt;Control-a>", "&lt;Control-A>"]:
            self.text.master.bind(key, self.select_all)
        for key in ["&lt;Button-1>", "&lt;Return>"]:
            self.text.master.bind(key, self.deselect_all)
        return

    def select_all(self, event):
        self.text.tag_add("sel", '1.0', 'end')
        return

    def deselect_all(self, event):
        self.text.tag_remove("sel", '1.0', 'end')
        return


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Internalium")
    pad = tkinter.Text(root, wrap='none')
    pad.storeobj = {}
    StationeryFunctions(pad)
    pad.pack()
    root.mainloop()