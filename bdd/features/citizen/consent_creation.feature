@citizen
Feature: Onboard on a tpp

    Background:
        Given TppA is a valid tpp
        And  TppB is a valid tpp

        #Scenario 1
    Scenario: Onboard user not already onboarded
        Given citizenA not onboarded on TppA
        When an onboarding for citizenA on TppA request arrives
        Then the request is successful
        And others onboarding are not visible

        #Scenario 2
    Scenario: Onboard user already onboarded on the tpp
        Given citizenA already onboarded on TppA
        When an onboarding for citizenA on TppA request arrives
        Then the request is idempotent
        And others onboarding are not visible

        #Scenario 3
    Scenario: Onboard user already onboarded on another tpp
        Given citizenA onboarded on TppA and not on TppB
        When an onboarding for citizenA on TppB request arrives
        Then the request is successful
        And others onboarding are not visible