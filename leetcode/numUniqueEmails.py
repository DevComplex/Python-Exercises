def parseEmail(email):
    output = []
    ignore = False

    for index, letter in enumerate(email):
        if letter == "@":
            output.append(email[index:])
            return "".join(output)
        if letter == "." or ignore:
            continue
        if letter == "+":
            ignore = True
        else:
            output.append(letter)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

def numUniqueEmails(emails):
    output = set()

    for email in emails:
        parsedEmail = parseEmail(email)
        output.add(parsedEmail)

    return len(output)

print(numUniqueEmails(emails))