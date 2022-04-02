#coded  by Hassan Ali
#Date 3/22/2022
#Description : Vernam Encrypt and Decrypt

def  xor (binaryOne,binaryTwo):
    xored  =  ""
    for bit in range(len(binaryOne)):
        if binaryOne[bit] == "0"  and binaryTwo[bit] == "0" :
            xored= xored + "0"
        elif binaryOne[bit] == "0"  and binaryTwo[bit] == "1" :
            xored= xored + "1"
        elif binaryOne[bit] == "1"  and binaryTwo[bit] == "0" :
            xored= xored + "1"
        elif binaryOne[bit] == "1"  and binaryTwo[bit] == "1" :
            xored= xored + "0"
    return xored

def binary_to_hex(binary):
    result = ""
    b = binary[1:]
    list = b.split(" ")
    for byte in list:
        convert_to_decimal =int(byte, 2)
        convert_decimal_to_hex =hex(convert_to_decimal)
        result = result + " " + convert_decimal_to_hex
    return result

def hex_to_binary(n):
    convert_to_decimal = int(n,16)
    decimal_to_binary = bin(int(convert_to_decimal)).replace("b","")
    #print(decimal_to_binary)
    #padding
    if len(decimal_to_binary) < 8:
        pad = 8 - len(decimal_to_binary)
        decimal_to_binary = pad * "0" +  decimal_to_binary
    return decimal_to_binary

def  encrypt (plaintext, key ) :
    #display the cyphertext as hex
    cyphertext_in_binary =  ""
    for i in range(len(plaintext)):
        plaintext_char_in_binary = bin(ord(plaintext[i])).replace("b","")
        key_char_in_binary = bin(ord(key[i])).replace("b","")
        #xor them :
        cyphertext_in_binary = cyphertext_in_binary + " " + xor(plaintext_char_in_binary,key_char_in_binary )
    print("binary :  " + cyphertext_in_binary)
    cyphertext_in_binary_to_hex  = binary_to_hex(cyphertext_in_binary)
    return cyphertext_in_binary_to_hex


def decrypt (cyphertext,key  )  :
    # the  input will be in hex for the cypher
    plaintext = ""
    splitter = cyphertext.split(" ")
    cyphertext_in_binary = ""
    for hex_item in splitter:
        cyphertext_in_binary = cyphertext_in_binary + " " + hex_to_binary(hex_item)

    for i in range(len(key)):
        cypher_char_in_binary = cyphertext_in_binary[1:].split(" ")[i]
        key_char_in_binary = bin(ord(key[i])).replace("b", "")
        #xor them :
        plaintext = plaintext + " " + xor(cypher_char_in_binary,  key_char_in_binary)
    print("plain text in binary " + plaintext)#for binary
    plaintext_not_in_binary = ""
    plaintext_spliter =  plaintext.split(" ")[1:]
    for byte in plaintext_spliter:
        plaintext_not_in_binary = plaintext_not_in_binary + chr(int(byte,2))
    return plaintext_not_in_binary


choose = input(""" Welcome to My vernam program  
[+] press E to encrypt
[+] press D to decrypt
> """)

if choose == "E" :
    plaintext = input("enter plaintext :")
    key = input("enter key : ")
    if len(key) == len(plaintext):
        cyphertext = encrypt(plaintext, key)
        print("hex : " + cyphertext)
    else:
        print("[!] Error the key and the plain text must be the same length ")
elif choose == "D" :
    cyphertext  =  input("enter cyphertext in hex :")
    key  =  input("enter key :")
    print("your plaintext is :" + decrypt(cyphertext, key))
else :
    print("[!] error  ")