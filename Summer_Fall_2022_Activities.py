import pandas as pd
import math
import matplotlib.pyplot as plt

# Function to convert "m:ss" format to seconds as a float
def time_str_to_seconds(time_str):
    try:
        if ':' in time_str:
            minutes, seconds = time_str.split(':')
            total_seconds = int(minutes) * 60 + float(seconds)
            return total_seconds
        else:
            return 0  # Handle cases where time format is not valid
    except ValueError:
        return 0  # Handle invalid time format gracefully
    
def seconds_to_time_str(total_seconds):
    if math.isnan(total_seconds):
        return None
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds % 1) * 10)
    return f"{minutes}:{seconds:02d}.{milliseconds:01d}"

try:
    run_22 = pd.read_csv('Summer_Fall_2022_Activities.csv')
except FileNotFoundError:
    print("The file does not exist.")
except pd.errors.EmptyDataError:
    print("The file is empty.")
except pd.errors.ParserError as e:
    print(f"An error occurred while parsing the CSV: {e}")
else:
    print("CSV file read successfully.")
    
print()


#======================================================================================

run_22['Date'] = run_22['Date'].str.split(' ').str[0]

# convert the date column to datetime format
run_22['Date'] = pd.to_datetime(run_22['Date'])

# change the datetime format
run_22['Date_Formatted'] = run_22['Date'].dt.strftime('%Y/%m/%d')

#======================================================================================
#           May Mileage
#======================================================================================

def add_date(may_start_day):
    may_start_day = pd.to_datetime('2022-05-01')
    
    while may_start_day not in run_22['Date'].values:
        may_start_day += pd.Timedelta(days=1)
    
    return may_start_day

def remove_date(may_end_day):
    may_end_day = pd.to_datetime('2022-05-31')
    
    while may_end_day not in run_22['Date'].values:
        may_end_day -= pd.Timedelta(days=1)
    
    return may_end_day

start_date = pd.to_datetime('2022-05-01')

new_start_date = add_date(start_date)

end_date = pd.to_datetime('2022-05-31')

new_end_date = remove_date(end_date)

may_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= new_start_date) & (run_22['Date'] <= new_end_date)]

may_mileage = may_activities['Distance'].sum().round(2)

print("May Mileage:", may_mileage, "miles (~", (may_mileage / 1).round(2), "miles per day)")

#======================================================================================
#           June Mileage
#======================================================================================

def add_date(jun_start_day):
    jun_start_day = pd.to_datetime('2022-06-01')
    
    while jun_start_day not in run_22['Date'].values:
        jun_start_day += pd.Timedelta(days=1)
    
    return jun_start_day

def remove_date(jun_end_day):
    jun_end_day = pd.to_datetime('2022-06-30')
    
    while jun_end_day not in run_22['Date'].values:
        jun_end_day -= pd.Timedelta(days=1)
    
    return jun_end_day

start_date = pd.to_datetime('2022-06-01')

new_start_date = add_date(start_date)

end_date = pd.to_datetime('2022-06-30')

new_end_date = remove_date(end_date)

jun_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= new_start_date) & (run_22['Date'] <= new_end_date)]

jun_mileage = jun_activities['Distance'].sum().round(2)

print("June Mileage:", jun_mileage, "miles (~", (jun_mileage / 30).round(2), "miles per day)")

#======================================================================================
#           July Mileage
#======================================================================================

def add_date(jul_start_day):
    jul_start_day = pd.to_datetime('2022-07-01')
    
    while jul_start_day not in run_22['Date'].values:
        jul_start_day += pd.Timedelta(days=1)
    
    return jul_start_day

def remove_date(jul_end_day):
    jul_end_day = pd.to_datetime('2022-07-31')
    
    while jul_end_day not in run_22['Date'].values:
        jul_end_day -= pd.Timedelta(days=1)
    
    return jul_end_day

start_date = pd.to_datetime('2022-07-01')

new_start_date = add_date(start_date)

end_date = pd.to_datetime('2022-07-31')

new_end_date = remove_date(end_date)

jul_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= new_start_date) & (run_22['Date'] <= new_end_date)]

jul_mileage = jul_activities['Distance'].sum().round(2)

print("July Mileage:", jul_mileage, "miles (~", (jul_mileage / 31).round(2), "miles per day)")

#======================================================================================
#           August Mileage
#======================================================================================

def add_date(aug_start_day):
    aug_start_day = pd.to_datetime('2022-08-01')
    
    while aug_start_day not in run_22['Date'].values:
        aug_start_day += pd.Timedelta(days=1)
    
    return aug_start_day

def remove_date(aug_end_day):
    aug_end_day = pd.to_datetime('2022-08-31')
    
    while aug_end_day not in run_22['Date'].values:
        aug_end_day -= pd.Timedelta(days=1)
    
    return aug_end_day

start_date = pd.to_datetime('2022-08-01')

new_start_date = add_date(start_date)

end_date = pd.to_datetime('2022-08-31')

new_end_date = remove_date(end_date)

aug_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= new_start_date) & (run_22['Date'] <= new_end_date)]

aug_mileage = aug_activities['Distance'].sum().round(2)

print("August Mileage:", aug_mileage, "miles (~", (aug_mileage / 31).round(2), "miles per day)")

#======================================================================================
#           September Mileage
#======================================================================================

def add_date(sep_start_day):
    sep_start_day = pd.to_datetime('2022-09-01')
    
    while sep_start_day not in run_22['Date'].values:
        sep_start_day += pd.Timedelta(days=1)
    
    return sep_start_day

def remove_date(sep_end_day):
    sep_end_day = pd.to_datetime('2022-09-30')
    
    while sep_end_day not in run_22['Date'].values:
        sep_end_day -= pd.Timedelta(days=1)
    
    return sep_end_day

start_date = pd.to_datetime('2022-09-01')

new_start_date = add_date(start_date)

end_date = pd.to_datetime('2022-09-30')

new_end_date = remove_date(end_date)

sep_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= new_start_date) & (run_22['Date'] <= new_end_date)]

sep_mileage = sep_activities['Distance'].sum().round(2)

print("September Mileage:", sep_mileage, "miles (~", (sep_mileage / 30).round(2), "miles per day)")

#======================================================================================
#           October Mileage
#======================================================================================

def add_date(oct_start_day):
    oct_start_day = pd.to_datetime('2022-10-01')
    
    while oct_start_day not in run_22['Date'].values:
        oct_start_day += pd.Timedelta(days=1)
    
    return oct_start_day

def remove_date(oct_end_day):
    oct_end_day = pd.to_datetime('2022-10-31')
    
    while oct_end_day not in run_22['Date'].values:
        oct_end_day -= pd.Timedelta(days=1)
    
    return oct_end_day

start_date = pd.to_datetime('2022-10-01')

new_start_date = add_date(start_date)

end_date = pd.to_datetime('2022-10-31')

new_end_date = remove_date(end_date)

oct_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= new_start_date) & (run_22['Date'] <= new_end_date)]

oct_mileage = oct_activities['Distance'].sum().round(2)

print("October Mileage:", oct_mileage, "miles (~", (oct_mileage / 31).round(2), "miles per day)")

#======================================================================================
#           November Mileage
#======================================================================================

def add_date(nov_start_day):
    nov_start_day = pd.to_datetime('2022-11-01')
    
    while nov_start_day not in run_22['Date'].values:
        nov_start_day += pd.Timedelta(days=1)
    
    return nov_start_day

def remove_date(nov_end_day):
    nov_end_day = pd.to_datetime('2022-11-30')
    
    while nov_end_day not in run_22['Date'].values:
        nov_end_day -= pd.Timedelta(days=1)
    
    return nov_end_day

start_date = pd.to_datetime('2022-11-01')

new_start_date = add_date(start_date)

end_date = pd.to_datetime('2022-11-30')

new_end_date = remove_date(end_date)

nov_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= new_start_date) & (run_22['Date'] <= new_end_date)]

nov_mileage = nov_activities['Distance'].sum().round(2)

print("November Mileage:", nov_mileage, "miles (~", (nov_mileage / 30).round(2), "miles per day)")

#======================================================================================
#           December Mileage
#======================================================================================

def add_date(dec_start_day):
    dec_start_day = pd.to_datetime('2022-12-01')
    
    while dec_start_day not in run_22['Date'].values:
        dec_start_day += pd.Timedelta(days=1)
    
    return dec_start_day

def remove_date(dec_end_day):
    dec_end_day = pd.to_datetime('2022-12-31')
    
    while dec_end_day not in run_22['Date'].values:
        dec_end_day -= pd.Timedelta(days=1)
    
    return dec_end_day

start_date = pd.to_datetime('2022-12-01')

new_start_date = add_date(start_date)

end_date = pd.to_datetime('2022-12-31')

new_end_date = remove_date(end_date)

dec_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= new_start_date) & (run_22['Date'] <= new_end_date)]

dec_mileage = dec_activities['Distance'].sum().round(2)

print("December Mileage:", dec_mileage, "miles (~", (dec_mileage / 31).round(2), "miles per day)")

#======================================================================================

print()

total_mileage = run_22['Distance'].sum()

print("Total Mileage from Run_22:", total_mileage, "miles")

print()

avg_mileage_day = total_mileage / run_22['Distance'].count().round(2)

print("Average Mileage Per Day:", avg_mileage_day, "miles")

print()

mileage_highest = run_22[['Date', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[run_22["Activity Type"] == 'Running'].sort_values(by=['Distance'], ascending=[False]).head(25)

print("Top 25 Highest Mileage Days:")
print(mileage_highest)

print()

best_pace = run_22[["Distance", "Avg Pace"]].sort_values(by=['Avg Pace'], ascending=[True])

run_22['Converted'] = run_22['Avg Pace'].apply(time_str_to_seconds)

sub_six = run_22[run_22['Converted'] < 360].sort_values(by=['Avg Pace'], ascending=[True])

sub_six_final = sub_six[['Date', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[run_22["Activity Type"] == 'Running']

print("Activities where the pace is less than 6:00:")
print(sub_six_final)

print()

#sub_six_final_final = sub_six_final.sort_values(by=['Distance'], ascending=[False]).head(1)

favorites = run_22[['Date', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[run_22["Favorite"] == True]

print("Favorites:")
print(favorites)

print()

sep_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= '2022-09-01') & (run_22['Date'] <= '2022-09-30')].sort_index(axis=0, ascending=False)

sep_activities.rename(columns={"Date_Formatted": "Date"}, inplace=True)

print("All September Activities:")
print(sep_activities)

print()

all_activities = run_22[['Date_Formatted', 'Distance']].loc[(run_22['Date'] >= '2022-05-31') & (run_22['Date'] <= '2022-12-18')].sort_index(axis=0, ascending=False)

filtered_activities =  all_activities.loc[(run_22["Activity Type"] == 'Running') | (run_22["Activity Type"] == 'Treadmill Running')]

filtered_activities.loc[:, 'Date_Formatted'] = pd.to_datetime(filtered_activities['Date_Formatted'])

filtered_activities.set_index('Date_Formatted', inplace=True)

# Resample data by week (W-SAT) and calculate the sum for each week
weekly_sum = filtered_activities.resample('W-SAT').sum().round(1)

end_day = pd.to_datetime(run_22['Date_Formatted'])
    
end_day -= pd.Timedelta(days=6)

cumulative_sum = weekly_sum.cumsum()

# Print out the weekly sums
print("Weekly Sums:")
print(cumulative_sum)

print()

#===============================================================================

# # Convert 'Year' column to integers
# result['Year'] = result['Year'].astype(int)

# # Sort the DataFrame by 'Year' column in ascending order
# result = result.sort_values(by=['Year'])

# # # Get the maximum value from the 'Converted' column
# min_value = result['Converted'].min() - 181
# max_value = result['Converted'].max() - 60

# # # Calculate the y-ticks
# y_ticks = list(range(0, int(min_value), 2))

# # # Calculate the x-ticks
# x_ticks = list(result['Year'])
# #x_ticks = (list(range(0, int(max_value), 1)))




# # #x_ticks = list(result['Year'].unique())
# # # unique_years = result['Year'].unique()
# # # x_ticks = list(result['Year'].unique()[::5])

# # # Sort the DataFrame in descending order based on 'Converted' column
# result = result.sort_values(by=['Converted'], ascending=[False])

# # # Creates a bar graph to visualize the average times for each year
# plt.figure(figsize=(24, 10))
# plt.bar(result['Year'], result['conv'], color='red')
# plt.xlabel('Year')
# plt.ylabel('Average Time (seconds)')
# plt.title('Average 800 Meter Times for Each Year (Top 4)')

# # # Customize y-axis ticks to display values every 5 ticks
# plt.yticks(y_ticks)

# # # # Customize y-axis ticks to display values every 5 ticks
# plt.xticks(x_ticks, rotation=45, fontsize=7.8)

# plt.grid(axis='x', linestyle='--', alpha=0.7)
# plt.grid(axis='y', linestyle='--', alpha=0.7)

# # # Show the graph
# #plt.tight_layout()
# #plt.show()
# plt.savefig('best16.png')