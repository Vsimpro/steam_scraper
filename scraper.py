import json,requests,datetime

# Global Variables
item_list = []

def get_timestamp():
    time = datetime.datetime.now().strftime("|%Y-%m-%d|%H:%M:%S|")
    return  f"{time}"

def get_items():
    head = "https://steamcommunity.com/market/listings/730/Sticker%20%7C%20"
    tail = "%20%28Holo%29%20%7C%20Stockholm%202021\n"
    with open("items.txt", "r") as file:
        for i in file.readlines():
            if not i == "":
                i = i.replace(head,"")
                i = i.replace(tail,"")
                item_list.append(i)

def pull(team):
    # Returns a code accordingly,
    # 0: Succesfull
    # 1: Null from api
    # 2: Error from api
    code = 0
    url = (f"http://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name=Sticker%20%7C%20{team}%20%28Holo%29%20%7C%20Stockholm%202021&currency=3")
    pull = requests.get(url)
    data = json.loads(pull.content)
    if data == None:
        print(f"[!] Error: datavalue is: {data}\nThis might be due to too many pull requests.\nItem: {team}")
        code = 1
        
    elif data["success"] == False:
        print(f"[!] COULD NOT PULL {team}, check its hashname!")    
        code = 2
        
    else: 
        print(f"[+] {team}::{data}::{get_timestamp()}")

    # Before returning you might want to log the data you've gained.
    # I've excluded my logging system from this script for now.
    return code     

#Example of the loop I used:
while True:
    get_items()
    for team in item_list:
            pull(team)
