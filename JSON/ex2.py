import json
import re
import countries 


countries_list = countries.export_countries()
count = dict()

for js in countries_list:
        for k,v in js.items():
                if k == 'languages':
                        for i in v:
                                count[i] = count.get(i,0) + 1


arranged_dic = dict(sorted(count.items(), key=lambda item:item[1], reverse=True))

counting = 1
most_spoken = []
for k,v in arranged_dic.items():
        if counting <= 10:
                most_spoken.append((k,v))
                counting += 1
        else:
                break


print(most_spoken)
