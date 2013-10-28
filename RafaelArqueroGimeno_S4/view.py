import Tkinter
from time import time

#inherit from Tk makes view handling cleaner
class MainApp(Tkinter.Tk):
    def __init__(self, parser, add, search, getnext, users, *args, **kwargs):
        '''User interface Constructor'''
        Tkinter.Tk.__init__(self, *args, **kwargs)#super()

        #defaults
        self.users  = users#users loaded
        self.result = []#search result, empty collection at start
        self.low    = 0.0#lowest value for relevance, linked with their SpinBox
        self.high   = 1.0#highest value for relevance, linked with their SpinBox

        self.parser     = parser
        self._add       = add
        self._search    = search
        self._getnext   = getnext

        self.txtfromval = Tkinter.StringVar()
        self.txttoval   = Tkinter.StringVar()  
        self.txtfromval.set(str(self.low * 100))
        self.txttoval.set(str(self.high * 100))
        self.txtfromval.trace("w", self.OnChange)#when StrinVar changes, activate OnChange event
        self.txttoval.trace("w", self.OnChange)

        self.userinfo   = Tkinter.StringVar()
        #provide some useful info, better than prompt useless Loading...
        self.userinfo.set("Click ADD to start\n SEARCH to filter results\n SHOW NEXT to browse the results") 

        self.counter   = Tkinter.StringVar()
        self.counter.set("0/0")

        self.varadding      = Tkinter.StringVar()
        self.varsearching   = Tkinter.StringVar()
        self.varadding.set("ADDING cost: XXX")
        self.varsearching.set("SEARCHING cost: XXX")

        self.title("Users LastFM")

        #SEARCH MENU
        self.menusearch = Tkinter.Frame()
        #this or inside lambda is a little hack :P (to call two functions)
        self.btnsearch  = Tkinter.Button(self.menusearch, text="SEARCH", command=lambda:self.search() or self.show_next())        
        self.lblfrom    = Tkinter.Label(self.menusearch, text="From relevance:")
        self.txtfrom    = Tkinter.Spinbox(self.menusearch, from_=0, to=100, increment=0.1, textvariable=self.txtfromval)
        self.lblto      = Tkinter.Label(self.menusearch, text="To relevance:")
        self.txtto      = Tkinter.Spinbox(self.menusearch, from_=0, to=100, increment=0.1, textvariable=self.txttoval)

        self.menusearch.grid(row=0, column=1, padx=(0, 5), pady=(5,0), columnspan=2)#aesthetic top-right margin
        self.btnsearch.grid(row=2, pady=10, columnspan=2, sticky=(Tkinter.W, Tkinter.E))#full horizontal
        self.lblfrom.grid(row=0, column=0, sticky=(Tkinter.E))
        self.txtfrom.grid(row=0, column=1)
        self.lblto.grid(row=1, column=0, sticky=(Tkinter.E)) 
        self.txtto.grid(row=1, column=1)

        #ADD
        self.btnadd     = Tkinter.Button(text="ADD", width=12, command=self.add)
        self.btnadd.grid(row=1, column=1, sticky=(Tkinter.W))#align left

        #SHOW NEXT
        self.btnnext    = Tkinter.Button(text="SHOW NEXT", width=12, command=self.show_next)        
        self.btnnext.grid(row=1, column=2)    

        #USER INFO
        self.lbluser    = Tkinter.Label(textvariable=self.userinfo, width=30, height=7)#hold enough space   
        self.lbluser.grid(row=0, column=0)

        #COUNTER
        self.lblcounter  = Tkinter.Label(textvariable=self.counter, height=3)#hold enough space
        self.lblcounter.grid(row=1, column=0)

        #BENCHMARK
        self.benchmark      = Tkinter.Frame(borderwidth=5, relief="sunken")          
        self.lbladding      = Tkinter.Label(self.benchmark, textvariable=self.varadding, width=30)
        self.lblsearching   = Tkinter.Label(self.benchmark, textvariable=self.varsearching, width=30)

        self.benchmark.grid(row=2, column=0, columnspan=3, sticky=(Tkinter.N, Tkinter.S, Tkinter.E, Tkinter.W))#cool efects
        self.lbladding.grid(row=0, column=0)
        self.lblsearching.grid(row=0, column=1)

    def add(self):
        '''wraps user add functiom'''
        start   = time()
        self.users = self._add(self.users, self.parser)
        end     = time()
        self.varadding.set("ADDING cost: " + str(1000 * (end - start)) + "ms")  
        self.updatecounter()

    def search(self):
        '''wraps user search function'''
        start   = time()
        self.result = self._search(self.users, self.low, self.high)
        end     = time()
        self.varsearching.set("SEARCHING cost: " + str(1000 * (end - start)) + "ms")  

    def show_next(self):
        '''wraps user getnext function'''
        user = self._getnext(self.result)        
        self.userinfo.set(str(user))        
        self.updatecounter()
        if len(self.result) is 0 and user is not None:#we've just shown the las result!!!
            self.search()#search one more time

    def updatecounter(self):
        self.counter.set(str(len(self.result))  + "/" + str(len(self.users)))
        
    def OnChange(self, *args):
        '''Invoked when some SpinBox changes. Transforms the percentages (0-100) to coeficients (0-1)'''
        try:
            self.low    = float(self.txtfromval.get()) / 100.0#try to parse
            assert 0.0 <= self.low <= self.high#coherence
        except:#if not float or invalid number, reset
            self.low = 0
            self.txtfromval.set(self.low*100)

        try:
            self.high   = float(self.txttoval.get()) / 100.0#try to parse
            assert self.low <= self.high <= 1.0#coherence
        except:#if not float or invalid number, reset
            self.high = 1
            self.txttoval.set(self.high*100)
            
        

        
        #print self.low, self.high#debug
            

