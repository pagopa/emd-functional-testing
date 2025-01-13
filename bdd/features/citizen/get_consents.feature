@citizen
# Feature fails if scenario ar not sorted
Feature: Get the citizens' consent

    #Scenario 1
    Scenario: User not already onboarded
        Given citizenB never onboarded
        When a get consents list for citizenB request arrives
        Then the get consents list request fail

    #Scenario 2
    Scenario: User onboarded
        Given citizenA already onboarded on TppA
        When a get consents list for citizenA request arrives
        Then the get consents list request is successful
        And the consents list is not empty