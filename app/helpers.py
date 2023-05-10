import pandas as pd
from collections import Counter

# delivery_date,weight,vehicle_size,billed_miles,total,pickup_state,deliver_state,duration_hours,rpm,predicted_cost,predicted_rpm,error,label
# def get_all_data():
#     df = pd.read_csv('data.csv'):
#     data = []
#     for

def get_filtered_data(startDate, endDate):
    df = pd.read_csv('app/data.csv')
    df['delivery_date'] = pd.to_datetime(df['delivery_date'])
    df.drop(['rpm', 'predicted_cost', 'predicted_rpm', 'error', 'label'], axis=1, inplace=True)
    df = df[(df['delivery_date'] >= startDate) & (df['delivery_date'] <= endDate)]

    pickup_states = get_states(df['pickup_state'])
    deliver_states = get_states(df['deliver_state'])
    vehicles = get_vehicle(df['vehicle_size'])
    distances = get_distance(df['billed_miles'])
    weights = get_weight(df['weight'])
    durations = get_duration(df['duration_hours'])
    costs = get_cost(df['total'])
    all_data = get_scatter_data(df)

    return {'pickup_states': pickup_states, 'deliver_states': deliver_states, 'vehicles': vehicles, 'distances': distances,
            'weights': weights, 'durations': durations, 'costs': costs, 'all_data': all_data}

def get_states(states):
    state_data = Counter(states)
    state_data_sorted_list = sorted(state_data.items(), key=lambda x:x[1], reverse=True)
    other = 0
    data_dict_keep = {}
    for i, key_value in enumerate(state_data_sorted_list):
        key, value = key_value[0], key_value[1]
        if i > 15:
            other += value
        else:
            data_dict_keep[key] = value
    if other:
        data_dict_keep['other'] = other
    state_data = []
    for key, value in data_dict_keep.items():
        state_data.append({'key': key, 'value': value})
    return state_data

def get_vehicle(vehicles):
    vehicle_data_dict = Counter(vehicles)
    vehicle_data = []
    for key, value in vehicle_data_dict.items():
        if key == 'DOCK HIGH STRAIGHT':
            key = 'DOCK HIGH'
        vehicle_data.append({'key': key, 'value': value})
    return vehicle_data

def get_distance(miles):
    distance_data = {'4': 0, '6': 0, '8': 0, '10': 0, '12': 0, '14': 0, '16': 0, '18': 0, '20': 0,
                 '22': 0, '24': 0, '26': 0, '28': 0, '30': 0, '30+': 0}
    for x in miles:
        if x <= 400:
            distance_data['4'] += 1
        elif x <= 600:
            distance_data['6'] += 1
        elif x <= 800:
            distance_data['8'] += 1
        elif x <= 1000:
            distance_data['10'] += 1
        elif x <= 1200:
            distance_data['12'] += 1
        elif x <= 1400:
            distance_data['14'] += 1
        elif x <= 1600:
            distance_data['16'] += 1
        elif x <= 1800:
            distance_data['18'] += 1
        elif x <= 2000:
            distance_data['20'] += 1
        elif x <= 2200:
            distance_data['22'] += 1
        elif x <= 2400:
            distance_data['24'] += 1
        elif x <= 2600:
            distance_data['26'] += 1
        elif x <= 2800:
            distance_data['28'] += 1
        elif x <= 3000:
            distance_data['30'] += 1
        else:
            distance_data['30+'] += 1

    distance_data = [{'key': key, 'value': value} for key, value in distance_data.items()]
    return distance_data

def get_weight(weight):
    weight_data = {'.5': 0, '1': 0, '2': 0, '4': 0, '6': 0, '8': 0, '10': 0, '12': 0, '14': 0, '16': 0,
                   '18':0, '20': 0, '30': 0, '40': 0, '50': 0, '60': 0, '70': 0, '80': 0, '80+': 0}
    for x in weight:
        if x <= 500:
            weight_data['.5'] += 1
        if x <= 1000:
            weight_data['1'] += 1
        elif x <= 2000:
            weight_data['2'] += 1
        elif x <= 4000:
            weight_data['4'] += 1
        elif x <= 6000:
            weight_data['6'] += 1
        elif x <= 8000:
            weight_data['8'] += 1
        elif x <= 10000:
            weight_data['10'] += 1
        elif x <= 12000:
            weight_data['12'] += 1
        elif x <= 14000:
            weight_data['14'] += 1
        elif x <= 16000:
            weight_data['16'] += 1
        elif x <= 18000:
            weight_data['18'] += 1
        elif x <= 20000:
            weight_data['20'] += 1
        elif x <= 30000:
            weight_data['30'] += 1
        elif x <= 40000:
            weight_data['40'] += 1
        elif x <= 50000:
            weight_data['50'] += 1
        elif x <= 60000:
            weight_data['60'] += 1
        elif x <= 70000:
            weight_data['70'] += 1
        elif x <= 80000:
            weight_data['80'] += 1
        else:
            weight_data['80+'] += 1

    weight_data = [{'key': key, 'value': value} for key, value in weight_data.items()]
    return weight_data

def get_duration(duration):
    duration_data = {'10':0, '20': 0, '30': 0, '40':0, '50': 0, '60': 0, '70':0, '80':0, '90':0, '100': 0, '110': 0,
                 '120':0, '130':0, '140':0, '150':0, '150+':0}
    for x in duration:
        if x <= 10:
            duration_data['10'] += 1
        elif x <= 20:
            duration_data['20'] += 1
        elif x <= 30:
            duration_data['30'] += 1
        elif x <= 40:
            duration_data['40'] += 1
        elif x <= 50:
            duration_data['50'] += 1
        elif x <= 60:
            duration_data['60'] += 1
        elif x <= 70:
            duration_data['70'] += 1
        elif x <= 80:
            duration_data['80'] += 1
        elif x <= 90:
            duration_data['90'] += 1
        elif x <= 100:
            duration_data['100'] += 1
        elif x <= 110:
            duration_data['110'] += 1
        elif x <= 120:
            duration_data['120'] += 1
        elif x <= 130:
            duration_data['130'] += 1
        elif x <=140:
            duration_data['140'] += 1
        elif x <=150:
            duration_data['150'] += 1
        else:
            duration_data['150+'] += 1

    duration_data = [{'key': key, 'value': value} for key, value in duration_data.items()]
    return duration_data

def get_cost(cost):
    cost_data = {'.5': 0, '1': 0, '1.5': 0, '2': 0, '2.5': 0, '3': 0, '3.5': 0, '4': 0,
              '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '10+': 0}
    for x in cost:
        if x <= 500:
            cost_data['.5'] += 1
        elif x <= 1000:
            cost_data['1'] += 1
        elif x <= 1500:
            cost_data['1.5'] += 1
        elif x <= 2000:
            cost_data['2'] += 1
        elif x <= 2500:
            cost_data['2.5'] += 1
        elif x <= 3000:
            cost_data['3'] += 1
        elif x <= 3500:
            cost_data['3.5'] += 1
        elif x <= 4000:
            cost_data['4'] += 1
        elif x <= 5000:
            cost_data['5'] += 1
        elif x <= 6000:
            cost_data['6'] += 1
        elif x <= 7000:
            cost_data['7'] += 1
        elif x <= 8000:
            cost_data['8'] += 1
        elif x <= 9000:
            cost_data['9'] += 1
        elif x <= 10000:
            cost_data['10'] += 1
        else:
            cost_data['10+'] += 1

    cost_data = [{'key': key, 'value': value} for key, value in cost_data.items()]
    return cost_data

def get_scatter_data(df):
    data = []
    for i, row in df.iterrows():
        delivery_date = row['delivery_date']
        weight = row['weight']
        vehicle_size = row['vehicle_size']
        billed_miles = row['billed_miles']
        total = row['total']
        pickup_state = row['pickup_state']
        deliver_state = row['deliver_state']
        duration_hours = row['duration_hours']
        data.append({'delivery_date': delivery_date, 'weight': weight, 'vehicle_size': vehicle_size, 'billed_miles': billed_miles,
                     'total': total, 'pickup_state': pickup_state, 'deliver_state': deliver_state, 'duration_hours': duration_hours})
    return data
