@tpp
Feature: Get tpp info

    Scenario: Tpp tpp not onboarded
        Given tppA never onboarded
        When a get info for TppA request arrives
        Then the get info request fail

    Scenario: Tpp already onboarded
        Given tppA already onboarded
        When a get info for TppA request arrives
        Then the get info request is successful

