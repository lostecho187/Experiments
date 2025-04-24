import pandas as pd
# import igraph as ig
# import random
# import itertools
# import operator
import pickle

##user_id,item_id,timestamp,state_label,comma_separated_list_of_features
auth = pd.read_csv("./auth_ntlm.csv")

authlog = auth[['time', 'user', 'src', 'dst']]
del auth


# ## 1- Build In Host User Map
def BuildInHostUserMap(authlog):
    InHostUserMap = {}
    for index, event in authlog.iterrows():
        if event['dst'] not in InHostUserMap:
            InHostUserMap[event['dst']] = {}
        if event['user'] not in InHostUserMap[event['dst']]:
            InHostUserMap[event['dst']][event['user']] = {}
        day = event['time']/86400
        if day not in InHostUserMap[event['dst']][event['user']]:
             InHostUserMap[event['dst']][event['user']][day] = 0
        InHostUserMap[event['dst']][event['user']][day] += 1
        
    return InHostUserMap

InHostUserMap = BuildInHostUserMap(authlog)
pickle.dump(InHostUserMap, open("InHostUserMap.pkl", "wb"))


# ## 2- Build In Host Src Map
def BuildInHostSrcMap(authlog):
    InHostSrcMap = {}
    for index, event in authlog.iterrows():
        if event['dst'] not in InHostSrcMap:
            InHostSrcMap[event['dst']] = {}
        if event['src'] not in InHostSrcMap[event['dst']]:
            InHostSrcMap[event['dst']][event['src']] = {} 
        day = event['time']/86400
        if day not in InHostSrcMap[event['dst']][event['src']]:
             InHostSrcMap[event['dst']][event['src']][day] = 0
        InHostSrcMap[event['dst']][event['src']][day] += 1
        
    return InHostSrcMap


InHostSrcMap = BuildInHostSrcMap(authlog)
pickle.dump(InHostSrcMap, open("InHostSrcMap.pkl", "wb")) 


# ## 3- Build In Host Usr Src Map
def BuildInHostUsrSrcMap(authlog):
    InHostUsrSrcMap = {}
    for index, event in authlog.iterrows():
        if event['dst'] not in InHostUsrSrcMap:
            InHostUsrSrcMap[event['dst']] = {}
        if event['user']+event['src'] not in InHostUsrSrcMap[event['dst']]:
            InHostUsrSrcMap[event['dst']][event['user']+event['src']] = {} 
        day = event['time']/86400
        if day not in InHostUsrSrcMap[event['dst']][event['user']+event['src']]:
             InHostUsrSrcMap[event['dst']][event['user']+event['src']][day] = 0
        InHostUsrSrcMap[event['dst']][event['user']+event['src']][day] += 1
        
    return InHostUsrSrcMap

InHostUsrSrcMap = BuildInHostUsrSrcMap(authlog)
pickle.dump(InHostUsrSrcMap, open("InHostUsrSrcMap.pkl", "wb")) 


# ## 4- Build Out Host Usr Map
def BuildOutHostUsrMap(authlog):
    OutHostUserMap = {}
    for index, event in authlog.iterrows():
        if event['src'] not in OutHostUserMap:
            OutHostUserMap[event['src']] = {}
        if event['user'] not in OutHostUserMap[event['src']]:
            OutHostUserMap[event['src']][event['user']] = {} 
        day = event['time']/86400
        if day not in OutHostUserMap[event['src']][event['user']]:
             OutHostUserMap[event['src']][event['user']][day] = 0
        OutHostUserMap[event['src']][event['user']][day] += 1
        
    return OutHostUserMap

OutHostUserMap = BuildOutHostUsrMap(authlog)
pickle.dump(OutHostUserMap, open("OutHostUserMap.pkl", "wb")) 


# ## 5- Build Out Host Dst Map
def BuildOutHostDstMap(authlog):
    OutHostDstMap = {}
    for index, event in authlog.iterrows():
        if event['src'] not in OutHostDstMap:
            OutHostDstMap[event['src']] = {}
        if event['dst'] not in OutHostDstMap[event['src']]:
            OutHostDstMap[event['src']][event['dst']] = {} 
        day = event['time']/86400
        if day not in OutHostDstMap[event['src']][event['dst']]:
             OutHostDstMap[event['src']][event['dst']][day] = 0
        OutHostDstMap[event['src']][event['dst']][day] += 1
        
    return OutHostDstMap

OutHostDstMap = BuildOutHostDstMap(authlog)
pickle.dump(OutHostDstMap, open("OutHostDstMap.pkl", "wb")) 


# ## 6- Build Out Host Usr Dst Map
def BuildOutHostUsrDstMap(authlog):
    OutHostUsrDstMap = {}
    for index, event in authlog.iterrows():
        if event['src'] not in OutHostUsrDstMap:
            OutHostUsrDstMap[event['src']] = {}
        if event['user']+event['dst'] not in OutHostUsrDstMap[event['src']]:
            OutHostUsrDstMap[event['src']][event['user']+event['dst']] = {} 
        day = event['time']/86400
        if day not in OutHostUsrDstMap[event['src']][event['user']+event['dst']]:
             OutHostUsrDstMap[event['src']][event['user']+event['dst']][day] = 0
        OutHostUsrDstMap[event['src']][event['user']+event['dst']][day] += 1
        
    return OutHostUsrDstMap

OutHostUsrDstMap = BuildOutHostUsrDstMap(authlog)
pickle.dump(OutHostUsrDstMap, open("OutHostUsrDstMap.pkl", "wb")) 
