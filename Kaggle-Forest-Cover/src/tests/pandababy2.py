'''
Created on Mar 9, 2015

@author: puneeth
'''

import pandas, csv, time
from collections import Counter

start = time.time()

ifname = 'train.csv'
# ofname = 'train_data.csv'
         
tifname = 'test.csv'
# tofname = 'test_data.csv'

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

cover = Counter(df_train.Cover_Type)
print('Count of each cover type:')
print(cover)

prob_cover = Counter(df_train.Cover_Type)
for cover_type in prob_cover:
    prob_cover[cover_type] = prob_cover[cover_type] / len(df_train.index)
print('Probability of each cover type:')
print(prob_cover)

print('Count each Feature')
elevation = (df_train[['Elevation', 'Cover_Type']].groupby(['Elevation', 'Cover_Type'],
                                                    as_index=False, sort=False)['Cover_Type'].count() + 1) / (2160 + 7)
                                                    
aspect = (df_train[['Aspect', 'Cover_Type']].groupby(['Aspect', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)

slope = (df_train[['Slope', 'Cover_Type']].groupby(['Slope', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)

h_hydro = (df_train[['Horizontal_Distance_To_Hydrology', 'Cover_Type']].groupby(['Horizontal_Distance_To_Hydrology', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)

v_hydro = (df_train[['Vertical_Distance_To_Hydrology', 'Cover_Type']].groupby(['Vertical_Distance_To_Hydrology', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)

h_roadways = (df_train[['Horizontal_Distance_To_Roadways', 'Cover_Type']].groupby(['Horizontal_Distance_To_Roadways', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)

hillshade9am = (df_train[['Hillshade_9am', 'Cover_Type']].groupby(['Hillshade_9am', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)

hillshadenoon = (df_train[['Hillshade_Noon', 'Cover_Type']].groupby(['Hillshade_Noon', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)

hillshade3pm = (df_train[['Hillshade_3pm', 'Cover_Type']].groupby(['Hillshade_3pm', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)

h_fire = (df_train[['Horizontal_Distance_To_Fire_Points', 'Cover_Type']].groupby(['Horizontal_Distance_To_Fire_Points', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)

soil = (df_train[['Soil', 'Cover_Type']].groupby(['Soil', 'Cover_Type'],
                                                    as_index=False, sort=True)['Soil'].count() + 1) / (2160 + 7)

wilderness = (df_train[['Wilderness_Area', 'Cover_Type']].groupby(['Wilderness_Area', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (2160 + 7)
       
result_dict = {}

print('Length of test.csv', len(df_test.index))

print('Start Classifying Test')
count = 0
for index, row in df_test.iterrows():
    class_count = [[]]
            
    for i in range(1, 8):
        try:
            try:
                elevation_prob = elevation[row.Elevation][i]
            except KeyError:
                elevation_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                elevation_prob = (0 + 1) / (2160 + 7)
            
            try:
                aspect_prob = aspect[row.Aspect][i]
            except KeyError:
                aspect_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                aspect_prob = (0 + 1) / (2160 + 7)
            
            try:
                slope_prob = slope[row.Slope][i]
            except KeyError:
                slope_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                slope_prob = (0 + 1) / (2160 + 7)
            
            try:    
                h_hydro_prob = h_hydro[row.Horizontal_Distance_To_Hydrology][i]
            except KeyError:
                h_hydro_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                h_hydro_prob = (0 + 1) / (2160 + 7)
            
            try: 
                v_hydro_prob = v_hydro[row.Vertical_Distance_To_Hydrology][i]
            except KeyError:
                v_hydro_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                v_hydro_prob = (0 + 1) / (2160 + 7)
            
            try:
                h_roadways_prob = h_roadways[row.Horizontal_Distance_To_Roadways][i]
            except KeyError:
                h_roadways_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                h_roadways_prob = (0 + 1) / (2160 + 7)
            
            try:
                hillshade9am_prob = hillshade9am[row.Hillshade_9am][i]
            except KeyError:
                hillshade9am_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                hillshade9am_prob = (0 + 1) / (2160 + 7)
            
            try:
                hillshadenoon_prob = hillshadenoon[row.Hillshade_Noon][i]
            except KeyError:
                hillshadenoon_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                hillshadenoon_prob = (0 + 1) / (2160 + 7)
            
            try:
                hillshade3pm_prob = hillshade3pm[row.Hillshade_3pm][i]
            except KeyError:
                hillshade3pm_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                hillshade3pm_prob = (0 + 1) / (2160 + 7)
            
            try:
                h_fire_prob = h_fire[row.Horizontal_Distance_To_Fire_Points][i]
            except KeyError:
                h_fire_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                h_fire_prob = (0 + 1) / (2160 + 7)
            
            try:
                soil_prob = soil[row.Soil][i]
            except KeyError:
                soil_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                soil_prob = (0 + 1) / (2160 + 7)
            
            try:
                wilderness_prob = wilderness[row.Wilderness_Area][i]
            except KeyError:
                wilderness_prob = (0 + 1) / (2160 + 7)
            except IndexError:
                wilderness_prob = (0 + 1) / (2160 + 7)
            
            class_cover = (elevation_prob * aspect_prob * slope_prob * 
                            h_hydro_prob * v_hydro_prob * 
                            h_roadways_prob * 
                            hillshade9am_prob * hillshadenoon_prob * hillshade3pm_prob * 
                            h_fire_prob * soil_prob * wilderness_prob)
            
            class_count.append([class_cover, i])
        except KeyError:
            pass
    
    class_count.sort(reverse=True)
    result_dict[row.Id] = class_count[0][1]
    
    count = count + 1
    if count % 20000 == 0:
        print(count)
            
f = open("pandababy2.csv", "w")
writer = csv.writer(f)
writer.writerow(['Id', 'Cover_Type'])
for key, value in result_dict.items():
    writer.writerow([key, value])

f.close()

end = time.time()

runtime = end - time

print('Runtime:', str(runtime))