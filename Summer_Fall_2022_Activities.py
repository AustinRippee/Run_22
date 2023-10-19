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

def add_date(monthnumber):
    start_day = pd.to_datetime(f'2022-{monthnumber:02d}-01')
    
    # Assuming run_22 is defined somewhere in your code
    while start_day not in run_22['Date'].values:
        start_day += pd.Timedelta(days=1)
    
    return start_day

def remove_date(monthnumber):
    
    daynumber = 0
    
    end_day = pd.to_datetime(f'2022-{monthnumber:02d}-{daynumber:02d}')
    
    while end_day not in run_22['Date'].values:
        end_day -= pd.Timedelta(days=1)
    else:
        if monthnumber == 4 or 6 or 9 or 11:
            daynumber = 30
        elif monthnumber == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            daynumber = 31
        else:
            daynumber = 28
        
        end_day = pd.to_datetime(f'2022-{monthnumber:02d}-{daynumber:02d}')
    
    return end_day

#======================================================================================
#           May Mileage
#======================================================================================

# monthnumber = 5

# start_date = add_date(monthnumber)

# print(start_date)

# end_date = remove_date(monthnumber)

# end_date = remove_date(monthnumber)

# may_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= start_date) & (run_22['Date'] <= end_date)]

# may_mileage = may_activities['Distance'].sum().round(2)

# print("May Mileage:", may_mileage, "miles (~", (may_mileage / 1).round(2), "miles per day)")

# #======================================================================================
# #           June Mileage
# #======================================================================================

# monthnumber = 6

# start_date = add_date(monthnumber)

# end_date = remove_date(monthnumber)

# jun_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= start_date) & (run_22['Date'] <= end_date)]

# jun_mileage = jun_activities['Distance'].sum().round(2)

# print("June Mileage:", jun_mileage, "miles (~", (jun_mileage / 30).round(2), "miles per day)")

# #======================================================================================
# #           July Mileage
# #======================================================================================

# monthnumber = 7

# start_date = add_date(monthnumber)

# end_date = remove_date(monthnumber)

# jul_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= start_date) & (run_22['Date'] <= end_date)]

# jul_mileage = jul_activities['Distance'].sum().round(2)

# print("July Mileage:", jul_mileage, "miles (~", (jul_mileage / 31).round(2), "miles per day)")

# #======================================================================================
# #           August Mileage
# #======================================================================================

# monthnumber = 8

# start_date = add_date(monthnumber)

# end_date = remove_date(monthnumber)

# aug_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= start_date) & (run_22['Date'] <= end_date)]

# aug_mileage = aug_activities['Distance'].sum().round(2)

# print("August Mileage:", aug_mileage, "miles (~", (aug_mileage / 31).round(2), "miles per day)")

# #======================================================================================
# #           September Mileage
# #======================================================================================

# monthnumber = 9

# start_date = add_date(monthnumber)

# end_date = remove_date(monthnumber)

# sep_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= start_date) & (run_22['Date'] <= end_date)]

# sep_mileage = sep_activities['Distance'].sum().round(2)

# print("September Mileage:", sep_mileage, "miles (~", (sep_mileage / 30).round(2), "miles per day)")

# #======================================================================================
# #           October Mileage
# #======================================================================================

# monthnumber = 10

# start_date = add_date(monthnumber)

# end_date = remove_date(monthnumber)

# oct_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= start_date) & (run_22['Date'] <= end_date)]

# oct_mileage = oct_activities['Distance'].sum().round(2)

# print("October Mileage:", oct_mileage, "miles (~", (oct_mileage / 31).round(2), "miles per day)")

# #======================================================================================
# #           November Mileage
# #======================================================================================

# monthnumber = 11

# start_date = add_date(monthnumber)

# end_date = remove_date(monthnumber)

# nov_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= start_date) & (run_22['Date'] <= end_date)]

# nov_mileage = nov_activities['Distance'].sum().round(2)

# print("November Mileage:", nov_mileage, "miles (~", (nov_mileage / 30).round(2), "miles per day)")

# #======================================================================================
# #           December Mileage
# #======================================================================================

# monthnumber = 12

# start_date = add_date(monthnumber)

# end_date = remove_date(monthnumber)

# dec_activities = run_22[['Date_Formatted', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[(run_22['Date'] >= start_date) & (run_22['Date'] <= end_date)]

# dec_mileage = dec_activities['Distance'].sum().round(2)

# print("December Mileage:", dec_mileage, "miles (~", (dec_mileage / 31).round(2), "miles per day)")

#======================================================================================

print()

total_mileage = run_22['Distance'].sum()

print("Total Mileage from Run_22:", total_mileage, "miles")

print()

avg_mileage_day = total_mileage / run_22['Distance'].count().round(1)

print("Average Mileage Per Day:", avg_mileage_day.round(2), "miles")

print()

mileage_highest = run_22[['Date', 'Title', 'Distance', 'Time', 'Avg Pace']].loc[run_22["Activity Type"] == 'Running'].round(1).sort_values(by=['Distance', 'Date'], ascending=[False, True]).head(25)

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