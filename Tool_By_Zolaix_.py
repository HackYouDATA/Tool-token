#Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.GREEN + """ 


                              ╔═════════════════════════════════════════════════════╗
                              ║       - Tool By Zolaix                              ║
                              ║       - Discord : https://discord.gg/ThETmwDj       ║
                              ║       - Contact Dev - Zolaix#4254                   ║
                              ╚═════════════════════════════════════════════════════╝


       # # # # #     # # # # #     #                    #            # # # # # # #      #       #
              #      #       #     #                   # #                 #             #     #
             #       #       #     #                  #   #                #              #   #
            #        #       #     #                 #     #               #               # #
           #         #       #     #              # # # # # # #            #                #
          #          #       #     #               #         #             #               # #
         #           #       #     #              #           #            #              #   #
        #            #       #     #             #             #           #             #     #
       # # # # #     # # # # #     # # # # # #   #             #     # # # # # # #      #       #    # # # # # # 


  """ + Fore.GREEN)
print(banner)
userid = input(" USER ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [Première Partie] TOKEN : {encodedStr}')
os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)