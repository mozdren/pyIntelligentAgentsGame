import xmlrpclib
import random
import visualizer
import xml.etree.ElementTree as ET

class Agent(object):
    def __init__(self, filename):
        # TODO 1 - nacist data z configuracniho xml souboru (nazev v parametru
        # filename)
        # TODO 2 - vytvorit instancni promenne (login, data, vizualizer, 
        # gameserver)
        # login - naplnit daty prectenymi z XML
        # data - prazny list, kde budou ukladana data ze serveru
        # visualizer - instance tridy v visualizer.Visualizer
        # gameserver - pripojit se k XML-RPC serveru (url v XML souboru)
        # TODO 3 - na serveru zavolat metodu add_player s parametrem login
        # (v instancni promenne login)
    
    def action(self):
        # TODO 4 - zavolat z xml-rpc serveru metodu make_action
        # metoda ma 3 parametry (login, nazev_akce, parametry)
        # vsechny tri jsou retezce. My volame metodu look na rozhlizeni
        # kolem sebe bez parametru (prazdny retezec). Kazda akce vraci pole
        # retezcu, kde kazdy radek reprezentuje jeden radek z okoli.
        # Kazdy retezec ma sirku 11 znaku a samotnych radku je 22. Prvnich
        # jedenact reprezentuje okoli agenta a dalsich jedenact, objekty v
        # jeho okoli (zatim pouze "p" - ostatni agenti). Hrac je v tomto
        # okoli na pozici [5][5] (paty radek, paty znak). Objekty na stejne
        # pozici neleznete na souradnicich [5+11][5].
        # "~" voda
        # " " trava
        # "*" cesta
        # "t" strom
        # "o" skala (zed)
        # "f" dlazdena podlaha
        # "p" hrac
    
    def __str__(self):
        # TODO 5 - Vrati retezec, ktery bude hezkou reprezentaci ulozenych
        # dat ulozenych v instancni promenne data.

    def save_data(self):
        # TODO 6 - ulozi data do souboru data.txt

class AgentRandom(Agent):
    # TODO 7 - tento agent bude dedit z agenta predchoziho a
    # upravi funkci action tak, ze akci bude "move" a v parametru
    # preda jeden ze smeru "north", "west", "south", "east". Tyto
    # smery bude vybirat nahodne (najdete vhodnou metodu z balicku
    # random)

class AgentLeftRight(Agent):
    # TODO 8 - tento agent bude chodit stale doleva, dokud nenarazi na prekazku.
    # V takovem pripade obrati svuj smer a pohybuje se stale doprava, nez take
    # narazi na prekazku.

#agent = Agent(login, "config.xml")
#agent = AgentRandom(login, "config.xml")
agent = AgentLeftRight("config.xml")
while agent.visualizer.running:
    agent.action()
    print agent
agent.save_data()
