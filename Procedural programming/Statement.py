#https://roadmap.sh/python
#https://realpython.com/python-conditional-statements/

#if
young = 17

if young >= 18 :
    print("You can opean brows")
print("You dont have access")    


print()

older = 70

if older >= 18:
    print("You can opean brows")
    

print()

#if in
if 'hotel' in 'Hello my dear friend, i miss you. I want meet with you next mount in a cafe, if you want':
    print('exist')
print('not exist')

if 'cafe' in 'Hello my dear friend, i miss you. I want meet with you next mount in a cafe, if you want':
    print('exist')

if 'foo' in ['bar', 'baza', 'foo']:
    print(True)


print()

#if else
young_1 = 17

if young_1 >= 18:
    print('He is 18 years')
else:
    print('He is not 18 years')

older_1 = 77

if older_1 >= 18:
    print('He is 18 years')
else:
    print('He is not 18 years')

print()

#if elif
name = "Valeria"

if name == "Victora":
    print("Hello Victoria")
elif name == "Dianna":
    print("Hello Dianna")
elif name == "Steav":
    print("Hello Steav")
elif name == "Valeria":
    print("Hello Valeria")

print()

#match case
httpsStatusCode = 200

def https_status_code_description(code):
    match code:
        case 200:
            print("OK")
        case 201:
            print("Create")
        case 400:
            print("Bad Request")
        case 404:
            print("Not found")
        case 500 | 501 | 502:
            print("Server error")
        case _:
            print("Unknown")

https_status_code_description(httpsStatusCode)