@citizen
Feature: Get the citizens' consent

    Scenario: User not already onboarded
        Given citizenB never onboarded
        When a get consents list for citizenB request arrives
        Then the get consents list request fail

    Scenario: User onboarded
        Given citizenA already onboarded on TppA
        When a get consents list for citizenA request arrives
        Then the get consents list request is successful
        And the consents list is not empty