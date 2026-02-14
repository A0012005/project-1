{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPytnxYVSeBJLZRaX6aqB8C",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/A0012005/project-1/blob/main/password_checker.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1laN8A0H68JQ",
        "outputId": "eb077294-e3fd-4318-a289-f0501ca2b865"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Smart Password Strength Checker\n",
            "Enter a password: 123007\n",
            "Password Strength Result: \n",
            "Weak Password \n",
            "Suggestions to improve your password:\n",
            "- Password should be atleast 8 characters long\n",
            "- Add at least one uppercase letter\n",
            "- Add at least one lowercase letter\n",
            "- Include at least one special character.\n"
          ]
        }
      ],
      "source": [
        "import re\n",
        "print(\"Smart Password Strength Checker\")\n",
        "password = input(\"Enter a password: \")\n",
        "\n",
        "score = 0\n",
        "feedback = []\n",
        "\n",
        "if len(password) >= 8:\n",
        "  score += 1\n",
        "else:\n",
        "  feedback.append(\"Password should be atleast 8 characters long\")\n",
        "\n",
        "if re.search(r\"[A-Z]\", password):\n",
        "  score += 1\n",
        "else:\n",
        "  feedback.append(\"Add at least one uppercase letter\")\n",
        "\n",
        "if re.search(r\"[a-z]\", password):\n",
        "  score += 1\n",
        "else:\n",
        "  feedback.append(\"Add at least one lowercase letter\")\n",
        "\n",
        "if re.search(r\"[0-9]\", password):\n",
        "  score += 1\n",
        "else:\n",
        "  feedback.append(\"Include at least one number \")\n",
        "\n",
        "if re.search(r\"[!@#$%^&*(),.?\\\":{}|<>]\", password):\n",
        "    score += 1\n",
        "else:\n",
        "    feedback.append(\"Include at least one special character.\")\n",
        "\n",
        "print(\"Password Strength Result: \")\n",
        "\n",
        "if score >= 5:\n",
        "    print(\"Strong Password \")\n",
        "elif score >= 3:\n",
        "    print(\"Medium Password \")\n",
        "else:\n",
        "    print(\"Weak Password \")\n",
        "\n",
        "if feedback:\n",
        "    print(\"Suggestions to improve your password:\")\n",
        "    for item in feedback:\n",
        "        print(\"-\", item)"
      ]
    }
  ]
}