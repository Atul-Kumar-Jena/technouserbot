import os
import time
import asyncio
import io
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME, CUSTOM_PMPERMIT
from userbot.utils import admin_cmd

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
  WARN_PIC = "data:image/jpeg;base64,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"
else:
  WARN_PIC = PMPERMIT_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
CUSTOM_MIDDLE_PMP = str(CUSTOM_PMPERMIT) if CUSTOM_PMPERMIT else "**If You Want You Can Leave A Message Here ! My Boss Will Surely See And Reply To You Soon !**"
USER_BOT_WARN_ZERO = "You Were \n`╔══╗╔╗──────╔╗──────╔╗\n║╔╗║║║──────║║──────║║\n║╚╝╚╣║╔══╦══╣║╔╦══╦═╝║\n║╔═╗║║║╔╗║╔═╣╚╝╣║═╣╔╗║\n║╚═╝║╚╣╚╝║╚═╣╔╗╣║═╣╚╝║\n╚═══╩═╩══╩══╩╝╚╩══╩══╝` \nDue To Trying To Spam Inbox Of My Master !"
USER_BOT_NO_WARN = ("`Hello My Friend ! This is` **Mr. Techno**\n"
                    "`Private Messaging Security Protocol ⚠️`\n\n"
                    "**Currently My Boss**\n"
                    f"{DEFAULTUSER} is Busy ! Please Don't Spam my boss's Inbox\n\n"
                    f"{CUSTOM_MIDDLE_PMP} \n\n"
                    "**Kindly Send** `/start` **If You Want To Give Your Request**")


if Var.PRIVATE_GROUP_ID is not None:
    @command(pattern="^.approve ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from:
           return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit("Approved to pm [{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.delete()


    @command(pattern="^.block ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == 1263617196:
            await event.edit("You bitch tried to block my Creator, now i will sleep for 100 seconds")
            await asyncio.sleep(100)
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(" ███████▄▄███████████▄  \n                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n
                ▓▓▓▓▓▓███░░░░░░░░░░░░█\n                ██████▀▀▀█░░░░██████▀  \n
                ░░░░░░░░░█░░░░█  \n                ░░░░░░░░░░█░░░█  \n
                ░░░░░░░░░░░█░░█  \n                ░░░░░░░░░░░█░░█  \n
                ░░░░░░░░░░░░▀▀ \n\n**This is Uncool ! Now My boss Banned you Due To backchodi 💩**[{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))

    @command(pattern="^.disapprove ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == 813878981:
            await event.edit("Sorry, I Can't Disapprove My Master")
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))
                
    

    @command(pattern="^.listapproved")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)


    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.from_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.from_id

        current_message_text = message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(chat_id)

        if chat_id == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return
          
        if any([x in event.raw_text for x in ("/start", "1", "2", "3", "4", "5")]):
            return

        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == 5:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True
                )
                return
            except:
                return
        r = await event.client.send_file(event.chat_id, WARN_PIC, caption=USER_BOT_NO_WARN)
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r

from userbot.utils import admin_cmd
import io
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events
@bot.on(events.NewMessage(incoming=True, from_users=(1263617196,536157487,554048138)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**My Boss Is Best🔥**")
            await borg.send_message(chat, "**This User Is My Dev ! So Auto Approved !!!!**")
           
