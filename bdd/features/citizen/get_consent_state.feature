@citizen
# Feature fails if scenario ar not sorted
Feature: Get a specific citizens' consent

    #Scenario 1
    Scenario: User not already onboarded
        Given citizenB never onboarded
        When a get consent state for citizenB and TppA request arrives
        Then the get consent state request fail

    #Scenario 2
    Scenario: User not onboarded on the tpp
      Given citizenA not onboarded on TppC
      When a get consent state for citizenA and TppC request arrives
      Then the get consent state request fail

    #Scenario 3
    Scenario: User onboarded on the tpp
      Given citizenA already onboarded on TppA
      When a get consent state for citizenA and TppA request arrives
      Then the get consent state request is successful
      And others onboarding are not visible
