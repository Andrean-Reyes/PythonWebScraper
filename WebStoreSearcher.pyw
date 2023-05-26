import webbrowser
import tkinter as tk

class itemSearcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x75")
        self.title("Web Store Searcher")
        
        self.itemnamevar = tk.StringVar()
        self.fbcheckvar = tk.IntVar()
        self.amacheckvar = tk.IntVar()
        self.walcheckvar = tk.IntVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.createWidgets()

    def createWidgets(self):
        itemLabel = tk.Label(self,text="Enter name of Item")
        itemLabel.grid(column=0,row=0)
        
        itemEntry = tk.Entry(self,textvariable = self.itemnamevar)
        itemEntry.grid(column=1,row=0)

        searchButton = tk.Button(self, text='Search',command=self.Search)
        searchButton.grid(column=2,row=0)

        fbcheckButton = tk.Checkbutton(self,text='Facebook Marketplace',variable=self.fbcheckvar)
        fbcheckButton.grid(column=0,row=1)

        amacheckButton = tk.Checkbutton(self,text='Amazon',variable=self.amacheckvar)
        amacheckButton.grid(column=1,row=1)

        walcheckButton = tk.Checkbutton(self,text='Walmart',variable=self.walcheckvar)
        walcheckButton.grid(column=2,row=1)

        
    def Search(self):
        if self.amacheckvar.get() == 1:
            webbrowser.open('https://www.amazon.com/s?k='+''.join(self.itemnamevar.get()))
        if self.fbcheckvar.get() == 1:
            webbrowser.open('https://www.facebook.com/marketplace/search/?query='+''.join(self.itemnamevar.get()))
        if self.walcheckvar.get() == 1:
            webbrowser.open('https://www.walmart.com/search?q='+''.join(self.itemnamevar.get()))

if __name__ == '__main__':
    window = itemSearcher()
    window.mainloop()
    
