import time
import calendar
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    cities = ['chicago', 'new york city', 'washington']
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please choose a city: chicago, new york city, washington\n").lower()
    while city not in cities:
        city = input('The city you selected is not valid, please select another city\n').lower()
    
    
    

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please choose a month based on the first 6 months we have data for: january through june or select all\n").lower()
    while month not in months:
        month = input('We only have data for the first 6 months (january - june), please select a valid month').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please choose a day of the week: monday through sunday or select all\n").lower()
    while day not in days:
        day = input('Please select a valid day (monday - sunday)').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
      
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # load CSV files based on city selected by user #
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    # convert the Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time column to create new columns for Month and Day
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
    # extract hour from the Start Time column to create Hour column
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.strftime('%I'' %p')

    # filter by month if applicable
    if month != 'all':
        # extract the index number from the months list to use as a filter
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # create the new dataframe by filtering on month
        df = df[df['Month'] == month]

    if day != 'all':
        # create the new dataframe by filtering on day
        df = df[df['Day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most frequent month to bike
    bike_month = calendar.month_name[df['Month'].value_counts().idxmax()]

    print("What is the most popular month to bike?\n")
    print(bike_month)
    
      
    


    # TO DO: display the most common day of week
    bike_day = df['Day'].value_counts().idxmax()
    print("\nWhat is the most popular day to bike?\n")
    print(bike_day)


    # TO DO: display the most common start hour
    bike_hour = df['Hour'].value_counts().idxmax()
    print("\nWhat is the most popular hour in the day to bike?\n")
    print(bike_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
   

    # TO DO: display most commonly used start station
    
    print("\nWhat is the most commonly used start station to bike?\n")
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print(popular_start_station)
    
     


    # TO DO: display most commonly used end station
    print("\nWhich station do most bikers end their trip?\n")
    popular_end_station = df['End Station'].value_counts().idxmax()
    print(popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    print("\nWhat is the most frequent combination of start and end stations?\n")
    popular_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#use divmod function to assist in converting total seconds to days, hours, minutes, and seconds since trip duration column is in seconds#
def second_conversion(seconds):
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    return days, hours, minutes, seconds
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = int(df['Trip Duration'].sum())
    total_days, total_hours, total_minutes, total_seconds = second_conversion(total_duration)
    print("\nWhat is the total travel time?\n")
    print("Bikers biked a total of: {} days, {} hours, {} minutes, {} seconds".format(total_days, total_hours, total_minutes, total_seconds))
  
                          
   


    # TO DO: display mean travel time
    average_duration = int(df['Trip Duration'].mean())
    average_days, average_hours, average_minutes, average_seconds = second_conversion(average_duration)
    print("\nWhat is the average travel time per bike trip?\n")
    print("\nBikers biked an average of: {} days, {} hours, {} minutes, {} seconds per trip".format(average_days, average_hours, average_minutes, average_seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types_of_users = df['User Type'].value_counts()
    user_percent_breakdown = df['User Type'].value_counts(normalize=True) * 100
    print("\nWhat is the breakdown of user types?\n")
    print(types_of_users)
    print("\nWhat is the percent breakdown of user types?\n")
    print(user_percent_breakdown)
    
                        


    # TO DO: Display counts of gender
    print("\nWhat is breakdown of users by gender?\n")
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print("Sorry, there is no gender data in the data filters you selected, please try again")
    
    print("\nWhat is the percent breakdown of users by gender?\n")
    if 'Gender' in df.columns:
        gender_count_percent = df['Gender'].value_counts(normalize=True) * 100
        print(gender_count_percent)
    else:
        print("Sorry, there is no gender data in the data filters you selected, please try again")


    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nWhat is the earliest birth year, most recent birth year, and most common birth year of all bikers in your filters?\n")
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].value_counts().idxmax())
        print("Earliest Birth Year: {}, Most Recent Birth Year: {}, Most Common Birth Year: {}".format(earliest_birth_year, most_recent_birth_year, most_common_birth_year))
    else:
        print("Sorry, there is no birth year data in the data filters you selected, please try again")
                                     
                                     


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#get individual row data#    
def detailed_trip_data(df):
    choices = ['Yes','No', 'yes', 'no']
    choice = input("\nWould you like to see individual trip data? [Yes/No]\n")
    count = 0
    while choice not in choices:
        choice = input("\nYou did not select a valid response. Would you like to see individual trip data? [Yes/No]\n")
        choice = choice.title()
        
    if choice.title() == 'Yes':
        for row in df.iterrows():
            print(row)
            count += 1
            if count != 0 and count % 5 == 0:
                choice = input("\nWould you like to see additional individual trip data? [Yes/No]\n")
                if choice.title() != 'Yes':
                    break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        detailed_trip_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 


if __name__ == "__main__":
	main()
            

               

    


    
    


