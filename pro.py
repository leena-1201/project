{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "102972a2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f30f2f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import speech_recognition\n",
    "\n",
    "def record_voice():\n",
    "\tmicrophone = speech_recognition.Recognizer()\t\n",
    "\n",
    "\twith speech_recognition.Microphone() as live_phone:\n",
    "\t\tmicrophone.adjust_for_ambient_noise(live_phone)\n",
    "\n",
    "\t\tprint(\"I'm trying to hear you: \")\n",
    "\t\taudio = microphone.listen(live_phone)\n",
    "\t\ttry:\n",
    "\t\t\tphrase = microphone.recognize_google(audio, language='en')\n",
    "\t\t\treturn phrase\n",
    "\t\texcept speech_recognition.UnkownValueError:\n",
    "\t\t\treturn \"I didn't understand what you said\"\n",
    "\n",
    "if __name__ == '__main__':\n",
    "\tphrase = record_voice()\n",
    "\n",
    "\twith open('you_said_this.txt','w') as file:\n",
    "\t\tfile.write(phrase) \n",
    "\n",
    "\tprint('the last sentence you spoke was saved in you_said_this.txt') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58d26e62",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86304189",
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
