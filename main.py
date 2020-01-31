import csv
from sklearn.neighbors import KNeighborsClassifier

#Voter class representing voter
class Voter:
  def __init__(self, optimus_id, age, party, ethnicity, income, education, marital_status, occupation_industry, 
              vh00p, vh00g, vh02p, vh02g, 
              vh04p, vh04g, vh06p, vh06g, 
              vh08p, vh08g, vh10p, vh10g, vh12p, vh12g, vh14p, 
              net_worth, donates_to_liberal_causes, donates_to_conservative_causes, congressional_district, designated_market_area,
              g08_precinct_turnout, g10_precinct_turnout, g12_precinct_turnout, 
              p08_precinct_turnout, p10_precinct_turnout, p12_precinct_turnout):
    self.optimus_id = optimus_id
    
    #Previous election data is coming as string 
    #Converting string to integer value
    self.vh00p = int(vh00p)
    self.vh02p = int(vh02p)
    self.vh04p = int(vh04p)
    self.vh06p = int(vh06p)
    self.vh08p = int(vh08p)
    self.vh10p = int(vh10p)

    self.vh00g = int(vh00g)
    self.vh02g = int(vh02g)
    self.vh04g = int(vh04g)
    self.vh06g = int(vh06g)
    self.vh08g = int(vh08g)
    self.vh10g = int(vh10g)

    self.vh12p = int(vh12p)
    self.vh12g = int(vh12g)

    self.vh14p = int(vh14p)
    # Percint turnout information was missing on some voters
    # Checking if value string is "0.32" or ""
    if len(g08_precinct_turnout) == 0:
      g08_precinct_turnout = "0"
    if len(p08_precinct_turnout) == 0:
      p08_precinct_turnout = "0"
    if len(g10_precinct_turnout) == 0:
      g10_precinct_turnout = "0"
    if len(p10_precinct_turnout) == 0:
      p10_precinct_turnout = "0"
    if len(p12_precinct_turnout) == 0:
      p12_precinct_turnout = "0"
    if len(g12_precinct_turnout) == 0:
      g12_precinct_turnout = "0"
    self.g08_precinct_turnout = float(g08_precinct_turnout)
    self.g10_precinct_turnout = float(g10_precinct_turnout)
    self.g12_precinct_turnout = float(g12_precinct_turnout)
    self.p08_precinct_turnout = float(p08_precinct_turnout)
    self.p10_precinct_turnout = float(p10_precinct_turnout)
    self.p12_precinct_turnout = float(p12_precinct_turnout)

    # Also congressional_district was empty
    if len(congressional_district) == 0:
      congressional_district = 0
    self.congressional_district = float(congressional_district)

    # Representing values with integer values
    if "Married" in marital_status:
      self.marital_status = 1
    elif "Non-Traditional" in marital_status:
      self.marital_status = 2
    else:
      self.marital_status = 3

    # Representing values with integer values
    if "LAS VEGAS DMA (EST.)" in designated_market_area:
      self.designated_market_area = 1
    elif "RENO DMA (EST.)" in designated_market_area:
      self.designated_market_area = 2
    else:
      self.designated_market_area = 3
    
    # len(age) is zero when age = "" so age = 0
    if len(age) == 0:
      age = 0
    self.age = float(age)
    # Representing values with integer values
    if party == "Republican":
      self.party = 1
    elif party == "Democratic":
      self.party = 2
    elif party == "American Independent":
      self.party = 3
    else:
      self.party = 4
    
    # Representing values with integer values
    if ethnicity == "European":
      self.ethnicity = 1
    elif ethnicity == "African-American":
      self.ethnicity = 2
    elif ethnicity == "Asian":
      self.ethnicity = 3
    elif ethnicity == "Hispanic":
      self.ethnicity = 4
    elif ethnicity == "Other":
      self.ethnicity = 5
    else:
      self.ethnicity = 6
    
    # Representing values with integer values
    if "Medical" in occupation_industry:
      self.occupation_industry = 1
    elif "Manufacturing" in occupation_industry:
      self.occupation_industry = 2
    elif "Management" in occupation_industry:
      self.occupation_industry = 3
    elif "Clerical/Office" in occupation_industry:
      self.occupation_industry = 4
    elif "Other" in occupation_industry:
      self.occupation_industry = 5
    elif "Financial Services" in occupation_industry:
      self.occupation_industry = 6
    elif "Skilled Trades" in occupation_industry:
      self.occupation_industry = 7
    elif "Food Services" in occupation_industry:
      self.occupation_industry = 8
    elif "Engineering" in occupation_industry:
      self.occupation_industry = 9
    elif "Military" in occupation_industry:
      self.occupation_industry = 10
    elif "Computer Professional" in occupation_industry:
      self.occupation_industry = 11
    elif "Education" in occupation_industry:
      self.occupation_industry = 12
    elif "Financial Services" in occupation_industry:
      self.occupation_industry = 13
    else:
      self.occupation_industry = 14

    # Representing values with integer values
    if "Grad Degree" in education:
      self.education = 1
    elif "Bach Degree" in education:
      self.education = 2
    elif "Less than HS Diploma" in education:
      self.education = 3
    elif "HS Diploma" in education:
      self.education = 4
    elif "Some College" in education:
      self.education = 5
    else:
      self.education = 6
    
    # Representing values with integer values
    if "200k+" in income:
      self.income = 1
    elif "125k-200k" in income:
      self.income = 2
    elif "75k-125k" in income:
      self.income = 3
    elif "35k-75k" in income:
      self.income = 4
    elif "0-35k" in income:
      self.income = 5
    else:
      self.income = 6
    
    # Representing values with integer values
    if "$499999+" in net_worth:
      self.net_worth = 1
    elif "$250000-499999" in net_worth:
      self.net_worth = 2
    elif "$10000-24999" in net_worth:
      self.net_worth = 3
    elif "$50000-99999" in net_worth:
      self.net_worth = 4
    elif "$25000-49999" in net_worth:
      self.net_worth = 5
    elif "$10000-24999" in net_worth:
      self.net_worth = 6
    elif "$5000-9999" in net_worth:
      self.net_worth = 7
    elif "$1-4999" in net_worth:
      self.net_worth = 8
    else:
      self.net_worth = 9

    # Representing values with integer values
    if "Yes" in donates_to_liberal_causes:
      self.donates_to_liberal_causes = 1
    else:
      self.donates_to_liberal_causes = 2

    # Representing values with integer values
    if "Yes" in donates_to_conservative_causes:
      self.donates_to_conservative_causes = 1
    else:
      self.donates_to_conservative_causes = 2

  def __repr__(self):
    str = ""
    for k, v in self.__dict__.items():
      str += v + ", "
    return str

def makeVoter (args=[]):
  #returning new voter class with given arguments
  return Voter(optimus_id=args[0],
                age=args[1],
                party=args[2],
                ethnicity=args[3], 
                marital_status=args[4],
                income=args[6],
                education=args[7],
                congressional_district=args[8],
                designated_market_area=args[9],
                occupation_industry=args[10],
                vh14p=args[11],
                vh12g=args[12],
                vh12p=args[13],
                vh10g=args[14],
                vh10p=args[15],
                vh08g=args[16],
                vh08p=args[17],
                vh06g=args[18],
                vh06p=args[19],
                vh04g=args[20],
                vh04p=args[21], 
                vh02g=args[22],
                vh02p=args[23], 
                vh00g=args[24],
                vh00p=args[25],
                net_worth=args[26],
                donates_to_liberal_causes=args[30],
                donates_to_conservative_causes=args[31],
                g08_precinct_turnout=args[33],
                g10_precinct_turnout=args[34],
                g12_precinct_turnout=args[35],
                p08_precinct_turnout=args[36],
                p10_precinct_turnout=args[37],
                p12_precinct_turnout=args[38]
                )

# choosing features for model training
def make_features(voters = []):
  features = []
  for voter in voters:
    entry = []
    entry.append(voter.age)
    entry.append(voter.party)
    entry.append(voter.ethnicity)
    entry.append(voter.income)
    entry.append(voter.marital_status)
    entry.append(voter.occupation_industry)
    entry.append(voter.vh02g)
    entry.append(voter.vh04g)
    entry.append(voter.vh06g)
    entry.append(voter.vh08g)
    entry.append(voter.vh10g)
    entry.append(voter.vh12g)
    entry.append(voter.donates_to_liberal_causes)
    entry.append(voter.congressional_district)
    features.append(entry)
  return features

# labeling training data
def make_labels(voters = []):
  labels = []
  for voter in voters:
    labels.append(voter.vh12p)
  return labels

# Returning trained model
def train_model(voters = []):
  clf = KNeighborsClassifier(n_neighbors=10)
  features = make_features(voters)
  labels = make_labels(voters)
  clf = clf.fit(features, labels)
  return clf

# Picking features of voter with given index
def pick_person (voters, index):
  person = []
  person.append(voters[index].age)
  person.append(voters[index].party)
  person.append(voters[index].ethnicity)
  person.append(voters[index].income)
  person.append(voters[index].marital_status)
  person.append(voters[index].occupation_industry)
  person.append(voters[index].vh02g)
  person.append(voters[index].vh04g)
  person.append(voters[index].vh06g)
  person.append(voters[index].vh08g)
  person.append(voters[index].vh10g)
  person.append(voters[index].vh12g)
  person.append(voters[index].donates_to_liberal_causes)
  person.append(voters[index].congressional_district)
  return person

#opening voterfile.csv file as csvfile
with open('voterfile.csv', 'r') as csvfile:
  spamreader = csv.reader(csvfile) #spamreader is now voterfile.csv
  next(spamreader) #skipping headers line
  voter_list = []
  #initializing Voter classes
  for row in spamreader:
    new_voter = makeVoter(args=row)
    voter_list.append(new_voter) 
  
  # training model with voter data from csvfile
  model = train_model(voter_list)
  
  with open('results.csv', 'w') as csvfile:
    #filewriter is now results.csv file
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    # headers of results.csv file
    headers = ["optimus_id", "age", "party", "ethnicity", "income", "marital_status", "occupation_industry", "vh02g", "vh04g", "vh06g", "vh08g", "vh10g", "vh12g"]
    headers.append("donates_to_liberal_causes")
    headers.append("congressional_district")
    headers.append("vote")
    headers.append("vote_prob")
    
    filewriter.writerow(headers)
    
    # writing all voter forecast with features used to forecast
    for i in range(len(voter_list)):
      v = voter_list[i]
      row = [v.optimus_id, v.age, v.party, v.ethnicity, v.income, v.marital_status, v.occupation_industry, v.vh02g, v.vh04g, v.vh06g, v.vh08g, v.vh10g, v.vh12g]
      row.append(v.donates_to_liberal_causes)
      row.append(v.congressional_district)
      example = pick_person(voter_list, i)
      outcome = model.predict([example])[0]
      prob = model.predict_proba([example])[0][1]
      row.append(outcome)
      row.append(prob)
      
      filewriter.writerow(row)
      
