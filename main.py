import string, json, requests, random
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep
from fortnite_python import Fortnite
from fortnite_python.domain import Mode

fortnite = Fortnite('24f4e59e-c238-40b9-993e-b896775bf07a')

system('cls')
boucle1 = True
boucle2 = True
boucle3 = True


header_final = """
   
████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░  ███████╗░█████╗░██████╗░████████╗███╗░░██╗██╗████████╗███████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗  ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝████╗░██║██║╚══██╔══╝██╔════╝
░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝  █████╗░░██║░░██║██████╔╝░░░██║░░░██╔██╗██║██║░░░██║░░░█████╗░░
░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗  ██╔══╝░░██║░░██║██╔══██╗░░░██║░░░██║╚████║██║░░░██║░░░██╔══╝░░
░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║  ██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██║░╚███║██║░░░██║░░░███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚══════╝\n\n\n\n"""


header1 = """
 
░██████╗████████╗░█████╗░████████╗░██████╗  ███████╗░█████╗░██████╗░████████╗███╗░░██╗██╗████████╗███████╗
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝  ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝████╗░██║██║╚══██╔══╝██╔════╝
╚█████╗░░░░██║░░░███████║░░░██║░░░╚█████╗░  █████╗░░██║░░██║██████╔╝░░░██║░░░██╔██╗██║██║░░░██║░░░█████╗░░
░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░░╚═══██╗  ██╔══╝░░██║░░██║██╔══██╗░░░██║░░░██║╚████║██║░░░██║░░░██╔══╝░░
██████╔╝░░░██║░░░██║░░██║░░░██║░░░██████╔╝  ██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██║░╚███║██║░░░██║░░░███████╗
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚══════╝\n\n\n\n"""



header11 = """
 _________                                 __                 
|  _   _  |                               [  |                
|_/ | | \_|  __   _      .---.   .--.      | |.--.     .--./) 
    | |     [  | | |    / /__\\ ( (`\]     | '/'`\ \  / /'`\; 
   _| |_     | \_/ |,   | \__.,  `'.'.     |  \__/ |  \ \._// 
  |_____|    '.__.'_/    '.__.' [\__) )   [__;.__.'   .',__`  
                                                     ( ( __)) 
\n\n\n\n"""

while boucle1:
    print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.yellow_to_red, "[?] Pseudo ↓"))
    pseudo = input("")
    boucle1 = False
    system('cls')

    player = fortnite.player(pseudo)

    stats = player.get_stats(Mode.SOLO)
    
    stat = player.get_stats(Mode.DUO)

    sec = player.get_stats(Mode.SQUAD)

while boucle2:
    print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header1)))
    print(f"Stats de {pseudo} à " + stats.top1 + " top1 en solo, il y a "+ stat.top1 + " de top 1 en duo est il a " + sec.top1 + " de top1 en squad")
    choix = input("As tu aimer le logielle ? (oui,non) : ")
    if choix.startswith("oui"):
    	boucle2 = False



while boucle3:
	print(Colorate.Diagonal(Colors.blue_to_red, Center.XCenter(header11)))
	boucle3 = False
	

