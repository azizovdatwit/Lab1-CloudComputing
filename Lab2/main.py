import requests
import json

def maindriver():
    continueLoop = True
    while continueLoop:
        print("Main Menu")
        print("1. Root Route (/)")
        print("2. All Houses (/houses)")
        print("3. Get House Info (/house/{name})")
        print("4. Get House Head (/house/{name}/head)")
        print("5. Get House Mascot (/house/{name}/mascot)")
        print("6. Get House Founder (/house/{name}/founder)")
        print("7. Get House Colors (/house/{name}/colors)")
        print("8. Sorting Hat (/sortingHat?student=...)")
        print("9. Spells (/spells?spell=...)")
        print("10. Best Character (/bestCharacter?person=...)")
        print("11. Cookie")
        print("12. Header")
        print("0. Exit")

        choice = input("Enter your choice (0-12): ")

        if choice == '1':
            url = "http://localhost:8080/"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '2':
            url = "http://localhost:8080/houses"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '3':
            name = input("Enter house name: ")
            url = f"http://localhost:8080/house/{name}"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '4':
            name = input("Enter house name: ")
            url = f"http://localhost:8080/house/{name}/head"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '5':
            name = input("Enter house name: ").lower()
            url = f"http://localhost:8080/house/{name}/mascot"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '6':
            name = input("Enter house name: ")
            url = f"http://localhost:8080/house/{name}/founder"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '7':
            name = input("Enter house name: ")
            url = f"http://localhost:8080/house/{name}/colors"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '8':
            student = input("Enter student name: ")
            url = f"http://localhost:8080/sortingHat?student={student}"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '9':
            spell = input("Enter spell name: ")
            url = f"http://localhost:8080/spells?spell={spell}"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '10':
            person = input("Enter person name: ")
            url = f"http://localhost:8080/bestCharacter?person={person}"
            response = requests.get(url)
            print("Response Body:", response.json())

        elif choice == '11':
            cookie = input("Enter cookie value for 'username': ")
            url = "http://localhost:8080/welcome"
            response = requests.get(url, cookies={"username": cookie})
            print("Response Body:", response.json())

        elif choice == '12':
            header = input("Enter header value for 'house': ")
            url = "http://localhost:8080/verify-house"
            response = requests.get(url, headers={"house": header})
            print("Response Body:", response.text)

        elif choice == '0':
            print("Exiting the program.")
            continueLoop = False


        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    maindriver()
