import base64

print("""
      
                      welcome to cre8
                simple base64 encoding/decoding
                
                                        
""")
choice = input("[+] encode or decode (1/2) > ")
if choice == '1':
    nigger = input("[#] Text/Code to encode > ")
    nigger_encoded = nigger.encode('utf-8')
    encode_nigger = base64.b64encode(nigger_encoded)
    print(f"""
[+] Success!
[+] Text/Code encoded!
[>] Before: {nigger}
[>] After: {encode_nigger}""")
elif choice == '2':
    no_racism = input("[#] Text/Code to decode > ")
    racism = base64.b64decode(no_racism).decode('utf-8')
    print(f"""
[+] Success!
[+] Text/Code encoded!
[>] Before: {no_racism}
[>] After: {racism}""")
