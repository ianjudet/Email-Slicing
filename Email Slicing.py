'''
Email Slicing

    Google Bard:
    -   Email slicing is the process of splitting an email address into its two parts: the username and the domain name. 
    The username is the part that comes before the "@" symbol, and the domain name is the part that comes after the "@" symbol.

'''

# Code by: Ian Jude Timbungco / Sept 13,2023

def emailSlice(email):

    ##Slicing email from its username and domain
    username = email[:email.index('@')] 
    domain = email[email.index('@') + 1:]

    return f"Your username is {username} & domain is {domain}" 


def main():
    slice_email = emailSlice(str(input("Enter Email: ").strip()))
    print(slice_email)

if __name__ == '__main__':
    main()
