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
   
Title("Discord Server Info")

try:
    invite = input(f"{color.BLUE}\n{INPUT} Server Invitation -> {color.RESET}")
    try:
        invite_code = invite.split("/")[-1]
    except:
        invite_code = invite
    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code == 200:
        data = response.json()
        try:
            type_value = data['type']
        except:
            type_value= "None"
        try:
            code_value = data['code']
        except:
            code_value = "None"
        try:
            inviter_id = data['inviter']['id']
        except:
            inviter_id = "None"
        try:
            inviter_username = data['inviter']['username']
        except:
            inviter_username = "None"
        try:
            inviter_avatar = data['inviter']['avatar']
        except:
            inviter_avatar = "None"
        try:
            inviter_discriminator = data['inviter']['discriminator']
        except:
            inviter_discriminator = "None"
        try:
            inviter_public_flags = data['inviter']['public_flags']
        except:
            inviter_public_flags = "None"
        try:
            inviter_flags = data['inviter']['flags']
        except:
            inviter_flags = "None"
        try:
            inviter_banner = data['inviter']['banner']
        except:
            inviter_banner = "None"
        try:
            inviter_accent_color = data['inviter']['accent_color']
        except:
            inviter_accent_color = "None"
        try:
            inviter_global_name = data['inviter']['global_name']
        except:
            inviter_global_name = "None"
        try:
            inviter_banner_color = data['inviter']['banner_color']
        except:
            inviter_banner_color = "None"
        try:
            expires_at = data['expires_at']
        except:
            expires_at = "None"
        try:
            flags = data['flags']
        except:
            flags = "None"
        try:
            server_id = data['guild_id']
        except:
            server_id = "None"
        try:
            server_name = data['guild']['name']
        except:
            server_name = "None"
        try:
            server_icon = data['guild']['icon']
        except:
            server_icon = "None"
        try:
            server_features = data['guild']['features']
        except:
            server_features = "None"
        try:
            server_verification_level = data['guild']['verification_level']
        except:
            server_verification_level = "None"
        try:
            server_nsfw_level = data['guild']['nsfw_level']
        except:
            server_nsfw_level = "None"
        try:
            server_nsfw = data['guild']['nsfw']
        except:
            server_nsfw = "None"
        try:
            server_premium_subscription_count = data['guild']['premium_subscription_count']
        except:
            server_premium_subscription_count = "None"
        try:
            channel_id = data['channel']['id']
        except:
            channel_id = "None"
        try:
            channel_type = data['channel']['type']
        except:
            channel_type = "None"
        try:
            channel_name = data['channel']['name']
        except:
            channel_name = "None"
    else:
        ErrorUrl()

    print(f"""{color.BLUE}
    Invitation Information:
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Invitation        : {color.WHITE}{invite}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Type              : {color.WHITE}{type_value}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Code              : {color.WHITE}{code_value}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Expired           : {color.WHITE}{expires_at}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Server ID         : {color.WHITE}{server_id}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Server Name       : {color.WHITE}{server_name}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Channel ID        : {color.WHITE}{channel_id}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Channel Name      : {color.WHITE}{channel_name}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Channel Type      : {color.WHITE}{channel_type}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Server Icon       : {color.WHITE}{server_icon}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Server Features   : {color.WHITE}{server_features}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Server NSFW Level : {color.WHITE}{server_nsfw_level}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Server NSFW       : {color.WHITE}{server_nsfw}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Flags             : {color.WHITE}{flags}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Server Verification Level         : {color.WHITE}{server_verification_level}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Server Premium Subscription Count : {color.WHITE}{server_premium_subscription_count}{color.BLUE}

    Inviter Information:
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} ID            : {color.WHITE}{inviter_id}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Username      : {color.WHITE}{inviter_username}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Global Name   : {color.WHITE}{inviter_global_name}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Avatar        : {color.WHITE}{inviter_avatar}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Discriminator : {color.WHITE}{inviter_discriminator}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Public Flags  : {color.WHITE}{inviter_public_flags}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Flags         : {color.WHITE}{inviter_flags}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Banner        : {color.WHITE}{inviter_banner}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Accent Color  : {color.WHITE}{inviter_accent_color}{color.BLUE}
    {color.WHITE}[{color.BLUE}+{color.WHITE}]{color.BLUE} Banner Color  : {color.WHITE}{inviter_banner_color}{color.BLUE}
    """)
    Continue()
    Reset()
except Exception as e:
    Error(e)