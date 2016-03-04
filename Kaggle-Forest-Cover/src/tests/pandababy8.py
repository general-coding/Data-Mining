'''
Created on Mar 11, 2015

@author: puneeth
'''

import pandas, csv, time, math
import statistics

start = time.time()
print(str(start))

ifname = './csvfiles/train.csv'
ofname = './csvfiles/train_data.csv'

print('Read train.csv')
df_train = pandas.read_csv(ifname)
 
print('Consolidate 40 Soil Types. Use only one Soil Type')
df_train['Soil'] = 0
for i in range(1, 41):
    df_train['Soil'] = df_train['Soil'] + i * df_train['Soil_Type' + str(i)]
      
print('Consolidate 4 Wilderness Areas. Use only one Wilderness Area')
df_train['Wilderness_Area'] = 0
for i in range(1, 5):
    df_train['Wilderness_Area'] = df_train['Wilderness_Area'] + i * df_train['Wilderness_Area' + str(i)]
 
print('Remove 40 Soil Types and 4 Wilderness Areas')
for i in range(1, 41):
    df_train.pop('Soil_Type' + str(i))
    if i < 5:
        df_train.pop('Wilderness_Area' + str(i))
 
# print('Put above data into train_data.csv')
# df_train.to_csv(ofname, index=False)

print('Calculate mean and variance of each feature')
elevation_mv_list = [[0], [], [], [], [], [], [], []]
aspect_mv_list = [[0], [], [], [], [], [], [], []]
slope_mv_list = [[0], [], [], [], [], [], [], []]
h_hydro_mv_list = [[0], [], [], [], [], [], [], []]
v_hydro_mv_list = [[0], [], [], [], [], [], [], []]
h_roadways_mv_list = [[0], [], [], [], [], [], [], []]
hillshade9am_mv_list = [[0], [], [], [], [], [], [], []]
hillshadenoon_mv_list = [[0], [], [], [], [], [], [], []]
hillshade3pm_mv_list = [[0], [], [], [], [], [], [], []]
h_fire_mv_list = [[0], [], [], [], [], [], [], []]
soil_mv_list = [[0], [], [], [], [], [], [], []]
wilderness_mv_list = [[0], [], [], [], [], [], [], []]

elevation_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
aspect_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
slope_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
h_hydro_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
v_hydro_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
h_roadways_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
hillshade9am_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
hillshadenoon_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
hillshade3pm_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
h_fire_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
soil_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
wilderness_mv_dict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}

for index, row in df_train.iterrows():
    for i in range(1, 8):
        if row.Cover_Type == i:
            elevation_mv_list[i].append(row.Elevation)
            aspect_mv_list[i].append(row.Aspect)
            slope_mv_list[i].append(row.Slope)
            h_hydro_mv_list[i].append(row.Horizontal_Distance_To_Hydrology)
            v_hydro_mv_list[i].append(row.Vertical_Distance_To_Hydrology)
            h_roadways_mv_list[i].append(row.Horizontal_Distance_To_Roadways)
            hillshade9am_mv_list[i].append(row.Hillshade_9am)
            hillshadenoon_mv_list[i].append(row.Hillshade_Noon)
            hillshade3pm_mv_list[i].append(row.Hillshade_3pm)
            h_fire_mv_list[i].append(row.Horizontal_Distance_To_Fire_Points)
            soil_mv_list[i].append(row.Soil)
            wilderness_mv_list[i].append(row.Wilderness_Area)
        
    
for i in range (1, 8):
    elevation_mv_dict[i]['mean'] = statistics.mean(elevation_mv_list[i])
    aspect_mv_dict[i]['mean'] = statistics.mean(aspect_mv_list[i])
    slope_mv_dict[i]['mean'] = statistics.mean(slope_mv_list[i])
    h_hydro_mv_dict[i]['mean'] = statistics.mean(h_hydro_mv_list[i])
    v_hydro_mv_dict[i]['mean'] = statistics.mean(v_hydro_mv_list[i])
    h_roadways_mv_dict[i]['mean'] = statistics.mean(h_roadways_mv_list[i])
    hillshade9am_mv_dict[i]['mean'] = statistics.mean(hillshade9am_mv_list[i])
    hillshadenoon_mv_dict[i]['mean'] = statistics.mean(hillshadenoon_mv_list[i])
    hillshade3pm_mv_dict[i]['mean'] = statistics.mean(hillshade3pm_mv_list[i])
    h_fire_mv_dict[i]['mean'] = statistics.mean(h_fire_mv_list[i])
    soil_mv_dict[i]['mean'] = statistics.mean(soil_mv_list[i])
    wilderness_mv_dict[i]['mean'] = statistics.mean(wilderness_mv_list[i])
    
    elevation_mv_dict[i]['variance'] = statistics.variance(elevation_mv_list[i])
    aspect_mv_dict[i]['variance'] = statistics.variance(aspect_mv_list[i])
    slope_mv_dict[i]['variance'] = statistics.variance(slope_mv_list[i])
    h_hydro_mv_dict[i]['variance'] = statistics.variance(h_hydro_mv_list[i])
    v_hydro_mv_dict[i]['variance'] = statistics.variance(v_hydro_mv_list[i])
    h_roadways_mv_dict[i]['variance'] = statistics.variance(h_roadways_mv_list[i])
    hillshade9am_mv_dict[i]['variance'] = statistics.variance(hillshade9am_mv_list[i])
    hillshadenoon_mv_dict[i]['variance'] = statistics.variance(hillshadenoon_mv_list[i])
    hillshade3pm_mv_dict[i]['variance'] = statistics.variance(hillshade3pm_mv_list[i])
    h_fire_mv_dict[i]['variance'] = statistics.variance(h_fire_mv_list[i])
    soil_mv_dict[i]['variance'] = statistics.variance(soil_mv_list[i])
    wilderness_mv_dict[i]['variance'] = statistics.variance(wilderness_mv_list[i])

# for i in range(1, 8):
#     print(i, wilderness_mv_dict[i])
#
# # exit()
         
tifname = './csvfiles/test.csv'
tofname = './csvfiles/test_data.csv'

print('Read test.csv')
df_test = pandas.read_csv(tifname)
 
print('Consolidate 40 Soil Types. Use only one Soil Type')
df_test['Soil'] = 0
for i in range(1, 41):
    df_test['Soil'] = df_test['Soil'] + i * df_test['Soil_Type' + str(i)]
      
print('Consolidate 4 Wilderness Areas. Use only one Wilderness Area')
df_test['Wilderness_Area'] = 0
for i in range(1, 5):
    df_test['Wilderness_Area'] = df_test['Wilderness_Area'] + i * df_test['Wilderness_Area' + str(i)]
 
print('Remove 40 Soil Types and 4 Wilderness Areas')
for i in range(1, 41):
    df_test.pop('Soil_Type' + str(i))
    if i < 5:
        df_test.pop('Wilderness_Area' + str(i))
 
# print('Put above data into test_data.csv')
# df_test.to_csv(tofname, index=False)

# exit()

result_dict = {}
count = 0
# exit()

print('Length of test.csv', len(df_test.index))

print('Start Classifying Test')
loopstart = time.time()
# for count in range(0, len(df_test.index)):
for index, row in df_test.iterrows():
    class_count = [[]]
                
    for cover_type in range(1, 8):
        try:
            numerator = math.exp(math.pow((row.Elevation - elevation_mv_dict[cover_type]['mean']), 2) / (2 * elevation_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * elevation_mv_dict[cover_type]['variance'])            
            elevation_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Aspect - aspect_mv_dict[cover_type]['mean']), 2) / (2 * aspect_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * aspect_mv_dict[cover_type]['variance'])          
            aspect_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Slope - slope_mv_dict[cover_type]['mean']), 2) / (2 * slope_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * slope_mv_dict[cover_type]['variance'])            
            slope_prob = (1 / denominator) * numerator 
            
            numerator = math.exp(math.pow((row.Horizontal_Distance_To_Hydrology - h_hydro_mv_dict[cover_type]['mean']), 2) / (2 * h_hydro_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * h_hydro_mv_dict[cover_type]['variance'])           
            h_hydro_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Vertical_Distance_To_Hydrology - v_hydro_mv_dict[cover_type]['mean']), 2) / (2 * v_hydro_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * v_hydro_mv_dict[cover_type]['variance'])
            v_hydro_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Horizontal_Distance_To_Roadways - h_roadways_mv_dict[cover_type]['mean']), 2) / (2 * h_roadways_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * h_roadways_mv_dict[cover_type]['variance'])            
            h_roadways_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Hillshade_9am - hillshade9am_mv_dict[cover_type]['mean']), 2) / (2 * hillshade9am_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * hillshade9am_mv_dict[cover_type]['variance'])         
            hillshade9am_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Hillshade_Noon - hillshadenoon_mv_dict[cover_type]['mean']), 2) / (2 * hillshadenoon_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * hillshadenoon_mv_dict[cover_type]['variance'])
            hillshadenoon_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Hillshade_3pm - hillshade3pm_mv_dict[cover_type]['mean']), 2) / (2 * hillshade3pm_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * hillshade3pm_mv_dict[cover_type]['variance'])
            hillshade3pm_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Horizontal_Distance_To_Fire_Points - h_fire_mv_dict[cover_type]['mean']), 2) / (2 * h_fire_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * h_fire_mv_dict[cover_type]['variance'])
            h_fire_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Soil - soil_mv_dict[cover_type]['mean']), 2) / (2 * soil_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * soil_mv_dict[cover_type]['variance'])
            soil_prob = (1 / denominator) * numerator
            
            numerator = math.exp(math.pow((row.Wilderness_Area - wilderness_mv_dict[cover_type]['mean']), 2) / (2 * wilderness_mv_dict[cover_type]['variance']))
            denominator = math.sqrt(2 * math.pi * wilderness_mv_dict[cover_type]['variance'])
#             print(row.Id, cover_type)
            try:
                wilderness_prob = (1 / denominator) * numerator
            except ZeroDivisionError:
                wilderness_prob = (0 + 1) / (2160 + 7)
                        
            class_cover = float(elevation_prob) * float(aspect_prob) * float(slope_prob) * float(h_hydro_prob) * float(v_hydro_prob) * float(h_roadways_prob) * float(hillshade9am_prob) * float(hillshadenoon_prob) * float(hillshade3pm_prob) * float(h_fire_prob) * float(soil_prob) * float(wilderness_prob)
#             print(type(class_cover), class_cover)
            
            class_count.append([math.fabs(class_cover), cover_type])
    
        except KeyError:
            print()

    count = count + 1        
    if count % 20000 == 0:
        loopend = time.time()
        print(count, str((loopend - loopstart) / 60))
        
    class_count.sort(reverse=True)
    result_dict[row.Id] = class_count[0][1]
            
f = open("./csvfiles/pandababy7.csv", "w")
writer = csv.writer(f)
writer.writerow(['Id', 'Cover_Type'])
for key, value in result_dict.items():
    writer.writerow([key, value])

f.close()

end = time.time()
print(str(end))

runtime = float(end - start) / 60

print('Runtime:', str(runtime))
