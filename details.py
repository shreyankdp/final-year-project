import os
path1='C:\\Users\shrey\Downloads\AGE_INVARIANT\AGE_INVARIANT\criminal'
dir_crim=os.listdir(path1)
path2='C:\\Users\shrey\Downloads\AGE_INVARIANT\AGE_INVARIANT\children'
dir_child=os.listdir(path2)

crim=[]
child=[]
for i in dir_crim:

    if i[1:3] in crim:
        continue
    crim.append(i[1:3])
for i in dir_child:

    if i[1:3] in child:
        continue
    child.append(i[1:3])
print(crim)

mc=[
    {
    'name':'Joseph',
    'sex':'Male',
    'crime':'Chain snatch',
    'punishment':'Imprisonment',
    'wanted by':'USA',
    'nationality':'Russian'
    },
    {
    'name':'Alex',
    'sex':'Male',
    'crime':'Murder',
    'punishment':'Life imprisonment',
    'wanted by':'USA',
    'nationality':'USA'
    },
    {
    'name':'Isabella',
    'sex':'Female',
    'crime':'Serial killer',
    'punishment':'Death penalty',
    'wanted by':'England',
    'nationality':'England'
    },
    {
    'name':'Chris',
    'sex':'Male',
    'crime':'Robbery',
    'punishment':'Fines',
    'wanted by':'Jamica',
    'nationality':'England'
    },
    {
    'name':'Will',
    'sex':'Male',
    'crime':'Murder',
    'punishment':'Life imprisonment',
    'wanted by':'India',
    'nationality':'UN'
    },
    {
    'name':'David',
    'sex':'Male',
    'crime':'Human Trafficing',
    'punishment':'Death Penalty',
    'wanted by':'USA',
    'nationality':'UN'
    },
    {
    'name':'Anthony',
    'sex':'Male',
    'crime':'Chain Snatch',
    'punishment':'Fine',
    'wanted by':'Russia',
    'nationality':'England'
    },
    {
    'name':'Daniel',
    'sex':'Male',
    'crime':'Harrasment',
    'punishment':'Life imprisonment',
    'wanted by':'USA',
    'nationality':'England'
    },
    {
    'name':'Butcher',
    'sex':'Male',
    'crime':'Drug Pedlar',
    'punishment':'Forfeiture',
    'wanted by':'USA',
    'nationality':'England'
    },
    {
    'name':'Mohammad Ali',
    'sex':'Male',
    'crime':'Terrorist',
    'punishment':'Death Sentence',
    'wanted by':'India',
    'nationality':'Pakistan'
    },
    {
    'name':'Dawood',
    'sex':'Male',
    'crime':'Smuggler',
    'punishment':'Imprisonment',
    'wanted by':'India',
    'nationality':'Afghanistan'
    },
    {
    'name':'Sam',
    'sex':'Male',
    'crime':'Chain snatch',
    'punishment':'Fine',
    'wanted by':'USA',
    'nationality':'UK'
    },
    {
    'name':'Kim',
    'sex':'Male',
    'crime':'Pedlar',
    'punishment':'Restitution',
    'wanted by':'USA',
    'nationality':'UP'
    },
    {
    'name':'Tim',
    'sex':'Male',
    'crime':'Forgery',
    'punishment':'Fine',
    'wanted by':'USA',
    'nationality':'UK'
    },
    {
    'name':'Olivia',
    'sex':'Woman',
    'crime':'Homicide',
    'punishment':'Life Imprisonment',
    'wanted by':'England',
    'nationality':'Russia'
    },
    {
    'name':'Walter',
    'sex':'Male',
    'crime':'Cannibalism',
    'punishment':'Death Sentence',
    'wanted by':'England',
    'nationality':'Russia'
    },
    {
    'name':'Morgan',
    'sex':'Male',
    'crime':'Assault',
    'punishment':'Imprisonment',
    'wanted by':'England',
    'nationality':'UK'
    },
    {
    'name':'Victor',
    'sex':'Male',
    'punishment':'Probation',
    'crime':'Theft',
    'wanted by':'Jamica',
    'nationality':'India'
    }
    
]
crim_details=dict(zip(crim,mc))

missing_children = [
    {
        'Name': 'Bob',
        'Sex': 'Male',
        'Missing Year': 2022,
        'Missing Place': 'New York City',
        'language':'English',
        'Guardian Contact Number': '+1-555-1234'
    },
    {
        'Name': 'Alice',
        'Sex': 'Female',
        'Missing Year': 2021,
        'Missing Place': 'Los Angeles',
        'language':'English',
        'Guardian Contact Number': '+1-555-5678'
    },
    {
        'Name': 'Charlie',
        'Sex': 'Male',
        'Missing Year': 2022,
        'Missing Place': 'Chicago',
        'language':'English',
        'Guardian Contact Number': '+1-555-9101'
    },
    {
        'Name': 'Ethan',
        'Sex': 'Male',
        'Missing Year': 2021,
        'Missing Place': 'Houston',
        'language':'Spanish and Vietnamese',
        'Guardian Contact Number': '+1-555-1121'
    },
    {
        'Name': 'Joe',
        'Sex': 'Male',
        'Missing Year': 2022,
        'Missing Place': 'Miami',
        'language':'Spanish',
        'Guardian Contact Number': '+1-555-3141'
    },
    {
        'Name': 'Ana',
        'Sex': 'Female',
        'Missing Year': 2021,
        'Missing Place': 'Phoenix',
        'language':'English',
        'Guardian Contact Number': '+1-555-5161'
    },
    {
        'Name': 'Roger',
        'Sex': 'Male',
        'Missing Year': 2022,
        'Missing Place': 'Philadelphia',
        'language':'English and Spanish',
        'Guardian Contact Number': '+1-555-7181'
    },
    {
        'Name': 'Milly',
        'Sex': 'Female',
        'Missing Year': 2021,
        'Missing Place': 'San Antonio',
        'language':'Tagalog',
        'Guardian Contact Number': '+1-555-9202'
    },
    {
        'Name': 'Amith',
        'Sex': 'Male',
        'Missing Year': 2022,
        'Missing Place': 'India',
        'language':'Kannada and Hindi',
        'Guardian Contact Number': '+91 7896541234'
    },
    {
        'Name': 'Jacob',
        'Sex': 'Male',
        'Missing Year': 2021,
        'Missing Place': 'Dallas',
        'language':'English and Arabic',
        'Guardian Contact Number': '+1-555-4252'
    },
    {
        'Name': 'Lily',
        'Sex': 'Female',
        'Missing Year': 2022,
        'Missing Place': 'Seattle',
        'language':'Spanish and Chinese',
        'Guardian Contact Number': '+1-555-6272'
    },
    {
        'Name': 'Mike',
        'Sex': 'Male',
        'Missing Year': 2021,
        'Missing Place': 'Atlanta',
        'language':'English and Mandarin Chinese',
        'Guardian Contact Number': '+1-555-8292'
    },
    {
        'Name': 'Will',
        'Sex': 'Male',
        'Missing Year': 2022,
        'Missing Place': 'Washington DC',
        'language':'English',
        'Guardian Contact Number': '+1-555-1313'
    },
    {
        'Name': 'Eleven',
        'Sex': 'Female',
        'Missing Year': 2021,
        'Missing Place': 'Denver',
        'language':'English',
        'Guardian Contact Number': '+1-555-3333'
    },
    {
        'Name': 'Patrick',
        'Sex': 'Male',
        'Missing Year': 2022,
        'Missing Place': 'Boston',
        'language':'English',
        'Guardian Contact Number': '+1-555-5353'
    },
    {
        'Name': 'Quinn',
        'Sex': 'Male',
        'Missing Year': 2021,
        'Missing Place': 'Portland',
        'language':'English and Tagalog',
        'Guardian Contact Number': '+1-555-7373'
    },
    {
        'Name': 'Ryan',
        'Sex': 'Male',
        'Missing Year': 2022,
        'Missing Place': 'San Francisco',
        'language':'English',
        'Guardian Contact Number': '+1-555-9393'
    },
    {
        'Name': 'George',
        'Sex': 'Male',
        'Missing Year': 2021,
        'Missing Place': 'Austin',
        'language':'English',
        'Guardian Contact Number': '+1-555-1414'
    },
    {
        'Name': 'Tyler',
        'Sex': 'Male',
        'Missing Year': 2022,
        'Missing Place': 'Las Vegas',
        'language':'English and Korean',
        'Guardian Contact Number': '+1-555-3434'
    }
]
child_details=dict(zip(child,missing_children))
