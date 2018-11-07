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
    city = ""
    month = ""
    day = ""

    print('Hello! Let\'s have a look at some US bikeshare data!')

    while city not in ["chicago", "new york city", "washington"]:
        city = input("Which city would you like to look at: Chicago, New York City or Washington? ").lower()

    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        month = input("Which month (between January and June) would you like to see? Type 'all' to see all months: ").lower()

    while day not in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]:
        day = input("Which weekday would you like to see (Sunday to Saturday)? Type 'all' to see all days: ").lower()

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # create new column 'route' by concatenating start and end stations for each trip
    df['route'] = df['Start Station'] + ' to ' + df['End Station']



    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_route = df['route'].mode()[0]
    print('Most Popular Route:', popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time during periond (in seconds):', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time during periond (in seconds):', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print('Number of users by type:\n', counts_user_types, '\n')

    # TO DO: Display counts of gender - if city is chicago or new york city
    if city in ['chicago', 'new york city']:
        counts_gender = df['Gender'].value_counts()
        print('Number of users by gender:\n', counts_gender, '\n')
    else: print('Gender data not available for this city \n')

    # TO DO: Display earliest, most recent, and most common year of birth - if city is chicago or new york city
    if city in ['chicago', 'new york city']:
        min_birth_year = df['Birth Year'].min()
        print('Earliest birth year:', min_birth_year)
        max_birth_year = df['Birth Year'].max()
        print('Latest birth year:', max_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most common birth year:', common_birth_year)
    else: print('Birth year data not available for this city \n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_rows(df):
    row = 0
    more_rows = input("Would you like to see 5 rows of data? Type 'yes' if so. ").lower()
    while more_rows == 'yes':
        print(df.iloc[row:row+5])
        more_rows = input("\n Would you like to see 5 more rows of data? Type 'yes' if so. ").lower()
        row += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
