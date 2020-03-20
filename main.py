# Import modules
import argparse
import core.xor  as Xor
import core.salt as Salt
import core.hash as Hash

# Encrypt function
def Encrypt(text, key):
    salt = Hash.getSaltByKey(key, text)
    saltedText = Salt.protect(text, salt)
    xoredText  = Xor.encode(saltedText, key)
    print("Encrypted value: " + xoredText)

# Decrypt function
def Decrypt(text, key):
    unxoredText = Xor.decode(text, key)
    salt = Hash.getSaltByKey(key, unxoredText)
    unsaltData  = Salt.unprotect(unxoredText, salt)
    print("Decrypted value: " + unsaltData)

# Main
if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser(description = "Encrypt/Decrypt you data with Key & Salt")
    parser.add_argument("-e", "--encrypt", type = str, metavar = "<DATA>", help = "Your string to be encrypted.", required = False)
    parser.add_argument("-d", "--decrypt", type = str, metavar = "<DATA>", help = "Your string to be decrypted.", required = False)
    parser.add_argument("-k", "--key",  type = str, metavar = "<KEY>", help = "Your encryption key.", required = True)
    args = parser.parse_args()

    dtext = args.decrypt
    etext = args.encrypt
    key   = args.key

    if(dtext):
        Decrypt(dtext, key)
    elif(etext):
        Encrypt(etext, key)
    else:
        print("Select mode: --encrypt \"string\" or --decrypt \"string\"")