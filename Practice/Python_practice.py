# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])


# dictionary1 = {
#     1: "AAAA",
#     2: "DDDDD",
#     3: "RRRRR"
# }

# for key, value in dictionary1.items():
#      print(f"value has {key} voters.")                           #print(value + " count has " + str(key) + " registered votes")
    
""" print(dictionary1)

print(dictionary1.keys())

print(dictionary1.values())

dictionary1.items()
print(key,value) """ 

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for key, value  in counties_dict.items():
#     print(f"{key}  county has {value} reg vot")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
               {"county":"Denver", "registered_voters": 463353}, 
               {"county":"Jefferson", "registered_voters": 432438}]

#for county, registered_voters in voting_data:
for i in range(len(voting_data)):
 print(f"{voting_data[i]['county']} and reg voter are {voting_data[i]['registered_voters']}")
    
#{voting_data.registered_voters}")
#county has registered_voters reg vot"

# for county_dict in voting_data:
#     for county,registered_voters in county_dict:
#         print(f" {county} {registered_voters}")


