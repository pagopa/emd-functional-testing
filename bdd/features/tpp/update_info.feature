@tpp
Feature: Update tpp token info

    Scenario: Onboard tpp not onboarded
        Given tppA never onboarded
        When an update info for TppA request arrives
        Then the update info request fail

    Scenario: Onboard tpp already onboarded
        Given tppA already onboarded
        When a state change for TppA request arrives
        Then the state change request is successful
