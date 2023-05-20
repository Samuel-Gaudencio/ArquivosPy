{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNXd6XOK9YvHF+orHfpze5x"
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
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "Yo2Hpt97kLnn"
      },
      "outputs": [],
      "source": [
        "linhas = [\n",
        "    '1°; São Paulo; 12396372\\n',\n",
        "    '2°; Rio de Janeiro; 6775561\\n',\n",
        "    '3°; Brasília; 3094325\\n',\n",
        "    '4°; Salvador; 2900319\\n',\n",
        "    '5°; Fortaleza; 2703391\\n',\n",
        "    '6°; Belo Horizonte; 2530701\\n',\n",
        "    '7°; Manaus; 2255903\\n',\n",
        "    '8°; Curitiba; 1963726\\n',\n",
        "    '9°; Recife; 1661017\\n',\n",
        "    '10°; Goiânia; 1555626\\n',\n",
        "]\n",
        "arquivo = open('cidades.txt', 'a')\n",
        "arquivo.writelines(linhas)\n",
        "arquivo.close()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "soma = 0\n",
        "arquivo = open('cidades.txt', 'r')\n",
        "for linha in arquivo:\n",
        "    cidade = linha.split(' ')\n",
        "    populacao = int(cidade[-1])\n",
        "    # print(cidade)\n",
        "    # print(populacao)\n",
        "    soma = soma + populacao\n",
        "arquivo.close()\n",
        "print(f\"A soma da população dos 10 municípios com maior populaçao do Brasil é\", soma)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RLU4bGtjmuM8",
        "outputId": "ae24c4a3-3b96-4978-e7ce-008b40dbb7c9"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A soma da população dos 10 municípios com maior populaçao do Brasil é 37836941\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "linhas = [\n",
        "    '11°; Belém; 1506420\\n',\n",
        "    '12°; Porto Alegre; 1492530\\n',\n",
        "    '13°; Guarulhos; 1404694\\n',\n",
        "    '14°; Campinas; 1223237\\n',\n",
        "    '15°; São Luís; 1115932\\n',\n",
        "    '16; São Gonçalo; 1098357\\n',\n",
        "    '17°; Maceió; 1031597\\n',\n",
        "    '18°; Duque de Caxias; 929449\\n',\n",
        "    '19°; Campo Grande; 916001\\n',\n",
        "    '20°; Natal; 896708\\n',\n",
        "]\n",
        "\n",
        "arquivo = open('cidades.txt', 'a')\n",
        "arquivo.writelines(linhas)\n",
        "arquivo.close()\n"
      ],
      "metadata": {
        "id": "5NePHztAohv8"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "soma = 0 \n",
        "arquivo = open('cidades.txt', 'r')\n",
        "for linha in arquivo:\n",
        "    cidades = linha.split(' ')\n",
        "    # print(cidades)\n",
        "    populacao = int(cidade[-1])\n",
        "    # print(populacao)\n",
        "    soma = soma + populacao\n",
        "arquivo.close()\n",
        "print(f\"A soma da população dos 20 municípios com maior populaçao do Brasil é\", soma)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AD620w4RqJTc",
        "outputId": "7e37226d-09c4-4b9d-c3fa-9fd0cb73f86f"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A soma da população dos 20 municípios com maior populaçao do Brasil é 31112520\n"
          ]
        }
      ]
    }
  ]
}