import Tkinter
import tkMessageBox

from benchmark import benchmarkFunction as benchmark

__author__ = "Rafael Arquero Gimeno"


class MainApp(Tkinter.Tk):  # inherit from Tk makes view handling cleaner
    def __init__(self, parser, add, search, remove, info, users, *args, **kwargs):
        """Users LastFM interface Constructor
        :param parser:
        :param add:
        :param search:
        :param users:
        :param args:
        :param kwargs:
        """
        Tkinter.Tk.__init__(self, *args, **kwargs)  # super()

        self.title("Users LastFM")

        #defaults
        self.users = users  # users loaded
        self.result = None  # search result, None at start
        self.minimum = 0.0  # lowest value for relevance, linked with their SpinBox
        self.maximum = 1.0  # highest value for relevance, linked with their SpinBox

        self._parser = parser
        self._add = add
        self._search = search
        self._remove = remove
        self._info = info

        self.varFrom = Tkinter.StringVar()
        self.varTo = Tkinter.StringVar()
        self.varUser = Tkinter.StringVar()
        self.varUsefulInfo = Tkinter.StringVar()
        self.varAddCost = Tkinter.StringVar()
        self.varSearchCost = Tkinter.StringVar()
        self.varRemoveCost = Tkinter.StringVar()

        self.varFrom.set(str(self.minimum * 100))
        self.varTo.set(str(self.maximum * 100))
        self.varAddCost.set("ADDING cost: ???")
        self.varSearchCost.set("SEARCHING cost: ???")
        self.varRemoveCost.set("REMOVING cost: ???")
        #provide some useful info, better than prompt an useless "Loading..."
        self.varUser.set(
            "Click ADD to start\n" +
            "SEARCH to filter results\n" +
            "SHOW NEXT to browse the results\n" +
            "REMOVE to remove the first user"
        )

        #SEARCH MENU
        self.frmSearch = Tkinter.Frame()
        self.btnSearch = Tkinter.Button(self.frmSearch, text="SEARCH", command=self.search)
        self.lblFrom = Tkinter.Label(self.frmSearch, text="From relevance:")
        self.txtFrom = Tkinter.Spinbox(self.frmSearch, from_=0, to=100, increment=1, textvariable=self.varFrom)
        self.lblTo = Tkinter.Label(self.frmSearch, text="To relevance:")
        self.txtTo = Tkinter.Spinbox(self.frmSearch, from_=0, to=100, increment=1, textvariable=self.varTo)

        self.frmSearch.grid(row=0, column=1, padx=(0, 5), pady=(5, 0), columnspan=2)  # aesthetic top-right margin
        self.btnSearch.grid(row=2, pady=10, sticky=(Tkinter.W, Tkinter.E), columnspan=2)  # full horizontal
        self.lblFrom.grid(row=0, column=0, sticky=Tkinter.E)
        self.txtFrom.grid(row=0, column=1)
        self.lblTo.grid(row=1, column=0, sticky=Tkinter.E)
        self.txtTo.grid(row=1, column=1)

        #BUTTON WRAPPER
        self.frmButtons = Tkinter.Frame()
        self.frmButtons.grid(row=1, column=1, padx=(0, 5), pady=(5, 10), columnspan=3)

        #ADD
        self.btnAdd = Tkinter.Button(self.frmButtons, text="ADD", width=10, command=self.add)
        self.btnAdd.grid(row=1, column=1)  # align left

        #SHOW NEXT
        self.btnNext = Tkinter.Button(self.frmButtons, text="SHOW NEXT", width=10, command=self.showNext)
        self.btnNext.grid(row=1, column=2)

        # REMOVE
        self.btnRemove = Tkinter.Button(self.frmButtons, text="REMOVE", width=10, command=self.remove)
        self.btnRemove.grid(row=1, column=3)

        #USER INFO
        self.lblUser = Tkinter.Label(textvariable=self.varUser, width=30, height=7)  # hold enough space
        self.lblUser.grid(row=0, column=0, rowspan=2)

        #USEFUL INFO
        self.lblUsefulInfo = Tkinter.Label(textvariable=self.varUsefulInfo, width=30, height=1)  # hold enough space
        self.lblUsefulInfo.grid(row=1, column=0, rowspan=2)

        #BENCHMARK
        self.frmBenchmark = Tkinter.Frame(borderwidth=5, relief="sunken")
        self.lblAddCost = Tkinter.Label(self.frmBenchmark, textvariable=self.varAddCost, width=25)
        self.lblSearchCost = Tkinter.Label(self.frmBenchmark, textvariable=self.varSearchCost, width=25)
        self.lblRemoveCost = Tkinter.Label(self.frmBenchmark, textvariable=self.varRemoveCost, width=25)

        self.frmBenchmark.grid(row=2, column=0, columnspan=3,
                               sticky=(Tkinter.N, Tkinter.S, Tkinter.E, Tkinter.W))  # cool effects
        self.lblAddCost.grid(row=0, column=0)
        self.lblSearchCost.grid(row=0, column=1)
        self.lblRemoveCost.grid(row=0, column=2)

    def add(self):
        """wraps given add function"""
        self.users, time = benchmark(lambda: self._add(self.users, self._parser))
        self.varAddCost.set("ADDING cost: {0:.4}ms".format(1000 * time))  # up to 4 decimals
        self.update_info()

    def search(self):
        """wraps given search function"""
        if self.validate():  # if no exceptions are thrown, i.e. valid input
            self.result, time = benchmark(lambda: self._search(self.users, self.minimum, self.maximum))
            self.varSearchCost.set("SEARCHING cost: {0:.4}ms".format(1000 * time))
            self.showNext()  # show the first result

    def remove(self):
        """wraps given remove function"""
        if self.validate():
            self.users, time = benchmark(lambda: self._remove(self.users, self.minimum, self.maximum))
            self.varRemoveCost.set("REMOVING cost: {0:.4}ms".format(1000 * time))
            self.update_info()

    def update_info(self):
        self.varUsefulInfo.set(self._info(self.users))  # update useful info

    def showNext(self):
        if self.result is None:
            self.varUser.set("No search results")
        else:
            user = self.result.next()
            self.varUser.set(str(user))

    def parse(self):
        self.minimum = float(self.varFrom.get()) / 100.0  # try to parse
        self.maximum = float(self.varTo.get()) / 100.0  # try to parse
        assert 0 <= self.minimum <= 1
        assert 0 <= self.minimum <= 1
        assert self.minimum <= self.maximum

    def validate(self):
        try:
            self.parse()
        except ValueError:
            tkMessageBox.showwarning("Unexpected input", "Only numbers are allowed!")
            return False
        except AssertionError:
            tkMessageBox.showwarning("Input not valid",
                                     "Both numbers must be between 0 and 100 and FROM must not be greater than TO.")
            return False
        else:
            return True
