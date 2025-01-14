@citizen
# Feature fails if scenario ar not sorted
Feature: Get the citizens onboarded on a tpp

    #Scenario 1
    Scenario: Tpp not already onboarded
        Given TppD is not valid
        When a get citizens onboarded list for TppD request arrives
        Then the get citizens onboarded list request is successful
        And the tpp consents list is empty

    #Scenario 2
    Scenario: Tpp onboarded
        Given TppA is a valid tpp
        And  citizenA already onboarded on TppA
        When a get citizens onboarded list for TppA request arrives
        Then the get citizens onboarded list request is successful
        And the tpp consents list is not empty
        And only the tpp enabled consent are visible

