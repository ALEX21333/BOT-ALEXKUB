import interactions
import os 
import platform
import random
import requests
from interactions import *
from keep_alive import keep_alive

token = "MTIyNzU1NzkwMjY2ODAwOTU0Mw.GcTNXa.XKRR3x56wyb5Vy1FzvxwP9lpsTR5wkAlioDqmE"

meoaw = interactions.Client(token=token, intents=Intents.ALL)

ch_id = "1230940770652127365" # ช่องสำหรับส่ง panel

phone = "0630102037 "

# Log Config

log_id = "1230940924624764948" # ไอดีช่องหลังบ้าน !

# Embed Config

m_title = "VIPTJ"

m_tn = "https://media.discordapp.net/attachments/1230918596272590981/1230920080011952170/background_removed.png?ex=663512a8&is=66229da8&hm=1bab3b7e08a5b1cd554a2f9e82940e6352e5b14f98a6b706db5003bab0249d5e&=&format=webp&quality=lossless"

m_img = "https://cdn.discordapp.com/attachments/1090081082373840989/1095949438008176700/aungpao_truewallet_03.jpg"

# Role Config

role_01 = "1230885677802197093" # ไอดียศที่ 1

role01_name = "VIPBOY" # ชื่อยศที่ 1

role_01p = "70.00" # ราคายศที่ 1 ใส่ลงท้าย .00 เช่น 10 บาท ก็คือ 10.00

role_02 = "1230885755006484601" # ไอดียศที่ 2

role02_name = "VIPCUTE" # ชื่อยศที่ 2

role_02p = "60.00" # ราคายศที่ 2 ใส่ลงท้าย .00 เช่น 20 บาท ก็คือ 20.00

role_03 = "1230885807393476729" # ไอดียศที่ 3

role03_name = "Super VIP" # ชื่อยศที่ 3

role_03p = "110.00" # ราคายศที่ 3 ใส่ลงท้าย .00 เช่น 30 บาท ก็คือ 30.00

@interactions.listen()
async def on_ready():

    ch = await meoaw.fetch_channel(channel_id=ch_id)

    main_embed = interactions.Embed(title=f"**{m_title} Topup**", description="_ _", color=0x00FF00)

    main_embed.add_field(name="> วิธีใช้งาน", value="_ _\n`❓`: กดปุ่ม `เติมเงิน` เพื่อใช้งาน !\n_ _\n_ _")

    main_embed.set_thumbnail(m_tn) 

    main_embed.set_image(m_img)

    main_embed.set_footer("© 2023 MeoawJi Studio All rights reserved")

    topup = Button(
        style=ButtonStyle.GREEN,
        custom_id="topup_cb",
        label="เติมเงิน",
    )

    all = Button(
        style=ButtonStyle.SECONDARY,
        custom_id="all_cb",
        label="ดูยศทั้งหมด",
    )

    await ch.send(embeds=main_embed, components=[topup, all])


    if platform.system() == 'Windows':

        os.system(f'cls & title {m_title} Topup ( 5.1 )')

        print(" ")

        print(f"{m_title} Topup ( 5.1 )")

        print(" ")

    else:

        os.system("clear")

        print(" ")

        print(f"{m_title} Topup (5.1 )")

        print(" ")

@interactions.listen()
async def on_component(event: BaseComponent):

    ctx = event.ctx

    match ctx.custom_id:
        case "topup_cb":
            select_plan = StringSelectMenu(
                [
                    interactions.StringSelectOption(label="เติมเงิน", emoji="💸", value="test"),
                ],
                placeholder="🟢 เลือกยศที่จะซื้อ",
                min_values=1,
                max_values=1,
            )

            await ctx.send(components=select_plan, ephemeral=True)

            def check(component: Button) -> bool:
                return component.ctx.author.id == ctx.author.id

            try:

                used_component = await meoaw.wait_for_component(components=select_plan, check=check, timeout=30)
                used_ctx = used_component.ctx

                rolebuy = used_ctx.values[0]

                topup_modal = Modal(
                    ShortText(
                    label="ลิงค์ซองของขวัญ",
                    custom_id="giftLink",
                    required=True,
                    placeholder="กรุณาใส่ลิ้งค์ซอง !",
                    max_length=80,
                    ),
                    title="🧧 เติมเงินรับยศ!",
                )
                await used_ctx.send_modal(modal=topup_modal)

                modal_ctx: ModalContext = await used_ctx.bot.wait_for_modal(topup_modal)

                giftLink = modal_ctx.responses['giftLink']

                auth = requests.get(f"https://zamex-hub.000webhostapp.com/index.php?phone={phone}&link={giftLink}")

                gotji = auth.json()

                if gotji["status"] == "SUCCESS":

                    if gotji["amount"] == role_01p:

                        role_01s = interactions.Embed(title=f"**{m_title} Success ( 1 )**", description="_ _", color=0x92f0a3)

                        role_01s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")

                        role_01s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_01}>\n_ _\n")

                        role_01s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@&{role_01p}>\n_ _\n")

                        await ctx.send(embeds=role_01s, ephemeral=True)

                        log_01 = await meoaw.fetch_channel(channel_id=log_id)

                        await ctx.author.add_role(role_01, "เติม vip class 1 สำเร็จ !")

                        log_01eb = interactions.Embed(title=f"**{m_title} Log**", description="_ _", color=0x75ffb1)

                        log_01eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")

                        log_01eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_01}>\n_ _\n_ _")

                        await log_01.send(f"<@{ctx.author.id}>", embeds=log_01eb)

                    elif gotji["amount"] == role_02p:

                        role_02s = interactions.Embed(title=f"**{m_title} Success ( 2 )**", description="_ _", color=0x92f0a3)

                        role_02s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")

                        role_02s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_02}>\n_ _\n")

                        role_02s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@&_{role_02p}>\n_ _\n")

                        await ctx.author.add_role(role_02, "เติม vip class 2 สำเร็จ !")

                        await ctx.send(embeds=role_02s, ephemeral=True)

                        log_02 = await meoaw.fetch_channel(channel_id=log_id)

                        log_02eb = interactions.Embed(title=f"**{m_title} Log**", description="_ _", color=0x75ffb1)

                        log_02eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")

                        log_02eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_02}>\n_ _\n_ _")

                        await log_02.send(f"<@{ctx.author.id}>", embeds=log_02eb)

                    elif gotji["amount"] == role_03p:

                        role_03s = interactions.Embed(title=f"**{m_title} Success ( 3 )**", description="_ _", color=0x92f0a3)

                        role_03s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")

                        role_03s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_03}>\n_ _\n")

                        role_03s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@&{role_03p}>\n_ _\n")

                        await ctx.author.add_role(role_03, "เติม vip class 3 สำเร็จ !")

                        await ctx.send(embeds=role_03s, ephemeral=True)

                        log_03 = await meoaw.fetch_channel(channel_id=log_id)

                        log_03eb = interactions.Embed(title=f"**{m_title} Log**", description="_ _", color=0x75ffb1)

                        log_03eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")

                        log_03eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_03}>\n_ _\n_ _")

                        await log_03.send(f"<@{ctx.author.id}>", embeds=log_03eb)

                    else:

                        role_04s = interactions.Embed(title=f"**{m_title} Success ( 4 )**", description="_ _", color=0xf59300)

                        role_04s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")

                        role_04s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: ไม่พบยศ !\n_ _\n")

                        role_04s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: ไม่สามารถดึงค่าได้ !\n_ _\n")

                        await ctx.send(embeds=role_04s, ephemeral=True)

                        log_04 = await meoaw.fetch_channel(channel_id=log_id)

                        log_04eb = interactions.Embed(title=f"**{m_title} Log**", description="_ _", color=0x75ffb1)

                        log_04eb.add_field(name="> สถานะ", value="_ _\n`❗`: เติมเงินเกินกว่าที่ระบบตั้งไว้ !\n_ _\n_ _")

                        await log_04.send(f"<@{ctx.author.id}>", embeds=log_04eb)

                else:

                    print("Fail")

                    fail = interactions.Embed(title=f"**{m_title} Fail**", description="_ _", color=0xf50049)

                    fail.add_field(name="> สถานะ", value="_ _\n`❌`: เติมเงินไม่สำเร็จ\n_ _\n")

                    await ctx.send(embeds=fail, ephemeral=True)

                    fail_x = await meoaw.fetch_channel(channel_id=log_id)

                    faileb = interactions.Embed(title=f"**{m_title} Log**", description="_ _", color=0xff004c)

                    faileb.add_field(name="> สถานะ", value="_ _\n`❌`: เติมเงินไม่สำเร็จ\n_ _\n_ _")

                    await fail_x.send(f"<@{ctx.author.id}>", embeds=faileb)

            except TimeoutError:

                print("Timed Out!")

        case "all_cb":

            role_all = interactions.Embed(title=f"**{m_title} Role**", description="_ _", color=0xeef092)

            role_all.add_field(name=f"> ยศ {role01_name}", value=f"_ _\n<@&{role_01}>\n_ _\n`💰`: `{role_01p}`\n_ _\n_ _")

            role_all.add_field(name=f"> ยศ {role02_name}", value=f"_ _\n<@&{role_02}>\n_ _\n`💰`: `{role_02p}`\n_ _\n_ _")

            role_all.add_field(name=f"> ยศ {role03_name}", value=f"_ _\n<@&{role_03}>\n_ _\n`💰`: `{role_03p}`\n_ _\n_ _")

            role_all.set_footer("© 2023 MeoawJi Studio All rights reserved")

            await ctx.send(embeds=role_all, ephemeral=True)

keep_alive()

meoaw.start(token)

# Code by Meoaw | discord.gg/meoaw | Last update 30/5/66 19:42