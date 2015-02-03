import json

class ElectedOfficial:
  pass


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


