import logging

class TheLog():
    def __init__(self):
        logging.basicConfig(filename='logs.log', format='%(filename)s: %(message)s', level=logging.DEBUG)

    def MessageErreur(self):
        logging.warning("Erreur")
   
    def information_log(self,msg):
        logging.info(str(msg))
        print(str(msg))

    def SMSG(self,author,msg):
        logging.debug(str(author)+": "+str(msg))