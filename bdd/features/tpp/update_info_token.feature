@tpp
Feature: Update tpp token info

    Scenario: Onboard tpp not onboarded
        Given tppA never onboarded
        When an update info token  for TppA request arrives
        Then the update info token request fail

    Scenario: Onboard tpp already onboarded
        Given tppA already onboarded
        When an update info token  for TppA request arrives
        Then the update info token request is successful