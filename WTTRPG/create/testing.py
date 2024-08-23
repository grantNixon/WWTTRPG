def leveling_table(stat,table):
        i = 0
        keys = list(table.keys())
        while i < len(keys):
            if stat == keys[i]:
                return table.get(keys[i])
            if stat > keys[i]:
                if stat < keys[i + 1]:
                    return table.get(keys[i])
                else:
                    i = i + 1
                



gump_health = {5:15,10:20,20:25,30:35,40:40,50:55,60:65,70:75,80:90,90:115,100:130}
str_move = {5:15,15:20,30:25,45:30,60:35,75:40,90:45,100:50}
agi_ec = {5:11,10:12,20:13,30:14,40:15,50:16,60:17,70:18,80:19,90:20,100:23}
level_ap = {1:4,3:6,8:7,15:8,20:9}
    
print(leveling_table(100,gump_health))