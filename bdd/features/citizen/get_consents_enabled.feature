@citizen
# Feature fails if scenario ar not sorted
Feature: Get the citizens' consent enabled

    #Scenario 1
    Scenario: User not already onboarded
        Given citizenB never onboarded
        When a get consents list enabled for citizenB request arrives
        Then the get consents list enabled request fail

    #Scenario 2
    Scenario: User onboarded
        Given citizenA already onboarded on TppA
        When a get consents list enabled for citizenA request arrives
        Then the get consents list enabled request is successful
        And the consents list is not empty
        And all the consents are enabled

    #Scenario 3
    Scenario: User onboarded but no enabled consents
        Given citizenC onboarded on TppA but disabled
        When a get consents list enabled for citizenC request arrives
        Then the get consents list enabled request is successful
        And the consents list is empty