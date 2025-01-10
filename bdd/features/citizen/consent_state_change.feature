@citizen
# Feature fails if scenario ar not sorted
Feature: Consent state change

    #Scenario 1
    Scenario: User user not already onboarded
      Given citizenB never onboarded
      When a state change for citizenB on TppA request arrives
      Then the state change request fail

    #Scenario 2
    Scenario: User not onboarded on the tpp
      Given citizenA not onboarded on TppC
      When a state change for citizenA on TppC request arrives
      Then the state change request fail

    #Scenario 3
    Scenario: User onboarded want to disable consent
      Given citizenA already onboarded on TppB
      When a state change for citizenA on TppB request arrives
      Then the state change request is successful
      And others onboarding are not visible

