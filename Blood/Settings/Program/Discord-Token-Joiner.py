# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import requests
except Exception as e:
   ErrorModule(e)
   

Title("Discord Token Joiner")

try:
    print()
    token = Choice1TokenDiscord()
    invite = input(f"{color.BLUE}{INPUT} Server Invitation -> {color.RESET}")

    invite_code = invite.split("/")[-1]

    try:
        response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
        if response.status_code == 200:
            server_name = response.json().get('guild', {}).get('name')
        else:
            server_name = invite
    except:
        server_name = invite

    try:
            headers = {
                'Authorization': token
            }
            response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers)
            
            if response.status_code == 200:
                print(f"\n{blue}[{white}{current_time_hour()}{blue}] {ADD} Status: {color.WHITE}Joined{color.BLUE} | Server: {color.WHITE}{server_name}{color.BLUE}\n")
            else:
                print(f"\n{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status: {color.WHITE}Error {response.status_code}{color.BLUE} | Server: {color.WHITE}{server_name}{color.BLUE}\n")
    except:
        print(f"\n{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status: {color.WHITE}Error{color.BLUE} | Server: {color.WHITE}{server_name}{color.BLUE}\n")

    Continue()
    Reset()
except Exception as e:
    Error(e)