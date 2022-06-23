import random

hedges = ("Please tell me more.",
 "Many of my patients tell me the same thing.",
 "Please continue.")

qualifiers = ("Why do you say that ",
 "You seem to think that ",
 "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your",
 "we":"you", "us":"you", "mine":"yours"}

class Doctor:
    def __init__(self):
        pass
    
    def greetings(self):
        return "Hi, I hope you are well today.\n I am the Doctor program, nice to meet you! :).\n Anyways, what can I do for you?";
        
    def r(self,sentence):
        probability = random.randint(1,5)
        if probability == 1 :
            answer = random.choice(hedges)
        else:
            answer = random.choice(qualifiers) + changePerson(sentence)
            return answer       
    
def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word,word))
    return " ".join(replyWords)

def main():
    doctor=Doctor()
    print(doctor.greetings())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day! :)")
            break
        print(doctor.r(sentence))


if __name__ == "__main__":
    main()
    
    
    

   
    
    