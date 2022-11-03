from os import chdir
import time
import pandas as pd
import numpy as np

chdir ('/Users/sarahyadegari/sarah_code/udacity_python_project/project_files')


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print(" Which city are you interested in investigating? Please choose between Chicago, New York City, or Washington \n ")
        city = str(input('Enter a city: ')).lower()

    
        if city not in CITY_DATA.keys():
            print("That city is not within our database, please try again")

    print (" You have selected {},let's filter by month and specific day of the week ".format(city.title()))

    # get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'all':0,'january' :1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}    
    month = ''
    while month not in MONTH_DATA.keys():
        print(" Which month are you interested in? January until June data available, choose 'all' or a specified month  \n ")
        month = str(input('Enter a month: ')).lower()
    
        if month not in MONTH_DATA.keys():
            print("That month is not within our database, please try again")
    print (" You have selected {},let's filter by specific day of the week ".format(month.title()))
 
    # get user input for day of week (all, monday, tuesday, ... sunday)
   
    DAY_DATA = {'all':0,'sunday' :1, 'monday':2, 'tuesday':3, 'wednesday':4, 'thursday':5, 'friday':6, 'saturday':7, 'sunday':8}
    day = ''
    while day not in DAY_DATA.keys():
        print(" Which day are you interested in? Choose 'all' for each day of the week, or specify a particular day.  \n ")
        day = str(input('Enter a day: ')).lower()
    
        if day not in DAY_DATA.keys():
            print("That input is not within our database, please try again")
    print (" You have selected {},let's filter by specific day of the week ".format(day.title()))
  
    return city, month, day

print('-'*40)


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
    print("Loading data \n")
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
   
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    #Filter by day of week to create the new dataframe
    if day != 'all':
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']
        day = days.index(day) + 1
      
        #Filter by day to create the new dataframe 
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    date_time = pd.to_datetime(df['Start Time'], infer_datetime_format=True)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'], infer_datetime_format=True)

    # display the most common month
    print(df)
    popular_month = df['month'].value_counts().idxmax()

    print("Most popular month to travel:", popular_month)

    # display the most common day of week
  
    popular_day = df['day_of_week'].value_counts().idxmax()

    print("Most Popular day to travel:", popular_day )


    # display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()

    print("Most Popular hour to travel:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].value_counts().idxmax()
    #print(df['Start Station'].value_counts())
    

    # display most commonly used end station
    popular_end = df['End Station'].value_counts().idxmax()
   #print(df['End Station'].value_counts())

    # display most frequent combination of start station and end station trip
    popular_combo = df[['Start Station','End Station']].mode().loc[0]

    print('Most popular start station:', popular_start)
    print('Most popular end station:', popular_end)
    print('Most popular station combination', popular_combo[0],'and ', popular_combo[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()

    print('Total trip duration', total_travel)
    print('Mean travel duration:', mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Statistics...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()


    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    # Display earliest, most recent, and most common year of birth
    try:
        recent_birth= df['Birth Year'].max()
        print('Birth year of youngest user:', recent_birth)
        earliest_birth= df['Birth Year'].min()
        print('Birth year of oldest user:', earliest_birth)
        freq_birth = df['Birth Year'].value_counts().idxmax()
        print('Most common birth year', freq_birth)
    except:
        print("\nThere is no 'Birth Year' column in this file.")


    print('User Types Statistics:',(df['User Type'].value_counts()))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
