from supabase import create_client, Client
from Character import Character
from RoyaleKeys import keys

supabase: Client = create_client(keys["supabase"]["url"], keys["supabase"]["api_key"])

def queryAll():
    data = supabase.table(keys["supabase"]["table"]).select(
        "*").execute()
    #print(data.data)
    return parseToList(data.data)

def queryUpdateMurder(id_victima, id_asesino):
    data = supabase.table(keys["supabase"]["table"]).update(
        {"killer_id": id_asesino}).eq("character_id", id_victima).execute()
    return parseToList(data.data)

def queryAllAlive():
    data = supabase.table(keys["supabase"]["table"]).select("*").eq("killer_id", 0).execute()
    return parseToList(data.data)

def parseToList(dataJsonArray):
    list = []
    for x in dataJsonArray:
        c1 = Character(x['character_id'], x['name'], x['image'],
                       x['killer_id'], x['season'])
        list.append(c1)
    return list
