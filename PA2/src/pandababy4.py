'''
Created on Mar 10, 2015

@author: puneeth
'''

import pandas, csv, time
from collections import Counter
from astropy.table.row import Row

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
elevation_grouped = (df_train[['Elevation', 'Cover_Type']].groupby(['Elevation', 'Cover_Type'],
                                                    as_index=False, sort=False)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)
                                                    
aspect_grouped = (df_train[['Aspect', 'Cover_Type']].groupby(['Aspect', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

slope_grouped = (df_train[['Slope', 'Cover_Type']].groupby(['Slope', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

h_hydro_grouped = (df_train[['Horizontal_Distance_To_Hydrology', 'Cover_Type']].groupby(['Horizontal_Distance_To_Hydrology', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

v_hydro_grouped = (df_train[['Vertical_Distance_To_Hydrology', 'Cover_Type']].groupby(['Vertical_Distance_To_Hydrology', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

h_roadways_grouped = (df_train[['Horizontal_Distance_To_Roadways', 'Cover_Type']].groupby(['Horizontal_Distance_To_Roadways', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

hillshade9am_grouped = (df_train[['Hillshade_9am', 'Cover_Type']].groupby(['Hillshade_9am', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

hillshadenoon_grouped = (df_train[['Hillshade_Noon', 'Cover_Type']].groupby(['Hillshade_Noon', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

hillshade3pm_grouped = (df_train[['Hillshade_3pm', 'Cover_Type']].groupby(['Hillshade_3pm', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

h_fire_grouped = (df_train[['Horizontal_Distance_To_Fire_Points', 'Cover_Type']].groupby(['Horizontal_Distance_To_Fire_Points', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

soil_grouped = (df_train[['Soil', 'Cover_Type']].groupby(['Soil', 'Cover_Type'],
                                                    as_index=False, sort=True)['Soil'].count() + 1) / (cover_grouped[1] + c)

wilderness_grouped = (df_train[['Wilderness_Area', 'Cover_Type']].groupby(['Wilderness_Area', 'Cover_Type'],
                                                    as_index=False, sort=True)['Cover_Type'].count() + 1) / (cover_grouped[1] + c)

# print(h_fire_grouped[2684])
result_dict = {}
count = 0

print('Start Classifying Test')
loopstart = time.time()
for index, row in df_test.iterrows():
    class_count = [[]]
        
    for cover_type in range(1, 8):
#         print(row.Horizontal_Distance_To_Roadways, cover_type)
        try:
            try:
                elevation_prob = elevation_grouped[row.Elevation][cover_type]
#                 print(elevation_prob)
            except:
                elevation_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                aspect_prob = aspect_grouped[row.Aspect][cover_type]
            except:
                aspect_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                slope_prob = slope_grouped[row.Slope][cover_type]
            except:
                slope_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                h_hydro_prob = h_hydro_grouped[row.Horizontal_Distance_To_Hydrology][cover_type]
            except:
                h_hydro_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                v_hydro_prob = v_hydro_grouped[row.Vertical_Distance_To_Hydrology][cover_type]
            except:
                v_hydro_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                h_roadways_prob = h_roadways_grouped[row.Horizontal_Distance_To_Roadways][cover_type]
            except:
                h_roadways_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                hillshade9am_prob = hillshade9am_grouped[row.Hillshade_9am][cover_type]
            except:
                hillshade9am_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                hillshadenoon_prob = hillshadenoon_grouped[row.Hillshade_Noon][cover_type]
            except:
                hillshadenoon_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                hillshade3pm_prob = hillshade3pm_grouped[row.Hillshade_3pm][cover_type]
            except:
                hillshade3pm_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                h_fire_prob = h_fire_grouped[row.Horizontal_Distance_To_Fire_Points][cover_type]
            except:
                h_fire_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                soil_prob = soil_grouped[row.Soil][cover_type]
            except:
                soil_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            try:
                wilderness_prob = wilderness_grouped[row.Wilderness_Area][cover_type]
            except:
                wilderness_prob = (0 + 1) / (cover_grouped[cover_type] + c)
            
            class_cover = (elevation_prob * aspect_prob * 
                           slope_prob * 
                           h_hydro_prob, v_hydro_prob * 
                           h_roadways_prob * 
                           hillshade9am_prob * hillshadenoon_prob * hillshade3pm_prob * 
                           h_fire_prob * soil_prob * wilderness_prob * prob_cover_grouped[cover_type]) 
            
            class_count.append([class_cover, cover_type])
        
        except:
            print()
        
    if count % 20000 == 0:
        loopend = time.time()
        print('loopend', count, str((loopend - loopstart) / 60))
    
    count = count + 1
    
    class_count.sort(reverse=True)
    result_dict[df_test.Id[count]] = class_count[0][1]
#     break
            
f = open("pandababy4.csv", "w")
writer = csv.writer(f)
writer.writerow(['Id', 'Cover_Type'])
for key, value in result_dict.items():
    writer.writerow([key, value])

f.close()

end = time.time()
print(str(end))

runtime = float(end - start) / 60

print('Runtime:', str(runtime))