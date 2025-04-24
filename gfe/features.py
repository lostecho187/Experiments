import pandas as pd
import pickle
import time
import numpy as np


InHostUserMap = {}
with open('InHostUserMap.pkl', 'rb') as pickle_file:
    InHostUserMap = pickle.load(pickle_file)

InHostSrcMap = {}
with open('InHostSrcMap.pkl', 'rb') as pickle_file:
    InHostSrcMap = pickle.load(pickle_file)

InHostUsrSrcMap = {}
with open('InHostUsrSrcMap.pkl', 'rb') as pickle_file:
    InHostUsrSrcMap = pickle.load(pickle_file)

OutHostDstMap = {}
with open('OutHostDstMap.pkl', 'rb') as pickle_file:
    OutHostDstMap = pickle.load(pickle_file)

OutHostUserMap = {}
with open('OutHostUserMap.pkl', 'rb') as pickle_file:
    OutHostUserMap = pickle.load(pickle_file)

OutHostUsrDstMap = {}
with open('OutHostUsrDstMap.pkl', 'rb') as pickle_file:
    OutHostUsrDstMap = pickle.load(pickle_file)


def Average(lst):
    return sum(lst) / len(lst)

def Stddev(lst):
    mean = Average(lst)
    variance = sum([((x - mean) ** 2) for x in lst]) / len(lst)
    stddev = variance ** 0.5
    return stddev

## Algorithm 7
def Calculate_IDusr(dst):
    InHostUserMap_list = list(InHostUserMap.keys())
    if dst in InHostUserMap_list:
        return len(list(InHostUserMap[dst].values()))
    else:
        return 0

## Algorithm 8
def Calculate_IDsrc(dst):
    InHostSrcMap_list = list(InHostSrcMap.keys())
    if dst in InHostSrcMap_list:
        return len(list(InHostSrcMap[dst].values()))
    else:
        return 0

## Algorithm 9
def Calculate_IDusr_src(dst):
    InHostUsrSrcMap_list = list(InHostUsrSrcMap.keys())
    if dst in InHostUsrSrcMap_list:
        return len(list(InHostUsrSrcMap[dst].values()))
    else:
        return 0

## Algorithm 10
def Calculate_ODusr(src):
    if src in list(OutHostUserMap.keys()):
        return len(list(OutHostUserMap[src].values()))
    else:
        return 0

## Algorithm 11
def Calculate_ODdst(src):
    if src in list(OutHostDstMap.keys()):
        return len(list(OutHostDstMap[src].values()))
    else:
        return 0

## Algorithm 12
def Calculate_ODusr_dst(src):
    if src in list(OutHostUsrDstMap.keys()):
        return len(list(OutHostUsrDstMap[src].values()))
    else:
        return 0

## Algorithm 13
def Calculate_IDAFusr(dst):
    UserFrequency = []
    if dst in list(InHostUserMap.keys()):
        for user in list(InHostUserMap[dst].keys()):
            UserFreq = Average(InHostUserMap[dst][user].values())
            UserFrequency.append(UserFreq)
        return Average(UserFrequency)
    else:
        return 0

## Algorithm 14
def Calculate_IDAFsrc(dst):
    SrcFrequency = []
    if dst in list(InHostSrcMap.keys()):
        for src in list(InHostSrcMap[dst].keys()):
            SrcFreq = Average(InHostSrcMap[dst][src].values())
            SrcFrequency.append(SrcFreq)
        return Average(SrcFrequency)
    else:
        return 0

## Algorithm 15
def Calculate_IDAFusr_src(dst):
    UsrSrcFrequency = []
    if dst in list(InHostUsrSrcMap.keys()):
        for usrsrc in list(InHostUsrSrcMap[dst].keys()):
            UsrSrcFreq = Average(InHostUsrSrcMap[dst][usrsrc].values())
            UsrSrcFrequency.append(UsrSrcFreq)
        return Average(UsrSrcFrequency)
    else:
        return 0

## Algorithm 16
def Calculate_ODAFusr(src):
    if src in OutHostUserMap:
        UserFrequency = [Average(OutHostUserMap[src][user].values()) for user in OutHostUserMap[src]]
        return np.mean(UserFrequency)
    else:
        return 0

## Algorithm 17
def Calculate_ODAFdst(src):
    if src in OutHostDstMap:
        DstFrequency = [Average(OutHostDstMap[src][dst].values()) for dst in OutHostDstMap[src]]
        return np.mean(DstFrequency)
    else:
        return 0

## Algorithm 18
def Calculate_ODAFusr_dst(src):
    if src in OutHostUsrDstMap:
        UsrDstFrequency = [Average(OutHostUsrDstMap[src][usrdst].values()) for usrdst in OutHostUsrDstMap[src]]
        return np.mean(UsrDstFrequency)
    else:
        return 0

## Algorithm 19
def Calculate_IDAFSTDusr(dst):
    UserFrequency = []
    if dst in list(InHostUserMap.keys()):
        for user in list(InHostUserMap[dst].keys()):
            UserFreq = Average(InHostUserMap[dst][user].values())
            UserFrequency.append(UserFreq)
        return Stddev(UserFrequency)
    else:
        return 0

## Algorithm 20
def Calculate_IDAFSTDsrc(dst):
    SrcFrequency = []
    if dst in list(InHostSrcMap.keys()):
        for src in list(InHostSrcMap[dst].keys()):
            SrcFreq = Average(InHostSrcMap[dst][src].values())
            SrcFrequency.append(SrcFreq)
        return Stddev(SrcFrequency)
    else:
        return 0

## Algorithm 21
def Calculate_IDAFSTDusr_src(dst):
    UsrSrcFrequency = []
    if dst in list(InHostUsrSrcMap.keys()):
        for usersrc in list(InHostUserMap[dst].keys()):
            UsrSrcFreq = Average(InHostUserMap[dst][usersrc].values())
            UsrSrcFrequency.append(UsrSrcFreq)
        return Stddev(UsrSrcFrequency)
    else:
        return 0

## Algorithm 22
def Calculate_ODAFSTDusr(src):
    UserFrequency = []
    if src in list(OutHostUserMap.keys()):
        for user in list(OutHostUserMap[src].keys()):
            UserFreq = Average(OutHostUserMap[src][user].values())
            UserFrequency.append(UserFreq)
        return Stddev(UserFrequency)
    else:
        return 0

## Algorithm 23
def Calculate_ODAFSTDdst(src):
    DstFrequency = []
    if src in list(OutHostDstMap.keys()):
        for dst in list(OutHostDstMap[src].keys()):
            DstFreq = Average(OutHostDstMap[src][dst].values())
            DstFrequency.append(DstFreq)
        return Stddev(DstFrequency)
    else:
        return 0

## Algorithm 24
def Calculate_ODAFSTDusr_dst(src):
    UsrDstFrequency = []
    if src in list(OutHostUsrDstMap.keys()):
        for userdst in list(OutHostUsrDstMap[src].keys()):
            UsrDstFreq = Average(OutHostUsrDstMap[src][userdst].values())
            UsrDstFrequency.append(UsrDstFreq)
        return Stddev(UsrDstFrequency)
    else:
        return 0

def features(authlog):
    for i, event in authlog.iterrows():
        authlog.at[i,'ID_usr'] = Calculate_IDusr(event['dst'])
        authlog.at[i,'ID_src'] = Calculate_IDsrc(event['dst'])
        authlog.at[i,'ID_usr_src'] = Calculate_IDusr_src(event['dst'])
        
        authlog.at[i,'OD_usr'] = Calculate_ODusr(event['src'])
        authlog.at[i,'OD_dst'] = Calculate_ODdst(event['src'])
        authlog.at[i,'OD_usr_dst'] = Calculate_ODusr_dst(event['src'])
        
        #authlog.at[i,'IDAF_usr'] = Calculate_IDAFusr(event['dst'])
        #authlog.at[i,'IDAF_src'] = Calculate_IDAFsrc(event['dst'])
        #authlog.at[i,'IDAF_usr_src'] = Calculate_IDAFusr_src(event['dst'])
        
        authlog.at[i,'ODAF_usr'] = Calculate_ODAFusr(event['src'])
        authlog.at[i,'ODAF_dst'] = Calculate_ODAFdst(event['src'])
        authlog.at[i,'ODAF_usr_dst'] = Calculate_ODAFusr_dst(event['src'])
        
        #authlog.at[i,'IDAFSTD_usr'] = Calculate_IDAFSTDusr(event['dst'])
        #authlog.at[i,'IDAFSTD_src'] = Calculate_IDAFSTDsrc(event['dst'])
        #authlog.at[i,'IDAFSTD_usr_src'] = Calculate_IDAFSTDusr_src(event['dst'])
        
        #authlog.at[i,'ODAFSTD_usr'] = Calculate_ODAFSTDusr(event['src'])
        #authlog.at[i,'ODAFSTD_dst'] = Calculate_ODAFSTDdst(event['src'])
        #authlog.at[i,'ODAFSTD_usr_dst'] = Calculate_ODAFSTDusr_dst(event['src'])
        
    return authlog


chunksize = 100000
cont = False
# cont = True
start = 6400000
## user_id, item_id, timestamp, state_label, comma_seperated_list_of_features
if not cont:
    with open("new_feat_authlog.csv", "wb") as file:
        pass
for i, auth in enumerate(pd.read_csv("./auth_ntlm.csv", chunksize=chunksize)):
    if cont and (i * chunksize <= start):
        continue
    authlog = auth[['src', 'dst', 'time', 'user']]
    del auth

    authlog['ID_usr'] = 0.0
    authlog['ID_src'] = 0.0
    authlog['ID_usr_src'] = 0.0

    authlog['OD_usr'] = 0.0
    authlog['OD_dst'] = 0.0
    authlog['OD_usr_dst'] = 0.0

    #authlog['IDAF_usr'] = 0.0
    #authlog['IDAF_src'] = 0.0
    #authlog['IDAF_usr_src'] = 0.0

    authlog['ODAF_usr'] = 0.0
    authlog['ODAF_dst'] = 0.0
    authlog['ODAF_usr_dst'] = 0.0

    #authlog['IDAFSTD_usr'] = 0.0
    #authlog['IDAFSTD_src'] = 0.0
    #authlog['IDAFSTD_usr_src'] = 0.0

    #authlog['ODAFSTD_usr'] = 0.0
    #authlog['ODAFSTD_dst'] = 0.0
    #authlog['ODAFSTD_usr_dst'] = 0.0

    new_feat_authlog = features(authlog)
    del authlog
    new_feat_authlog.to_csv("./new_feat_authlog.csv", mode='a', header=False, index=False)
    with open("new_feat_count.txt", "w") as file:
        file.write(str(i * chunksize))
with open("new_feat_count.txt", "w") as file:
    file.write('done')
