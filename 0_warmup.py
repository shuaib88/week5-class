import congress

# Congressional representatives have:
# - name
# - party
# - state
# - loyalty_factor (% of votes with their party)

representatives = congress.read_congress_data()



#
# Write code to display the correct answers.
#

# 1. What type of object is held inside the 'representatives' variable?
print(representatives[0].parties)

print(type(representatives))

# 2. How many representatives are there?
print(len(representatives))

# 3. Display the name of the last representative.
# print(representatives[-1].name)

# 4. Which rep is most loyal to their party?
loyal_rep = representatives[0]
for rep in representatives:
  if rep.loyalty_factor > loyal_rep.loyalty_factor:
    loyal_rep = rep

print(loyal_rep.name, loyal_rep.loyalty_factor)
# 5. Which rep is a traitor to their party?

disloyal_rep = representatives[0]
for rep in representatives:
  if rep.loyalty_factor > 0:
    if rep.loyalty_factor < disloyal_rep.loyalty_factor:
      disloyal_rep = rep

print(disloyal_rep.name, disloyal_rep.loyalty_factor)
# 6. Can you make the following code work?
#    You can modify the congress.py file if you want to.

first_rep = representatives[0]
print(first_rep.one_line_display())

#    should display:
#
#    Robert, Aderholt. Republican.

