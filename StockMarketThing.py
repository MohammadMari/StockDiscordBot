import discord
import os
from discord.ext import commands
import random

client = commands.Bot(command_prefix=">")


NIO = 100000
TLRY = 100000
SNDL = 100000
ETH = 100000
DOGE = 100000
BTC = 100000
            
@client.command()
async def NIO (ctx, message):
    try:
        NIO = float(message)
        output = "NIO Updated to " + message
        await ctx.send(output)
    except:
        await ctx.send("Please enter valid input")

@client.command()
async def TLRY (ctx, message):
    try:
        TLRY = float(message)
        output = "TLRY Updated to " + message
        await ctx.send(output)
    except:
        await ctx.send("Please enter valid input")

@client.command()
async def SNDL (ctx, message):
    try:
        SNDL = float(message)
        output = "SNDL Updated to " + message
        await ctx.send(output)
    except:
        await ctx.send("Please enter valid input")

@client.command()
async def ETH (ctx, message):
    try:
        ETH = float(message)
        output = "ETH Updated to " + message
        await ctx.send(output)
    except:
        await ctx.send("Please enter valid input")

@client.command()
async def DOGE (ctx, message):
    try:
        DOGE = float(message)
        output = "DOGE Updated to " + message
        await ctx.send(output)
    except:
        await ctx.send("Please enter valid input")

@client.command()
async def BTC (ctx, message):
    try:
        BTC = float(message)
        output = "BTC Updated to " + message
        await ctx.send(output)
    except:
        await ctx.send("Please enter valid input")

@client.event
async def on_ready():
    print("Bot is ready")
    
client.run("")


import matplotlib.pyplot as plt
import PySimpleGUI as sg
from yahoo_fin import stock_info
import cryptocompare



# layout = [  [sg.Text('Enter Notification Price for NIO'), sg.InputText(key='NIO')],
#             [sg.Text('Enter Notification Price for TLRY'), sg.InputText(key='TLRY')],
#             [sg.Text('Enter Notification Price for SNDL'), sg.InputText(key='SNDL')],
#             [sg.Text('Enter Notification Price for ETH'), sg.InputText(key='ETH')],
#             [sg.Text('Enter Notification Price for DOGE'), sg.InputText(key='DOGE')],
#             [sg.Text('Enter Notification Price for BTC'), sg.InputText(key='BTC')],
#             [sg.Button('Quit')]]
            

# # Create the Window
# window = sg.Window('gloom#2026 #1 qt', layout)
# # Create an event loop

# NIONotif = False
# TLRYNotif = False
# SNDLNotif = False
# ETHNotif = False
# DOGENotif = False
# BTCNotif = False

# counter = 600

# while True:
#     event, values = window.read(timeout=1000)

#     if counter < 1:
#         NIONotif = False
#         TLRYNotif = False
#         SNDLNotif = False
#         ETHNotif = False
#         DOGENotif = False
#         BTCNotif = False

#     #print("1")
#     try:
#         if float(values['NIO']) > stock_info.get_live_price("NIO") and not NIONotif:
#             print("NIO")
#             NIONotif = True
#     except:
#         print("")

#    # print("2")
#     try:
#         if float(values['TLRY']) > stock_info.get_live_price("TLRY") and not TLRYNotif:
#             print("TLRY")
#             TLRYNotif = True
#     except:
#         print("")

#    # print("3")

#     try:
#         if float(values['SNDL']) > stock_info.get_live_price("SNDL") and not SNDLNotif:
#             print("SNDL")
#             SNDLNotif = True
#     except:
#         print("")

#    # print("4")

#     try:
#         if float(values['BTC']) > cryptocompare.get_price('BTC', currency='USD')['BTC']['USD'] and not BTCNotif:
#             print("BTC")
#             BTCNotif = True
#     except:
#         print("")

#     try:
#         if float(values['DOGE']) > cryptocompare.get_price('DOGE', currency='USD')['DOGE']['USD'] and not BTCNotif:
#             print("DOGE")
#             BTCNotif = True
#     except:
#         print("")

#     try:
#         if float(values['ETH']) > cryptocompare.get_price('ETH', currency='USD')['ETH']['USD'] and not BTCNotif:
#             print("ETH")
#             BTCNotif = True
#     except:
#         print("")

#    # print("5")

#     if event == sg.WIN_CLOSED or event == 'Quit':
#         break
