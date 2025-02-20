# The groups_per_user function receives a dictionary, which contains group names
# with the list of users. Users can belong to multiple groups.
# Return a dictionary with the users as keys and a list of their groups as values.

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for host,users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user in user_groups:
				user_groups[user].append(host)
			else:
				user_groups[user] = [host]

	return user_groups

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))