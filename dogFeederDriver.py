
from dogClass import dogClass

def main():

    objective = 0
    sentinel = True

    # Greeting
    print("Hello welcome to DogFeeder")

    # while loop to continue program
    while sentinel:
        objective = getObjectiveInput()
        if objective == 1:
            dog = dogClass()
            dog.setName(input("What is your dogs name: "))
            dog.setAge(input("How old is your dog: "))
            dog.setWeight(input("How much does your dog weigh in pounds: "))


def getObjectiveInput():

    sentinel = True

    while sentinel:
        objective = input("What would you like to do? ")

        if objective == "1":
            print("Okay lets add your dog to your household.")
            return 1
        else:
            print("Invalid Input, Please try again.")


main()