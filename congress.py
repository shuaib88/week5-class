import json



class ElectedOfficial:

  parties = ["D", "R", "I"]

  def __init__(self, data = None):
    if data != None:
      self.name = "{0}, {1}".format(data["last_name"], data["first_name"])
      self.party = data["party"]
      self.state = data["state"]
      self.loyalty_factor = float(data["votes_with_party_pct"])


  def select_all_from_state(desired_state): # "IL"
    with open("congress.json") as f:
      data = json.load(f)

    rep_data = data["results"][0]["members"]
    member_list = []

    for person in rep_data:
      if person["state"] == desired_state:
        person = ElectedOfficial()
        person.name = "{0}, {1}".format(person["last_name"], person["first_name"])
        person.party = person["party"]
        person.state = person["state"]
        person.loyalty_factor = float(person["votes_with_party_pct"])
        member_list.append(person)


    return member_list


  def one_line_display(self):
    return "{0} is a member {1} party.".format(self.name, self.party)


def read_congress_data():
  with open("congress.json") as f:
    data = json.load(f)

  rep_data = data["results"][0]["members"]
  member_list = []

  for person in rep_data:
    new_member = ElectedOfficial()
    new_member.name = "{0}, {1}".format(person["last_name"], person["first_name"])
    new_member.party = person["party"]
    new_member.state = person["state"]
    new_member.loyalty_factor = float(person["votes_with_party_pct"])
    member_list.append(new_member)

  return member_list


