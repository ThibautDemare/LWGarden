import time
from LWApi import LWApi
import os
import json


def main():
    """Main function, it constites of a Menu where you can select
    an action to perform:
     - Get All AIs"""
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██████▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁████▓▓▓▓▓▓████▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁████▁▁██▓▓▓▓▓▓▓▓▓▓██▁▁████▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁██▓▓▓▓████▓▓▓▓▓▓▓▓▓▓████▓▓▓▓██▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▁▁▁▁")
    print("▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓██▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓██▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁██▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁██▁▁██▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁██▁▁██▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▒▒▒▒▁▁▒▒▒▒██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁██▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██████▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")

    print("\nWelcome to the Leek Garden, a tool to empower your leeks on LeekWars!")

    print("\nTry to login on the LeekWars Api, please ensure that a config.json is present, with your username and password")
    with open("./src/config.json", "r") as configfile:
        config = json.load(configfile)
    api = LWApi()
    api.connect(config["username"], config["password"])

    menu = {}
    menu['1']="Get your AIs."
    menu['2']="Launch fight"
    menu['3']="Get Register"
    menu['4']="Get Farmer's Throphies"
    menu['5']="Exit"
    while True:
        options=sorted(menu.keys())

        for entry in options:
            print(entry, menu[entry])

        selection=input("Please Select:") 
        if selection =='1':
            GetAllAIs(api, config)
        elif selection == '2':
            print("delete")
        elif selection == '3':
            GetRegister(api,config)
        elif selection == '4':
            GetFarmerTrophies(api,config)
            break
        elif selection == '5':
            break
        else:
            print("Unknown Option Selected!")

def GetAllAIs(api, config):
    """Get all AIs from LeekWars, and save them in a directory location
    The folder hiearchie will be respected"""
    print("\nGetAllAIs()\n")
    allAIs = api.getIAs()

    allFolders = { 0 : "./" }
    for folder in  allAIs["folders"]:
        allFolders[folder["id"]] = folder["name"]
        path = os.path.join(config["AIs_folder"],folder["name"])
        if(not(os.path.exists(path))) :
            os.mkdir(path)

    for ai in  allAIs["ais"]:
        name = ai["name"]
        folder = os.path.join(config["AIs_folder"],allFolders[ai["folder"]])
        code = api.getIA(str(ai["id"]))["ai"]["code"]
        with open(os.path.join(folder,name+".leek"), "w") as outfile:
            outfile.write(code)
        time.sleep(0.2)

def Fight(api,config):
    print("\nFight()\n")


def GetRegister(api,config):
    print("\nRegister()\n")
    registers = api.getRegisters("82210")
    menu ={}
    i=0
    for register in registers["registers"]:
        menu[str(i)]= register["key"]
        i+=1
    
    while True:
        options=sorted(menu.keys())
        for entry in options: 
            print(entry, menu[entry])
        selection=input("Please Select: (input any other key to exit)")
        if options.__contains__(selection) :
            selectedRegister = next(filter(lambda x: x["key"] == menu[selection] , registers["registers"]))
            last = sorted(json.loads(selectedRegister["value"]).values(), reverse=True)
            print(last)
            somme = sum(last)
            total = len(last)
            print(somme/total)
            print(last[0])
        else: 
            break
        print("\n")

def GetFarmerTrophies(api,config):
    selection=input("Please enter farmer id: ")
    trophies= api.getFarmerTrophies(selection)
    pyro = next(filter(lambda x: x["code"] == "explorator" , trophies["trophies"]))
    print(pyro)


# Here goes all the magic
main()
