import Pyro4
from tower import Watchtower


wt = Watchtower()

Pyro4.Daemon.serveSimple(
    {
        wt: "dev.amorfo.watchtower"
    },
    ns=False)


# wt.start_case()
# print(str(wt.search_clues(0)))
