names = ["David", "Jimmy", "Steve", "Ava", "Ally", "Emma", "Emily", "Addy", "Abby", "Abigail", "Gabby", "Gabriella", "Jax", "Jonothan", "Jacob", "Madi", "Madison"]

names = str(names)

lowercase = names.lower()

#Convert to lowercase

vowel_counts = {}


for vowel in "aeiou":

    count = lowercase.count(vowel)

#Count vowels

    vowel_counts[vowel] = count

#Add to dictionary


print(vowel_counts)