{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2889a51c",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'googletrans'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\ADMINI~1\\AppData\\Local\\Temp/ipykernel_8752/3831091062.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mgoogletrans\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mTranslator\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mtranslator\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mTranslator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m language = {\"bn\": \"Bangla\",\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'googletrans'"
     ]
    }
   ],
   "source": [
    "from googletrans import Translator\n",
    "\n",
    "translator = Translator()\n",
    "\n",
    "language = {\"bn\": \"Bangla\",\n",
    "            \"en\": \"English\",\n",
    "            \"ko\": \"Koren\",\n",
    "            \"fr\": \"French\",\n",
    "            \"de\": \"German\",\n",
    "            \"he\": \"Hebrew\",\n",
    "            \"hi\": \"Hindi\",\n",
    "            \"it\": \"Italian\",\n",
    "            \"ja\": \"Japanese\",\n",
    "            'la': \"Latin\",\n",
    "            \"ms\": \"Malay\",\n",
    "            \"ne\": \"Nepali\",\n",
    "            \"ru\": \"Russian\",\n",
    "            \"ar\": \"Arabic\",\n",
    "            \"zh\": \"Chinese\",\n",
    "            \"es\": \"Spanish\"\n",
    "            }\n",
    "\n",
    "allow = True  # variable to control correct language code input\n",
    "\n",
    "while allow:  # checking if language code is valid\n",
    "\n",
    "    user_code = input(\n",
    "        f\"Please input desired language code. To see the language code list enter 'options' \\n\")\n",
    "\n",
    "    if user_code == \"options\":  # showing language options\n",
    "        print(\"Code : Language\")  # Heading of language option menu\n",
    "        for i in language.items():\n",
    "            print(f\"{i[0]} => {i[1]}\")\n",
    "        print()  # adding an empty space\n",
    "\n",
    "    else:  # validating user input\n",
    "        for lan_code in language.keys():\n",
    "            if lan_code == user_code:\n",
    "                print(f\"You have selected {language[lan_code]}\")\n",
    "                allow = False\n",
    "        if allow:\n",
    "            print(\"It's not a valid language code!\")\n",
    "\n",
    "while True:  # starting translation loop\n",
    "    string = input(\n",
    "        \"\\nWrite the text you want to translate: \\nTo exit the program write 'close'\\n\")\n",
    "\n",
    "    if string == \"close\":  # exit program command\n",
    "        print(f\"\\nHave a nice Day!\")\n",
    "        break\n",
    "\n",
    "    # translating method from googletrans\n",
    "    translated = translator.translate(string, dest=user_code)\n",
    "\n",
    "    # printing translation\n",
    "    print(f\"\\n{language[user_code]} translation: {translated.text}\")\n",
    "    # printing pronunciation\n",
    "    print(f\"Pronunciation : {translated.pronunciation}\")\n",
    "\n",
    "    for i in language.items():  # checking if the source language is listed on language dict and printing it\n",
    "        if translated.src == i[0]:\n",
    "            print(f\"Translated from : {i[1]}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe00c863",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
