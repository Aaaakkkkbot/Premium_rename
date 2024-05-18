class script(object):
    HELP_TXT = """<b>๏ ʜᴇʏ 😎</b> {}
    
<b>Here Is The Help For My Commands.</b>"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>

<b>⦿ /set_caption - Use This Command To Set Your Caption</b>
<b>⦿ /see_caption - Use This Command To See Your Caption</b>
<b>⦿ /del_caption - Use This Command To Delete Your Caption</b>"""
   
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>

<b>⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....</b>

<b>⦿ /viewthumb - Use This Command To See Your Thumbnail</b>
<b>⦿ /delthumb - Use This Command To Delete Your Thumbnail</b>"""

    ABOUT_TXT = """<b>🤖 My Name :</b> <a href='https://t.me/Fast_Renamer_ZBot'>Fast Renamer ZBot</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/ZPro_Bots'>ZPro Bots</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/Devil_Eyes_ZX'>Devil Eyes</a>

<b>♻ Bot Made By :</b> @ZPro_Bots"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> <code>anime-legend@axl</code> 

<b>๏ ᴍᴀsᴛᴇʀ :- @Devil_Eyes_ZX</b> """

    ADMIN_TXT = """<b><u>🦋 ADMIN ALL COMMANDS HERE</u></b>

<b>⦿ /users - Use This Command To See Total Users</b>
<b>⦿ /allids - Use This Command To See All Users IDs</b>
<b>⦿ /broadcast - Use This Command To Send A Message To Users</b>
<b>⦿ /warn - Use This Command To Send A Message To A User</b>
<b>⦿ /resetpower - Use This Command To Reset User Power</b>
<b>⦿ /ceasepower - Use This Command To Cease User Power</b>
<b>⦿ /addpremium - Use This Command To Add Premium To Users</b>
<b>⦿ /restart - Use This Command To Cancel All Process And Restart The Bot</b>"""

     UPGRADE_TXT= """<b>Fʀᴇᴇ ᴘʟᴀɴ ᴜsᴇʀᴜsᴇʀ</b>

<b>☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 2.0 GB</b>
<b>☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 2</b>
<b>☞ ᴛɪᴍᴇᴏᴜᴛ: 1 ᴍɪɴᴜᴛᴇꜱ</b>
<b>☞ ᴛɪᴍᴇ ɢᴀᴘ: ʏᴇꜱ</b>
	
<b>▼ Uᴘɢʀᴀᴅᴇ ᴘʟᴀɴ ▼</b>"""

     FREE_TXT= """<b>❤️‍🔥 sɪʟᴠᴇʀ ᴘʟᴀɴ</b>

<b>☞ ᴜᴘʟᴏᴀᴅ 2ɢʙ ꜰɪʟᴇꜱ: ᴛʀᴜᴇ</b>
<b>☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 2ɢʙ</b>
<b>☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 2</b>
<b>☞ ᴛɪᴍᴇ ɢᴀᴘ: ɴᴏ ᴛɪᴍᴇ ɢᴀᴘ</b>

<b>💰 ᴘʟᴀɴ ᴘʀɪᴄᴇ</b>

<b>☞ ᴘʀɪᴄᴇ: 0</b>
<b>☞ ᴠᴀʟɪᴅɪᴛʏ: ʟɪғᴇᴛɪᴍᴇ</b>"""

     SILVER_TXT="""<b>🥈 sɪʟᴠᴇʀ ᴘʟᴀɴ</b>

<b>☞ ᴜᴘʟᴏᴀᴅ 4ɢʙ ꜰɪʟᴇꜱ: ᴛʀᴜᴇ</b>
<b>☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 20.0ɢʙ</b>
<b>☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 2</b>
<b>☞ ᴛɪᴍᴇ ɢᴀᴘ: ɴᴏ ᴛɪᴍᴇ ɢᴀᴘ</b>

<b>💰 <b>ᴘʟᴀɴ ᴘʀɪᴄᴇ</>

<b>☞ ᴘʀɪᴄᴇ: ₹49</b>
<b>☞ ᴠᴀʟɪᴅɪᴛʏ: 𝟹𝟶ᴅᴀʏs</b>"""

     GOLDEN_TXT="""<b>🎖 Gᴏʟᴅᴇɴ ᴘʟᴀɴ</b>

<b>☞ ᴜᴘʟᴏᴀᴅ 4ɢʙ ꜰɪʟᴇꜱ: ᴛʀᴜᴇ</b>
<b>☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 50.0ɢʙ</b>
<b>☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 3</b>
<b>☞ ᴛɪᴍᴇ ɢᴀᴘ: ɴᴏ ᴛɪᴍᴇ ɢᴀᴘ</b>

<b>💰 ᴘʟᴀɴ ᴘʀɪᴄᴇ</b>

<b>☞ ᴘʀɪᴄᴇ: ₹99</b>
<b>☞ ᴠᴀʟɪᴅɪᴛʏ: 𝟹𝟶ᴅᴀʏs</b>"""

     DIAMOND_TXT= """<b>💎 Dɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</b>

<b>☞ ᴜᴘʟᴏᴀᴅ 4ɢʙ ꜰɪʟᴇꜱ: ᴛʀᴜᴇ</b>
<b>☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 100.0ɢʙ</b>
<b>☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 5</b>
<b>☞ ᴛɪᴍᴇ ɢᴀᴘ: ɴᴏ ᴛɪᴍᴇ ɢᴀᴘ</b>

<b>💰 ᴘʟᴀɴ ᴘʀɪᴄᴇ</b>

<b>☞ ᴘʀɪᴄᴇ: ₹159</b>
<b>☞ ᴠᴀʟɪᴅɪᴛʏ: 𝟹𝟶ᴅᴀʏs</b>"""
