def processfile(csvfile):
  with open(csvfile, 'r') as f:
    results = []
    for line in f:
      words = line.split(',')
      results.append((words[0], words[1:]))
  return results

def getvals(country, csv):
  monthlist = []
  for row in csv: # row = ('RUS', ['Europe', 'Russia', '25/11/2020', '23393', '498\n'])
    if row[1][1] == country:
      date = row[1][2]
      month = date[:-5]
      month = month[-2:] # individual listings of month
      case = {'month': month, 'cases': row[1][3] }
      monthlist.append(case)
  jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = [], [], [], [], [], [], [], [], [], [], [], []
  for row in monthlist: # row = {'month': '01', 'cases': '10798'}
    if row['month'] == '01':
      jan.append(row['cases']) # e.g., ['22210', '11825', '14245', '10798', '15375', '20326', '18416', '17529', '19976', '18625']
    if row['month'] == '02':
      feb.append(row['cases'])
    if row['month'] == '03':
      mar.append(row['cases'])
    if row['month'] == '04':
      apr.append(row['cases'])
    if row['month'] == '05':
      may.append(row['cases'])
    if row['month'] == '06':
      jun.append(row['cases'])
    if row['month'] == '07':
      jul.append(row['cases'])
    if row['month'] == '08':
      aug.append(row['cases'])
    if row['month'] == '09':
      sep.append(row['cases'])
    if row['month'] == '10':
      oct.append(row['cases'])
    if row['month'] == '11':
      nov.append(row['cases'])
    if row['month'] == '12':
      dec.append(row['cases'])
  allmonths = [jan] + [feb] + [mar] + [apr] + [may] + [jun] + [jul] + [aug] + [sep] + [oct] + [nov] + [dec]
  for month in allmonths:
    if '0' in month:
      month.remove('0')
    if len(month) == 0:
      month.append('0')
  return allmonths

def findMinMax(allmonths):
  minimum = []
  maximum = []
  for month in allmonths:
    month = [int(x) for x in month] # convert strings into ints
    month.sort()
    minimum.append(month[0])
  for month in allmonths:
    month = [int(x) for x in month] # convert strings into ints
    month.sort(reverse=True)
    maximum.append(month[0])
  return minimum, maximum

def average_standarddev(allmonths):
  # work out average
  average = []
  for month in allmonths:
    month = [int(x) for x in month] # convert strings into ints
    sum = 0
    for val in month:
      sum = sum+val
    avg = round(sum/len(month), 4)
    average.append(avg)
  # work out std
  standarddev = []
  return average, standarddev

def main(csvfile, country, type):
  csv = processfile(csvfile)
  type = type.replace(" ", "").lower()
  if type == 'statistics':
    country = country.replace(" ", "").capitalize()
    allmonths = getvals(country, csv)
    mn1, mxl = findMinMax(allmonths)
    avgl, stdl = average_standarddev(allmonths)
    print(mn1,mxl,avgl,stdl)
  if type == 'correlation':
    country1 = country[0].replace(" ", "").capitalize()
    country2 = country[1].replace(" ", "").capitalize()
    allmonths_country1 = getvals(country1, csv)
    allmonths_country2 = getvals(country2, csv)
    print(allmonths_country1)


#main('Covid-data-for-project_1_sample.csv', "France", "statistics")
#main('Covid-data-for-project_1_sample.csv', ["france","italy"],"correlation")

