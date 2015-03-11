'''
Created on Mar 10, 2015

@author: puneeth
'''

import pandas, csv, time, math
from collections import Counter

start = time.time()
print(str(start))

ifname = 'train.csv'
ofname = 'train_data.csv'

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
         
tifname = 'test.csv'
tofname = 'test_data.csv'

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

cover_grouped = Counter(df_train.Cover_Type)
print('Count of each cover type:', cover_grouped, len(cover_grouped))

c = len(cover_grouped)

prob_cover_grouped = Counter(df_train.Cover_Type)
for cover_type in prob_cover_grouped:
    prob_cover_grouped[cover_type] = prob_cover_grouped[cover_type] / len(df_train.index)
print('Probability of each cover type:', prob_cover_grouped)

# exit()

print('Count each Feature')
elevation_grouped = df_train[['Elevation', 'Cover_Type']].groupby(['Elevation', 'Cover_Type'],
                                                    as_index=False, sort=False)['Cover_Type'].count()
                                                     
aspect_grouped = df_train[['Aspect', 'Cover_Type']].groupby(['Aspect', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()
 
slope_grouped = df_train[['Slope', 'Cover_Type']].groupby(['Slope', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()
 
h_hydro_grouped = df_train[['Horizontal_Distance_To_Hydrology', 'Cover_Type']].groupby(['Horizontal_Distance_To_Hydrology', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()
 
v_hydro_grouped = df_train[['Vertical_Distance_To_Hydrology', 'Cover_Type']].groupby(['Vertical_Distance_To_Hydrology', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()
 
h_roadways_grouped = df_train[['Horizontal_Distance_To_Roadways', 'Cover_Type']].groupby(['Horizontal_Distance_To_Roadways', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()
 
hillshade9am_grouped = df_train[['Hillshade_9am', 'Cover_Type']].groupby(['Hillshade_9am', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()
 
hillshadenoon_grouped = df_train[['Hillshade_Noon', 'Cover_Type']].groupby(['Hillshade_Noon', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()
 
hillshade3pm_grouped = df_train[['Hillshade_3pm', 'Cover_Type']].groupby(['Hillshade_3pm', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()
 
h_fire_grouped = df_train[['Horizontal_Distance_To_Fire_Points', 'Cover_Type']].groupby(['Horizontal_Distance_To_Fire_Points', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()
 
soil_grouped = df_train[['Soil', 'Cover_Type']].groupby(['Soil', 'Cover_Type'],
                                                    as_index=False, sort=True)['Soil'].count()
 
wilderness_grouped = df_train[['Wilderness_Area', 'Cover_Type']].groupby(['Wilderness_Area', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count()

elevation_prob_dict = elevation_grouped.to_dict()
aspect_prob_dict = aspect_grouped.to_dict()
slope_prob_dict = slope_grouped.to_dict()
h_hydro_prob_dict = h_hydro_grouped.to_dict()
v_hydro_prob_dict = v_hydro_grouped.to_dict()
h_roadways_prob_dict = h_roadways_grouped.to_dict()
hillshade9am_prob_dict = hillshade9am_grouped.to_dict()
hillshadenoon_prob_dict = hillshadenoon_grouped.to_dict()
hillshade3pm_prob_dict = hillshade3pm_grouped.to_dict()
h_fire_prob_dict = h_fire_grouped.to_dict()
soil_prob_dict = soil_grouped.to_dict()
wilderness_prob_dict = wilderness_grouped.to_dict()

result_dict = {}

test_dict = df_test.to_dict()
# exit()

print('Length of test.csv', len(df_test.index))

print('Start Classifying Test')
loopstart = time.time()
for count in range(0, len(df_test.index)):
    class_count = [[]]
                
    for cover_type in range(0, 7):
        try:
            elevation_key = test_dict['Elevation'][count], cover_type
            aspect_key = test_dict['Aspect'][count], cover_type
            slope_key = test_dict['Slope'][count], cover_type
            horizontal_distance_to_hydrology_key = test_dict['Horizontal_Distance_To_Hydrology'][count], cover_type
            vertical_distance_to_hydrology_key = test_dict['Vertical_Distance_To_Hydrology'][count], cover_type
            horizontal_distance_to_roadways_key = test_dict['Horizontal_Distance_To_Roadways'][count], cover_type
            hillshade_9am_key = test_dict['Hillshade_9am'][count], cover_type
            hillshade_noon_key = test_dict['Hillshade_Noon'][count], cover_type
            hillshade_3pm_key = test_dict['Hillshade_3pm'][count], cover_type
            horizontal_distance_to_fire_points_key = test_dict['Horizontal_Distance_To_Fire_Points'][count], cover_type
            soil_key = test_dict['Soil'][count], cover_type
            wilderness_area_key = test_dict['Wilderness_Area'][count], cover_type
            
            try:
                elevation_prob = elevation_prob_dict[elevation_key]
            except KeyError:
                elevation_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                aspect_prob = aspect_prob_dict[aspect_key]
            except KeyError:
                aspect_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                slope_prob = slope_prob_dict[slope_key]
            except KeyError:
                slope_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                h_hydro_prob = h_hydro_prob_dict[horizontal_distance_to_hydrology_key]
            except KeyError:
                h_hydro_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                v_hydro_prob = v_hydro_prob_dict[vertical_distance_to_hydrology_key]
            except KeyError:
                v_hydro_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                h_roadways_prob = h_roadways_prob_dict[horizontal_distance_to_roadways_key]
            except KeyError:
                h_roadways_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                hillshade9am_prob = hillshade9am_prob_dict[hillshade_9am_key]
            except KeyError:
                hillshade9am_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                hillshadenoon_prob = hillshadenoon_prob_dict[hillshade_noon_key]
            except KeyError:
                hillshadenoon_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                hillshade3pm_prob = hillshade3pm_prob_dict[hillshade_3pm_key]
            except KeyError:
                hillshade3pm_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                h_fire_prob = h_fire_prob_dict[horizontal_distance_to_fire_points_key]
            except KeyError:
                h_fire_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                soil_prob = soil_prob_dict[soil_key]
            except KeyError:
                soil_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
            
            try:
                wilderness_prob = wilderness_prob_dict[wilderness_area_key]
            except KeyError:
                wilderness_prob = (0 + 1) / (cover_grouped[cover_type + 1] + c)
                        
            class_cover = float(elevation_prob) * float(aspect_prob) * float(slope_prob) * float(h_hydro_prob) * float(v_hydro_prob) * float(h_roadways_prob) * float(hillshade9am_prob) * float(hillshadenoon_prob) * float(hillshade3pm_prob) * float(h_fire_prob) * float(soil_prob) * float(wilderness_prob) * float(prob_cover_grouped[cover_type + 1])
#             print(type(class_cover), class_cover)
            
            class_count.append([math.fabs(class_cover), cover_type])
    
        except KeyError:
            print()
        
    if count % 20000 == 0:
        loopend = time.time()
        print(count, str((loopend - loopstart) / 60))
        
    class_count.sort(reverse=True)
    result_dict[df_test.Id[count]] = class_count[0][1]
            
f = open("pandababy6.csv", "w")
writer = csv.writer(f)
writer.writerow(['Id', 'Cover_Type'])
for key, value in result_dict.items():
    writer.writerow([key, value])

f.close()

end = time.time()
print(str(end))

runtime = float(end - start) / 60

print('Runtime:', str(runtime))