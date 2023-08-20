# create a text file and add the below content without quotation marsk
# """
# Hi *user*!

# We've found the best article for you based on your interest: *title*
# Please click *here* to open the article
# """

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link

# after running the program three times
# the file user_email.txt must have all three users content

file = open("email_format.txt", "r")
content = file.read()
file.close()

content = content.replace("*user*", "Saboor")
content = content.replace("*title*", "Backend Development")
content = content.replace("*here*", "www.google.com")

file = open("user_email.txt", "a")
file.write(content + "\n")
file.close()
