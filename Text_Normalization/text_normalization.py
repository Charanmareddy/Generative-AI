class TextNormalization:

    def __init__(self,data):
        self.data =  data
        self.start()
    
    def start(self):
        print('''
              1) Converting strings to lower case
              2) Removing punctuations
              3) Removing special characters
              4) Handling Emojis
              5) Removing Extra Spaces
              6) Contractions
              7) Correcting the words
              ''')
        print("1) Converting strings to lower case.......")
        self.strings_lowercase()
        print("2.Removing punctuations....")
        opt_punctuation = input("Enter yes/no: ").lower()
        if opt_punctuation == 'yes':
            self.removing_punctuations()
        print("3. Removing special characters...")
        opt_splchars = input("Enter your option remove(yes)/ skip(no): ").lower()
        if opt_splchars == 'yes':
            self.removing_spl_char()
        print("4.Handling Emojis....")
        opt_emojis = int(input("Enter you want to Remove Emojis(1)/Demojize(0): "))
        self.handle_emojis(opt_emojis)
        print("5. Removing Extra spaces...")
        self.remove_extra_spaces()
        print("6. Expanding words and Abbrevations....")
        self.contractions()
        print('7. Correcting words...')
        self.correcting_words()

        print(self.data)
        
    def strings_lowercase(self):
        # This function should return updated text
        self.data = self.data.lower()

    def removing_punctuations(self):
        chars = self.data
        import string
        punctuations = string.punctuation
        for char in punctuations:
            chars = chars.replace(char,'')
        self.data = chars

    def removing_spl_char(self):
        chars = self.data
        for char in chars:
            if not char.isalnum() and not ord(char) == 32:
                chars = chars.replace(char,'')
        self.data = chars

    def handle_emojis(self,opt):
        import emoji
        chars = self.data
        if opt == 1:
            chars = emoji.replace_emoji(chars,"")
        elif opt == 0:
            chars = emoji.demojize(chars)
        else:
            print("Invalid option, choose valid option from(Remove Emojis(1)/Demojize(0))")
        self.data = chars
    
    def remove_extra_spaces(self):
        chars = self.data.split()
        self.data = ' '.join(chars)
    
    def contractions(self):
        import contractions
        self.data = contractions.fix(self.data)

    def correcting_words(self):
        from textblob import TextBlob
        self.data = TextBlob(self.data).correct()

obj = TextNormalization("  Hiiiii!!!   I'm ChArAn 😊🎉, and I can'ttt believee   " \
"thissss isss soooo coool!!!  " \
"I've paid ₹5,000 @ Amazon.com on 12/07/2026...   Visit: https://example.com My e-mail is " \
"Charan_123@gmail.com!!!   #AI #MachineLearning It's   amazzingggg, isn'ttt it???   😂🔥")
    


'''
obj = class()

When we creating the object for class, first it will call the magic/dunder method called __new__() method internally, 
now later the new() will call the __init__() method
'''