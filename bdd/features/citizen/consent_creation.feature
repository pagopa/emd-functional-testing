@citizen
Feature: Onboard on a tpp

    Background:
        Given TppA is a valid tpp
        And  TppB is a valid tpp

        #Scenario 1
    Scenario: Onboard user not already onboarded
        Given citizenA not onboarded on TppA
        When an onboarding for citizen on tppA request arrives
        Then the request is successful
        And others onboarding are not visibile

        #Scenario 2
    Scenario: Onboard user already onboarded on the tpp
        Given citizenA already onboarded on TppA
        When an onboarding for citizenA on tppA request arrives
        Then the request is idempotent

        #Scenario 3
    Scenario: Onboard user already onboarded on another tpp
        Given a citizenA onborded on TppA and not on TppB
        When an onboarding for citizenA on tppB request arrives
        Then the request is successful
        And others onboarding are not visible