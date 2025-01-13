@citizen
# Feature fails if scenario ar not sorted
Feature: Onboard on a tpp

    #Scenario 1
    Scenario: Onboard user not already onboarded
        Given citizenA never onboarded
        When an onboarding for citizenA on TppA request arrives
        Then the creation request is successful
        And others onboarding are not visible

    #Scenario 2
    Scenario: Onboard user already onboarded on the tpp
        Given citizenA already onboarded on TppA
        When an onboarding for citizenA on TppA request arrives
        Then the creation request is idempotent
        And others onboarding are not visible

    #Scenario 3
    Scenario: Onboard user already onboarded on another tpp
        Given citizenA onboarded on TppA and not on TppB
        When an onboarding for citizenA on TppB request arrives
        Then the creation request is successful
        And others onboarding are not visible