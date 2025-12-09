class Varialbes:
    __author__  = "kernelstub"
    __version__ = "v1.6"
    __repo__    = "github.com/kernelstub/Apophis"


class Display:
    @staticmethod
    def banner() -> None:
        print(f'''
                        m
     $m                mm            m
      "$mmmmm        m$"    mmmmmmm$"
            """$m   m$    m$""""""
          mmmmmmm$$$$$$$$$"mmmm
    mmm$$$$$$$$$$$$$$$$$$ m$$$$m  "    m  "
   $$$$$$$$$$$$$$$$$$$$$  $$$$$$"$$$                       Author   ➜  {Varialbes.__author__}
   mmmmmmmmmmmmmmmmmmmmm  $$$$$$$$$$                       Version  ➜  {Varialbes.__version__}
   $$$$$$$$$$$$$$$$$$$$$  $$$$$$$"""  m                    Repo     ➜  {Varialbes.__repo__}
   "$$$$$$$$$$$$$$$$$$$$$ $$$$$$  "      "
       """""""$$$$$$$$$$$m """"
         mmmmmmmm"  m$   "$mmmmm
       $$""""""      "$     """"""$$
        ''')

