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

print(type(representatives))

# 2. How many representatives are there?

print(len(representatives))

# 3. Display the name of the last representative.

print(representatives[-1].name)

# 4. Which rep is most loyal to their party?

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


# 6. Can you make the following code work?
#    You can modify the congress.py file if you want to.

#    first_rep = representatives[0]
#    print(first_rep.one_line_display)

#    should display:
#
#    Robert, Aderholt. Republican.

