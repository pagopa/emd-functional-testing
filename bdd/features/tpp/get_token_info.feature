@tpp
Feature: Get tpp token info

    Scenario: Onboard tpp not onboarded
        Given tppA never onboarded
        When a get token info for TppA request arrives
        Then the get token info request fail

    Scenario: Onboard tpp already onboarded
        Given tppA already onboarded
        When a get info for TppA request arrives
        Then the get info request is successful