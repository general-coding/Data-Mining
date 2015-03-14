'''
Created on Feb 22, 2015

@author: puneeth
'''

import pandas, csv, time
from collections import Counter

start  = time.time()

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
print('Count of each cover type:')
print(cover_grouped)

prob_cover_grouped = Counter(df_train.Cover_Type)
for cover_type in prob_cover_grouped:
    prob_cover_grouped[cover_type] = prob_cover_grouped[cover_type] / len(df_train.index)
print('Probability of each cover type:')
print(prob_cover_grouped)

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

# print(elevation_grouped)
# print(elevation_grouped[2684])
# print(h_roadways_grouped[2684])
# exit()

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

for key in elevation_prob_dict:
    elevation_prob_dict[key] = (elevation_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in aspect_prob_dict:
    aspect_prob_dict[key] = (aspect_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in slope_prob_dict:
    slope_prob_dict[key] = (slope_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in h_hydro_prob_dict: 
    h_hydro_prob_dict[key] = (h_hydro_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in v_hydro_prob_dict:
    v_hydro_prob_dict[key] = (v_hydro_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in h_roadways_prob_dict: 
    h_roadways_prob_dict[key] = (h_roadways_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in hillshade9am_prob_dict: 
    hillshade9am_prob_dict[key] = (hillshade9am_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in hillshadenoon_prob_dict:
    hillshadenoon_prob_dict[key] = (hillshadenoon_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in hillshade3pm_prob_dict:
    hillshade3pm_prob_dict[key] = (hillshade3pm_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in h_fire_prob_dict:
    h_fire_prob_dict[key] = (h_fire_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in soil_prob_dict:
    soil_prob_dict[key] = (soil_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

for key in wilderness_prob_dict: 
    wilderness_prob_dict[key] = (wilderness_prob_dict[key] + 1) / (cover_grouped[key[1]] + 7)

result_dict = {}

print('Length of test.csv', len(df_test.index))

print('Start Classifying Test')
for count in range(0, len(df_test.index)):
    class_count = [[]]
    
    if count % 20000 == 0:
        print(count)
                
    for cover_type in range(1, 8):
#         print(count, cover_type)
        try:
            elevation_key = df_test.Elevation[count], cover_type
            aspect_key = df_test.Aspect[count], cover_type
            slope_key = df_test.Slope[count], cover_type
            horizontal_distance_to_hydrology_key = df_test.Horizontal_Distance_To_Hydrology[count], cover_type
            vertical_distance_to_hydrology_key = df_test.Vertical_Distance_To_Hydrology[count], cover_type
            horizontal_distance_to_roadways_key = df_test.Horizontal_Distance_To_Roadways[count], cover_type
            hillshade_9am_key = df_test.Hillshade_9am[count], cover_type
            hillshade_noon_key = df_test.Hillshade_Noon[count], cover_type
            hillshade_3pm_key = df_test.Hillshade_3pm[count], cover_type
            horizontal_distance_to_fire_points_key = df_test.Horizontal_Distance_To_Fire_Points[count], cover_type
            soil_key = df_test.Soil[count], cover_type
            wilderness_area_key = df_test.Wilderness_Area[count], cover_type
            
            try:
                elevation_prob = elevation_prob_dict[elevation_key]
            except:
                elevation_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                aspect_prob = aspect_prob_dict[aspect_key]
            except:
                aspect_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                slope_prob = slope_prob_dict[slope_key]
            except:
                slope_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                h_hydro_prob = h_hydro_prob_dict[horizontal_distance_to_hydrology_key]
            except:
                h_hydro_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                v_hydro_prob = v_hydro_prob_dict[vertical_distance_to_hydrology_key]
            except:
                v_hydro_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                h_roadways_prob = h_roadways_prob_dict[horizontal_distance_to_roadways_key]
            except:
                h_roadways_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                hillshade9am_prob = hillshade9am_prob_dict[hillshade_9am_key]
            except:
                hillshade9am_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                hillshadenoon_prob = hillshadenoon_prob_dict[hillshade_noon_key]
            except:
                hillshadenoon_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                hillshade3pm_prob = hillshade3pm_prob_dict[hillshade_3pm_key]
            except:
                hillshade3pm_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                h_fire_prob = h_fire_prob_dict[horizontal_distance_to_fire_points_key]
            except:
                h_fire_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                soil_prob = soil_prob_dict[soil_key]
            except:
                soil_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            try:
                wilderness_prob = wilderness_prob_dict[wilderness_area_key]
            except:
                wilderness_prob = (0 + 1) / (cover_grouped[cover_type] + 7)
            
            class_cover = (elevation_prob * aspect_prob * slope_prob * 
                           h_hydro_prob * v_hydro_prob * h_roadways_prob * 
                           hillshade9am_prob * hillshadenoon_prob * hillshade3pm_prob * 
                           h_fire_prob * soil_prob * wilderness_prob * prob_cover_grouped[cover_type])
             
            class_count.append([class_cover, cover_type])

        except:
            print()

    class_count.sort(reverse=True)
    result_dict[df_test.Id[count]] = class_count[0][1]
#     print(result_dict)
        
f = open("forest_cover.csv", "w")
writer = csv.writer(f)
writer.writerow(['Id', 'Cover_Type'])
for key, value in result_dict.items():
    writer.writerow([key, value])
    
end = time.time()
runtime = end - start

print(str(runtime))