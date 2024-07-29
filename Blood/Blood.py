# Copyright (c) yzret 
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Settings.Program.Config.Config import *
from Settings.Program.Config.Util import *

try:
   import webbrowser
   import re
   import colorama
except:
   ErrorModule()

colorama.init()

try:
   url = url_config
   response = requests.get(url)
   if response.status_code == 200:
       content = response.text
       match = re.search(r'version_tool\s*=\s*"([^"]+)"', content)
       if match:
           current_version = match.group(1)
           if current_version != version_tool:
               print(f"{INFO} Please download the new version of the tool ! {white}{version_tool}{color.LIGHTYELLOW_EX} -> {white}{current_version}{blue}")
               webbrowser.open(github_tool)
               input(f"{INFO} Enter to still use this version -> {color.RESET}")
               popup_version = f"{color.LIGHTYELLOW_EX}Please update the tool: {white}{version_tool}{color.LIGHTYELLOW_EX} -> {white}{current_version}{blue}"


           else:
               popup_version = ""
       else:
           popup_version = ""
   else:
       popup_version = ""
except:
   popup_version = ""

option_01 = "Tool-Info"
option_02 = "Tool-Website"
option_03 = "Virus-Build-(Stealer,-Malware)"
option_04 = "Sql-Vulnerability"
option_05 = "Phishing-Attack"
option_06 = "Website-Info-Scanner"
option_07 = "Website-Url-Scanner"
option_08 = "Illegal-Website"
option_09 = "Search-In-DataBase"
option_10 = "Dox-Create"
option_11 = "Dox-Tracker-(OSINT)"
option_12 = "Username-Tracker-(OSINT)"
option_13 = "Email-Tracker-(OSINT)"
option_14 = "Email-Info-(Lookup)"
option_15 = "Number-Info-(Lookup)"
option_16 = "Ip-Info-(Lookup)"
option_17 = "Ip-Port-Scanner"
option_18 = "Ip-Pinger"
option_19 = "Ip-Generator"
option_20 = "Password-Encrypted"
option_21 = "Password-Decrypted"
option_22 = "Get-Your-Ip"
option_23 = "Discord-Token-Info"
option_24 = "Discord-Token-Nuker"
option_25 = "Discord-Token-Joiner"
option_26 = "Discord-Token-Leaver"
option_27 = "Discord-Token-Login"
option_28 = "Discord-Token-To-Id-And-Brute"
option_29 = "Discord-Token-Server-Raid"
option_32 = "Discord-Token-Spammer"
option_33 = "Discord-Token-Delete-Friends"
option_34 = "Discord-Token-Block-Friends"
option_35 = "Discord-Token-Mass-Dm"
option_36 = "Discord-Token-Delete-Dm"
option_37 = "Discord-Token-Status-Changer"
option_38 = "Discord-Token-Language-Changer"
option_39 = "Discord-Token-House-Changer"
option_40 = "Discord-Token-Theme-Changer"
option_41 = "Discord-Token-Generator"
option_42 = "Discord-Bot-Server-Nuker"
option_43 = "Discord-Bot-Invite-To-Id"
option_44 = "Discord-Server-Info"
option_45 = "Discord-Nitro-Generator"
option_46 = "Discord-Webhook-Info"
option_47 = "Discord-Webhook-Delete"
option_48 = "Discord-Webhook-Spammer"
option_49 = "Discord-Webhook-Generator"
option_50 = "Roblox-Cookie-Login"
option_51 = "Roblox-Cookie-Info"
option_52 = "Roblox-User-Info"
option_53 = "Roblox-Id-Info"
option_54 = "Soon"
option_55 = "Soon"
option_56 = "Soon"
option_57 = "Soon"
option_58 = "Soon"
option_59 = "Soon"
option_60 = "Soon"
option_61 = "Soon" 
option_62 = "Soon"
option_63 = "Soon"
option_64 = "Soon"
option_65 = "Soon"
option_66 = "Soon"
option_67 = "Soon"
option_68 = "Soon"
option_69 = "Soon"

option_next = "Next Page >>"
option_previous = "<< Previous Page"

option_01_txt = option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = option_09.ljust(30)[:30].replace("-", " ")
option_10_txt = option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = option_19.ljust(30)[:30].replace("-", " ")
option_20_txt = option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = option_22.ljust(30)[:30].replace("-", " ")
option_23_txt = option_23.ljust(30)[:30].replace("-", " ")
option_24_txt = option_24.ljust(30)[:30].replace("-", " ")
option_25_txt = option_25.ljust(30)[:30].replace("-", " ")
option_26_txt = option_26.ljust(30)[:30].replace("-", " ")
option_27_txt = option_27.ljust(30)[:30].replace("-", " ")
option_28_txt = option_28.ljust(30)[:30].replace("-", " ")
option_29_txt = option_29.ljust(30)[:30].replace("-", " ")

option_32_txt = option_32.ljust(30)[:30].replace("-", " ")
option_33_txt = option_33.ljust(30)[:30].replace("-", " ")
option_34_txt = option_34.ljust(30)[:30].replace("-", " ")
option_35_txt = option_35.ljust(30)[:30].replace("-", " ")
option_36_txt = option_36.ljust(30)[:30].replace("-", " ")
option_37_txt = option_37.ljust(30)[:30].replace("-", " ")
option_38_txt = option_38.ljust(30)[:30].replace("-", " ")
option_39_txt = option_39.ljust(30)[:30].replace("-", " ")
option_40_txt = option_40.ljust(30)[:30].replace("-", " ")
option_41_txt = option_41.ljust(30)[:30].replace("-", " ")
option_42_txt = option_42.ljust(30)[:30].replace("-", " ")
option_43_txt = option_43.ljust(30)[:30].replace("-", " ")
option_44_txt = option_44.ljust(30)[:30].replace("-", " ")
option_45_txt = option_45.ljust(30)[:30].replace("-", " ")
option_46_txt = option_46.ljust(30)[:30].replace("-", " ")
option_47_txt = option_47.ljust(30)[:30].replace("-", " ")
option_48_txt = option_48.ljust(30)[:30].replace("-", " ")
option_49_txt = option_49.ljust(30)[:30].replace("-", " ")
option_50_txt = option_50.ljust(30)[:30].replace("-", " ")
option_51_txt = option_51.ljust(30)[:30].replace("-", " ")
option_52_txt = option_52.ljust(30)[:30].replace("-", " ")
option_53_txt = option_53.ljust(30)[:30].replace("-", " ")
option_54_txt = option_54.ljust(30)[:30].replace("-", " ")
option_55_txt = option_55.ljust(30)[:30].replace("-", " ")
option_56_txt = option_56.ljust(30)[:30].replace("-", " ")
option_57_txt = option_57.ljust(30)[:30].replace("-", " ")
option_58_txt = option_58.ljust(30)[:30].replace("-", " ")
option_59_txt = option_59.ljust(30)[:30].replace("-", " ")
option_60_txt = option_60.ljust(30)[:30].replace("-", " ")
option_61_txt = option_61.ljust(30)[:30].replace("-", " ")
option_62_txt = option_62.ljust(30)[:30].replace("-", " ")
option_63_txt = option_63.ljust(30)[:30].replace("-", " ")
option_64_txt = option_64.ljust(30)[:30].replace("-", " ")
option_65_txt = option_65.ljust(30)[:30].replace("-", " ")
option_66_txt = option_66.ljust(30)[:30].replace("-", " ")
option_67_txt = option_67.ljust(30)[:30].replace("-", " ")
option_68_txt = option_68.ljust(30)[:30].replace("-", " ")
option_69_txt = option_69.ljust(30)[:30].replace("-", " ")

option_previous_txt = option_previous.ljust(30)[:30]
option_next_txt = option_next.ljust(30)[:30]

page1 = f"""{white}[{blue}Menu n°1{white}]
   {white}[{blue}01{white}] {blue}->{white} {option_01_txt} {white}[{blue}11{white}] {blue}->{white} {option_11_txt} {white}[{blue}21{white}] {blue}->{white} {option_21_txt}
   {white}[{blue}02{white}] {blue}->{white} {option_02_txt} {white}[{blue}12{white}] {blue}->{white} {option_12_txt} {white}[{blue}22{white}] {blue}->{white} {option_22_txt}
   {white}[{blue}03{white}] {blue}->{white} {option_03_txt} {white}[{blue}13{white}] {blue}->{white} {option_13_txt} {white}[{blue}23{white}] {blue}->{white} {option_23_txt}
   {white}[{blue}04{white}] {blue}->{white} {option_04_txt} {white}[{blue}14{white}] {blue}->{white} {option_14_txt} {white}[{blue}24{white}] {blue}->{white} {option_24_txt}
   {white}[{blue}05{white}] {blue}->{white} {option_05_txt} {white}[{blue}15{white}] {blue}->{white} {option_15_txt} {white}[{blue}25{white}] {blue}->{white} {option_25_txt}
   {white}[{blue}06{white}] {blue}->{white} {option_06_txt} {white}[{blue}16{white}] {blue}->{white} {option_16_txt} {white}[{blue}26{white}] {blue}->{white} {option_26_txt}
   {white}[{blue}07{white}] {blue}->{white} {option_07_txt} {white}[{blue}17{white}] {blue}->{white} {option_17_txt} {white}[{blue}27{white}] {blue}->{white} {option_27_txt}
   {white}[{blue}08{white}] {blue}->{white} {option_08_txt} {white}[{blue}18{white}] {blue}->{white} {option_18_txt} {white}[{blue}28{white}] {blue}->{white} {option_28_txt}
   {white}[{blue}09{white}] {blue}->{white} {option_09_txt} {white}[{blue}19{white}] {blue}->{white} {option_19_txt} {white}[{blue}29{white}] {blue}->{white} {option_29_txt}
   {white}[{blue}10{white}] {blue}->{white} {option_10_txt} {white}[{blue}20{white}] {blue}->{white} {option_20_txt} {white}[{blue}30{white}] {blue}-> {option_next_txt}

{blue}┌───({white}{username_pc}@Blood{blue})─[{white}~/Menu-1{blue}]""".replace("(OSINT)", f"{blue}(OSINT){white}").replace("(Lookup)", f"{blue}(Lookup){white}").replace("(Stealer, Malware)", f"{blue}(Stealer, Malware){white}").replace("(Pentest)", f"{blue}(Pentest){white}")

page2 = f"""{white}[{blue}Menu n°2{white}]
   {white}[{blue}31{white}] {blue}-> {option_previous_txt} {white}[{blue}41{white}] {blue}->{white} {option_41_txt} {white}[{blue}51{white}] {blue}->{white} {option_51_txt}
   {white}[{blue}32{white}] {blue}->{white} {option_32_txt} {white}[{blue}42{white}] {blue}->{white} {option_42_txt} {white}[{blue}52{white}] {blue}->{white} {option_52_txt}
   {white}[{blue}33{white}] {blue}->{white} {option_33_txt} {white}[{blue}43{white}] {blue}->{white} {option_43_txt} {white}[{blue}53{white}] {blue}->{white} {option_53_txt}
   {white}[{blue}34{white}] {blue}->{white} {option_34_txt} {white}[{blue}44{white}] {blue}->{white} {option_44_txt} {white}[{blue}54{white}] {blue}->{white} {option_54_txt}
   {white}[{blue}35{white}] {blue}->{white} {option_35_txt} {white}[{blue}45{white}] {blue}->{white} {option_45_txt} {white}[{blue}55{white}] {blue}->{white} {option_55_txt}
   {white}[{blue}36{white}] {blue}->{white} {option_36_txt} {white}[{blue}46{white}] {blue}->{white} {option_46_txt} {white}[{blue}56{white}] {blue}->{white} {option_56_txt}
   {white}[{blue}37{white}] {blue}->{white} {option_37_txt} {white}[{blue}47{white}] {blue}->{white} {option_47_txt} {white}[{blue}57{white}] {blue}->{white} {option_57_txt}
   {white}[{blue}38{white}] {blue}->{white} {option_38_txt} {white}[{blue}48{white}] {blue}->{white} {option_48_txt} {white}[{blue}58{white}] {blue}->{white} {option_58_txt}
   {white}[{blue}39{white}] {blue}->{white} {option_39_txt} {white}[{blue}49{white}] {blue}->{white} {option_49_txt} {white}[{blue}59{white}] {blue}->{white} {option_59_txt}
   {white}[{blue}40{white}] {blue}->{white} {option_40_txt} {white}[{blue}50{white}] {blue}->{white} {option_50_txt} {white}[{blue}60{white}] {blue}-> {option_next_txt}

{blue}┌───({white}{username_pc}@Blood{blue})─[{white}~/Menu-2{blue}]""".replace("(OSINT)", f"{blue}(OSINT){white}").replace("(Lookup)", f"{blue}(Lookup){white}").replace("(Stealer, Malware)", f"{blue}(Stealer, Malware){white}")

def Menu():
   try:
      with open("./Settings/Program/Config/Page.txt", "r") as file:
         page = file.read()
      if page in ["1"]:
         page = page1
         Title("Menu 1")
      elif page in ["2"]:
         page = page2
         Title("Menu 2")
      else:
         page = page1
         Title("Menu 1")
   except:
      page = page1
      Title("Menu 1")

   menu = f"""{popup_version}{blue}                                                                                                  
 					   ____  _      ____   ____  _____  
 					  |  _ \| |    / __ \ / __ \|  __ \ 
 					  | |_) | |   | |  | | |  | | |  | |
 					  |  _ <| |   | |  | | |  | | |  | |
 					  | |_) | |___| |__| | |__| | |__| |
 					  |____/|______\____/ \____/|_____/ 
                                   
                                   
                                           	{white}{github_tool}
                                                    {white}╔════════════╗
                                                    {white}║ {blue}Multi-Tool{white} ║
                                                    {white}╚════════════╝
   {page}"""
   return menu


while True:
   try:
      Clear()
      Slow(Menu())
      choice = input(f"""└──{white}$ {reset}""")

      if choice in ['1', '01']:
         StartProgram(f"{option_01}.py")

      elif choice in ['2', '02']:
         StartProgram(f"{option_02}.py")

      elif choice in ['3', '03']:
         StartProgram(f"{option_03}.py")

      elif choice in ['4', '04']:
         StartProgram(f"{option_04}.py")

      elif choice in ['5', '05']:
         StartProgram(f"{option_05}.py")

      elif choice in ['6', '06']:
         StartProgram(f"{option_06}.py")

      elif choice in ['7', '07']:
         StartProgram(f"{option_07}.py")

      elif choice in ['8', '08']:
         StartProgram(f"{option_08}.py")

      elif choice in ['9', '09']:
         StartProgram(f"{option_09}.py")

      elif choice in ['10']:
         StartProgram(f"{option_10}.py")

      elif choice in ['11']:
         StartProgram(f"{option_11}.py")

      elif choice in ['12']:
         StartProgram(f"{option_12}.py")

      elif choice in ['13']:
         StartProgram(f"{option_13}.py")

      elif choice in ['14']:
         StartProgram(f"{option_14}.py")

      elif choice in ['15']:
         StartProgram(f"{option_15}.py")

      elif choice in ['16']:
         StartProgram(f"{option_16}.py")

      elif choice in ['17']:
         StartProgram(f"{option_17}.py")

      elif choice in ['18']:
         StartProgram(f"{option_18}.py")

      elif choice in ['19']:
         StartProgram(f"{option_19}.py")
      
      elif choice in ['20']:
         StartProgram(f"{option_20}.py")
      
      elif choice in ['21']:
         StartProgram(f"{option_21}.py")
      
      elif choice in ['22']:
         StartProgram(f"{option_22}.py")
      
      elif choice in ['23']:
         StartProgram(f"{option_23}.py")
      
      elif choice in ['24']:
         StartProgram(f"{option_24}.py")
      
      elif choice in ['25']:
         StartProgram(f"{option_25}.py")
      
      elif choice in ['26']:
         StartProgram(f"{option_26}.py")
      
      elif choice in ['27']:
         StartProgram(f"{option_27}.py")
      
      elif choice in ['28']:
         StartProgram(f"{option_28}.py")
      
      elif choice in ['29']:
         StartProgram(f"{option_29}.py")
      

      elif choice in ['30']:
         page = page2
         with open("./Settings/Program/Config/Page.txt", "w") as file:
            file.write("2")
            Title("Menu 2")

      elif choice in ['31']:
         page = page1
         with open("./Settings/Program/Config/Page.txt", "w") as file:
            file.write("1")
            Title("Menu 1")


      elif choice in ['32']:
         StartProgram(f"{option_32}.py")
      
      elif choice in ['33']:
         StartProgram(f"{option_33}.py")
      
      elif choice in ['34']:
         StartProgram(f"{option_34}.py")

      elif choice in ['35']:
         StartProgram(f"{option_35}.py")

      elif choice in ['36']:
         StartProgram(f"{option_36}.py")

      elif choice in ['37']:
         StartProgram(f"{option_37}.py")

      elif choice in ['38']:
         StartProgram(f"{option_38}.py")

      elif choice in ['39']:
         StartProgram(f"{option_39}.py")

      elif choice in ['40']:
         StartProgram(f"{option_40}.py")

      elif choice in ['41']:
         StartProgram(f"{option_41}.py")

      elif choice in ['42']:
         StartProgram(f"{option_42}.py")

      elif choice in ['43']:
         StartProgram(f"{option_43}.py")
   
      elif choice in ['44']:
         StartProgram(f"{option_44}.py")

      elif choice in ['45']:
         StartProgram(f"{option_45}.py")

      elif choice in ['46']:
         StartProgram(f"{option_46}.py")

      elif choice in ['47']:
         StartProgram(f"{option_47}.py")

      elif choice in ['48']:
         StartProgram(f"{option_48}.py")

      elif choice in ['49']:
         StartProgram(f"{option_49}.py")

      elif choice in ['50']:
         StartProgram(f"{option_50}.py")

      elif choice in ['51']:
         StartProgram(f"{option_51}.py")

      elif choice in ['52']:
         StartProgram(f"{option_52}.py")

      elif choice in ['53']:
         StartProgram(f"{option_53}.py")

      elif choice in ['54']:
         StartProgram(f"{option_54}.py")

      elif choice in ['55']:
         StartProgram(f"{option_55}.py")

      elif choice in ['56']:
         StartProgram(f"{option_56}.py")

      elif choice in ['57']:
         StartProgram(f"{option_57}.py")

      elif choice in ['58']:
         StartProgram(f"{option_58}.py")

      else:
         ErrorChoiceStart()
         
   except Exception as e:
      Error(e)