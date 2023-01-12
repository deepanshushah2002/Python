print("\n\t\t----------: 𝓦 𝓮𝓵𝓬𝓸𝓶 𝓮 𝓣𝓸 𝓚.𝓑.𝓒 :----------")
questions = [
    ["Which of the following gods is also known as 'Gauri Nandan?'",
        "Agni   ", "Indra", "Hanuman", "Ganesha", 4],  # 1
    ["Which of these is made of bone?", "Walrus tusk ",
        "Rhino horns", "Deer antlers", "Elephant tusk", 3],  # 2
    ["The language of Lakshadweep. a Union Territory of India, is",
        "Tamil    ", "Hindi", "Malayalam", "Telugu", 3],  # 3
    ["Which of these sports will have matches of the shortest durations?",
        "T20 cricket", "Test cricket", "Football   ", "Hockey", 4],  # 4
    ["Which is a capital of India?", "Delhi  ",
        "Mumbai", "Chennai", "Kolkata", 1],  # 5
    ["In the game of ludo the discs or tokens are of how many colours?",
        "One  ", "Two", "Three", "Four", 4],  # 6
    ["Which of these are names of national parks located in Madhya Pradesh?",
        "Krishna and Kanhaiya", "Kanha and Madhav", "Ghanshyam and Murari", "Girdhar and Gopal", 2],  # 7
    ["Bahubali festival is related to",
        "Islam   ", "Hinduism", "Buddhism", "Jainism", 4],  # 8
    ["September 27 is celebrated every year as", "Teachers' Day    ",
        "National Integration Day", "World Tourism Day", "International Literacy Day", 3],  # 9
    ["In which decade was the American Institute of Electrical Engineers (AIEE) founded?",
     "1850s", "1880s", "1930s", "1950s", 2],  # 10
    ["When is the World Population Day observed?", "May 31     ",
        "October 4", "December 10", "July 11", 4],  # 11
    ["The famous Dilwara Temples are situated in", "Uttar Pradesh",
        "Rajasthan", "Maharashtra  ", "Madhya Pradesh", 2],  # 12
    ["The largest Indian State by area is", "Rajasthan    ",
        "Maharashtra", "Uttar Pradesh", "Madhya Pradesh", 1],  # 13
    ["'Dandia' is a popular dance of", "Punjab    ",
        "Gujarat", "Tamil Nadu", "Maharashtra", 2],  # 14
    ["For which of the following disciplines is Nobel Prize awarded?", "Physics and Chemistry          ",
        "Physiology or Medicine", "Literature, Peace and Economics", "All of the above", 4]  # 15
]
amount = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print("\n\t-: Your", i+1, "Question is ₹", amount[i], ":-\n")
    print(i+1, end="")
    print(")", question[0], "\n")
    print(f"1. {question[1]}            2. {question[2]}")
    print(f"3. {question[3]}            4. {question[4]}")
    answer = int(input("\nEnter a answer: "))

    if (question[5] == answer):
        print("\tYour answer is correct")
    else:
        print("Wrong answer\n")
        if (i >= 5 and i < 10):
            money = 10000
            print("Your Win Total amount is:- ₹", money)
        elif (i >= 10 and i < 15):
            money = 320000
            print("Your Win Total amount is:- ₹", money)
        elif (i >= 15):
            money = 10000000
            print("Your Win Total amount is:- ₹", money)
            print("--------You are Win ₹1,Crore--------")
        else:
            print("You Have Entered Wrong Answer and You don't :-", money)
        break
