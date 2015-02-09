from congress import ElectedOfficial
from congress import read_congress_data

# Congressional representatives have:
# - name
# - party
# - state
# - laziness_factor (% of votes missed)

representatives = read_congress_data()

# 1. Make sure that read_congress_data() returns a list object.
assert type(representatives) is list

# 2. Ensure that there are 442 representives.
assert 442 == len(representatives)

# 3. Ensure that each item in the list is of type ElectedOfficial
for rep in representatives:
  assert type(rep) is ElectedOfficial



print("Congratulations, all assertions passed!")
