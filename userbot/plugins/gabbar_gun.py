"""command: Epic Gun Of Gabbar from Sholey: .gun"""

#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from telethon import events

import random

import asyncio

@borg.on(events.NewMessage(pattern=r"\.gu(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str in "n":

        emoticons = [

            "💥🔫 <<Suwar Ke Bacchon >>User<< Killed>>",

            "🔫 ≈No Bullet, U Are Safe≈",

            "🔫 ≈No Bullet, U Are Safe≈",

            "🔫 ≈No Bullet, U Are Safe≈",

            "🔫 ≈No Bullet, U Are Safe≈",

            "🔫 ≈No Bullet, U Are Safe≈",

        ]

    elif input_str in "thinking":

        emoticons = [

            "(҂⌣̀_⌣́)",

            "（；¬＿¬)",

            "(-｡-;",

            "┌[ O ʖ̯ O ]┐",

            "〳 ͡° Ĺ̯ ͡° 〵",

        ]

    elif input_str in "waving":

        emoticons = [

            "(ノ^∇^)",

            "(;-_-)/",

            "@(o・ェ・)@ノ",

            "ヾ(＾-＾)ノ",

            "ヾ(◍’౪◍)ﾉﾞ♡",

            "(ό‿ὸ)ﾉ",

            "(ヾ(´・ω・｀)",

        ]

    elif input_str in "wtf":

        emoticons = [

            "༎ຶ‿༎ຶ",

            "(‿ˠ‿)",

            "╰U╯☜(◉ɷ◉ )",

            "(;´༎ຶ益༎ຶ)♡",

            "╭∩╮(︶ε︶*)chu",

            "( ＾◡＾)っ (‿|‿)",

        ]

    elif input_str in "love":

        emoticons = [

            "乂❤‿❤乂",

            "(｡♥‿♥｡)",

            "( ͡~ ͜ʖ ͡°)",

            "໒( ♥ ◡ ♥ )७",

            "༼♥ل͜♥༽",

        ]

    elif input_str in "confused":

        emoticons = [

            "(・_・ヾ",

            "｢(ﾟﾍﾟ)",

            "﴾͡๏̯͡๏﴿",

            "(￣■￣;)!?",

            "▐ ˵ ͠° (oo) °͠ ˵ ▐",

            "(-_-)ゞ゛",

        ]

    elif input_str in "dead":

        emoticons = [

            "(✖╭╮✖)",

            "✖‿✖",

            "(+_+)",

            "(✖﹏✖)",

            "∑(✘Д✘๑)",

        ]

    elif input_str in "sad":

        emoticons = [

            "(＠´＿｀＠)",

            "⊙︿⊙",

            "(▰˘︹˘▰)",

            "●︿●",

            "(　´_ﾉ` )",

            "彡(-_-;)彡",

        ]

    elif input_str in "dog":

        emoticons = [

            "-ᄒᴥᄒ-",

            "◖⚆ᴥ⚆◗",

        ]

    else:    

        emoticons = [

            "( ͡° ͜ʖ ͡°)",

            "¯\_(ツ)_/¯",

            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",

            "ʕ•ᴥ•ʔ",

            "(▀ Ĺ̯▀   )",

            "(ง ͠° ͟ل͜ ͡°)ง",

            "༼ つ ◕_◕ ༽つ",

            "ಠ_ಠ",

            "(☞ ͡° ͜ʖ ͡°)☞",

            "¯\_༼ ି ~ ି ༽_/¯",

            "c༼ ͡° ͜ʖ ͡° ༽⊃",

        ]

    index = random.randint(0, len(emoticons))

    output_str = emoticons[index]

    await event.edit(output_str)
