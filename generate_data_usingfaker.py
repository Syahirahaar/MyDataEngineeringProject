#using faker to generate unique id, timestamp, locationFAKER
import numpy as np
import pandas as pd
from faker.providers.person.en import Provider
from faker import Faker

fake = Faker()

from datetime import datetime


def random_names(name_type, size):
    """
    Generate n-length ndarray of person names.
    name_type: a string, either first_names or last_names
    """
    names = getattr(Provider, name_type)
    return np.random.choice(names, size=size)


def random_genders(size, p=None):
    """Generate n-length ndarray of genders."""
    if not p:
        # default probabilities
        p = (0.49, 0.49, 0.01, 0.01)
    gender = ("M", "F", "O", "")
    return np.random.choice(gender, size=size, p=p)

def random_dates(start, end, size):

    # Unix timestamp is in nanoseconds by default, so divide it by
    # 24*60*60*10**9 to convert to days.
    divide_by = 24 * 60 * 60 * 10**9
    start_u = start.value // divide_by
    end_u = end.value // divide_by
    return pd.to_datetime(np.random.randint(start_u, end_u, size), unit="s")

    # How many records do we want to create in our CSV? In this example
    # we are generating 100, but you could also find relatively fast results generating
    # much larger datasets
def random_location(location,size):
    location = []
    for _ in range(size):
        location.append(fake.location_on_land())
    return location

def random_id(id,size):
    id = []
    for _ in range(size):
        id.append(fake.ssn())
    return id

size = 10
df = pd.DataFrame(columns=['flight_id','review_id','timestamp','Location','Names','Gender','lala','lali'])
df['First'] = random_names('first_names', size)
df['Last'] = random_names('last_names', size)
df['Names'] = df['First'] + ' ' + df['Last']
df['flight_id'] = random_id('id',size)
df['review_id'] = np.random.randint(1,10,len(df) )
df['Location'] = random_location('location', size)
df['Gender'] = random_genders(size)
df['timestamp'] = random_dates(start=pd.to_datetime('2017-01-01'), end=pd.to_datetime('2018-01-01'), size=size)
df['lala'] = df['Location'][3][4]
df['Destination'] = [x.split('/')[-1] for x in df['lala']]
#df['timestamp'] = randomtimes(stime=pd.to_datetime('01-01-2010 00:00:00'),etime=pd.to_datetime('01-01-2012 00:00:00'),size=size)
df1 = df[['flight_id','review_id','timestamp','Names','Gender','Destination']]
df1.to_csv('generate_fake_data.csv')
