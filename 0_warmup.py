import congress

# Congressional representatives have:
# - name
# - party
# - state
# - loyalty_factor (% of votes with their party)

representatives = congress.read_congress_data()


# Write code to display the correct answers.
#

# 1. What type of object is held inside the 'representatives' variable?
print(representatives[0].parties)

print(type(representatives))

# 2. How many representatives are there?
<<<<<<< HEAD

print(len(representatives))

# 3. Display the name of the last representative.

print(representatives[-1].name)
=======
print(len(representatives))

# 3. Display the name of the last representative.
# print(representatives[-1].name)
>>>>>>> FETCH_HEAD

# 4. Which rep is most loyal to their party?
loyal_rep = representatives[0]
for rep in representatives:
  if rep.loyalty_factor > loyal_rep.loyalty_factor:
    loyal_rep = rep

<<<<<<< HEAD
def most_loyal():

	greatest_loyalty_factor = 0
	most_loyal = "Bart Simpson"

	for person in representatives:
		if person.loyalty_factor > greatest_loyalty_factor:
			greatest_loyalty_factor = person.loyalty_factor
			most_loyal_rep = person

	return most_loyal_rep.name, most_loyal_rep.loyalty_factor


print(most_loyal())

# 5. Which rep is a traitor to their party?

def most_disloyal():

	lowest_loyalty_factor = 100
	most_disloyal_rep = "Bart Simpson"

	for person in representatives:
		if person.loyalty_factor < lowest_loyalty_factor and person.loyalty_factor != 0:
			lowest_loyalty_factor = person.loyalty_factor
			most_disloyal_rep = person

	return most_disloyal_rep.name, most_disloyal_rep.loyalty_factor

print(most_disloyal())

=======
print(loyal_rep.name, loyal_rep.loyalty_factor)
# 5. Which rep is a traitor to their party?

disloyal_rep = representatives[0]
for rep in representatives:
  if rep.loyalty_factor > 0:
    if rep.loyalty_factor < disloyal_rep.loyalty_factor:
      disloyal_rep = rep
>>>>>>> FETCH_HEAD

print(disloyal_rep.name, disloyal_rep.loyalty_factor)
# 6. Can you make the following code work?
#    You can modify the congress.py file if you want to.

first_rep = representatives[0]
print(first_rep.one_line_display())

#    should display:
#
#    Robert, Aderholt. Republican.

