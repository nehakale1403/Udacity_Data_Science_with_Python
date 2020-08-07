import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Enter a city from chicago, new york city or washington: ').lower()
    while (1):
        if (city=='chicago' or city=='new york city' or city=='washington'):
            break
        else:
            print('Invalid input!')
            city=input('Please enter a valid city name: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list=['all','january','february','march','april','may','june']
    month=input('Enter the month name (all,january, february, march, april, may, june): ').lower()
    while(1):
        if(month in month_list):
            break
        else:
            print('Invalid input!')
            month=input('Please enter a valid month name: ').lower()
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_list=['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    day=input('Enter the day of the week(all, monday, tuesday, ... sunday): ').lower()
    while(1):
        if(day in days_list):
            break
        else:
            print('Invalid input!')
            day=input('Please enter a valid  day: ').lower()
            
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
    df = pd.read_csv(CITY_DATA[city])
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month kya hua hai??
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    common_month=df['month'].mode()[0]
    print('The most common month is: {}'.format(common_month))

    # TO DO: display the most common day of week
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['day']=df['Start Time'].dt.weekday_name
    common_day=df['day'].mode()[0]
    print('The most common day is: '+ common_day)

    # TO DO: display the most common start hour
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('The most common hour is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].value_counts().idxmax()
    print('The most common start station is: {}'.format(most_common_start_station))
        

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].value_counts().idxmax()
    print('The most common end station is: {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_combination=df[['Start Station','End Station']].mode().loc[0]
    print('The most common start station  and end station trip is: {}'.format(most_common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean travel time is: {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types=df['User Type'].value_counts()
    print('Counts of user types:\n {}'.format(count_of_user_types))

    print('\n')
    
    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('No gender in this city')
    else :
        gender_of_users = df.groupby('Gender',as_index=False).count()
        print('Number of genders of users mentioned in the data are {}'.format(len(gender_of_users)))
        for i in range(len(gender_of_users)):
            print('{}s - {}'.format(gender_of_users['Gender'][i], gender_of_users['Start Time'][i]))
        print('Gender data for {} users is not available.'.format(len(df)-gender_of_users['Start Time'][0]-gender_of_users['Start Time'][1]))
    print('\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('No Birth Year data available')
    else:
        
        #earliest
        earliest_year_of_birth=df['Birth Year'].min()
        print('Earliest year of birth:{}'.format(int(earliest_year_of_birth)))

        #recent
        recent_year_of_birth=df['Birth Year'].max()
        print('Recent year of birth:{}'.format(int(recent_year_of_birth)))

        #most common
        most_common_year_of_birth=df['Birth Year'].value_counts().idxmax()
        print('Most common year of birth: {}'.format(int(most_common_year_of_birth)))


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
def display_data(df):
    yes_or_no=input('Do you want to see raw data?(Yes or No) ').lower()
  
    if yes_or_no=='yes' or yes_or_no=='y':
        choice = True
    elif yes_or_no=='no' or yes_or_no=='n':
        choice = False
    else:
        print('Invalid Input!')
        display_data(df)
        return
    
    if choice:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print("\n")
            choice = input('Another five? Yes/No ').lower()
            if choice=='yes' or choice=='y':
                continue
            elif choice=='no' or choice=='n':
                break
            else:
                print('You did not enter a valid choice.')
                return
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
