def processfile(csvfile):
  with open(csvfile, 'r') as f:
    results = []
    for line in f:
      words = line.split(',')
      results.append((words[0], words[1:]))
  return results

def get_newcases(country, csv):
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
  # if '0' in month:
  #   month.remove('0')
  return minimum, maximum

def average_standarddev(allmonths):
  standarddev = []

  # work out average
  sumsofeachmonth = []
  average = []
  for month in allmonths:
    month = [int(x) for x in month] # convert strings into ints
    sum = 0
    for val in month:
      sum = sum+val # sum will be the sum of each month's new cases, e.g., 163198 for France in January
    avg = round(sum/len(month), 4) # avg will be the average of each month's new cases, e.g., 16319.8 for France in January

    average.append(avg) # will hold arithmetic mean of each month
    sumsofeachmonth.append(sum) # will hold sum of each month

    # work out standard deviation
    sumofdifferences = 0 # Add up the Squared Differences
    for val in month:
      differences = (val-avg)**2 # take each number, subtract the mean and square the result
      sumofdifferences = sumofdifferences + differences
    variance = (sumofdifferences)/len(month)
    std = round(variance**(1/2), 4) # calculate square root of variance to receive standard dev of month
    standarddev.append(std)

  return average, standarddev



def main(csvfile, country, type):
  csv = processfile(csvfile)
  type = type.replace(" ", "").lower()

  if type == 'statistics':
    country = country.replace(" ", "").capitalize()
    allmonths = get_newcases(country, csv)
    mn1, mxl = findMinMax(allmonths)
    avgl, stdl = average_standarddev(allmonths)
    print(mn1, mxl, avgl, stdl)

  if type == 'correlation':
    country1 = country[0].replace(" ", "").capitalize()
    country2 = country[1].replace(" ", "").capitalize()
    allmonths_country1 = get_newcases(country1, csv)
    allmonths_country2 = get_newcases(country2, csv)
    print(allmonths_country1)


#main('Covid-data-for-project_1_sample.csv', "France", "statistics")
#main('Covid-data-for-project_1_sample.csv', ["france","italy"],"correlation")
main('Covid-data-for-project_1_sample.csv', "France", "statistics")
