def capitalize_input_words():
    user_input = input("Enter a sentence: ") 
    result = [] #sonuc saklayacak lst
    word = "" #gecici kelime icin degisken
    
    for char in user_input:
        if char.isalpha():  # karakter harfmi
            word += char
            
        else:
            if word:
                result.append(word.capitalize())  
                ## Karakter harf değilse , word değişkenindeki kelimeyi büyük harf yapıp resulta ekler.
                word = ""
            result.append(char)  # Add the non-letter character directly to result
           
    
    if word: #son kelime icin
        result.append(word.capitalize())
    return ''.join(result)

result = capitalize_input_words()
print("Result:", result)
