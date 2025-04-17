print("🔮 Welcome to Hritik Anand's Fortune Teller (21JE0410) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Hritik Anand! Keep smiling. ✨")
elif mood == "sad":
    print("💧 Your fortune: Tough times don't last, but tough people do.")
elif mood == "neutral":
    print("🌤️ Your fortune: Calm days ahead, stay focused and grounded.")
elif mood == "stressed":
    print("💆 Take a deep breath, Hritik. Peace is on its way. 💆")
elif mood == "overwhelmed":
    print("🤡 Take a chill pill, Hritik. Success will come. 🤡")
else:
    print("🤔 Sorry, I don't understand that mood.")
