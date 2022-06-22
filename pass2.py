{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2341af96",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "import math\n",
    "\n",
    "alpha = \"abcdefghijklmnopqrstuvwxyz\"\n",
    "num = \"0123456789\"\n",
    "special = \"@#$%&*\"\n",
    "\n",
    "# pass_len=random.randint(8,13)  #without User INput\n",
    "pass_len = int(input(\"Enter Password Length\"))\n",
    "\n",
    "# length of password by 50-30-20 formula\n",
    "alpha_len = pass_len//2\n",
    "num_len = math.ceil(pass_len*30/100)\n",
    "special_len = pass_len-(alpha_len+num_len)\n",
    "\n",
    "\n",
    "password = []\n",
    "\n",
    "\n",
    "def generate_pass(length, array, is_alpha=False):\n",
    "    for i in range(length):\n",
    "        index = random.randint(0, len(array) - 1)\n",
    "        character = array[index]\n",
    "        if is_alpha:\n",
    "            case = random.randint(0, 1)\n",
    "            if case == 1:\n",
    "                character = character.upper()\n",
    "        password.append(character)\n",
    "\n",
    "\n",
    "# alpha password\n",
    "generate_pass(alpha_len, alpha, True)\n",
    "# numeric password\n",
    "generate_pass(num_len, num)\n",
    "# special Character password\n",
    "generate_pass(special_len, special)\n",
    "# suffle the generated password list\n",
    "random.shuffle(password)\n",
    "# convert List To string\n",
    "gen_password = \"\"\n",
    "for i in password:\n",
    "    gen_password = gen_password + str(i)\n",
    "print(gen_password)"
   ]
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
